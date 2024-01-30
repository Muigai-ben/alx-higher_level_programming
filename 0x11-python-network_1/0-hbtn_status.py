#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    Funtion to print a response of a specific url
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {<class 'bytes'>}'.format(type(html)))
        print('\t- content: {b'OK'}'.format(html))
        print('\t- utf8 content: {OK}'.format(html.decode('utf8')))

if __name__ == "__main__":
    main()
