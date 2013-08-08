#! /usr/bin/env python

import unittest

from sys import maxunicode
from tempfile import mkdtemp
import shutil, os.path
from StringIO import StringIO
from types import UnicodeType

MAX_CHAR=0x10FFFF
if maxunicode<MAX_CHAR:
	MAX_CHAR=maxunicode
	print "xml tests truncated to unichr(0x%X) by narrow python build"%MAX_CHAR

def suite():
	return unittest.TestSuite((
		unittest.makeSuite(XML20081126Tests,'test'),
		unittest.makeSuite(XMLDocumentTests,'test'),
		unittest.makeSuite(XMLCharacterTests,'test'),
		unittest.makeSuite(XMLEntityTests,'test'),
		unittest.makeSuite(XMLElementTests,'test'),
		unittest.makeSuite(XMLValidationTests,'test')
		))

TEST_DATA_DIR=os.path.join(os.path.split(os.path.abspath(__file__))[0],'data_xml20081126')
DTD_DATA=os.path.join(os.path.split(os.path.abspath(__file__))[0],'data_imsqtiv1p2p1','input')

from pyslet.xml20081126 import *

	
class NamedElement(XMLElement):
	XMLNAME="test"

def DecodeYN(value):
	return value=='Yes'
	
def EncodeYN(value):
	if value:
		return 'Yes'
	else:
		return 'No'


class GenericElementA(XMLElement):
	pass

class GenericSubclassA(GenericElementA):
	pass

class GenericElementB(XMLElement):
	pass

class GenericSubclassB(GenericElementB):
	pass


class ReflectiveElement(XMLElement):
	XMLNAME="reflection"
	
	XMLATTR_btest='bTest'
	XMLATTR_ctest=('cTest',DecodeYN,EncodeYN)
	XMLATTR_dtest=('dTest',DecodeYN,EncodeYN)
	XMLATTR_etest=('eTest',DecodeYN,EncodeYN)
	
	def __init__(self,parent):
		XMLElement.__init__(self,parent)
		self.atest=None
		self.bTest=None
		self.cTest=None
		self.dTest=[]
		self.eTest={}
		self.child=None
		self.generics=[]
		self.GenericElementB=None
		
	def GetAttributes(self):
		attrs=XMLElement.GetAttributes(self)
		if self.atest:
			attrs['atest']=self.atest
		return attrs
		
	def Set_atest(self,value):
		self.atest=value
	
	def GetChildren(self):
		children=XMLElement.GetChildren(self)
		if self.child:
			children.append(self.child)
		return children
		
	def ReflectiveElement(self):
		if self.child:
			return self.child
		else:
			e=ReflectiveElement(self)
			self.child=e
			return e

	def GenericElementA(self,childClass=GenericElementA):
		child=childClass(self)
		self.generics.append(child)
		return child
		

class ReflectiveDocument(XMLDocument):
	def GetElementClass(self,name):
		if name in ["reflection","etest"]:
			return ReflectiveElement
		else:
			return XMLElement

class EmptyElement(XMLElement):
	XMLNAME="empty"
	XMLCONTENT=XMLEmpty
	
class ElementContent(XMLElement):
	XMLNAME="elements"
	XMLCONTENT=XMLElementContent

class MixedElement(XMLElement):
	XMLNAME="mixed"
	XMLCONTENT=XMLMixedContent

class IDElement(XMLElement):
	XMLName="ide"
	XMLCONTENT=XMLEmpty
	ID="id"

class BadElement:
	XMLNAME="bad"

	
class Elements:
	named=NamedElement
	reflective=ReflectiveElement
	empty=EmptyElement
	elements=ElementContent
	mixed=MixedElement
	id=IDElement
	bad=BadElement
	
class XML20081126Tests(unittest.TestCase):		
	def testCaseConstants(self):
		#self.failUnless(APP_NAMESPACE=="http://www.w3.org/2007/app","Wrong APP namespace: %s"%APP_NAMESPACE)
		#self.failUnless(ATOMSVC_MIMETYPE=="application/atomsvc+xml","Wrong APP service mime type: %s"%ATOMSVC_MIMETYPE)
		#self.failUnless(ATOMCAT_MIMETYPE=="application/atomcat+xml","Wrong APP category mime type: %s"%ATOMCAT_MIMETYPE)
		pass

	def testCaseDeclare(self):
		classMap={}
		MapClassElements(classMap,Elements)
		self.failUnless(type(classMap['mixed']) is types.ClassType,"class type not declared")
		self.failIf(hasattr(classMap,'bad'),"class type declared by mistake")

		
