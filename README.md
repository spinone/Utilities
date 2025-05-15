# Utilities
Various useful scripts
**srtsync.py**
A quick and dirty script to modify the subtitle timings in a standard .srt video subtitle file
In the video, make a note of the exact time a specific phrase is spoken, e.g. **01:32** (1 min 32 seconds)
Find that phrase in the .srt file - 
there will be an index number, an associated start time and end time for the subtitle to be displayed, then the subtitle text, 
e.g.

       27
       00:01:55,333 --> 00:01:57,402
       Make sure he gets back alive.

 *** Note that the timing format is hh:mm:ss,milliseconds - This script ignores the milliseconds.
 Subtract the video elapsed time from the .srt entry time , e.g. 01:32 - 01:55
 in this case, the answer is -23, i.e., the subtitle track is 23 seconds behind the video
 now run the python script against the .srt file, using the offset in seconds e.g.
 python c:\scripts\srtsync.py c:\temp\subtrack1.srt -23
 (paths can be absolute or relative)
 The updated .srt file will be written to [filename]-resync.srt,
 e.g. c:\temp\subtrack1-resync.srt in the example above

 Chris Rundle, May 2025
