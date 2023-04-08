import requests.exceptions

from RetrieveData import retrieve_products

def create_dict_of_categories():
    categories={}
    try:
        for product in retrieve_products():
            categories[product["category"]] = categories.get(product["category"],0)+product["price"]
        return categories
    except requests.exceptions.HTTPError as e:
        print(e)


def CATEGORIES_TEST():
    print("all categories and the sum of their products: ")
    print(create_dict_of_categories())



if __name__ == '__main__':
    CATEGORIES_TEST()


