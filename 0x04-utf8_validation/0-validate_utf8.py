#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a
    valid UTF-8 encoding
    """
    def is_continuation_byte(byte):
        return (byte & 0xC0) == 0x80

    i = 0
    while i < len(data):
        first_byte = data[i]

        if first_byte < 0x80:  # 1-byte character
            i += 1
            continue

        num_bytes = 0
        if (first_byte & 0xE0) == 0xC0:  # 2-byte character
            num_bytes = 2
        elif (first_byte & 0xF0) == 0xE0:  # 3-byte character
            num_bytes = 3
        elif (first_byte & 0xF8) == 0xF0:  # 4-byte character
            num_bytes = 4
        else:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if not is_continuation_byte(data[i + j]):
                return False

        i += num_bytes

    return True
