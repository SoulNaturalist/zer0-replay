import argparse

def remove_empty_lines(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()


parser = argparse.ArgumentParser()


parser.add_argument('-file_name', type=str, help='File name to be processed', required=True)


parser.add_argument('-replace_value', type=str, help='Value to replace', required=True)

parser.add_argument('-delete_spaces', type=str, help='Boolean to delete spaces', required=True)

args = parser.parse_args()


with open(args.file_name, 'r') as f:
    new_data = f.read().replace(args.replace_value, '')
with open(args.file_name, 'w') as f:
    f.write(new_data)

if args.delete_spaces:
    remove_empty_lines(args.file_name)
