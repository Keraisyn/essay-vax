import argparse
import unplagiarize

parser = argparse.ArgumentParser(description='Unplagiarize some text')

parser.add_argument('-s', help = 'compile a specific file with a specified path.')
args = parser.parse_args()

with open(args.s, "r") as file:
    text = unplagiarize.unplagiarize(file.read())

output_path = str(args.s).replace(".txt", "") + "_out.txt"

with open(output_path, "w+") as file:
    file.write(text)

print(text)
