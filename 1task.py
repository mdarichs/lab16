import nltk
import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import os

# Завантаження необхідних ресурсів для токенізації
nltk.download('punkt')
nltk.download('stopwords')

# Перевірка наявності файлу та виведення вмісту директорії
file_path = 'D:/pyproject/pythonProject4/milton-paradise.txt'
if not os.path.isfile(file_path):
    print(f"Файл {file_path} не знайдено! Перевірте шлях до файлу.")
    print("Ось вміст поточної директорії:")
    print(os.listdir())
    exit(0)

# Завантаження тексту з файлу
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
except Exception as e:
    print(f"Помилка при відкритті файлу: {e}")
    exit(0)

# Функція для підрахунку кількості слів у тексті
def count_words(text):
    sentences = nltk.sent_tokenize(text)  # Токенізація по реченням
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        k_words += len(words)
    return k_words

# Функція для знаходження 10 найбільш вживаних слів у тексті
def most_used_words(text):
    words = nltk.word_tokenize(text.lower())  # Токенізація та зниження регістру
    words = [word for word in words if word not in string.punctuation]  # Видалення пунктуації
    cnt = Counter(words)  # Підрахунок слів
    cort = cnt.most_common(10)  # Найбільш вживані слова

    x = [cort[el][0] for el in range(len(cort))]  # Слова
    y = [cort[el][1] for el in range(len(cort))]  # Кількість повторень у тексті

    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

# Функція для видалення стоп-слів та пунктуації
def remove_stopwords_and_punctuation(text):
    stop_words = set(stopwords.words('english'))  # Стоп-слова для англійської мови
    text = text.lower()  # Перетворення тексту на малу літеру
    text = text.translate(str.maketrans('', '', string.punctuation))  # Видалення пунктуації
    words = nltk.word_tokenize(text)  # Токенізація
    filtered_words = [word for word in words if word not in stop_words]  # Видалення стоп-слів
    return filtered_words

# Підрахунок кількості слів у тексті
total_words = count_words(text)
print(f"Кількість слів у тексті: {total_words}")

# Побудова графіка для 10 найбільш вживаних слів
most_used_words(text)

# Видалення стоп-слів та пунктуації, потім пошук найбільш вживаних слів
filtered_words = remove_stopwords_and_punctuation(text)
cnt_filtered = Counter(filtered_words)
filtered_cort = cnt_filtered.most_common(10)

# Побудова графіка для 10 найбільш вживаних слів після очищення
x_filtered = [filtered_cort[el][0] for el in range(len(filtered_cort))]
y_filtered = [filtered_cort[el][1] for el in range(len(filtered_cort))]

plt.bar(x_filtered, y_filtered)
plt.title("10 найбільш вживаних слів після видалення стоп-слів та пунктуації")
plt.xlabel("Слова")
plt.ylabel("Зустрічаються разів у тексті")
plt.show()
