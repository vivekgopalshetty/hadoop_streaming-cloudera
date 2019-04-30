#!/usr/bin/python

import sys
flag=0

for input_line in sys.stdin:
 line = input_line.strip().split(",")
     if (flag==0):
         columns=line
         flag=1
     else:
         time = line[2].split("||")[1].split(":")
         hour = float(time[0])
         print "{0}\t{1}".format(hour,str(input_line.strip())) 
