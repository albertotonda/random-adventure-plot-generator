# Simple Python script that generates random plot seeds for an adventure
# by Alberto Tonda, <alberto.tonda@gmail.com>

import os
import pandas as pd
import random
import sys

def load_all_csv_from_folder(folder) :

    csv_files = [ os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".csv") ]

    pd_list = []
    for csv_file in csv_files :
        df = pd.read_csv(csv_file)
        pd_list.append(df)

    return pd.concat(pd_list)


def main() :

    tropes_folder = "tropes"

    print("Loading tropes...")
    pd_tropes = load_all_csv_from_folder(tropes_folder)

    # let's extract 5 random tropes
    random_indexes = []
    while len(random_indexes) < 5 :
        index = random.randint(0, len(pd_tropes))
        if index not in random_indexes :
            random_indexes.append(index)

    tropes = [ pd_tropes.iloc[i].values for i in random_indexes ]

    print("Random tropes:")
    for trope in tropes :
        print("\t\"%s\" -> %s" % (trope[0], trope[1]))

    return

if __name__ == "__main__" :
    sys.exit( main() )
