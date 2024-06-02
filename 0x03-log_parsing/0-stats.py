#!/usr/bin/python3
import sys
import signal

file_size_total = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0,
    401: 0, 403: 0, 404: 0,
    405: 0, 500: 0
    }


def print_statistics():
    print("File size: {}".format(file_size_total))
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(
                "{}: {}".format(
                    status_code, status_code_counts[status_code]
                    )
                )


def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
for line in sys.stdin:
    try:
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        file_size_total += file_size
        status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

    except Exception as e:
        continue

print_statistics()
