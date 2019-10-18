#!/usr/bin/python3
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


listy = []
argv = sys.argv
if os.path.exists('add_item.json'):
    listy += load_from_json_file('add_item.json')


for i in argv[1:]:
    listy.append(i)

save_to_json_file(listy, 'add_item.json')