class XMLCharacterTests(unittest.TestCase):
	# Test IsNameChar
	def testChar(self):
		"""[2] Char ::= #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]"""
		expectedEdges=[0x9,0xB,0xD,0xE,0x20,0xD800,0xE000,0xFFFE,0x10000,0x110000]
		if MAX_CHAR<0x10FFFF:
			expectedEdges=expectedEdges[0:8]
		self.failUnless(self.FindEdges(IsChar,MAX_CHAR)==expectedEdges,"IsChar")

	def testSpace(self):
		"""[3] S ::= (#x20 | #x9 | #xD | #xA)+"""
		expectedEdges=[0x9,0xB,0xD,0xE,0x20,0x21]
		self.failUnless(self.FindEdges(IsS,256)==expectedEdges,"IsS")
	
	def testNameStart(self):
		"""[4] NameStartChar ::= ":" | [A-Z] | "_" | [a-z] | [#xC0-#xD6] | [#xD8-#xF6] | [#xF8-#x2FF] | [#x370-#x37D] | [#x37F-#x1FFF] | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]
		[5] NameChar ::= NameStartChar | "-" | "." | [0-9] | #xB7 | [#x0300-#x036F] | [#x203F-#x2040]"""
		nNameStartChars=0
		nNameChars=0
		for code in xrange(0x10000):
			c=unichr(code)
			if IsNameChar(c):
				nNameChars+=1
				if IsNameStartChar(c):
					nNameStartChars+=1
			else:
				self.failIf(IsNameStartChar(c),"NameStart not a name char: %s"%c)
		self.failUnless(nNameChars==54129,"name char total %i"%nNameChars)
		self.failUnless(nNameStartChars==54002,"name start char total %i"%nNameStartChars)
				
	def testCharClasses(self):
		"""[84] Letter ::= BaseChar | Ideographic
		[85] BaseChar ::= [#x0041-#x005A] | ...
		[86] Ideographic ::= [#x4E00-#x9FA5] | #x3007 | [#x3021-#x3029]
		[87] CombiningChar ::= [#x0300-#x0345] | ...
		[88] Digit ::= [#x0030-#x0039] | ...
		[89] Extender ::= #x00B7 | ..."""
		nBaseChars=0
		nIdeographics=0
		nCombiningChars=0
		nDigits=0
		nExtenders=0
		for code in xrange(0x10000):
			c=unichr(code)
			if IsLetter(c):
				if IsIdeographic(c):
					nIdeographics+=1
				elif IsBaseChar(c):
					nBaseChars+=1
				else:
					self.fail("unichr(%#x) is a letter but not an ideographic or base character"%code)
			else:
				self.failIf(IsIdeographic(c) or IsBaseChar(c),
					"unichr(%#x) is an ideographic or base character but not a letter")
			if IsCombiningChar(c):
				nCombiningChars+=1
			if IsDigit(c):
				nDigits+=1
			if IsExtender(c):
				nExtenders+=1
		self.failUnless(nBaseChars==13602,"base char total %i"%nBaseChars)
		self.failUnless(nIdeographics==20912,"ideographic char total %i"%nIdeographics)
		self.failUnless(nCombiningChars==437,"combing char total %i"%nCombiningChars)
		self.failUnless(nDigits==149,"digit total %i"%nDigits)
		self.failUnless(nExtenders==18,"extender total %i"%nExtenders)

	def FindEdges(self,testFunc,max):
		edges=[]
		flag=False
		for code in xrange(max+1):
			c=unichr(code)
			if flag!=testFunc(c):
				flag=not flag
				edges.append(code)
		return edges

class XMLValidationTests(unittest.TestCase):
	def testCaseName(self):
		self.failUnless(IsValidName("Simple"))
		self.failUnless(IsValidName(":BadNCName"))
		self.failUnless(IsValidName("prefix:BadNCName"))
		self.failUnless(IsValidName("_GoodNCName"))
		self.failIf(IsValidName("-BadName"))
		self.failIf(IsValidName(".BadName"))
		self.failIf(IsValidName("0BadName"))
		self.failUnless(IsValidName("GoodName-0.12"))
		self.failIf(IsValidName("BadName$"))
		self.failIf(IsValidName("BadName+"))
		self.failUnless(IsValidName(u"Caf\xe9"))



