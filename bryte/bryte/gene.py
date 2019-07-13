# gene.py

"""
gene.py: This module is used for Developmental Engineering purposes.
"""

import os
import sys
import json
import requests
import subprocess
import universal

weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

whoami = "Mike Shobes"

headers = {'Content-type':'application/json'}

file_23andMe = "/Users/mike/Documents/Life/Business/GeneDyve/Orders/New/genome_Solange_Dorsinville_v5_Full_20190211213037 2.txt"
file_MyHeritage = "/Users/mike/Documents/Life/Business/Ancestry31/Orders/Pending/MyHeritage_raw_dna_data.csv"

raw_dna_file = file_23andMe 

filestatus = (universal.filestatus(raw_dna_file))
if(filestatus['status'] == 'exist'):
    filetype = (universal.lasttrim('.', raw_dna_file))
    if(filetype == 'txt'):
        data = universal.txt2dslistnoprefix(raw_dna_file, '#')
        data = universal.removeEmptyElementsFromList(data)
        rsids = []
        for index in range(len(data)):
            row = (data[index])
            # if(row[0] == 'rsid' or row[0] == 'RSID'):
            #     header = (data[index])
            #     print(header)
            rsids.append(row[0])
        
        dups = universal.getduplicateElementsFromList(rsids)
        # dups = set([x for x in rsids if rsids.count(x) > 1])
        print(dups)
    elif(filetype == 'csv'):
        content = universal.getfilecontent(raw_dna_file)
        print(content)
else:
    print(("ERROR: File \"{}\" doesn't exist!").format(raw_dna_file))
    sys.exit()