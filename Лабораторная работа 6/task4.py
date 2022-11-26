import json
from typing import List
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> List[dict]:
    list_dik = []
    list_rows = []
    with open(filename, 'r') as f:
        result = f.readlines()
        headers = result[0].rstrip().split(sep=',')
        for row in result[1:]:
            list_rows.append(row.rstrip().split(sep=','))
        for element in list_rows:
            son = {k:v for k, v in zip(headers, element)}
            list_dik.append(son)
    return list_dik
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
