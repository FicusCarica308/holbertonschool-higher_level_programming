#!/usr/bin/python3
"""

Description:
a Python script that takes in a URL,
sends a request to the URL and displays the
body of the response (decoded in utf-8).

"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            data = response.read()
            data_decoded = data.decode("UTF-8")
            print(data_decoded)
    except error.HTTPError as error:
        print("Error code:", error.code)
