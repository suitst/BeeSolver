# BeeSolver (Tim Suits 2023)

"""finds acceptable words for a given Spelling Bee input"""

import pandas as pd


def get_letters():
    center = input("Type the center letter here: ").lower()
    if len(center) != 1:
        raise Exception("Center must be only one letter")
    else:
        outer = input("Type the remaining six letters here: ").lower()
        query = center+outer
        if len(query) != 7:
            raise Exception("There must be six outer letters")
        else:
            return center, outer


def make_regex(center, outer):
    return f"[{center}+{outer}]+"


def find_words(words):
    center, letters = get_letters()
    search = make_regex(center, letters)

    words['Search'] = words['Words'].str.findall(search).where(words['Words'].str.contains(center))
    words['Found'] = words['Search'].str[0]

    answers = words['Found'].where(words['Found'] == words['Words'])
    answers.dropna(inplace=True)
    answers.reset_index(drop=True, inplace=True)

    answers.to_csv('./answers.csv')
    print(f'Words found: {answers}')


word_list = pd.read_csv('./words_proc.csv')


if __name__ == "__main__":
    find_words(word_list)
