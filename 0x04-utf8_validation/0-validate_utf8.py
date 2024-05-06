#!/usr/bin/python3
"""utf-8 validation function"""


def validUTF8(data):
    """Returns true if data is a valid encoding format else false"""
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow > 0:
            if not (byte & 0b11000000 == 0b10000000):
                return False
            bytes_to_follow -= 1
        else:
            if byte & 0b10000000 == 0:
                bytes_to_follow = 0
            elif byte & 0b11100000 == 0b11000000:
                bytes_to_follow = 1
            elif byte & 0b11110000 == 0b11100000:
                bytes_to_follow = 2
            elif byte & 0b11111000 == 0b11110000:
                bytes_to_follow = 3
            else:
                return False
    return bytes_to_follow == 0
