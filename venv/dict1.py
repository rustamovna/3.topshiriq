from googletrans import Translator

class Dictionary:
    def __init__(self, uz: str = '', en: str = '') -> None:
        self.uz = uz
        self.en = en
        self.translator = Translator() 

    def add_word(self) -> None:
        if not self.en:
            self.en = self.translator.translate(self.uz, src="uz", dest="en").text
            print(f"Avtomatik tarjima: {self.en}")
        
        id = 1
        with open("words.txt", "a+") as file:
            file.seek(0)  
            id = len(file.readlines()) 
            file.write(f"{id+1}) {self.uz}, {self.en}\n")
        print(f"So'z saqlandi: {self.uz} -> {self.en}")
    
    def show_words(self) -> list[tuple[str, str]]:
        words = []
        try:
            with open("words.txt") as file:
                for line in file:
                    _, pair = line.strip().split(") ")
                    uz, en = pair.split(", ")
                    words.append((uz, en))
        except FileNotFoundError:
            print("Hozircha hech qanday so'z qo'shilmagan.")
        return words
    
    def random_words(self, num: int):
        from random import sample
        words = self.show_words()
        if len(words) >= num:
            for uz, en in sample(words, num):
                print(f"O'zbekcha: {uz}, Inglizcha: {en}")

option = 1

while option:
    option = int(input("1. So'z qo'shish\n2. So'zlarni ko'rish\n3. Tasodifiy so'zlar\n0. Chiqish\nKiritish: "))

    if option == 1:
        uzbekcha = input("O'zbekchasini kiriting: ")
        obj = Dictionary(uzbekcha, inglizcha)
        obj.add_word()
    elif option == 2:
        obj = Dictionary()
        words = obj.show_words()
        for uz, en in words:
            print(f"{uz} -> {en}")
    elif option == 3:
        obj = Dictionary()
        num = int(input("Nechta so'z olishni xohlaysiz: "))
        obj.random_words(num)
    elif option == 0:
        print("Chiqish.")
    