class XMLEntityTests(unittest.TestCase):
	def testCaseConstructor(self):
		e=XMLEntity("<hello>")
		self.failUnless(e.lineNum==1)
		self.failUnless(e.linePos==1)
		self.failUnless(type(e.theChar) is UnicodeType and e.theChar==u'<')
		e=XMLEntity(u"<hello>")
		self.failUnless(type(e.theChar) is UnicodeType and e.theChar==u'<')
		e=XMLEntity(StringIO("<hello>"))
		self.failUnless(e.lineNum==1)
		self.failUnless(e.linePos==1)
		self.failUnless(type(e.theChar) is UnicodeType and e.theChar==u'<')

	def testCaseChars(self):
		e=XMLEntity("<hello>")
		for c in "<hello>":
			self.failUnless(e.theChar==c)
			e.NextChar()
		self.failUnless(e.theChar is None)
		e.Reset()
		self.failUnless(e.theChar=='<')

	def testLines(self):
		e=XMLEntity("Hello\nWorld\n!")
		while e.theChar is not None:
			c=e.theChar
			e.NextChar()
		self.failUnless(e.lineNum==3)
		self.failUnless(e.linePos==2)

	def testLookahead(self):
		e=XMLEntity("Hello")
		e.StartLookahead()
		e.NextChar()
		e.StopLookahead()
		self.failUnless(e.theChar=='e')
		e.StartLookahead()
		e.NextChar()
		self.failUnless(e.theChar=='l')
		e.RewindLookahead()
		self.failUnless(e.theChar=='e')

	def testCodecs(self):
		m=u'Caf\xe9'
		e=XMLEntity('Caf\xc3\xa9')
		for c in m:
			self.failUnless(e.theChar==c,"Print: parsing utf-8 got %s instead of %s"%(repr(e.theChar),repr(c)))
			e.NextChar()
		e=XMLEntity('Caf\xe9','latin_1')
		for c in m:
			self.failUnless(e.theChar==c,"Print: parsing latin-1 got %s instead of %s"%(repr(e.theChar),repr(c)))
			e.NextChar()
		# This string should be automatically detected
		e=XMLEntity('\xff\xfeC\x00a\x00f\x00\xe9\x00','utf-16')
		for c in m:
			self.failUnless(e.theChar==c,"Print: parsing utf-16LE got %s instead of %s"%(repr(e.theChar),repr(c)))
			e.NextChar()		
		e=XMLEntity('\xfe\xff\x00C\x00a\x00f\x00\xe9','utf-16')
		for c in m:
			self.failUnless(e.theChar==c,"Print: parsing utf-16BE got %s instead of %s"%(repr(e.theChar),repr(c)))
			e.NextChar()			
		e=XMLEntity('\xef\xbb\xbfCaf\xc3\xa9','utf-8')
		for c in m:
			self.failUnless(e.theChar==c,"Print: parsing utf-8 with BOM got %s instead of %s"%(repr(e.theChar),repr(c)))
			e.NextChar()
		e=XMLEntity('Caf\xe9')
		for c in 'Ca':
			e.NextChar()
		e.ChangeEncoding('ISO-8859-1')
		self.failUnless(e.theChar=='f',"Bad encoding change")
		e.NextChar()
		self.failUnless(e.theChar==u'\xe9',"Print: change encoding got %s instead of %s"%(repr(e.theChar),repr(u'\xe9')))

		
