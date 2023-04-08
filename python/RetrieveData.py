import json
from urllib.request import urlopen

import requests


def get_data(url):
    data = requests.get(url, headers = {"Accept":"application/json"})
    if data.status_code==200:
        return data.json()
    else:
        raise requests.exceptions.HTTPError("could not retrieve data")

def retrieve_users(): #throws
    return get_data("https://fakestoreapi.com/users")

def retrieve_carts(): #throws
    return get_data("https://fakestoreapi.com/carts")

def retrieve_products(): #throws
    return get_data("https://fakestoreapi.com/products")



def RETRIEVING_DATA_TEST():
    try:
        print("retrieving users:")
        print(retrieve_users())
    except requests.exceptions.HTTPError:
        print("could not load users")
    print()

    try:
        print("retrieving products:")
        print(retrieve_products())
    except requests.exceptions.HTTPError:
        print("could not load products")
    print()

    try:
        print("retrieving carts:")
        print(retrieve_carts())
    except requests.exceptions.HTTPError:
        print("could not load carts")






if __name__ == '__main__':
    RETRIEVING_DATA_TEST()


