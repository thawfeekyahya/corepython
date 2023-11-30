#Passing input to program using command  line arguments

import sys
import argparse

parser = argparse.ArgumentParser(description="This is a test program for argparse")

parser.add_argument("test",type=str,help="This is help info for the test argument")

args = parser.parse_args()


length  = len(sys.argv)

print("Argument length", len(sys.argv))
print("List of Arguments", sys.argv)
print("Loop  arguments --")
for i in sys.argv: print(i)