class XMLParserTests(unittest.TestCase):
	def testCaseConstructor(self):
		p=XMLParser()
		e=XMLEntity("<hello>")
		p=XMLParser(e)

	def testCaseRewind(self):
		data="Hello\r\nWorld\nCiao\rTutti!"
		data2="Hello\nWorld\nCiao\nTutti!"
		e=XMLEntity(data)
		p=XMLParser(e)
		for i in xrange(len(data2)):
			self.failUnless(p.theChar==data2[i],"Failed at data[%i] before look ahead"%i)
			for j in xrange(5):
				e.StartLookahead()
				for k in xrange(j):
					p.NextChar()
				p.Rewind()
				self.failUnless(p.theChar==data2[i],"Failed at data[%i] after Rewind(%i)"%(i,j))
			p.NextChar()
		
	def testDocument(self):
		"""[1] document ::= prolog element Misc* """
		os.chdir(TEST_DATA_DIR)
		f=open('readFile.xml','rb')
		e=XMLEntity(f)
		d=XMLDocument()
		d.Read(e)
		root=d.root
		self.failUnless(isinstance(root,XMLElement))
		self.failUnless(root.xmlname=='tag' and root.GetValue()=='Hello World')
		f.close()

	def testCaseDTD(self):
		f=open(os.path.join(DTD_DATA,'qmdextensions.xml'),'rb')
		e=XMLEntity(f)
		d=XMLDocument()
		d.Read(e)
			
	#	[2] Char ::= #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]

	def testCaseS(self):
		"""[3] S ::= (#x20 | #x9 | #xD | #xA)+ """
		e=XMLEntity(" \t\r\n \r \nHello")
		p=XMLParser(e)
		self.failUnless(p.ParseS()==" \t\n \n \n")
		self.failUnless(e.theChar=='H')
	
	def testCaseNames(self):
		"""
		[4]		NameStartChar ::= ":" | [A-Z] | "_" | [a-z] | [#xC0-#xD6] | [#xD8-#xF6] | [#xF8-#x2FF] | [#x370-#x37D] | [#x37F-#x1FFF] | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]
		[4a]   	NameChar ::= NameStartChar | "-" | "." | [0-9] | #xB7 | [#x0300-#x036F] | [#x203F-#x2040]
		[5]   	Name ::= NameStartChar (NameChar)*
		[6]   	Names ::= Name (#x20 Name)*
		[7]   	Nmtoken ::= (NameChar)+
		[8]   	Nmtokens ::= Nmtoken (#x20 Nmtoken)*
		"""
		e=XMLEntity("Hello World -Atlantis!")
		p=XMLParser(e)
		self.failUnless(p.ParseNames()==['Hello','World'])
		e.Reset()
		p=XMLParser(e)
		tokens=p.ParseNmtokens()
		self.failUnless(tokens==['Hello','World','-Atlantis'],repr(tokens))
		
	def testCaseEntityValue(self):
		"""[9] EntityValue ::= '"' ([^%&"] | PEReference | Reference)* '"' | "'" ([^%&'] | PEReference | Reference)* "'"	"""
		e=XMLEntity("'first'\"second\"'3&gt;2''2%ltpe;3'")
		m=['first','second','3>2','2<3']
		p=XMLParser(e)
		p.doc=XMLDocument()
		p.doc.DeclareParameterEntity('ltpe','<')
		for match in m:
			value=p.ParseEntityValue()
			self.failUnless(value==match,"Match failed: %s (expected %s)"%(value,match))
	
	def testAttValue(self):
		"""[10] AttValue ::= '"' ([^<&"] | Reference)* '"' |  "'" ([^<&'] | Reference)* "'" """
		e=XMLEntity("'first'\"second\"'3&gt;2''Caf&#xE9;'")
		m=['first','second','3>2',u'Caf\xe9']
		p=XMLParser(e)
		for match in m:
			value=p.ParseAttValue()
			self.failUnless(value==match,"Match failed: %s (expected %s)"%(value,match))
	
	def testSystemLiteral(self):
		"""[11] SystemLiteral ::= ('"' [^"]* '"') | ("'" [^']* "'") """
		e=XMLEntity("'first'\"second\"'3&gt;2''2%ltpe;3''Caf&#xE9;'")
		m=[u'first',u'second',u'3&gt;2',u'2%ltpe;3',u'Caf&#xE9;']
		p=XMLParser(e)
		for match in m:
			value=p.ParseSystemLiteral()
			self.failUnless(value==match,"Match failed: %s (expected %s)"%(value,match))
	
	def testPubidLiteral(self):
		"""
		[12] PubidLiteral ::= '"' PubidChar* '"' | "'" (PubidChar - "'")* "'"
		[13] PubidChar ::= #x20 | #xD | #xA | [a-zA-Z0-9] | [-'()+,./:=?;!*#@$_%]
		"""
		e=XMLEntity("'first'\"second\"'http://www.example.com/schema.dtd?strict''[bad]'")
		m=['first','second','http://www.example.com/schema.dtd?strict']
		p=XMLParser(e)
		for match in m:
			value=p.ParsePubidLiteral()
			self.failUnless(value==match,"Match failed: %s (expected %s)"%(value,match))
		try:
			value=p.ParsePubidLiteral()
			self.fail("Parsed bad PubidLiterasl: %s"%value)
		except XMLFatalError:
			pass
		
	def testCaseCharData(self):
		"""[14] CharData ::= [^<&]* - ([^<&]* ']]>' [^<&]*) """
		e=XMLEntity("First<Second&Third]]&Fourth]]>")
		m=['First','Second','Third]]','Fourth']
		p=XMLParser(e)
		for match in m:
			pStr=p.ParseCharData()
			p.NextChar()
			self.failUnless(pStr==match,"Match failed: %s (expected %s)"%(pStr,match))

	def testCaseComment(self):
		"""[15] Comment ::= '<!--' ((Char - '-') | ('-' (Char - '-')))* '-->' """
		e=XMLEntity("<!--First--><!--Secon-d--><!--Thi<&r]]>d--><!--Fourt<!-h--><!--Bad--Comment-->")
		m=['First','Secon-d','Thi<&r]]>d','Fourt<!-h']
		p=XMLParser(e)
		for match in m:
			if p.ParseLiteral('<!--'):
				pStr=p.ParseComment()
				self.failUnless(pStr==match,"Match failed: %s (expected %s)"%(pStr,match))
			else:
				self.fail("Comment start")
		try:
			if p.ParseLiteral('<!--'):
				pStr=p.ParseComment()
			self.fail("Parsed bad comment: %s"%pStr)
		except XMLFatalError:
			pass

	def testCasePI(self):
		"""[16] PI ::= '<?' PITarget (S (Char* - (Char* '?>' Char*)))? '?>' """
		e=XMLEntity("<?target instruction?><?xm_xml \n\r<!--no comment-->?><?markup \t]]>?&<?><?xml reserved?>")
		m=[('target','instruction'),('xm_xml','<!--no comment-->'),('markup',']]>?&<'),('xml','reserved')]
		p=XMLParser(e)
		for matchTarget,matchStr in m:
			if p.ParseLiteral('<?'):
				target,pStr=p.ParsePI()
			self.failUnless(target==matchTarget,"Match failed for target: %s (expected %s)"%(target,matchTarget))
			self.failUnless(pStr==matchStr,"Match failed for instruction: %s (expected %s)"%(pStr,matchStr))
			
	def testCaseCDSect(self):
		"""
		[18] CDSect ::=  CDStart CData CDEnd
		[19] CDStart ::= '<![CDATA['
		[20] CData ::= (Char* - (Char* ']]>' Char*))
		[21] CDEnd ::= ']]>'
		"""
		e=XMLEntity("<![CDATA[]]><![CDATA[<hello>&world;]]><![CDATA[hello]]world]]>")
		m=['','<hello>&world;','hello]]world']
		p=XMLParser(e)
		for match in m:
			if p.ParseLiteral('<![CDATA['):
				pStr=p.ParseCDSect()
			self.failUnless(pStr==match,"Match failed: %s (expected %s)"%(pStr,match))

		# 	[22]   	prolog	   ::=   	 XMLDecl? Misc* (doctypedecl Misc*)?
		# 	[23]   	XMLDecl	   ::=   	'<?xml' VersionInfo EncodingDecl? SDDecl? S? '?>'
		# 	[24]   	VersionInfo	   ::=   	 S 'version' Eq ("'" VersionNum "'" | '"' VersionNum '"')
		# 	[25]   	Eq	   ::=   	 S? '=' S?
		# 	[26]   	VersionNum	   ::=   	'1.' [0-9]+
		# 	[27]   	Misc	   ::=   	 Comment | PI | S

	def testCaseTags(self):
		e=XMLEntity("<tag hello='world' ciao=\"tutti\">")
		p=XMLParser(e)
		name,attrs,empty=p.ParseSTag()
		self.failUnless(name=='tag' and attrs['hello']=='world' and attrs['ciao']=='tutti' and empty==False)
		e=XMLEntity("<tag hello>")
		p=XMLParser(e)
		name,attrs,empty=p.ParseSTag()
		self.failUnless(name=='tag' and attrs['hello']==None and empty is False)
		e=XMLEntity("<tag width=20%>")
		p=XMLParser(e)
		p.compatibilityMode=True
		name,attrs,empty=p.ParseSTag()
		self.failUnless(name=='tag' and attrs['width']=='20%' and empty is False)


