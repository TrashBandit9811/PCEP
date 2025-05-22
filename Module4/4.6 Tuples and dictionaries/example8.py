dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])