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
    monsters_folder = "monsters"

    print("Loading tropes...")
    pd_tropes = load_all_csv_from_folder(tropes_folder)
    print("Loding monsters...")
    pd_monsters = load_all_csv_from_folder(monsters_folder)

    # let's extract 5 random tropes
    random_indexes = []
    while len(random_indexes) < 5 :
        index = random.randint(0, len(pd_tropes))
        if index not in random_indexes :
            random_indexes.append(index)

    tropes = [ pd_tropes.iloc[i].values for i in random_indexes ]

    print("%d random tropes:" % len(tropes))
    for trope in tropes :
        print("\t\"%s\" -> %s" % (trope[0], trope[1]))

    # let's extract 5 random D&D monsters
    random_indexes = []
    while len(random_indexes) < 5 :
        index = random.randint(0, len(pd_monsters))
        if index not in random_indexes :
            random_indexes.append(index)

    monsters = [ pd_monsters.iloc[i].values for i in random_indexes ]

    print("%d random monsters:" % len(monsters))
    for monster in monsters :
        print("\t\"%s\"" % monster[0])


    return

if __name__ == "__main__" :
    sys.exit( main() )
