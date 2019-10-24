import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file", help="input housing data file")

args = parser.parse_args()
file = args.file
data=open(file)
my_file = data.readlines()