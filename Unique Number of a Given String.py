def unique_numbers(s: str) -> set:
    return set(filter(str.isdigit, s))
Frequency of a Digit:

python
from collections import Counter
def frequency_of_digits(s: str) -> dict:
    return dict(Counter(filter(str.isdigit, s)))
Diwali Lights Problem:

python
def diwali_lights(n: int) -> int:
    return (2**n)