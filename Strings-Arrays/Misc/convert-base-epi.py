# Given a number as a string in base b1, convert it to base b2 and return the result as a string
import string
import functools

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    def convert_from_base(num_as_int, base):
        if num_as_int == 0:
            return ''
        else:
            return convert_from_base(num_as_int//base, base) + string.hexdigits[num_as_int % base].upper()
        
        
    is_negative = num_as_string[0] == '-'
    convert_to_int = lambda x, c: x * b1 + string.hexdigits.index(c.lower())
    num_as_int = reduce(convert_to_int, num_as_string[is_negative:],0)

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                        convert_from_base(num_as_int, b2))