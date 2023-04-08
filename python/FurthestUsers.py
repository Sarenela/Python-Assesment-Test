import requests.exceptions
from geopy.distance import distance
from RetrieveData import retrieve_users

def find_furthest_users():
    user1={}
    user2={}
    maxDist=0
    try:
        users = retrieve_users()
        for us1 in users:
            for us2 in users:
                if(not us1 == us2):
                    dist = distance((us1['address']['geolocation']['lat'],us1['address']['geolocation']['long']),(us2['address']['geolocation']['lat'],us2['address']['geolocation']['long'])).km
                    if dist > maxDist:
                        maxDist = dist
                        user1 = us1
                        user2 = us2


        print(f"{user1['name']['firstname']} {user1['name']['lastname']} and {user2['name']['firstname']} {user2['name']['lastname']}, distance:{maxDist:.2f}km")
    except requests.exceptions.HTTPError as e:
        print(e)

def FURTHEST_USERS_TEST():
    print("users that live the furthest from each other:")
    find_furthest_users()


if __name__ == '__main__':
     FURTHEST_USERS_TEST()


