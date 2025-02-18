import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def merge(f1_content, f2_content):
    for disease,information in f2_content.items():

        if disease not in f1_content:
            f1_content[disease] = information
            continue

        f1_content[disease].update(information)

    return f1_content


if __name__ == "__main__":
    f1_content = load_json("./data/first_query.json")
    f2_content = load_json("./data/second_query.json")
    f3_content = load_json("./data/third_query.json")
    f4_content = load_json("./data/fourth_query.json")

    content = merge(f1_content, f2_content)
    content = merge(content, f3_content)
    content = merge(content, f4_content)

    content = group_change_names(content)

    save_json("wikidata.json", content)
