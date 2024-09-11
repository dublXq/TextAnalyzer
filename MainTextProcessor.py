
import TextFormatter

"""Главный класс, для взаимодействия с пользователем"""

TF = TextFormatter.TextFormatter()

def formated_text(texter):

    TF.word_count(texter)
    TF.character_count(texter)
    TF.numbers_count(texter)
    TF.most_frequent_word(texter)

    print(f"Количество слов = {TF.lister[0]}\n"
          f"Количество символов = {TF.lister[1]}\n"
          f"Количество цифр = {TF.lister[2]}\n"
          f"Слово которое чаще всего повторяется = {TF.lister[3]}")

if __name__ == '__main__':

    print("\nЗдравствуйте.(👉ﾟヮﾟ)👉)\n\nЯ Анализатор Текста, который поможет обработать Вам объемные текста, и не только.\n"
          "\nЯ умею:\n1. Подсчитывать количество слов\n"
          "2. Подсчитывать количество символов\n"
          "3. Подсчитывать количество повторяемых слов\n"
          "4. Подсчитывать количество цифр/чисел\n"
          "\nЧтобы начать, введите цифру -> 1. Для выхода, введите цифру -> 2.\n\nСоздатель --> https://github.com/dublXq\n")
    while True:
        val = input("1. Начать Анализ Текста\n2. Выход\nВвод: ")
        if val == "1":
            val = input("Введите пожалуйста текст: ")
            formated_text(val)
            break
        elif val == "2":
            break
        else:
            print("Вы ввели что-то не то, повторите пожалуйста еще раз :) ")

