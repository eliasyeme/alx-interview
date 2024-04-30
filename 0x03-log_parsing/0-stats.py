#!/usr/bin/python3
"""Log Parsing"""
import sys

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0
count = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        tokens = line.split()
        if len(tokens) < 7:
            continue
        if tokens[-2] in status_codes:
            status_codes[tokens[-2]] += 1
        total_size += int(tokens[-1])
        count += 1
        if count == 10:
            print(f"File size: {total_size}")
            for k, v in sorted(status_codes.items()):
                if v:
                    print(f"{k}: {v}")
            count = 0
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for k, v in sorted(status_codes.items()):
        if v:
            print(f"{k}: {v}")
    raise
print(f"File size: {total_size}")
for k, v in sorted(status_codes.items()):
    if v:
        print(f"{k}: {v}")
