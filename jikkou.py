import sys

if len(sys.argv) == 2:
  sys.stdin = open(sys.argv[1])

exec(open("index.py").read())