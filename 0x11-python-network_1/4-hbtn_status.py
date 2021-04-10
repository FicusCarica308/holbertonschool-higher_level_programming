#!/usr/bin/python3
"""
Description:
a Python script that fetches https://intranet.hbtn.io/status
using the requests module instead of urllib
"""


if __name__ == "__main__":
    import requests as req

    response = req.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
