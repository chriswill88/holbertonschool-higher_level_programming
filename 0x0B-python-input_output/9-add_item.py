#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


listy = []
i = 1
argv = sys.argv
while i < len(argv):
    if i > 0:
        listy.append(argv[i])
    i += 1

save_to_json_file(listy, 'add_item.json')
load_from_json_file('add_item.json')
