import os
import subprocess
# os.system
# os.spawn*


def callMatlab():
    subprocess.call("heartrate/reproduce_results.bat")
    # subprocess.run("heartrate/reproduce_results.bat")
