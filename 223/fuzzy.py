#!/usr/bin/env python

import sys

def problem(a, b):
	return b == "".join(c for c in a if c in b)
print problem(sys.argv[1], sys.argv[2])
