#!/usr/bin/env python

__author__ = "jayaimzzz"

import requests
import turtle
import time

def print_astronauts():
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
    wn.setworldcoordinates(-180,-90,180,90)
    return wn

def display_ISS_and_update(wn):
    iss_image = "iss.gif"
    wn.register_shape(iss_image)
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

def place_dot_and_time_at(long_lat,text,wn):
    dot = turtle.Turtle()
    (long,lat) = long_lat
    dot.hideturtle()
    dot.color("yellow")
    dot.penup()
    dot.goto(long, lat)
    dot.dot()
    dot.goto(long + 5, lat - 2)
    dot.write(text)
    # wn.exitonclick()

def time_ISS_pass(long,lat):
    payload = {
        "lat":lat,
        "lon":long
        }
    r = requests.get("http://api.open-notify.org/iss-pass.json", params=payload)
    # print r.url
    data = r.json()
    next_ISS_pass_time = data["response"][0]['risetime']
    result = time.ctime(next_ISS_pass_time)
    return result


def main():
    print_astronauts()
    wn = create_graphic_screen() 
    indy_geo_coordinates = (-86.1234903, 40.267193)
    time_ISS_pass_Indy = time_ISS_pass(*indy_geo_coordinates) 
    place_dot_and_time_at(indy_geo_coordinates,time_ISS_pass_Indy,wn)
    display_ISS_and_update(wn)
    

if __name__ == '__main__':
    main()
