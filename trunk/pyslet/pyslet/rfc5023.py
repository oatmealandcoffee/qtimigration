#! /usr/bin/env python
"""This module implements the Atom Publishing Protocol specification defined in RFC 5023

References:

IRIs [RFC3987]; cf URI [RFC3986]
Before an IRI in a document is used by HTTP, the IRI is first converted to a
URI according to the procedure defined in Section 3.1 of [RFC3987]

xml:base attribute [W3C.REC-xmlbase-20010627]
xml:lang attribute [W3C.REC-xml-20040204], Section 2.12
"""

import string, StringIO, sys, traceback

import pyslet.xml20081126.structures as xml
import pyslet.xmlnames20091208 as xmlns
from pyslet import rfc4287 as atom
from pyslet import rfc2616 as http
import pyslet.rfc2396 as uri


APP_NAMESPACE="http://www.w3.org/2007/app"		#: The namespace to use for Atom Publishing Protocol elements
ATOMSVC_MIMETYPE="application/atomsvc+xml"		#: The mime type for service documents
ATOMCAT_MIMETYPE="application/atomcat+xml"		#: The mime type for category documents

APP_MIMETYPES={
	ATOMSVC_MIMETYPE:True,
	ATOMCAT_MIMETYPE:True,
	atom.ATOM_MIMETYPE:True
	}
	

def ParseYesNo(src):
	return src.strip().lower()=='yes'

def FormatYesNo(value):
	if value:
		return 'yes'
	else:
		return 'no'


class APPElement(xmlns.XMLNSElement):
	"""Base class for all APP elements.
	
	All APP elements can have xml:base, xml:lang and/or xml:space attributes. 
	These are handled by the base
	:py:class:`~pyslet.xml20081126.structures.Element` base class."""
	pass


class Accept(APPElement):
	"""Represents the accept element."""
	XMLNAME=(APP_NAMESPACE,'accept')

	
class Categories(APPElement):
	"""The root of a Category Document.
	
	A category document is a document that describes the categories allowed in a collection."""
	XMLNAME=(APP_NAMESPACE,'categories')
	
	XMLATTR_href=('href',uri.URIFactory.URI,str)
	XMLATTR_fixed=('fixed',ParseYesNo,FormatYesNo)
	XMLATTR_scheme='scheme'
	XMLCONTENT=xmlns.ElementContent

	def __init__(self,parent):
		APPElement.__init__(self,parent)
		self.href=None		#: an optional :py:class:`~pyslet.rfc2396.URI` to the category
		self.fixed=None		#: indicates whether the list of categories is a fixed set.  By default they're open.
		self.scheme=None	#: identifies the default scheme for categories defined by this element
		self.Category=[]	#: the list of categories, instances of :py:class:~pyslet.rfc4287.Category

	def GetChildren(self):
		for child in self.Category: yield child
		for child in APPElement.GetChildren(self): yield child
				
		
class Service(APPElement):
	"""The container for service information associated with one or more Workspaces."""
	XMLNAME=(APP_NAMESPACE,'service')
	
	def __init__(self,parent):
		APPElement.__init__(self,parent)
		self.Workspace=[]		#: a list of :py:class:`Workspace` instances
		
	def GetChildren(self):
		for child in APPElement.GetChildren(self):
			yield child
		for child in self.Workspace:
			yield child
		

class Workspace(APPElement):
	"""Workspaces are server-defined groups of Collections."""
	XMLNAME=(APP_NAMESPACE,'workspace')
	
	def __init__(self,parent):
		APPElement.__init__(self,parent)
		self.Title=None			#: the title of this workspace
		self.Collection=[]		#: a list of :py:class:`Collection`
		
	def GetChildren(self):
		for child in APPElement.GetChildren(self): yield child
		if self.Title: yield self.Title
		for child in self.Collection: yield child
		

