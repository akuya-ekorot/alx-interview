#!/usr/bin/env python3
"""Validate UTF-8"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determine if a given data set represents a valid UTF-8 encoding"""

    try:
        is_valid = True
        for i in range(len(data)):
            if data[i] > 255:
                return False
            if is_valid_one_byte(data[i]):
                is_valid = is_valid and True
            elif is_valid_two_byte(data[i]):
                is_valid = is_valid and is_cont_byte(data[i + 1])
                i += 1
            elif is_valid_three_byte(data[i]):
                is_valid = is_valid and (
                    is_cont_byte(data[i + 1]) and
                    is_cont_byte(data[i + 2])
                )
                i += 2
            elif is_valid_four_byte(data[i]):
                is_valid = is_valid and (
                    is_cont_byte(data[i + 1]) and
                    is_cont_byte(data[i + 2]) and
                    is_cont_byte(data[i + 3])
                )
                i += 3
            else:
                return False
        return is_valid
    except Exception as e:
        return False


def is_valid_one_byte(byte: int) -> bool:
    """Check if a byte is a valid one-byte UTF-8 character"""
    return byte & 0b10000000 == 0


def is_valid_two_byte(byte: int) -> bool:
    """Check if a byte is the first of a valid two-byte UTF-8 character"""
    return byte & 0b11100000 == 0b11000000


def is_valid_three_byte(byte: int) -> bool:
    """Check if a byte is the first of a valid three-byte UTF-8 character"""
    return byte & 0b11110000 == 0b11100000


def is_valid_four_byte(byte: int) -> bool:
    """Check if a byte is the first of a valid four-byte UTF-8 character"""
    return byte & 0b11111000 == 0b11110000


def is_cont_byte(byte: int) -> bool:
    """Check if a byte is a continuation byte"""
    return byte & 0b11000000 == 0b10000000
