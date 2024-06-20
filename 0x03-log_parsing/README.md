# Log Parsing

This project focuses on parsing and processing data streams in real-time.

The script `./0-stats.py` reads `stdin` and computes metrics:

- Input format:
  - `<IP-Address> - [<date>] "GET /projects/260 HTTP/1.1" <status-code> <file-size>`
  - If the format is not like this skip the line
- After every 10 lines and/or a keyboard interruption (CTRL + C),
  print these statistics from the beginning:
  - Total file size:
    - File size: where `<total size>` is the sum of all previous `<file size>`
  - Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
      if a status code does not appear or is not an integer,
      don’t print anything for this status code
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order
