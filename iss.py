#!/usr/bin/env python

__author__ = "jayaimzzz"

import requests
import turtle
import time

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
        result = (timestamp, float(longitude), float(latitude))
        return result
    except requests.exceptions.RequestException as err:
        print err



def create_graphic_screen():
    wn = turtle.Screen()
    wn.setup(width=720, height=360)
    wn.bgpic("map.gif")
    iss_image = "iss.gif"
    wn.setworldcoordinates(-180,-90,180,90)
    wn.register_shape(iss_image)
    iss = turtle.Turtle()
    iss.shape(iss_image)
    iss.penup()
    poll = True
    while poll:
        geo_coordinates = obtain_geo_coordinates()
        longitude = geo_coordinates[1]
        latitude = geo_coordinates[2]
        iss.goto(geo_coordinates[1],geo_coordinates[2])
        print (longitude, latitude)
        time.sleep(5)
        # wn.exitonclick()


def main():
    obtain_astronauts()
    create_graphic_screen()
    

if __name__ == '__main__':
    main()