class Collection(APPElement):
	"""Describes a collection (feed)."""
	XMLNAME=(APP_NAMESPACE,'collection')

	XMLATTR_href=('href',uri.URIFactory.URI,str)
	
	def __init__(self,parent):	
		APPElement.__init__(self,parent)
		self.href=None		#: the URI of the collection (feed)
		self.Title=None		#: the human readable title of the collection
		self.Accept=[]		#: list of :py:class:`Accept` media ranges that can be posted to the collection
		self.Categories=[]	#: list of :py:class:`Categories` that can be applied to members of the collection
	
	def GetChildren(self):
		for child in APPElement.GetChildren(self): yield child
		if self.Title: yield self.Title
		for child in self.Accept: yield child
		for child in self.Categories: yield child
		
	def GetFeedURL(self):
		"""Returns a fully resolved URL for the collection (feed)."""
		return self.ResolveURI(self.href)

		
class Document(atom.AtomDocument):
	"""Class for working with APP documents.
	
	This call can represent both APP and Atom documents."""
	classMap={}
	
	def __init__(self,**args):
		atom.AtomDocument.__init__(self,**args)
		self.defaultNS=APP_NAMESPACE
	
	def ValidateMimeType(self,mimetype):
		"""Checks *mimetype* against the mime types given in the APP or Atom specifications."""
		return mimetype in APP_MIMETYPES or atom.AtomDocument.ValidateMimeType(self,mimetype)
		
	def GetElementClass(self,name):
		"""Returns the APP or Atom class used to represent name.
		
		Overrides :py:meth:`~pyslet.rfc4287.AtomDocument.GetElementClass` when
		the namespace is :py:data:`APP_NAMESPACE`."""
		if name[0]==APP_NAMESPACE:
			return Document.classMap.get(name,atom.AtomDocument.classMap.get((name[0],None),APPElement))
		else:
			return atom.AtomDocument.GetElementClass(self,name)

xmlns.MapClassElements(Document.classMap,globals())
				

class Client(http.HTTPRequestManager):
	def __init__(self):
		http.HTTPRequestManager.__init__(self)

	def QueueRequest(self,request):
		request.SetHeader('Accept',string.join((atom.ATOM_MIMETYPE,ATOMSVC_MIMETYPE,ATOMCAT_MIMETYPE),','),True)
		http.HTTPRequestManager.QueueRequest(self,request)


class Server(object):

	def __init__(self,serviceRoot='http://localhost/'):
		if not isinstance(serviceRoot,uri.URI):
			self.serviceRoot=uri.URIFactory.URI(serviceRoot)
		else:
			self.serviceRoot=serviceRoot			
		self.serviceDoc=Document(root=Service,baseURI=self.serviceRoot)
		self.service=self.serviceDoc.root	#: the :py:class:`Service` instance that describes this service.
		self.service.SetBase(str(self.serviceRoot))		# make the base explicit in the document
		self.debugMode=False				#:	set this to True to expose python tracebacks in 500 responses, defaults to False

	def __call__(self,environ,start_response):
		"""wsgi interface for calling instances of this Atom server object.
		
		We add an additional optional parameter *responseHeaders*"""
		responseHeaders=[]
		if environ['SCRIPT_NAME']+environ['PATH_INFO']==self.serviceRoot.absPath:
			data=unicode(self.serviceDoc).encode('utf-8')
			responseHeaders.append(("Content-Type",ATOMSVC_MIMETYPE))
			responseHeaders.append(("Content-Length",str(len(data))))
			start_response("200 Ok",responseHeaders)
			return [data]
		else:
			return self.HandleMissing(environ,start_response)
			
	def HandleMissing(self,environ,start_response):
		responseHeaders=[]
		data="This server supports the Atom Publishing Protocol\r\nFor service information see: %s"%str(self.serviceRoot)
		responseHeaders.append(("Content-Length",str(len(data))))
		responseHeaders.append(("Content-Type",'text/plain'))
		start_response("404 Not found",responseHeaders)
		return [data]

	def HandleError(self,environ,start_response,code=500):
		"""Designed to be called by an otherwise uncaught exception.  Generates a 500 response by default."""
		responseHeaders=[]
		cData=StringIO.StringIO()
		if self.debugMode:
			traceback.print_exception(*sys.exc_info(),file=cData)
		else:
			cData.write("Sorry, there was an internal error while processing this request")
		responseHeaders.append(("Content-Type",'text/plain'))
		responseHeaders.append(("Content-Length",str(len(cData.getvalue()))))
		start_response("%i Unexpected error"%code,responseHeaders)
		return [cData.getvalue()]
		