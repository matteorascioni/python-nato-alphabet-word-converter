#Enter this commands before run this program
#python3 -m venv venv
#pip3 install pandas
import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)