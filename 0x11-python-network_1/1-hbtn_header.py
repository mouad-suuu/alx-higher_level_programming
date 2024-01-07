#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL, and
displays the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    # Check if a URL is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Send a request to the URL and display the value of X-Request-Id
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
