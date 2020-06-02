###The cyPHIr project, May - June 2020###
###String processing and the other shizzle required###

##Constants##

BYTEORDER = 'big'
ENCODING = 'latin-1'                                                     #UTF-8 has a system which means some strings of bytes cannot be converted to plaintext

##Main functions##

def separate(text: str):

    '''
    Splits a string into two equal-length substrings, representing a and
    b respectively. The text will be padded with ' ' so as to ensure that
    the strings can be of equal length, preventing any bytes from being
    obtained straight-off
    Potential code-breakers:
    This might be the opportunity to hack, but I'm not completely sure.
    '''

    text += ' '*(len(text)%2)
    index = len(text) // 2
    a_string, b_string = text[:index], text[index:] 
    return a_string, b_string

def to_int(text: str):

    '''
    Converts a string into an integer, by converting to and from bytes
    using the ENCODING and BYTEORDER as above. Inverse of to_text.
    '''

    byte_string = text.encode(ENCODING)
    return int.from_bytes(byte_string, byteorder = BYTEORDER)

def to_text(n: int):

    '''
    Converts an integer into a string, by converting to and from bytes
    using the ENCODING and BYTEORDER as above. Inverse of to_int.
    '''

    byte_string = (n).to_bytes((n.bit_length() + 7) // 8, byteorder = BYTEORDER)
    return byte_string.decode(ENCODING)
