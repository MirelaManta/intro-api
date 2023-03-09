# API - Application Programming Interface
# An API is a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with an external system.

# API is like a barrier/ interface between your program and the external system

# An API is all the things that you can do to interact with an external
# system such as a website that carries data (e.g. Yahoo weather)


# API Endpoint is equivalent to the address of the place that you want to get some data from
# or want to  communicate with (that's usually just a URL)

import requests
from datetime import datetime

MY_LAT = 44.426765
MY_LONG = 26.102537

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code)
# response.raise_for_status()  # will raise an HTTPErorr if the HTTP request returned an unsuccessful status code.
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# print(data)
#
# iss_position = (longitude, latitude)
# print(iss_position)

# HTTP status codes
# 1## : Hold On
# 2##: Here You Go (Success)
# 3##: You don't have permissions
# 4##: You Screwed Up (404-The thing that you're looking for doesn't exist0
# 5##: I Screwed Up (The server screwed up, maybe the server is down, the website is down etc.)


# API Parameters ( this is a way that allows you to give an input when you are making your API request,
# so you can get different pieces of data back, depending on your input
# Not all API have parameters

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters, )
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # this is how we get a hold of the hours only
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now.hour)









