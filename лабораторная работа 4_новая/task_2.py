import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(in_file, out_file) -> None:
    with open(in_file) as in_f:
        reader = [row for row in csv.DictReader(in_f)]
    with open(out_file, "w") as out_f:
        json.dump(reader, out_f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
