from menu_cycle_checker.main import get_children_of_menu
from menu_cycle_checker.main import get_number_of_pages
from menu_cycle_checker.main import get_menus
from menu_cycle_checker.main import get_menus_by_validity

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
            1: {'id': 1, 'data': 'a', 'child_ids': [2]},
            2: {'id': 2, 'data': 'b', 'child_ids': [2, 3]},
            3: {'id': 3, 'data': 'c', 'child_ids': []},
            4: {'id': 4, 'data': 'd', 'child_ids': [2]}
        }
        self.assertEqual(expected_menus, menus)

    def test_get_direct_children_of_menu(self):
        menus = {
            1: {'id': 1, 'data': 'a', 'child_ids': []},
            2: {'id': 2, 'data': 'b', 'child_ids': [1]},
            3: {'id': 3, 'data': 'c', 'child_ids': [4]},
            4: {'id': 4, 'data': 'd', 'child_ids': []}
        }
        self.assertEqual([], get_children_of_menu(menus, 1))
        self.assertIn(1, get_children_of_menu(menus, 2))
        self.assertIn(4, get_children_of_menu(menus, 3))
        self.assertEqual([], get_children_of_menu(menus, 4))

    def test_get_children_of_menu_recursively(self):
        menus = {
            1: {'id': 1, 'data': 'a', 'child_ids': [2]},
            2: {'id': 2, 'data': 'b', 'child_ids': [3]},
            3: {'id': 3, 'data': 'c', 'child_ids': []},
        }
        self.assertEqual([2, 3], get_children_of_menu(menus, 1))
        self.assertEqual([3], get_children_of_menu(menus, 2))
        self.assertEqual([], get_children_of_menu(menus, 3))

    def test_get_children_of_menu_cycling_to_self(self):
        menus = {
            1: {'id': 1, 'data': 'a', 'child_ids': [1]}
        }
        self.assertEqual([1], get_children_of_menu(menus, 1))

    def test_get_children_of_menu_cycling_to_self_indirectly(self):
        menus = {
            1: {'id': 1, 'data': 'a', 'child_ids': [2]},
            2: {'id': 2, 'data': 'b', 'child_ids': [1]}
        }
        self.assertEqual([1, 2], get_children_of_menu(menus, 1))
        self.assertEqual([1, 2], get_children_of_menu(menus, 2))

    def test_get_children_of_menu_with_diamond_cycle_to_self(self):
        menus = {
            1: {'id': 1, 'data': 'a', 'child_ids': [2, 3]},
            2: {'id': 2, 'data': 'b', 'child_ids': [4]},
            3: {'id': 3, 'data': 'c', 'child_ids': [4]},
            4: {'id': 4, 'data': 'd', 'child_ids': [1]}
        }

        self.assertEqual([1, 2, 3, 4], get_children_of_menu(menus, 1))
        self.assertEqual([1, 2, 3, 4], get_children_of_menu(menus, 2))
        self.assertEqual([1, 2, 3, 4], get_children_of_menu(menus, 3))
        self.assertEqual([1, 2, 3, 4], get_children_of_menu(menus, 4))

    def test_split_menus_by_validity(self):
        menus = {
            1: {'id': 1, 'data': 'a', 'child_ids': []},
            2: {'id': 2, 'data': 'b', 'child_ids': [3]},
            3: {'id': 3, 'data': 'c', 'child_ids': [4]},
            4: {'id': 4, 'data': 'd', 'child_ids': [1]},
            5: {'id': 5, 'data': 'e', 'child_ids': [5]},
            6: {'id': 6, 'data': 'f', 'child_ids': [7]},
            7: {'id': 7, 'data': 'g', 'child_ids': [6]},
            8: {'id': 8, 'data': 'h', 'child_ids': [5]}
        }
        valid_menus, invalid_menus = get_menus_by_validity(menus)
        expected_valid_menus = [
            {'id': 1, 'children': []},
            {'id': 2, 'children': [1, 3, 4]},
            {'id': 3, 'children': [1, 4]},
            {'id': 4, 'children': [1]},
            {'id': 8, 'children': [5]}
        ]
        expected_invalid_menus = [
            {'id': 5, 'children': [5]},
            {'id': 6, 'children': [6, 7]},
            {'id': 7, 'children': [6, 7]}
        ]
        self.assertEqual(expected_valid_menus, valid_menus)
        self.assertEqual(expected_invalid_menus, invalid_menus)