class XMLElementTests(unittest.TestCase):
	def testCaseConstructor(self):
		e=XMLElement(None)
		self.failUnless(e.xmlname==None,'element name on construction')
		self.failUnless(e.GetDocument() is None,'document set on construction')
		attrs=e.GetAttributes()
		self.failUnless(len(attrs.keys())==0,"Attributes present on construction")
		children=e.GetChildren()
		self.failUnless(len(children)==0,"Children present on construction")
		e=XMLElement(None,'test')
		self.failUnless(e.xmlname=='test','element named on construction')
		
	def testCaseDefaultName(self):
		e=NamedElement(None)
		self.failUnless(e.xmlname=='test','element default name on construction')
	
	def testSetXMLName(self):
		e=NamedElement(None,'test2')
		self.failUnless(e.xmlname=='test2','element named explicitly in construction')

	def testAttributes(self):
		e=XMLElement(None,'test')
		e.SetAttribute('atest','value')
		attrs=e.GetAttributes()
		self.failUnless(len(attrs.keys())==1,"Attribute not set")
		self.failUnless(attrs['atest']=='value',"Attribute not set correctly")
		e=ReflectiveElement(None)
		e.SetAttribute('atest','value')
		self.failUnless(e.atest=='value',"Attribute relfection")
		attrs=e.GetAttributes()
		self.failUnless(attrs['atest']=='value',"Attribute not set correctly")
		e.SetAttribute('btest','Yes')
		self.failUnless(e.bTest=='Yes',"Attribute relfection with simple assignment")
		attrs=e.GetAttributes()
		self.failUnless(attrs['btest']=='Yes',"Attribute not set correctly")
		e.SetAttribute('ctest','Yes')
		self.failUnless(e.cTest==True,"Attribute relfection with decode/encode")
		attrs=e.GetAttributes()
		self.failUnless(attrs['ctest']=='Yes',"Attribute not set correctly")
		e.SetAttribute('dtest','Yes No')
		self.failUnless(e.dTest==[True,False],"Attribute relfection with list")
		attrs=e.GetAttributes()
		self.failUnless(attrs['dtest']=='Yes No',"Attribute not set correctly")
		e.SetAttribute('etest','Yes No')
		self.failUnless(e.eTest=={True:'Yes',False:'No'},"Attribute relfection with list")
		attrs=e.GetAttributes()
		self.failUnless(attrs['etest']=='No Yes',"Attribute not set correctly")
				
	def testChildElements(self):
		"""Test child element behaviour"""
		e=XMLElement(None,'test')
		child1=e.ChildElement(XMLElement,'test1')
		children=e.GetChildren()
		self.failUnless(len(children)==1,"ChildElement failed to add child element")
	
	def testChildElementReflection(self):
		"""Test child element cases using reflection"""
		e=ReflectiveElement(None)
		child1=e.ChildElement(ReflectiveElement,'test1')
		self.failUnless(e.child is child1,"Element not set by reflection")
		children=e.GetChildren()
		self.failUnless(len(children)==1 and children[0] is child1,"ChildElement failed to add child element")
		# Now create a second child, should return the same one due to model restriction
		child2=e.ChildElement(ReflectiveElement,'test1')
		self.failUnless(e.child is child1 and child2 is child1,"Element model violated")
		child3=e.ChildElement(GenericElementA,'test3')
		self.failUnless(e.generics[0] is child3,"Generic element")
		child4=e.ChildElement(GenericSubclassA,'test4')
		self.failUnless(e.generics[1] is child4,"Generic sub-class element via method")
		child5=e.ChildElement(GenericSubclassB,'test5')
		self.failUnless(e.GenericElementB is child5,"Generic sub-class element via member")
		
	def testData(self):
		e=XMLElement(None)
		self.failUnless(e.IsMixed(),"Mixed default")
		e.AddData('Hello')
		self.failUnless(e.GetValue()=='Hello',"Data value")
		children=e.GetChildren()
		self.failUnless(len(children)==1,"Data child not set")
		self.failUnless(children[0]=="Hello","Data child not set correctly")
	
	def testEmpty(self):
		e=EmptyElement(None)
		self.failIf(e.IsMixed(),"EmptyElement is mixed")
		self.failUnless(e.IsEmpty(),"EmptyElement not empty")
		try:
			e.AddData('Hello')
			self.fail("Data in EmptyElement")
		except XMLValidationError:
			pass
		try:
			child=e.ChildElement(XMLElement)
			self.fail("Elements allowed in EmptyElement")
		except XMLValidationError:
			pass		

	def testElementContent(self):	
		e=ElementContent(None)
		self.failIf(e.IsMixed(),"ElementContent appears mixed")
		self.failIf(e.IsEmpty(),"ElementContent appears empty")
		try:
			e.AddData('Hello')
			self.fail("Data in ElementContent")
		except XMLValidationError:
			pass
		# white space should silently be ignored.
		e.AddData('  \n\r  \t')
		children=e.GetChildren()
		self.failUnless(len(children)==0,"Unexpected children")
		# elements can be added
		child=e.ChildElement(XMLElement)
		children=e.GetChildren()
		self.failUnless(len(children)==1,"Expected one child")
	
	def testMixedContent(self):
		e=MixedElement(None)
		self.failUnless(e.IsMixed(),"MixedElement not mixed")
		self.failIf(e.IsEmpty(),"MixedElement appears empty")
		e.AddData('Hello')
		self.failUnless(e.GetValue()=='Hello','Mixed content with a single value')
		child=e.ChildElement(XMLElement)
		try:
			e.GetValue()
		except XMLMixedContentError:
			pass
		
	def testCopy(self):
		e1=XMLElement(None)
		e2=e1.Copy()
		self.failUnless(isinstance(e2,XMLElement),"Copy didn't make XMLElement")
		self.failUnless(e1==e2 and e1 is not e2)
		

