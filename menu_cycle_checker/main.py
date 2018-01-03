from math import ceil

import requests

SHOPIFY_CHALLENGE_URL = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json"
SHOPIFY_CHALLENGE_ID = 1


def get_json_page(id, page):
    payload = {"id": id, "page": page}
    response = requests.get(SHOPIFY_CHALLENGE_URL, payload)
    return response.json()


def get_json_pages():
    first_page = get_json_page(SHOPIFY_CHALLENGE_ID, 1)
    number_of_pages = get_number_of_pages(first_page)
    return [
        get_json_page(SHOPIFY_CHALLENGE_ID, page_number)
        for page_number in range(1, number_of_pages + 1)
    ]


def get_number_of_pages(json_page):
    nb_total_menus = json_page["pagination"]["total"]
    nb_menus_per_page = json_page["pagination"]["per_page"]
    return ceil(nb_total_menus / nb_menus_per_page)


def get_menus(json_pages):
    pages_of_menus = [
        json_page["menus"]
        for json_page in json_pages
    ]
    menus_list = sum(pages_of_menus, [])
    return {
        menu["id"]: {
            key: menu[key] for key in menu if key != "id"
        }
        for menu in menus_list
    }


def main():
    json_pages = get_json_pages()
    menus = get_menus(json_pages)
    pass


if __name__ == "__main__":
    main()
