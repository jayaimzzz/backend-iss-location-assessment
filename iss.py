#!/usr/bin/env python

__author__ = "jayaimzzz"

import requests

def main():
    r = requests.get("http://api.open-notify.org/astros.json")
    data = r.json()
    for people in data["people"]:
        print "{} is currently on board the {}".format(people["name"],people["craft"])
    print "There are {} astronauts in space".format(len(data["people"]))

if __name__ == '__main__':
    main()
