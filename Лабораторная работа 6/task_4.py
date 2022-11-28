import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",",  new_line="\n"):
    table = []
    with open(filename) as f:
        header = f.readline().split(delimiter)
        for line in f:
            fields = line.strip(new_line).split(delimiter)
            entry = {}
            a = 0
            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()
                if a % len(fields) == 0:
                    table.append(entry)
                a += 1
    return table


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

