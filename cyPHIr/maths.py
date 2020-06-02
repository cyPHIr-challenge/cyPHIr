###The cyPHIr project, May - June 2020###
###Mathematical processing and the other shizzle required###

##The (only) required module - for arbitrary precision##

from sympy import *

##Constants##

SQRT5 = sqrt(5)
PHI = (SQRT5 + 1) / 2
PSI = (SQRT5 - 1) / 2                                                    # = 1/PHI = PHI - 1

##Main functions##

def inverse_fibb(n: int):
    
    '''Greatest n for which fibb(n) <= f, using Binet-type formula.'''
    
    k = floor(log(n*SQRT5 + 1/2, PHI))
    return k
    
def transform(a: int, b: int):
    
    '''Returns the expression a + bφ. (That's it).'''

    expr = a + b*PHI
    return expr

def log_lowest_difference(n: int):
    
    '''
    Returns the lowest logarithmic difference,
    log(|(a + bφ) - (a' + b'φ)|), between two distinct such expressions,
    where a, a', b, b' are integers such that 0 <= a, a', b, b' <= n with
    (a, b) != (a', b'). This is in essence calculating the value of

    log(min([
        abs(transform(p, -q)) for p in range(n + 1)
                              for q in range(n + 1)
                              if (p, q) != (0, 0)
            ]))

    where p := a - a', q := b - b'. However, this method would take
    O(n^2) time, which is horrendous for larger values of n.
    
    Fortunately, this can be calculated exactly, since this is exacly the
    problem of best Diophantine rational approximation - for φ, the best
    Diophantine approximants turn out to be the ratio between two
    consecutive Fibonacci numbers (which can be proven by looking at the
    continued fraction of φ, which turns out to be
    
                      1 + 1/(1 + 1/(1 + 1/(...))))
                      
    ); and it turns out that the simplest way to calculate this can be
    derived from Binet's formula - if F_k is the largest Fibonacci number
    below n, then the lowest absolute difference will be ψ^k/sqrt(5), and
    from this the logarithmic difference can be calculated exactly,
    without the previous issues of precision overflow which makes this
    problem difficult.
    
    Fun fact:
    did you know that φ is the most difficult number to approximate with
    rational numbers? It's almost like that was a deliberate design
    choice... (along with the fact that I'm not a fan of coding Pell's
    equation solutions for things like sqrt(2), which, although they are
    pretty neat, they really suck to reverse-engineer like what I'm doing
    here).
    '''
    
    k = inverse_fibb(n)
    logarithmic_difference = k*log(PSI) - log(SQRT5)
    return logarithmic_difference

def dp_needed_for_repr(n: int):
    
    '''
    The number of decimal places, d,  needed to guarantee that, for every
    0 <= a, b <= n, the values of (a, b) can be uniquely detemined given
    the value of a + bφ to d decimal places, under the conditions that
    0 <= a, b <= n (i.e, whenever 0 <= a, a', b, b' <= n with
    (a, b) != (a', b'), the values of a + bφ and a' + b'φ are distinct up
    to d decimal places). This can be determined directly from the value
    of lowest_difference(n); if d is such that

        |(a + bφ) - (a' + b'φ)| >= lowest_difference(n) >= 10^(-d)

    then we can guarantee that a + bφ and a' + b'φ will differ, at least
    up to d decimal places; from this, the minimal value of d can be
    determined. This also means that a unique decypherment of a + bφ to
    (a, b) exists.
    '''

    difference = log_lowest_difference(n)
    to_base_10 = -difference/log(10)
    decimal_places = ceiling(to_base_10)
    return decimal_places
    
def transform_to_decimal(a: int, b: int):

    '''
    Returns transform(a, b) to the number of decimal places determined by
    dp_needed_for_repr(a + bφ), so that a unique decypherment exists.
    Rounding is taken to be half up, half down as is standard - however,
    since the neither expression can be an exact non-integer decimal
    fraction, this won't affect the non-uniqueness. Since we can
    guarantee that a, b <= a + bφ, we can take this to be our value of n
    in dp_needed_for_repr.
    '''

    expr = transform(a, b)
    dp = dp_needed_for_repr(expr)
    string_form = str(S(expr).round(dp))
    return string_form
