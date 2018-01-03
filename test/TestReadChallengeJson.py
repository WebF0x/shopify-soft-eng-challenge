from menu_cycle_checker.main import get_number_of_pages
from menu_cycle_checker.main import get_menus

import unittest


class TestReadChallengeJson(unittest.TestCase):
    def test_get_number_of_pages(self):
        json_page = {
            'pagination': {
                'total': 15,
                'current_page': 1,
                'per_page': 3
            }
        }
        number_of_pages = get_number_of_pages(json_page)
        self.assertEqual(5, number_of_pages)

    def test_get_number_of_pages_with_non_full_last_page(self):
        json_page = {
            'pagination': {
                'total': 15,
                'current_page': 1,
                'per_page': 4
            }
        }
        number_of_pages = get_number_of_pages(json_page)
        self.assertEqual(4, number_of_pages)

    def test_get_menus_from_json_pages(self):
        json_page_1 = {
            'menus': [
                {'id': 1, 'data': 'a', 'child_ids': [2]},
                {'id': 2, 'data': 'b', 'child_ids': [2, 3]}
            ]
        }
        json_page_2 = {
            'menus': [
                {'id': 3, 'data': 'c', 'child_ids': []},
                {'id': 4, 'data': 'd', 'child_ids': [2]}
            ]
        }
        json_pages = [json_page_1, json_page_2]
        menus = get_menus(json_pages)
        expected_menus = {
            1: {'data': 'a', 'child_ids': [2]},
            2: {'data': 'b', 'child_ids': [2, 3]},
            3: {'data': 'c', 'child_ids': []},
            4: {'data': 'd', 'child_ids': [2]}
        }
        self.assertEqual(expected_menus, menus)
