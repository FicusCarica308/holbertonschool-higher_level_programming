#!/usr/bin/python3
"""
Description:
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Checks for invalid json using try: except:
with json.JSONDecodeError
"""


if __name__ == "__main__":
    import requests
    from sys import argv as argv

    if len(argv) == 1:
        param = {'q': ""}
    else:
        param = {'q': argv[1]}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        json = response.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except json.JSONDecodeError:
        print("Not a valid JSON")
