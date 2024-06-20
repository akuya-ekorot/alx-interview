#!/usr/bin/python3

"""This script reads stdin line by line and computes metrics"""
import re
import sys
from typing import Any


def main():
    """Entry point to the script"""
    total_size = 0
    matched_lines = 0
    status_code_lines: dict[str, int] = {}

    try:
        for line in sys.stdin:
            matched_dict = parse_line(line)

            if matched_dict is None:
                continue

            matched_lines += 1
            total_size += int(matched_dict["size"])

            if matched_dict["status_code"] in status_code_lines:
                status_code_lines[matched_dict["status_code"]] += 1
            else:
                status_code_lines[matched_dict["status_code"]] = 1

            if matched_lines % 10 == 0:
                print_metrics(total_size, status_code_lines)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code_lines)
        raise


def parse_line(line: str) -> dict[str, str | Any] | None:
    """Parses a single line from stdin"""

    ip_pattern = r"^(?P<ip>(\d{1,3}\.?){4})"
    data_pattern = r"(?P<date>\[.*\])"
    endpoint_pattern = r"(?P<endpoint>\"GET /projects/260 HTTP/1\.1\")"
    status_code_pattern = r"(?P<status_code>200|301|400|401|403|404|405|500)"
    size_pattern = r"(?P<size>\d*)$"

    pattern = " ".join(
        [
            ip_pattern,
            r"-",
            data_pattern,
            endpoint_pattern,
            status_code_pattern,
            size_pattern,
        ]
    )

    match = re.search(pattern, line)

    if match is not None:
        return match.groupdict()


def print_metrics(total_size: int, status_code_lines: dict[str, int]):
    """Prints metrics to stdout"""

    print(f"File size: {total_size}")

    for status_code, size in sorted(status_code_lines.items()):
        print(f"{status_code}: {size}")


if __name__ == "__main__":
    main()
