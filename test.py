import argparse
import os

parser = argparse.ArgumentParser(description='This is a test program.')
parser.add_argument('--number', type=float, default=100, help='A number will be displayed')
args = parser.parse_args()
print('num = ' + str(args.number))

os.mkdir('./testdir')