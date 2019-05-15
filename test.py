#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json



# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=
BASE_URL = 'https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}'


def getMovieTitles(substr):
    titles_list = []
    page = 1
    read_until_now = 0
    while True:
        req = Request(BASE_URL.format(substr, page))
        with urlopen(req) as response:
            rep = response.read()
        resp = json.loads(rep.decode("utf-8"))
        for elem in resp['data']:
            titles_list.append(elem['Title'])
        per_page = int(resp['per_page'])
        read_until_now += per_page
        if read_until_now >= int(resp['total']):
            break
    titles_list.sort()
    return titles_list




res = getMovieTitles('spiderman')

