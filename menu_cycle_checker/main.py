from math import ceil
from json import dumps

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
        menu["id"]: menu
        for menu in menus_list
    }


def get_children_of_menu(menus, menu_id, children_to_skip=None):
    if children_to_skip is None:
        children_to_skip = set([])
    children_to_skip.add(menu_id)

    direct_children_ids = menus[menu_id]["child_ids"]

    children_ids = set(direct_children_ids)
    for direct_child_id in direct_children_ids:
        if direct_child_id not in children_to_skip:
            children_of_children = get_children_of_menu(menus, direct_child_id, children_to_skip)
            children_ids.update(children_of_children)
    return list(children_ids)


def get_menus_by_validity(menus):
    menus_and_children = {
        menu_id: {"root_id": menu_id, "children": get_children_of_menu(menus, menu_id)}
        for menu_id in menus
    }
    valid_menus = [
        menus_and_children[menu_id]
        for menu_id in menus_and_children
        if menu_id not in menus_and_children[menu_id]["children"]
    ]
    invalid_menus = [
        menus_and_children[menu_id]
        for menu_id in menus_and_children
        if menu_id in menus_and_children[menu_id]["children"]
    ]
    return valid_menus, invalid_menus


def get_output_menus(valid_menus, invalid_menus):
    return {
        "valid_menus": valid_menus,
        "invalid_menus": invalid_menus
    }


def main():
    json_pages = get_json_pages()
    menus = get_menus(json_pages)
    valid_menus, invalid_menus = get_menus_by_validity(menus)
    output_menus = get_output_menus(valid_menus, invalid_menus)
    print(dumps(output_menus))
    pass


if __name__ == "__main__":
    main()
