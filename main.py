dictionary = {"speak" : "konuşmak",
                "walk" : "yürümek",
}
word=input("Aramak istediğiniz kelimeyi giriniz")
if word in dictionary.keys():
    print(dictionary[word])
    
else:
    dictionary.append(word)
