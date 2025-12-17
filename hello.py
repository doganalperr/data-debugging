# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    first = first_name.capitalize() if first_name else ""
    last = last_name.capitalize() if last_name else ""

    if first and last:
        return f"{first} {last}"

    return first or last
