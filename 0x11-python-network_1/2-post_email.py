#!/usr/bin/python3
"""
Description:
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

email is the variable we are posting to the url
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    query = parse.urlencode({'email': argv[2]})
    query_bytes = query.encode('ascii')
    post = request.Request(argv[1], query_bytes)
    with request.urlopen(post) as response:
        data = response.read()
        decoded = data.decode("UTF-8")
        print(decoded)
