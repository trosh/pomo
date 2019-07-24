#!/usr/bin/env python3

from subprocess import run
from time import sleep

worktime = 20 # Minutes
duration = 60
minsleep = 0.2
maxsleep = 2
nflashes = abs(duration/minsleep - duration/maxsleep) // 2

for minute in range(worktime):
    print(f"{worktime - minute} minutes left")
    sleep(60)
print("\nTIME OVER!")
for i in range(int(nflashes)):
    run(["xrefresh"])
    sleep(minsleep + (maxsleep - minsleep) * i / nflashes)
