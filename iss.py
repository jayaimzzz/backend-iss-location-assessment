#!/usr/bin/env python

__author__ = "jayaimzzz"

import requests

def obtain_astronauts():
    try:
        r = requests.get("http://api.open-notify.org/astros.json")
        data = r.json()
        for people in data["people"]:
            print "{} is currently on board the {}".format(people["name"],people["craft"])
        print "There are {} astronauts in space".format(len(data["people"]))
    except requests.exceptions.RequestException as err:
        print err

def obtain_geo_coordinates():
    try:
        r = requests.get("http://api.open-notify.org/iss-now.json")
        data = r.json()
        timestamp = data["timestamp"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        return (timestamp, latitude, longitude)
    except requests.exceptions.RequestException as err:
        print err

def main():
    obtain_astronauts()
    geo_coordinates = obtain_geo_coordinates()
    print geo_coordinates
    

if __name__ == '__main__':
    main()
