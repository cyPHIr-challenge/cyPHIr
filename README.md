# cyPHIr
## Introduction
*The cyPHIr challenge, this is it. Good luck.*
>```Solve, for a, b > 0 integer, a + bφ = 54888123178151685205915137560908906060865342614076076665795104078791496513184138083199713539943106875002116863434467670136728818193392804188033781550750098664018174.946099739052692422941959197011523537188662924717211208426240782739867621436656591257567592697983116889035922719750395238578929173046887044739879027405909570162421204```

By use of Diophantine approximation, it can be shown that exactly one solution exists for such `a` and `b`, where all rounding is taken to be half-up/half-down as is IEEE standard. *When decoded, the values of a and b reveal instructions for completion (see **Usage** below).*

The method of encryption works as follows: a string, `text`, is separated into two equal-sized substrings, `a_string` and `b_string`. Using the inbuilt int-to-bytes, the values are converted into two positive integers, `a` and `b`. The expression `a + bφ` is then calculated to enough decimal places to ensure exactly one solution exists (see cyPHIr/maths.py for more details about this). This is the ciphertext, and can be split into two values by the decimal point, `p` and `q`, which can be reconverted into byteform (this last stage is unnecessary, but is still included for interest's sake). The challenge is to calculate the values of `a` and `b` - once they have been found, the original string can be easily recovered.

>*Fun fact: did you know that φ is the most difficult number to approximate with rational numbers? It's almost like that was a deliberate design choice... (along with the fact that I'm not a fan of coding Pell's equation solutions for things like sqrt(2), which, although they are pretty neat, they really suck to reverse-engineer like what I'm doing here).*
## Usage
To encode given text:
```
from cyPHIr import main
_, _, cyphir_text = main.encode(plain_text)
```
and to decode, knowing values of *a* and *b*:
```
from cyPHIr import main
plain_text = main.decode(a, b)
```
## Notes
* Read https://en.wikipedia.org/wiki/Diophantine_approximation for some more details about Diophantine approximation.
* No, I am not a numerologist etc. I just chose φ because this makes the mathematics far simpler.
* Any other questions, email cyphir.challenge@gmail.com
* The competition will closed in exactly one year, or until the first correct solution arrives.
