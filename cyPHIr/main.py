###The cyPHIr project, May - June 2020###
###The main functions, encoding and decoding###

###Other modules###

import maths
import strings
import os

###Needed constant###

ESCAPE = 'unicode-escape'

###The main functions###

def encode(text: str):

    '''
    Encodes the text. The string is split into two components, which are
    converted into two integers, a and b. The encoded value is then
    a + bφ, to the minimal number of decimal places required to make sure
    that these are the only such a, b which will generate these values.
    '''

    a_string, b_string = strings.separate(text)
    a, b = strings.to_int(a_string), strings.to_int(b_string)
    string_form = maths.transform_to_decimal(a, b)
    return a, b, string_form

def decode(a: int, b: int):

    '''
    Decodes pair of integers into a single string, using the decoding
    method described in string.
    '''

    a_string, b_string = strings.to_text(a), strings.to_text(b)
    text = f'{a_string}{b_string}'
    return text

def cyphir(input_file: str, output_dir: str):

    '''
    Encodes the text in the input_file into a string, which can be
    interpreted as two integers, split by a decimal point. These two
    integers, p and q, will be written into two files within the
    output_dir, alongside the exact expression a + bφ, the values of a
    and b, and the plaintext.
    For the challenge:
    Only p, q and the exact expression will be given. a, b and the
    plaintext will remain secret.
    '''
    
    lines = open(input_file, 'r').readlines()
    text = '\n'.join(lines)
    print(text)
    
    a, b, string_form = encode(text)
    
    p_string, q_string = string_form.split('.')
    p, q = int(p_string), int(q_string)
    p_to_text, q_to_text = strings.to_text(p), \
                           strings.to_text(q)
    p_encoded, q_encoded = p_to_text.encode(strings.ENCODING).decode(ESCAPE), \
                           q_to_text.encode(strings.ENCODING).decode(ESCAPE)
    
    if not os.path.isdir(output_dir):                                    #Producing a directory if one does not exist already
        os.mkdir(output_dir)
    
    with open(f'{output_dir}\expression.txt', 'w') as file_expr, \
         open(f'{output_dir}\plain_text.txt', 'w') as file_text:         #Producing the files
        file_expr.write(f'Solve, for a, b >= 0 integer, a + b*PHI = {string_form}'), file_text.write(text)
        
    with open(f'{output_dir}\plain_text_a.txt', 'w') as file_a, \
         open(f'{output_dir}\plain_text_b.txt', 'w') as file_b:
        file_a.write(str(a)), file_b.write(str(b))
        
    with open(f'{output_dir}\cyphir_text_p.txt', 'w', encoding = strings.ENCODING) as file_p, \
         open(f'{output_dir}\cyphir_text_q.txt', 'w', encoding = strings.ENCODING) as file_q:
        file_p.write(p_encoded), file_q.write(q_encoded)
    
    summary = f'a = {a}\nb = {b}\np = {p_encoded}\nq = {q_encoded}\nexpr = {string_form}\nText encoded. Please open {output_dir}'
    print(summary)
    
if __name__ == '__main__':                                               #Demonstrating an example, with input from the user

    plain_text = input('Plain Text\n')
    input_file, output_dir = '.\plain_text.txt', '.\encoded'
    
    with open(input_file, 'w') as file_text:
        file_text.write(plain_text)
        
    cyphir(input_file, output_dir)
