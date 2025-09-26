import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

user_input = input("Text to convert: >").strip().upper()
input_split = [letter for letter in user_input]
dict_split = {row["letter"]:row["code"] for (index, row) in df.iterrows() if row["letter"] in input_split}

final_message = [dict_split[letter] for letter in input_split if letter in dict_split] #dict_split[letter] palauttaa kirjaimen yhteydessä olevan arvon, eli A -> Alpha.
print(final_message)