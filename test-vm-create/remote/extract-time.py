#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

unpaused = "libxl__device_nic_add: domain is unpaused; bailing out"

def parse(lines):
    phase = 0
    result = {}
    for line in lines:
        try:
            bits = line.split(" ")
            secs = bits[0]
            frac = bits[2]
            time = float(secs + "." + frac)
            if unpaused in line:
                return time
        except:
            pass

if __name__ == "__main__":
    t = parse(sys.stdin.readlines())
    print t
