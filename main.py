dictionary = {"speak": "konuşmak",
              "walk": "yürümek",
              "length": "uzunluk",
              "print": "yazdırmak",
              "append": "eklemek"}

print("Merhaba, modern kelimeler sözlüğüne hoş geldiniz, burada anlamını bilmediğin kelimeleri yazarak anlamını öğrenebilirsiniz:)")
for i in range(5):
    word = input("Lütfen aramak istediğiniz kelimeyi giriniz:")
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        meaning = input("Girdiğiniz kelime sözlükte bulunmamaktadır, bu kelimenin anlamını giriniz:")
        dictionary[word] = meaning
        print("kelime sözlüğe eklendi!")
        
print(dictionary)
