import sys
import os
import subprocess

for file in sorted(os.listdir("tests/")):
    print("running test: " + file)
    path = "tests/" + file
    os.system("time python3 t2.py " + path)
