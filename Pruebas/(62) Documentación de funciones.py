# Imprime la documentación de las funciones que queramos

from math import sin
from datetime import datetime

print(f"Información sobre la funcióna abs: {abs.__doc__}")
print(f"\nInformación sobre la funcióna int: {int.__doc__}")
print(f"\nInformación sobre la funcióna sin: {sin.__doc__}")
print(f"\nInformación sobre la funcióna now: {datetime.now.__doc__}")


# Lo que aparece al ejecutar el programa
'''
Información sobre la funcióna abs: Return the absolute value of the argument.

Información sobre la funcióna int: int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4

Información sobre la funcióna sin: Return the sine of x (measured in radians).

Información sobre la funcióna now: Returns new datetime object representing current time local to tz.

  tz
    Timezone object.

If no tz is specified, uses local timezone.
'''