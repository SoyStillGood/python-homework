import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file", help="input housing data file")

args = parser.parse_args()
file = args.file
data=open(file)
my_file = data.read()

my_file_lines = my_file.split('\n')
print(my_file)

for line in my_file_lines:
    print([line])