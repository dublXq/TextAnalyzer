from collections import Counter

class TextFormatter:

    def __init__(self):
        self.texter = None
        self.lister = []

    # Функция для подсчета количества слов
    def word_count(self, texter):
        self.texter = texter
        lst = texter.split()
        return self.lister.append(len(lst))

    # Функция для подсчета количества символов
    def character_count(self, texter):
        self.texter = texter
        return self.lister.append(len(texter))

    # Функция для подсчета цифр/чисел
    def numbers_count(self, texter):
        self.texter = texter
        val = 0
        for i in texter:
            if i.isdigit():
                val += 1
        return self.lister.append(val)

    # Функция на нахождения наиболее частого слова
    def most_frequent_word(self,texter):
        self.texter = texter
        lst = texter.split()
        val = 0
        counter = Counter(lst)
        for item in counter:
            c = counter[item]
            if c > 1:
                if c > val:
                    val = c
                    key = [key for key in counter if counter[key] == val]

        return self.lister.append(key)


