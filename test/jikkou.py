import glob
import sys
import os

input_files = glob.glob("./input/*")
output_files = glob.glob("./output/*")
solve_files = glob.glob("./solve/*")

for f in solve_files:
  os.remove(f)

if len(input_files) != len(output_files):
  print("length not equal")
  exit()

for inputfile in input_files:
  if inputfile == "./input\\.gitkeep":
    continue
  filename = inputfile.split("\\")[-1]
  solvefilename = f"./solve\\{filename}"
  outputfilename = f"./output\\{filename}"

  if outputfilename not in output_files:
    print(f"{inputfile} is not found")
    continue

  sys.stdin = open(inputfile)
  sys.stdout = open(solvefilename, 'a+')

  exec(open("./main.py").read())

  sys.stdout = sys.__stdout__

  if open(solvefilename).read() == open(outputfilename).read():
    print(f"{filename} : AC")
  else:
    print(f"{filename} : WA")
