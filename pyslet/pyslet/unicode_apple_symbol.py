""" Python Character Mapping Codec symbol generated from 'codecs/SYMBOL.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_map)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='apple-symbol',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({
    0x22: 0x2200,       #  FOR ALL
    0x24: 0x2203,       #  THERE EXISTS
    0x27: 0x220D,       #  SMALL CONTAINS AS MEMBER
    0x2A: 0x2217,       #  ASTERISK OPERATOR
    0x2D: 0x2212,       #  MINUS SIGN
    0x40: 0x2245,       #  APPROXIMATELY EQUAL TO
    0x41: 0x0391,       #  GREEK CAPITAL LETTER ALPHA
    0x42: 0x0392,       #  GREEK CAPITAL LETTER BETA
    0x43: 0x03A7,       #  GREEK CAPITAL LETTER CHI
    0x44: 0x0394,       #  GREEK CAPITAL LETTER DELTA
    0x45: 0x0395,       #  GREEK CAPITAL LETTER EPSILON
    0x46: 0x03A6,       #  GREEK CAPITAL LETTER PHI
    0x47: 0x0393,       #  GREEK CAPITAL LETTER GAMMA
    0x48: 0x0397,       #  GREEK CAPITAL LETTER ETA
    0x49: 0x0399,       #  GREEK CAPITAL LETTER IOTA
    0x4A: 0x03D1,       #  GREEK THETA SYMBOL
    0x4B: 0x039A,       #  GREEK CAPITAL LETTER KAPPA
    0x4C: 0x039B,       #  GREEK CAPITAL LETTER LAMDA
    0x4D: 0x039C,       #  GREEK CAPITAL LETTER MU
    0x4E: 0x039D,       #  GREEK CAPITAL LETTER NU
    0x4F: 0x039F,       #  GREEK CAPITAL LETTER OMICRON
    0x50: 0x03A0,       #  GREEK CAPITAL LETTER PI
    0x51: 0x0398,       #  GREEK CAPITAL LETTER THETA
    0x52: 0x03A1,       #  GREEK CAPITAL LETTER RHO
    0x53: 0x03A3,       #  GREEK CAPITAL LETTER SIGMA
    0x54: 0x03A4,       #  GREEK CAPITAL LETTER TAU
    0x55: 0x03A5,       #  GREEK CAPITAL LETTER UPSILON
    0x56: 0x03C2,       #  GREEK SMALL LETTER FINAL SIGMA
    0x57: 0x03A9,       #  GREEK CAPITAL LETTER OMEGA
    0x58: 0x039E,       #  GREEK CAPITAL LETTER XI
    0x59: 0x03A8,       #  GREEK CAPITAL LETTER PSI
    0x5A: 0x0396,       #  GREEK CAPITAL LETTER ZETA
    0x5C: 0x2234,       #  THEREFORE
    0x5E: 0x22A5,       #  UP TACK
    0x60: 0xF8E5,       #  radical extender # corporate char
    0x61: 0x03B1,       #  GREEK SMALL LETTER ALPHA
    0x62: 0x03B2,       #  GREEK SMALL LETTER BETA
    0x63: 0x03C7,       #  GREEK SMALL LETTER CHI
    0x64: 0x03B4,       #  GREEK SMALL LETTER DELTA
    0x65: 0x03B5,       #  GREEK SMALL LETTER EPSILON
    0x66: 0x03C6,       #  GREEK SMALL LETTER PHI
    0x67: 0x03B3,       #  GREEK SMALL LETTER GAMMA
    0x68: 0x03B7,       #  GREEK SMALL LETTER ETA
    0x69: 0x03B9,       #  GREEK SMALL LETTER IOTA
    0x6A: 0x03D5,       #  GREEK PHI SYMBOL
    0x6B: 0x03BA,       #  GREEK SMALL LETTER KAPPA
    0x6C: 0x03BB,       #  GREEK SMALL LETTER LAMDA
    0x6D: 0x03BC,       #  GREEK SMALL LETTER MU
    0x6E: 0x03BD,       #  GREEK SMALL LETTER NU
    0x6F: 0x03BF,       #  GREEK SMALL LETTER OMICRON
    0x70: 0x03C0,       #  GREEK SMALL LETTER PI
    0x71: 0x03B8,       #  GREEK SMALL LETTER THETA
    0x72: 0x03C1,       #  GREEK SMALL LETTER RHO
    0x73: 0x03C3,       #  GREEK SMALL LETTER SIGMA
    0x74: 0x03C4,       #  GREEK SMALL LETTER TAU
    0x75: 0x03C5,       #  GREEK SMALL LETTER UPSILON
    0x76: 0x03D6,       #  GREEK PI SYMBOL
    0x77: 0x03C9,       #  GREEK SMALL LETTER OMEGA
    0x78: 0x03BE,       #  GREEK SMALL LETTER XI
    0x79: 0x03C8,       #  GREEK SMALL LETTER PSI
    0x7A: 0x03B6,       #  GREEK SMALL LETTER ZETA
    0x7E: 0x223C,       #  TILDE OPERATOR
    0x80: None,
    0x81: None,
    0x82: None,
    0x83: None,
    0x84: None,
    0x85: None,
    0x86: None,
    0x87: None,
    0x88: None,
    0x89: None,
    0x8A: None,
    0x8B: None,
    0x8C: None,
    0x8D: None,
    0x8E: None,
    0x8F: None,
    0x90: None,
    0x91: None,
    0x92: None,
    0x93: None,
    0x94: None,
    0x95: None,
    0x96: None,
    0x97: None,
    0x98: None,
    0x99: None,
    0x9A: None,
    0x9B: None,
    0x9C: None,
    0x9D: None,
    0x9E: None,
    0x9F: None,
    0xA0: 0x20AC,       #  EURO SIGN
    0xA1: 0x03D2,       #  GREEK UPSILON WITH HOOK SYMBOL
    0xA2: 0x2032,       #  PRIME # minute
    0xA3: 0x2264,       #  LESS-THAN OR EQUAL TO
    0xA4: 0x2044,       #  FRACTION SLASH
    0xA5: 0x221E,       #  INFINITY
    0xA6: 0x0192,       #  LATIN SMALL LETTER F WITH HOOK
    0xA7: 0x2663,       #  BLACK CLUB SUIT
    0xA8: 0x2666,       #  BLACK DIAMOND SUIT
    0xA9: 0x2665,       #  BLACK HEART SUIT
    0xAA: 0x2660,       #  BLACK SPADE SUIT
    0xAB: 0x2194,       #  LEFT RIGHT ARROW
    0xAC: 0x2190,       #  LEFTWARDS ARROW
    0xAD: 0x2191,       #  UPWARDS ARROW
    0xAE: 0x2192,       #  RIGHTWARDS ARROW
    0xAF: 0x2193,       #  DOWNWARDS ARROW
    0xB2: 0x2033,       #  DOUBLE PRIME # second
    0xB3: 0x2265,       #  GREATER-THAN OR EQUAL TO
    0xB4: 0x00D7,       #  MULTIPLICATION SIGN
    0xB5: 0x221D,       #  PROPORTIONAL TO
    0xB6: 0x2202,       #  PARTIAL DIFFERENTIAL
    0xB7: 0x2022,       #  BULLET
    0xB8: 0x00F7,       #  DIVISION SIGN
    0xB9: 0x2260,       #  NOT EQUAL TO
    0xBA: 0x2261,       #  IDENTICAL TO
    0xBB: 0x2248,       #  ALMOST EQUAL TO
    0xBC: 0x2026,       #  HORIZONTAL ELLIPSIS
    0xBD: 0x23D0,       #  VERTICAL LINE EXTENSION (for arrows) # for Unicode 4.0 and later
    0xBE: 0x23AF,       #  HORIZONTAL LINE EXTENSION (for arrows) # for Unicode 3.2 and later
    0xBF: 0x21B5,       #  DOWNWARDS ARROW WITH CORNER LEFTWARDS
    0xC0: 0x2135,       #  ALEF SYMBOL
    0xC1: 0x2111,       #  BLACK-LETTER CAPITAL I
    0xC2: 0x211C,       #  BLACK-LETTER CAPITAL R
    0xC3: 0x2118,       #  SCRIPT CAPITAL P
    0xC4: 0x2297,       #  CIRCLED TIMES
    0xC5: 0x2295,       #  CIRCLED PLUS
    0xC6: 0x2205,       #  EMPTY SET
    0xC7: 0x2229,       #  INTERSECTION
    0xC8: 0x222A,       #  UNION
    0xC9: 0x2283,       #  SUPERSET OF
    0xCA: 0x2287,       #  SUPERSET OF OR EQUAL TO
    0xCB: 0x2284,       #  NOT A SUBSET OF
    0xCC: 0x2282,       #  SUBSET OF
    0xCD: 0x2286,       #  SUBSET OF OR EQUAL TO
    0xCE: 0x2208,       #  ELEMENT OF
    0xCF: 0x2209,       #  NOT AN ELEMENT OF
    0xD0: 0x2220,       #  ANGLE
    0xD1: 0x2207,       #  NABLA
    0xD2: 0x00AE,       #  REGISTERED SIGN # serif
    0xD3: 0x00A9,       #  COPYRIGHT SIGN # serif
    0xD4: 0x2122,       #  TRADE MARK SIGN # serif
    0xD5: 0x220F,       #  N-ARY PRODUCT
    0xD6: 0x221A,       #  SQUARE ROOT
    0xD7: 0x22C5,       #  DOT OPERATOR
    0xD8: 0x00AC,       #  NOT SIGN
    0xD9: 0x2227,       #  LOGICAL AND
    0xDA: 0x2228,       #  LOGICAL OR
    0xDB: 0x21D4,       #  LEFT RIGHT DOUBLE ARROW
    0xDC: 0x21D0,       #  LEFTWARDS DOUBLE ARROW
    0xDD: 0x21D1,       #  UPWARDS DOUBLE ARROW
    0xDE: 0x21D2,       #  RIGHTWARDS DOUBLE ARROW
    0xDF: 0x21D3,       #  DOWNWARDS DOUBLE ARROW
    0xE0: 0x25CA,       #  LOZENGE # previously mapped to 0x22C4 DIAMOND OPERATOR
    0xE1: 0x3008,       #  LEFT ANGLE BRACKET
    0xE2: (0x00AE, 0xF87F),     #  REGISTERED SIGN, alternate: sans serif
    0xE3: (0x00A9, 0xF87F),     #  COPYRIGHT SIGN, alternate: sans serif
    0xE4: (0x2122, 0xF87F),     #  TRADE MARK SIGN, alternate: sans serif
    0xE5: 0x2211,       #  N-ARY SUMMATION
    0xE6: 0x239B,       #  LEFT PARENTHESIS UPPER HOOK # for Unicode 3.2 and later
    0xE7: 0x239C,       #  LEFT PARENTHESIS EXTENSION # for Unicode 3.2 and later
    0xE8: 0x239D,       #  LEFT PARENTHESIS LOWER HOOK # for Unicode 3.2 and later
    0xE9: 0x23A1,       #  LEFT SQUARE BRACKET UPPER CORNER # for Unicode 3.2 and later
    0xEA: 0x23A2,       #  LEFT SQUARE BRACKET EXTENSION # for Unicode 3.2 and later
    0xEB: 0x23A3,       #  LEFT SQUARE BRACKET LOWER CORNER # for Unicode 3.2 and later
    0xEC: 0x23A7,       #  LEFT CURLY BRACKET UPPER HOOK # for Unicode 3.2 and later
    0xED: 0x23A8,       #  LEFT CURLY BRACKET MIDDLE PIECE # for Unicode 3.2 and later
    0xEE: 0x23A9,       #  LEFT CURLY BRACKET LOWER HOOK # for Unicode 3.2 and later
    0xEF: 0x23AA,       #  CURLY BRACKET EXTENSION # for Unicode 3.2 and later
    0xF0: 0xF8FF,       #  Apple logo
    0xF1: 0x3009,       #  RIGHT ANGLE BRACKET
    0xF2: 0x222B,       #  INTEGRAL
    0xF3: 0x2320,       #  TOP HALF INTEGRAL
    0xF4: 0x23AE,       #  INTEGRAL EXTENSION # for Unicode 3.2 and later
    0xF5: 0x2321,       #  BOTTOM HALF INTEGRAL
    0xF6: 0x239E,       #  RIGHT PARENTHESIS UPPER HOOK # for Unicode 3.2 and later
    0xF7: 0x239F,       #  RIGHT PARENTHESIS EXTENSION # for Unicode 3.2 and later
    0xF8: 0x23A0,       #  RIGHT PARENTHESIS LOWER HOOK # for Unicode 3.2 and later
    0xF9: 0x23A4,       #  RIGHT SQUARE BRACKET UPPER CORNER # for Unicode 3.2 and later
    0xFA: 0x23A5,       #  RIGHT SQUARE BRACKET EXTENSION # for Unicode 3.2 and later
    0xFB: 0x23A6,       #  RIGHT SQUARE BRACKET LOWER CORNER # for Unicode 3.2 and later
    0xFC: 0x23AB,       #  RIGHT CURLY BRACKET UPPER HOOK # for Unicode 3.2 and later
    0xFD: 0x23AC,       #  RIGHT CURLY BRACKET MIDDLE PIECE # for Unicode 3.2 and later
    0xFE: 0x23AD,       #  RIGHT CURLY BRACKET LOWER HOOK # for Unicode 3.2 and later
    0xFF: None,
})

### Encoding Map

encoding_map = {
    0x0000: 0x00,       #  CONTROL CHARACTER
    0x0001: 0x01,       #  CONTROL CHARACTER
    0x0002: 0x02,       #  CONTROL CHARACTER
    0x0003: 0x03,       #  CONTROL CHARACTER
    0x0004: 0x04,       #  CONTROL CHARACTER
    0x0005: 0x05,       #  CONTROL CHARACTER
    0x0006: 0x06,       #  CONTROL CHARACTER
    0x0007: 0x07,       #  CONTROL CHARACTER
    0x0008: 0x08,       #  CONTROL CHARACTER
    0x0009: 0x09,       #  CONTROL CHARACTER
    0x000A: 0x0A,       #  CONTROL CHARACTER
    0x000B: 0x0B,       #  CONTROL CHARACTER
    0x000C: 0x0C,       #  CONTROL CHARACTER
    0x000D: 0x0D,       #  CONTROL CHARACTER
    0x000E: 0x0E,       #  CONTROL CHARACTER
    0x000F: 0x0F,       #  CONTROL CHARACTER
    0x0010: 0x10,       #  CONTROL CHARACTER
    0x0011: 0x11,       #  CONTROL CHARACTER
    0x0012: 0x12,       #  CONTROL CHARACTER
    0x0013: 0x13,       #  CONTROL CHARACTER
    0x0014: 0x14,       #  CONTROL CHARACTER
    0x0015: 0x15,       #  CONTROL CHARACTER
    0x0016: 0x16,       #  CONTROL CHARACTER
    0x0017: 0x17,       #  CONTROL CHARACTER
    0x0018: 0x18,       #  CONTROL CHARACTER
    0x0019: 0x19,       #  CONTROL CHARACTER
    0x001A: 0x1A,       #  CONTROL CHARACTER
    0x001B: 0x1B,       #  CONTROL CHARACTER
    0x001C: 0x1C,       #  CONTROL CHARACTER
    0x001D: 0x1D,       #  CONTROL CHARACTER
    0x001E: 0x1E,       #  CONTROL CHARACTER
    0x001F: 0x1F,       #  CONTROL CHARACTER
    0x0020: 0x20,       #  SPACE
    0x0021: 0x21,       #  EXCLAMATION MARK
    0x0023: 0x23,       #  NUMBER SIGN
    0x0025: 0x25,       #  PERCENT SIGN
    0x0026: 0x26,       #  AMPERSAND
    0x0028: 0x28,       #  LEFT PARENTHESIS
    0x0029: 0x29,       #  RIGHT PARENTHESIS
    0x002B: 0x2B,       #  PLUS SIGN
    0x002C: 0x2C,       #  COMMA
    0x002E: 0x2E,       #  FULL STOP
    0x002F: 0x2F,       #  SOLIDUS
    0x0030: 0x30,       #  DIGIT ZERO
    0x0031: 0x31,       #  DIGIT ONE
    0x0032: 0x32,       #  DIGIT TWO
    0x0033: 0x33,       #  DIGIT THREE
    0x0034: 0x34,       #  DIGIT FOUR
    0x0035: 0x35,       #  DIGIT FIVE
    0x0036: 0x36,       #  DIGIT SIX
    0x0037: 0x37,       #  DIGIT SEVEN
    0x0038: 0x38,       #  DIGIT EIGHT
    0x0039: 0x39,       #  DIGIT NINE
    0x003A: 0x3A,       #  COLON
    0x003B: 0x3B,       #  SEMICOLON
    0x003C: 0x3C,       #  LESS-THAN SIGN
    0x003D: 0x3D,       #  EQUALS SIGN
    0x003E: 0x3E,       #  GREATER-THAN SIGN
    0x003F: 0x3F,       #  QUESTION MARK
    0x005B: 0x5B,       #  LEFT SQUARE BRACKET
    0x005D: 0x5D,       #  RIGHT SQUARE BRACKET
    0x005F: 0x5F,       #  LOW LINE
    0x007B: 0x7B,       #  LEFT CURLY BRACKET
    0x007C: 0x7C,       #  VERTICAL LINE
    0x007D: 0x7D,       #  RIGHT CURLY BRACKET
    0x007F: 0x7F,       #  CONTROL CHARACTER
    0x00A9: 0xD3,       #  COPYRIGHT SIGN # serif
    0x00AC: 0xD8,       #  NOT SIGN
    0x00AE: 0xD2,       #  REGISTERED SIGN # serif
    0x00B0: 0xB0,       #  DEGREE SIGN
    0x00B1: 0xB1,       #  PLUS-MINUS SIGN
    0x00D7: 0xB4,       #  MULTIPLICATION SIGN
    0x00F7: 0xB8,       #  DIVISION SIGN
    0x0192: 0xA6,       #  LATIN SMALL LETTER F WITH HOOK
    0x0391: 0x41,       #  GREEK CAPITAL LETTER ALPHA
    0x0392: 0x42,       #  GREEK CAPITAL LETTER BETA
    0x0393: 0x47,       #  GREEK CAPITAL LETTER GAMMA
    0x0394: 0x44,       #  GREEK CAPITAL LETTER DELTA
    0x0395: 0x45,       #  GREEK CAPITAL LETTER EPSILON
    0x0396: 0x5A,       #  GREEK CAPITAL LETTER ZETA
    0x0397: 0x48,       #  GREEK CAPITAL LETTER ETA
    0x0398: 0x51,       #  GREEK CAPITAL LETTER THETA
    0x0399: 0x49,       #  GREEK CAPITAL LETTER IOTA
    0x039A: 0x4B,       #  GREEK CAPITAL LETTER KAPPA
    0x039B: 0x4C,       #  GREEK CAPITAL LETTER LAMDA
    0x039C: 0x4D,       #  GREEK CAPITAL LETTER MU
    0x039D: 0x4E,       #  GREEK CAPITAL LETTER NU
    0x039E: 0x58,       #  GREEK CAPITAL LETTER XI
    0x039F: 0x4F,       #  GREEK CAPITAL LETTER OMICRON
    0x03A0: 0x50,       #  GREEK CAPITAL LETTER PI
    0x03A1: 0x52,       #  GREEK CAPITAL LETTER RHO
    0x03A3: 0x53,       #  GREEK CAPITAL LETTER SIGMA
    0x03A4: 0x54,       #  GREEK CAPITAL LETTER TAU
    0x03A5: 0x55,       #  GREEK CAPITAL LETTER UPSILON
    0x03A6: 0x46,       #  GREEK CAPITAL LETTER PHI
    0x03A7: 0x43,       #  GREEK CAPITAL LETTER CHI
    0x03A8: 0x59,       #  GREEK CAPITAL LETTER PSI
    0x03A9: 0x57,       #  GREEK CAPITAL LETTER OMEGA
    0x03B1: 0x61,       #  GREEK SMALL LETTER ALPHA
    0x03B2: 0x62,       #  GREEK SMALL LETTER BETA
    0x03B3: 0x67,       #  GREEK SMALL LETTER GAMMA
    0x03B4: 0x64,       #  GREEK SMALL LETTER DELTA
    0x03B5: 0x65,       #  GREEK SMALL LETTER EPSILON
    0x03B6: 0x7A,       #  GREEK SMALL LETTER ZETA
    0x03B7: 0x68,       #  GREEK SMALL LETTER ETA
    0x03B8: 0x71,       #  GREEK SMALL LETTER THETA
    0x03B9: 0x69,       #  GREEK SMALL LETTER IOTA
    0x03BA: 0x6B,       #  GREEK SMALL LETTER KAPPA
    0x03BB: 0x6C,       #  GREEK SMALL LETTER LAMDA
    0x03BC: 0x6D,       #  GREEK SMALL LETTER MU
    0x03BD: 0x6E,       #  GREEK SMALL LETTER NU
    0x03BE: 0x78,       #  GREEK SMALL LETTER XI
    0x03BF: 0x6F,       #  GREEK SMALL LETTER OMICRON
    0x03C0: 0x70,       #  GREEK SMALL LETTER PI
    0x03C1: 0x72,       #  GREEK SMALL LETTER RHO
    0x03C2: 0x56,       #  GREEK SMALL LETTER FINAL SIGMA
    0x03C3: 0x73,       #  GREEK SMALL LETTER SIGMA
    0x03C4: 0x74,       #  GREEK SMALL LETTER TAU
    0x03C5: 0x75,       #  GREEK SMALL LETTER UPSILON
    0x03C6: 0x66,       #  GREEK SMALL LETTER PHI
    0x03C7: 0x63,       #  GREEK SMALL LETTER CHI
    0x03C8: 0x79,       #  GREEK SMALL LETTER PSI
    0x03C9: 0x77,       #  GREEK SMALL LETTER OMEGA
    0x03D1: 0x4A,       #  GREEK THETA SYMBOL
    0x03D2: 0xA1,       #  GREEK UPSILON WITH HOOK SYMBOL
    0x03D5: 0x6A,       #  GREEK PHI SYMBOL
    0x03D6: 0x76,       #  GREEK PI SYMBOL
    0x2022: 0xB7,       #  BULLET
    0x2026: 0xBC,       #  HORIZONTAL ELLIPSIS
    0x2032: 0xA2,       #  PRIME # minute
    0x2033: 0xB2,       #  DOUBLE PRIME # second
    0x2044: 0xA4,       #  FRACTION SLASH
    0x20AC: 0xA0,       #  EURO SIGN
    0x2111: 0xC1,       #  BLACK-LETTER CAPITAL I
    0x2118: 0xC3,       #  SCRIPT CAPITAL P
    0x211C: 0xC2,       #  BLACK-LETTER CAPITAL R
    0x2122: 0xD4,       #  TRADE MARK SIGN # serif
    0x2135: 0xC0,       #  ALEF SYMBOL
    0x2190: 0xAC,       #  LEFTWARDS ARROW
    0x2191: 0xAD,       #  UPWARDS ARROW
    0x2192: 0xAE,       #  RIGHTWARDS ARROW
    0x2193: 0xAF,       #  DOWNWARDS ARROW
    0x2194: 0xAB,       #  LEFT RIGHT ARROW
    0x21B5: 0xBF,       #  DOWNWARDS ARROW WITH CORNER LEFTWARDS
    0x21D0: 0xDC,       #  LEFTWARDS DOUBLE ARROW
    0x21D1: 0xDD,       #  UPWARDS DOUBLE ARROW
    0x21D2: 0xDE,       #  RIGHTWARDS DOUBLE ARROW
    0x21D3: 0xDF,       #  DOWNWARDS DOUBLE ARROW
    0x21D4: 0xDB,       #  LEFT RIGHT DOUBLE ARROW
    0x2200: 0x22,       #  FOR ALL
    0x2202: 0xB6,       #  PARTIAL DIFFERENTIAL
    0x2203: 0x24,       #  THERE EXISTS
    0x2205: 0xC6,       #  EMPTY SET
    0x2207: 0xD1,       #  NABLA
    0x2208: 0xCE,       #  ELEMENT OF
    0x2209: 0xCF,       #  NOT AN ELEMENT OF
    0x220D: 0x27,       #  SMALL CONTAINS AS MEMBER
    0x220F: 0xD5,       #  N-ARY PRODUCT
    0x2211: 0xE5,       #  N-ARY SUMMATION
    0x2212: 0x2D,       #  MINUS SIGN
    0x2217: 0x2A,       #  ASTERISK OPERATOR
    0x221A: 0xD6,       #  SQUARE ROOT
    0x221D: 0xB5,       #  PROPORTIONAL TO
    0x221E: 0xA5,       #  INFINITY
    0x2220: 0xD0,       #  ANGLE
    0x2227: 0xD9,       #  LOGICAL AND
    0x2228: 0xDA,       #  LOGICAL OR
    0x2229: 0xC7,       #  INTERSECTION
    0x222A: 0xC8,       #  UNION
    0x222B: 0xF2,       #  INTEGRAL
    0x2234: 0x5C,       #  THEREFORE
    0x223C: 0x7E,       #  TILDE OPERATOR
    0x2245: 0x40,       #  APPROXIMATELY EQUAL TO
    0x2248: 0xBB,       #  ALMOST EQUAL TO
    0x2260: 0xB9,       #  NOT EQUAL TO
    0x2261: 0xBA,       #  IDENTICAL TO
    0x2264: 0xA3,       #  LESS-THAN OR EQUAL TO
    0x2265: 0xB3,       #  GREATER-THAN OR EQUAL TO
    0x2282: 0xCC,       #  SUBSET OF
    0x2283: 0xC9,       #  SUPERSET OF
    0x2284: 0xCB,       #  NOT A SUBSET OF
    0x2286: 0xCD,       #  SUBSET OF OR EQUAL TO
    0x2287: 0xCA,       #  SUPERSET OF OR EQUAL TO
    0x2295: 0xC5,       #  CIRCLED PLUS
    0x2297: 0xC4,       #  CIRCLED TIMES
    0x22A5: 0x5E,       #  UP TACK
    0x22C5: 0xD7,       #  DOT OPERATOR
    0x2320: 0xF3,       #  TOP HALF INTEGRAL
    0x2321: 0xF5,       #  BOTTOM HALF INTEGRAL
    0x239B: 0xE6,       #  LEFT PARENTHESIS UPPER HOOK # for Unicode 3.2 and later
    0x239C: 0xE7,       #  LEFT PARENTHESIS EXTENSION # for Unicode 3.2 and later
    0x239D: 0xE8,       #  LEFT PARENTHESIS LOWER HOOK # for Unicode 3.2 and later
    0x239E: 0xF6,       #  RIGHT PARENTHESIS UPPER HOOK # for Unicode 3.2 and later
    0x239F: 0xF7,       #  RIGHT PARENTHESIS EXTENSION # for Unicode 3.2 and later
    0x23A0: 0xF8,       #  RIGHT PARENTHESIS LOWER HOOK # for Unicode 3.2 and later
    0x23A1: 0xE9,       #  LEFT SQUARE BRACKET UPPER CORNER # for Unicode 3.2 and later
    0x23A2: 0xEA,       #  LEFT SQUARE BRACKET EXTENSION # for Unicode 3.2 and later
    0x23A3: 0xEB,       #  LEFT SQUARE BRACKET LOWER CORNER # for Unicode 3.2 and later
    0x23A4: 0xF9,       #  RIGHT SQUARE BRACKET UPPER CORNER # for Unicode 3.2 and later
    0x23A5: 0xFA,       #  RIGHT SQUARE BRACKET EXTENSION # for Unicode 3.2 and later
    0x23A6: 0xFB,       #  RIGHT SQUARE BRACKET LOWER CORNER # for Unicode 3.2 and later
    0x23A7: 0xEC,       #  LEFT CURLY BRACKET UPPER HOOK # for Unicode 3.2 and later
    0x23A8: 0xED,       #  LEFT CURLY BRACKET MIDDLE PIECE # for Unicode 3.2 and later
    0x23A9: 0xEE,       #  LEFT CURLY BRACKET LOWER HOOK # for Unicode 3.2 and later
    0x23AA: 0xEF,       #  CURLY BRACKET EXTENSION # for Unicode 3.2 and later
    0x23AB: 0xFC,       #  RIGHT CURLY BRACKET UPPER HOOK # for Unicode 3.2 and later
    0x23AC: 0xFD,       #  RIGHT CURLY BRACKET MIDDLE PIECE # for Unicode 3.2 and later
    0x23AD: 0xFE,       #  RIGHT CURLY BRACKET LOWER HOOK # for Unicode 3.2 and later
    0x23AE: 0xF4,       #  INTEGRAL EXTENSION # for Unicode 3.2 and later
    0x23AF: 0xBE,       #  HORIZONTAL LINE EXTENSION (for arrows) # for Unicode 3.2 and later
    0x23D0: 0xBD,       #  VERTICAL LINE EXTENSION (for arrows) # for Unicode 4.0 and later
    0x25CA: 0xE0,       #  LOZENGE # previously mapped to 0x22C4 DIAMOND OPERATOR
    0x2660: 0xAA,       #  BLACK SPADE SUIT
    0x2663: 0xA7,       #  BLACK CLUB SUIT
    0x2665: 0xA9,       #  BLACK HEART SUIT
    0x2666: 0xA8,       #  BLACK DIAMOND SUIT
    0x3008: 0xE1,       #  LEFT ANGLE BRACKET
    0x3009: 0xF1,       #  RIGHT ANGLE BRACKET
    0xF8E5: 0x60,       #  radical extender # corporate char
    0xF8FF: 0xF0,       #  Apple logo
    (0x00A9, 0xF87F): 0xE3,     #  COPYRIGHT SIGN, alternate: sans serif
    (0x00AE, 0xF87F): 0xE2,     #  REGISTERED SIGN, alternate: sans serif
    (0x2122, 0xF87F): 0xE4,     #  TRADE MARK SIGN, alternate: sans serif
}
