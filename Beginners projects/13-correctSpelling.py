from spellchecker import SpellChecker

spell = SpellChecker()
split_entry = []
entry = input("Please type something: ")
split_entry = str(entry).split()

def spellchecker(text):
    split_text = text.split()
    return spell.unknown(split_text)

print(spellchecker(entry))