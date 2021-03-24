import argparse

parser = argparse.ArgumentParser(prog='range')
parser.add_argument('start', type=int)
parser.add_argument('end',type=int)
parser.add_argument('-x','--exclusive', action='store_true')
parser.add_argument('--step',nargs='?', const=1, type=int, default=1)

args = parser.parse_args()

if args.exclusive==True:
    end = args.end -1
else:
    end = args.end

x = args.start

while x <= end:
    print(x)
    x+= args.step


