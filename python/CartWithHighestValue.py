#because the cart link does not work,  i assume that a cart is a dict with "userID", and "products"=list of productIDs
#example:{
#"userId": 7,
#"products:": (1,2,4,5,3,2,2,1,1)}}
import requests.exceptions
from RetrieveData import retrieve_products, retrieve_carts,retrieve_users


def get_user_name(userID):  # throws
    for user in retrieve_users():
        if user["id"] == userID:
            return f"{user['name']['firstname']} {user['name']['lastname']}"
    raise ValueError("user does not  exist")


def value_of_cart(cartEntry, products):
    value = 0
    try:
        for productId in cartEntry["products"]:
            value+= float(products[productId]["price"])
        return value
    except IndexError as e:
        raise ValueError("product does not exist")



def find_owner_and_highest_value_of_carts(carts=None):  # i put optional args because i wanted to test the function on my examples, this method should not normally have any args and just get carts from the link
    maxVal=0
    maxId=""
    try:
        products = retrieve_products()
        if carts == None:
            carts = retrieve_carts()

        for cart in carts:
            currentVal=value_of_cart(cart,products)
            if currentVal > maxVal:
                maxVal=currentVal
                maxId=cart["userId"]

        print(f"cart value: {maxVal},   cart user: {get_user_name(maxId)} ")
    except requests.exceptions.HTTPError as e:
        print(e)
    except ValueError as e:
        print(e)



def CARTS_VALUE_FROM_LINK_TEST_CASE():
    print("carts from link: ")
    find_owner_and_highest_value_of_carts()
    print()

def CARTS_VALUE_EXAMPLE_THAT_WORKS_TEST_CASE():
    print("carts custom example that works: ")
    find_owner_and_highest_value_of_carts([{"userId":1,"products":[1,2,4,3,2,1,1,1]},{"userId":3,"products":[1,1,2]}] )
    print()

def CARTS_VALUE_PRODUCT_NOTFOUND_TEST_CASE():
    print("carts when product not found: ")
    find_owner_and_highest_value_of_carts([{"userId": 1, "products": [1, 2, 4, 5, 3, 2, 100, 1, 1]}, {"userId": 3, "products": [1, 1, 2]}])
    print()

def CARTS_VALUE_USER_NOTFOUND_TEST_CASE():
    print("carts when user not found:")
    find_owner_and_highest_value_of_carts([{"userId": 100, "products": [1, 2, 4, 3, 2, 1, 1, 1]}, {"userId": 1, "products": [1, 1, 2]}])
    print()




if __name__ == '__main__':
        CARTS_VALUE_FROM_LINK_TEST_CASE()
        CARTS_VALUE_EXAMPLE_THAT_WORKS_TEST_CASE()
        CARTS_VALUE_PRODUCT_NOTFOUND_TEST_CASE()
        CARTS_VALUE_USER_NOTFOUND_TEST_CASE()


