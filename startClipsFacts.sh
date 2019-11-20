#! /bin/bash
cat startClipsCommands.txt |  ./clips 
python3 parseClipsOutput.py
rm outputfraudfound.txt
