# shopify-soft-eng-challenge
My solution for this job posting: https://jobs.lever.co/shopify/9a385896-9b30-44ad-ac46-bfa0ffbb305f

Good luck everyone!

## How to run the solution
- git clone https://github.com/WebF0x/shopify-soft-eng-challenge.git
- cd shopify-soft-eng-challenge/
- tox
- source .tox/py36/bin/activate
- python menu_cycle_checker/main.py

## Output
Solution to challenge #1:

{"valid_menus": [{"root_id": 2, "children": [8, 4, 5, 6]}, {"root_id": 4, "children": []}, {"root_id": 5, "children": [6]}, {"root_id": 6, "children": []}, {"root_id": 8, "children": []}, {"root_id": 9, "children": [10, 11, 12, 13, 14]}, {"root_id": 10, "children": []}, {"root_id": 11, "children": []}, {"root_id": 12, "children": [13, 14]}, {"root_id": 13, "children": []}, {"root_id": 14, "children": []}], "invalid_menus": [{"root_id": 1, "children": [1, 3, 7, 15]}, {"root_id": 3, "children": [1, 3, 15, 7]}, {"root_id": 7, "children": [1, 3, 7, 15]}, {"root_id": 15, "children": [1, 3, 15, 7]}]}

Solution to challenge #2:

{"valid_menus": [{"root_id": 2, "children": [8, 9, 10, 11]}, {"root_id": 3, "children": [18, 5]}, {"root_id": 5, "children": []}, {"root_id": 6, "children": []}, {"root_id": 8, "children": []}, {"root_id": 9, "children": [10]}, {"root_id": 10, "children": []}, {"root_id": 11, "children": []}, {"root_id": 12, "children": [13, 14, 15, 16, 17, 21]}, {"root_id": 13, "children": []}, {"root_id": 14, "children": []}, {"root_id": 15, "children": [16, 17, 21]}, {"root_id": 16, "children": []}, {"root_id": 17, "children": []}, {"root_id": 18, "children": []}, {"root_id": 19, "children": []}, {"root_id": 21, "children": []}], "invalid_menus": [{"root_id": 1, "children": [1, 3, 4, 5, 6, 7, 18, 19, 20]}, {"root_id": 4, "children": [1, 3, 4, 5, 6, 7, 18, 19, 20]}, {"root_id": 7, "children": [1, 3, 4, 5, 6, 7, 18, 19, 20]}, {"root_id": 20, "children": [1, 3, 4, 5, 6, 7, 18, 19, 20]}]}

My name is Maxime Dupuis and I hope we will meet soon :)
