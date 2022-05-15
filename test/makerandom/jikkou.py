import os, glob, sys
from time import time

output_files = glob.glob("../output/*")

for f in output_files:
  os.remove(f)

input_files = glob.glob("../input/*")

makeinputflag = input("make file ?")

if makeinputflag == "y":
  times = int(input("input times"))
  for f in input_files:
    os.remove(f)
  
  for i in range(1, times + 1):
    filename = f"../input\\random{str(i).zfill(len(str(times)))}.txt"
    sys.stdout = open(filename, 'a+')
    exec(open("./makeinput.py").read())
    sys.stdout = sys.__stdout__
    print(f"make file : {filename}")
  
  input_files = glob.glob("../input/*")

print("make output")

for inputfile in input_files:
  if inputfile == "../input\\.gitkeep":
    continue
  filename = inputfile.split("\\")[-1]
  outputfilename = f"../output\\{filename}"

  sys.stdin = open(inputfile)
  sys.stdout = open(outputfilename, 'a+')

  exec(open("./solve.py").read())

  sys.stdout = sys.__stdout__

  print(f"make file : {filename}")
