import time
import os

for file in sorted(os.listdir("tests/")):
    print("running test: " + file)
    path = "tests/" + file
    start_time = time.time()
    os.system("python3 t2.py " + path)
    print("--- %s seconds ---" % (time.time() - start_time))
