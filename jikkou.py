import sys

if len(sys.argv) == 3:
  sys.stdin = open(sys.argv[2])

exec(open(sys.argv[1]).read())