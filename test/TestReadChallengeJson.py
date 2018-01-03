from menu_cycle_checker.main import get_number_of_pages

import unittest


class TestReadChallengeJson(unittest.TestCase):
    def test_get_number_of_pages(self):
        challenge_json = {
            'pagination': {
                'total': 4}
        }
        number_of_pages = get_number_of_pages(challenge_json)
        self.assertEqual(4, number_of_pages)
