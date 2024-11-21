import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Читання тексту з файлу
with open('text100.txt', 'r') as file:
    text = file.read()

# Токенізація по словам
tokens = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha()]
stemmed_tokens = [stemmer.stem(token.lower()) for token in tokens if token.isalpha()]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token not in stop_words]

# Видалення пунктуації
filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Збереження обробленого тексту в новий файл
processed_text = ' '.join(filtered_tokens)

# Запис обробленого тексту у файл
with open('processed_text.txt', 'w') as file:
    file.write(processed_text)

print("Оброблений текст успішно записано в файл 'processed_text.txt'.")
