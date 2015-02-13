#!/bin/python

'''
    @author: Marius Lindauer
    
    Input: 
        bibfile: file with new entries
'''

import os
import sys
import json

def read_bib(bibfile):
    
    key_entry = {}
    with open(bibfile) as fp:
        current_entry = None
        for line in fp:
            if "@" in line:
                current_entry = line
                key = line.split("{")[1].strip("\n").strip(",")
                continue
            
            if current_entry:
                current_entry += line
            
            if not "=" in line and "}" in line:
                key_entry[key] = current_entry
                current_entry = None
                
    return key_entry

key_entry_new = read_bib(sys.argv[1])
key_entry_ref = read_bib("./bib/lib.bib")
#print(json.dumps(key_entry_new, indent=2))

new_keys = set(key_entry_new).difference(key_entry_ref)

try:
    with open("filter.json") as fp:
        declined_old = json.load(fp)
except:
    declined_old = []
    
new_keys = new_keys.difference(declined_old)

accepted = []
declined = []
for k in new_keys:
    if not key_entry_new[k]:
        continue
    print(key_entry_new[k])
    accept = raw_input("Keep? (y/n): ")
    while not accept in ["y", "n"]:
        accept = raw_input("Keep? (y/n): ")
    if accept == "y":
        accepted.append(k)
    else:
        declined.append(k)

print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        
for k in accepted:
    print(key_entry_new[k])
    
declined_old.extend(declined)


with open("filter.json", "w") as fp:
    json.dump(declined_old, fp, indent=2)