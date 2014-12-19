#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 9, 2014

@author: marius lindauer
'''

import os
import sys
import time
import json
from pybtex.database.input import bibtex


class BIBHTML(object):
    
    def __init__(self):
        '''
            constructor
        '''
        self._BIBFILES = ["./bib/lib.bib", "./bib/proc.bib"] 
        #self._BIBFILES = ["/home/lindauer/workspace/acsurvey/bib/lib.bib", "/home/lindauer/workspace/acsurvey/bib/proc.bib"] 
        self.bibdata = None
        
        #self.ACTIVE_KEYS = ["Algorithm Configuration", "Algorithm Schedules", "Algorithm Selection", "Hyper-Parameter Optimization"]
        self.ACTIVE_KEYS = ["Algorithm Configuration", "Global Optimization", "Algorithm Analysis"]
            
    def main(self):
        self.read_bib()
        self.resolve_crossref()
        entry_list = self.collect_by_entries()
        self.sort_by_year(entry_list)
        self.write_json(entry_list)
        
    def read_bib(self):
        parser = bibtex.Parser()
        for bib_file in self._BIBFILES:
            self.bibdata = parser.parse_file(bib_file)
            
    def resolve_crossref(self):
        for entry in self.bibdata.entries.values():
            if entry.fields.get("crossref"):
                cross_ref = entry.get_crossref()
                if not cross_ref.fields.get("booktitle"):
                    sys.stderr.write("[WARNING] Missing booktitle at %s\n" %(cross_ref))
                for key, value in cross_ref.fields.items():
                    if key == "title":
                        continue
                    entry.fields[key] = value
                #print(cross_ref)
            
    def collect_by_entries(self):
        return self.bibdata.entries.values()
        
    def sort_by_year(self,entry_list):
        entry_list.sort(key=lambda x: int(x.fields.get("year",1900)), reverse=True)
        
            
    def write_json(self, entry_list):
        
        lit_list = [] 
                   
        for entry in entry_list:
            if entry.original_type.upper() == "PROCEEDINGS":
                continue
            
            active = False
                
            if entry.fields.get("keywords") and entry.fields.get("keywords") != "":
                keys = sorted(map(lambda x: x.strip(" "), entry.fields.get("keywords").split(",")))
                for k in keys:
                    if k in self.ACTIVE_KEYS:
                        active = True
                        entry.fields["keywords"] = ", ".join(keys)
                        break
            if not active:
                sys.stderr.write("[WARNING]: Skipped: %s" %(entry.fields.get("title")))
                continue     
                
            list_entry = {"Year":1900, "Citation":{"short": "NA", "long": "NA"}, "Domain": "N/A", "Category": "N/A"}
                
                
            key_order = [("author", "%s<br/>"), ("title", "%s.<br/>"), 
                             ("booktitle", "%s.<br/>"), ("journal", "%s.<br/>"), 
                             ("pages", "p. %s. "), ("year", "%s.<br/>")]
                
            long_array = []
            for k,form in key_order:
                if entry.fields.get(k) and entry.fields.get(k) != "":
                    long_array.append(form %(self.format_string(entry.fields.get(k))))
            list_entry["Citation"]["long"] = "".join(long_array)
            #print(self.format_string(entry.fields.get("author")))
            list_entry["Citation"]["short"] = self.format_string(entry.fields.get("author"))+" ".encode("utf-8") \
                                              + self.format_string(entry.fields.get("year"))
            
            if entry.fields.get("year") and entry.fields.get("year") != "":
                list_entry["Year"] = entry.fields.get("year")
            if entry.fields.get("domain") and entry.fields.get("domain") != "":
                list_entry["Domain"] = ", ".join(sorted(map(lambda x: x.strip(), entry.fields.get("domain").split(","))))
            if entry.fields.get("keywords") and entry.fields.get("keywords") != "":
                list_entry["Category"] = entry.fields.get("keywords")
                
            lit_list.append(list_entry)
        
        with open("lit.json", "w") as fp:
            json.dump(lit_list,fp)
        
                
    def format_string(self, str_):
        str_ = str_.encode("utf-8")
        replaces = [("{", ""),
                    ("}", ""),
                    ("\\\"u", "ü"), #list to ensure order
                    ("\\\"o", "ö"),
                    ("\\\"a", "ä"),
                    ("\\'o", "ó"),
                    ("\\'a", "á"),
                    ("\\'e", "é"),
                    ("\\^e", "ê"),
                    ("\\'c", "ć"),
                    ("~", ""),
                    ("\\" , ""),
                    ("\"", ""),
                    ]
        for s,r in replaces:
            str_ = str_.replace(s,r)
        return str_
    
if __name__ == '__main__':
    bib = BIBHTML()
    bib.main()