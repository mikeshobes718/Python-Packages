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

# USE IN OTHER PROGRAMS TO DOWNLOAD MODULE
# module_file_name = "temp.py"
# module_url = "ENTER GIT RAW URL LINK HERE"
# proc_output = subprocess.Popen(["wget", "-o", "/dev/null", "-O", module_file_name, module_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# out, err = proc_output.communicate()

raw_dna_file = file_23andMe 

filestatus = (universal.filestatus(raw_dna_file))
if(filestatus['status'] == 'exist'):
    filetype = (universal.lasttrim('.', raw_dna_file))

    line_num = 0
    with open(raw_dna_file) as f:
        whole_file = f.readlines()
        # line = (whole_file[line_num])
        # line = universal.removeprefix(line, '#')
        for line in whole_file:
            print(line)

        # for line in whole_file:
        #     print(line)

    # infile = open(raw_dna_file, "r")
    # for line in infile:
    #     print(line)
        # print(infile.readline()
        # try:
        #     line = int(line) # convert to integer if possible
        # except ValueError:
        #     pass # conversion failed. The line is not an integer
        # print repr(line) # or do something else

    if(filetype == 'txt'):
        pass
        # print()
    elif(filetype == 'csv'):
        pass
else:
    print(("ERROR: File \"{}\" doesn't exist!").format(raw_dna_file))
    sys.exit()