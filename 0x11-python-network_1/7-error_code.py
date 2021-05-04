#!/usr/bin/python3
"""
Description:
a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.

uses requests module instead of urllib
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    status = response.status_code
    if status == 200:
        print(response.text)
    else:
        print("Error code:", response.status_code)