class XMLDocumentTests(unittest.TestCase):
	def setUp(self):
		self.cwd=os.getcwd()
		self.d=mkdtemp('.d','pyslet-test_xml20081126-')
		os.chdir(self.d)
		
	def tearDown(self):
		os.chdir(self.cwd)
		shutil.rmtree(self.d,True)

	def testCaseConstructor(self):
		d=XMLDocument()
		self.failUnless(d.root is None,'root on construction')
		self.failUnless(d.GetBase() is None,'base set on construction')
		d=XMLDocument(root=XMLElement)
		self.failUnless(isinstance(d.root,XMLElement),'root not created on construction')
		self.failUnless(d.root.GetDocument() is d,'root not linked to document')
	
	def testCaseBase(self):
		"""Test the use of a file path on construction"""
		fpath=os.path.abspath('fpath.xml')
		furl=str(URIFactory.URLFromPathname(fpath))
		d=XMLDocument(baseURI=furl)
		self.failUnless(d.GetBase()==furl,"Base not set in constructor")
		self.failUnless(d.root is None,'root on construction')
		d=XMLDocument(baseURI='fpath.xml',root=XMLElement)
		self.failUnless(d.GetBase()==furl,"Base not made absolute from relative URL:\n\t%s\n\t%s"%(furl,d.GetBase()))
		self.failUnless(isinstance(d.root,XMLElement),'root not created on construction')
		d=XMLDocument()
		d.SetBase(furl)
		self.failUnless(d.GetBase()==furl,"Base not set by SetBase")

	def testCaseReadFile(self):
		"""Test the reading of the XMLDocument from the file system"""
		os.chdir(TEST_DATA_DIR)
		d=XMLDocument(baseURI='readFile.xml')
		d.Read()
		root=d.root
		self.failUnless(isinstance(root,XMLElement))
		self.failUnless(root.xmlname=='tag' and root.GetValue()=='Hello World')
		
	def testCaseReadString(self):
		"""Test the reading of the XMLDocument from a supplied stream"""
		os.chdir(TEST_DATA_DIR)
		d=XMLDocument(baseURI='readFile.xml')
		f=open('readFile.xml')
		d.Read(src=f)
		f.close()
		root=d.root
		self.failUnless(isinstance(root,XMLElement))
		self.failUnless(root.xmlname=='tag' and root.GetValue()=='Hello World')
	
	def testCaseString(self):
		os.chdir(TEST_DATA_DIR)
		d=XMLDocument(baseURI='readFile.xml')
		d.Read()
		f=open('readFile.xml')
		fData=f.read()
		f.close()
		self.failUnless(str(d)==fData,"XML output: %s"%str(d))
		d=XMLDocument(baseURI='ascii.xml')
		d.Read()
		f=open('ascii.xml')
		fData=f.read()
		f.close()
		self.failUnless(str(d)==fData,"XML output: %s"%str(d))
		
	def testCaseResolveBase(self):
		"""Test the use of ResolveURI and ResolveBase"""
		os.chdir(TEST_DATA_DIR)
		parent=XMLElement(None)
		self.failUnless(parent.ResolveBase() is None,"No default base")
		child=XMLElement(parent)
		self.failUnless(child.ResolveBase() is None,"No xml:base by default")
		parent.SetBase('file:///index.xml')
		self.failUnless(child.ResolveBase()=='file:///index.xml',"No xml:base inheritance")
		# Tests with a document follow....
		furl=str(URIFactory.URLFromPathname(os.path.abspath('base.xml')))
		href=URIFactory.URLFromPathname(os.path.abspath('link.xml'))
		hrefPath=href.absPath
		href=str(href)
		altRef='file:///hello/link.xml'
		d=XMLDocument(baseURI='base.xml')
		self.failUnless(d.GetBase()==furl,"Base not resolved relative to w.d. by constructor")
		d.Read()
		tag=d.root
		self.failUnless(tag.ResolveBase()==furl,"Root element resolves from document")
		self.failUnless(tag.ResolveURI("link.xml")==href,"Root element HREF")
		self.failUnless(tag.RelativeURI(href)=='link.xml',"Root element relative")
		#self.failUnless(tag.RelativeURI(altRef)=='/hello/link.xml','Root element full path relative: %s'%tag.RelativeURI(altRef))
		childTag=tag._children[0]
		self.failUnless(childTag.ResolveBase()=="file:///hello/base.xml","xml:base overrides in childTag (%s)"%childTag.ResolveBase())
		self.failUnless(childTag.ResolveURI("link.xml")==altRef,"child element HREF")
		self.failUnless(childTag.RelativeURI(href)=='..'+hrefPath,"child element relative resulting in full path: %s"%childTag.RelativeURI(href))
		self.failUnless(childTag.RelativeURI(altRef)=='link.xml','child element relative')
		# We require this next test to ensure that an href to the current document comes up blank
		# Although this was a major source of bugs in browsers (<img src=''> causing infinite loading loops)
		# these are largely fixed now and obfuscating by using a non-empty relative link to ourselves is
		# likely to start the whole thing going again.
		self.failUnless(childTag.RelativeURI(childTag.ResolveBase())=='','child element relative avoiding empty URI(%s)'%childTag.RelativeURI(childTag.ResolveBase()))
		grandChildTag=childTag._children[0]
		self.failUnless(grandChildTag.ResolveBase()=="file:///hello/base.xml","xml:base inherited")
		self.failUnless(grandChildTag.ResolveURI("link.xml")==altRef,"grandChild element HREF inherited")
		self.failUnless(grandChildTag.RelativeURI(href)=='..'+hrefPath,"grandChild element relative inherited: %s"%grandChildTag.RelativeURI(href))
		self.failUnless(grandChildTag.RelativeURI(altRef)=='link.xml','grandChild element relative inherited')
	
	def testCaseResolveLang(self):
		"""Test the use of ResolveLang"""
		parent=XMLElement(None)
		self.failUnless(parent.ResolveLang() is None,"No default language")
		parent.SetLang('en-GB')
		self.failUnless(parent.GetLang()=='en-GB',"Lang Get/Set")
		child=XMLElement(parent)
		self.failUnless(child.GetLang() is None,"No xml:lang by default")
		self.failUnless(child.ResolveLang()=='en-GB',"Lang inheritence")
		# repeat tests with a parent document
		d=XMLDocument()
		parent=XMLElement(d)
		self.failUnless(parent.ResolveLang() is None,"No default language")
		
	def testCaseCreate(self):
		"""Test the creating of the XMLDocument on the file system"""		
		CREATE_1_XML="""<?xml version="1.0" encoding="UTF-8"?>
<test/>"""
		d=XMLDocument(root=NamedElement)
		d.SetBase('create1.xml')
		d.Create()
		try:
			f=open("create1.xml")
			data=f.read()
			f.close()
			self.failUnless(data==CREATE_1_XML,"Create Test")
		except IOError:
			self.fail("Create Test failed to create file")
	
	def testCaseUpdate(self):
		"""Test the updating of the MXLDocument on the file system"""
		UPDATE_1_XML="""<?xml version="1.0" encoding="UTF-8"?>
<test>
	<test/>
</test>"""
		d=XMLDocument(root=NamedElement)
		d.SetBase('update1.xml')
		try:
			d.Update()
			self.fail("Update XMLDocument failed to spot missing file")
		except XMLMissingFileError:
			pass
		d.Create()
		d.root.ChildElement(NamedElement)
		d.Update()
		try:
			f=open("update1.xml")
			data=f.read()
			f.close()
			self.failUnless(data==UPDATE_1_XML,"Update Test")
		except IOError:
			self.fail("Update Test failed to update file")			
		
	def testCaseID(self):
		"""Test the built-in handling of a document's ID space."""
		doc=XMLDocument()
		e1=XMLElement(doc)
		e2=XMLElement(doc)
		e1.id=e2.id='test'
		doc.RegisterElement(e1)
		try:
			doc.RegisterElement(e2)
			self.fail("Failed to spot ID clash")
		except XMLIDClashError:
			pass
		e2.id='test2'
		doc.RegisterElement(e2)
		self.failUnless(doc.GetElementByID('test') is e1,"Element look-up failed")
		newID=doc.GetUniqueID('test')
		self.failIf(newID=='test' or newID=='test2')
	
	def testCaseReflection(self):
		"""Test the built-in handling of reflective attributes and elements."""
		REFLECTIVE_XML="""<?xml version="1.0" encoding="UTF-8"?>
<reflection atest="Hello"><etest>Hello Again</etest></reflection>"""
		f=StringIO(REFLECTIVE_XML)
		d=ReflectiveDocument()
		d.Read(src=f)
		root=d.root
		self.failUnless(isinstance(root,ReflectiveElement))
		self.failUnless(root.atest,"Attribute relfection")
		self.failUnless(root.child,"Element relfection")

		
if __name__ == "__main__":
	unittest.main()