#!/usr/bin/env python3

from subprocess import run
from shlex import split
from time import sleep

worktime = 20 * 60
duration = 60
minsleep = 0.2
maxsleep = 2
nflashes = abs(duration/minsleep - duration/maxsleep) // 2

sleep(worktime)
for i in range(int(nflashes)):
    run(split("xrefresh -solid black"))
    sleep(minsleep + (maxsleep - minsleep) * i / nflashes)
