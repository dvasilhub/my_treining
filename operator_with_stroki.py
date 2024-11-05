import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        # Приводим строку к нижнему регистру и убираем пунктуацию
                        line = line.lower().translate(str.maketrans('', '', string.punctuation))
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)# + 1  # Позиция с 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)+1
        return words.count(word)

# Пример использования
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())  # Все слова
    print(finder.find('code'))      # Позиция слова
    print(finder.count('capitan'))     # Количество слов