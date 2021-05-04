#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
prints type of the data response (usually a byte object)
prints data (prints the data when still a byte object)
prints utf-8 decoded data (string conversion)
"""


if __name__ == "__main__":
    from urllib import request  # used for fetching URLS

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html_data = response.read()
        html = html_data.decode("UTF-8")
    # printing response type, utf-8 decoded content, and content before decode
        print("Body response:")
        print("\t- type:", type(html_data))
        print("\t- content:", html_data)
        print("\t- utf8 content:", html)
