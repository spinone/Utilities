#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python 3.6+ (uses formatted string literals, print(f"hello {variable}")    )

""" A quick and dirty script to modify the subtitle timings in a standard .srt video subtitle file """
# In the video, make a note of the exact time a specific phrase is spoken, e.g. 01:32 (1 min 32 seconds)
# Find that phrase in the .srt file - 
# there will be an index number, an associated start time and end time for the subtitle to be displayed, then the subtitle text, e.g.
#       27
#       00:01:55,333 --> 00:01:57,402
#       Make sure he gets back alive.
# *** Note that the timing format is hh:mm:ss,milliseconds - This script ignores the milliseconds.
# Subtract the video elapsed time from the .srt entry time , e.g. 01:32 - 01:55
# in this case, the answer is -23, i.e., the subtitle track is 23 seconds behind the video
# now run the python script against the .srt file, using the offset in seconds e.g.
# python c:\scripts\srtsync.py c:\temp\subtrack1.srt -23
# (paths can be absolute or relative)
# The updated .srt file will be written to [filename]-resync.srt,
# e.g. c:\temp\subtrack1-resync.srt in the example above
#
# Chris Rundle, May 2025
#


import re, time, os, sys

def checkargs():
    if len(sys.argv)!=3:
        print("[+] Usage: srtsync.py filename.srt offset_in_seconds")
        sys.exit()
        
def list_timestamps(filename):
    # Regular expression pattern to match HH:MM:SS format
    timestamp_pattern = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                matches = timestamp_pattern.findall(line)
                if matches:
                    for match in matches:
                        t2=changetimes(match,offset)    
                        line=line.replace(match,t2)
                        print(".",end = "")#append a screen dot for each timer line
                
                f.write(line)
    except FileNotFoundError:
        print(f"\n[!] Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
        
def changetimes(ts,offset):
    thistime=0
    timetuple = ts.split(":")
    x1=int(timetuple[0])
    thistime=thistime + (x1*360)
    x2=int(timetuple[1])
    thistime=thistime + (x2*60)
    x3=int(timetuple[2])
    thistime=thistime + x3 
    x4=int(offset)
    thistime=thistime + x4
    if thistime<0:
        #print(f"Negative offset - Setting {thistime} to 0")
        thistime=0
    return time.strftime("%H:%M:%S", time.gmtime(thistime))

checkargs
fn=sys.argv[1] 
offset=sys.argv[2] 
fn2=os.path.splitext(os.path.basename(fn))[0]
fn2=fn2+"-resync.srt"
if os.path.exists(fn2):
    os.remove(fn2)
f = open(fn2, "a")
print(f"\n[+] Offsetting subtitles in {fn} by {offset} seconds")
print(f"[-] and writing output to {fn2}\n==================================================\n")
list_timestamps(fn)
f.close
print(f"\n\n[>] {fn2}\n\n ============================ srtsync.py © Chris Rundle 2025 ==================================\n")
