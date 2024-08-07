<h1><div align="right">
<a href="README.md">🇺🇸</a>
<code>🇷🇺</code> 
</div>
IRPNet
</h1>

IRPNet - это модель для классификации текстовых отзывов на русском языке на положительные и отрицательные. Реализована в качестве бакалаврской выпускной квалификационной работы.

> Кстати, <samp><mark>IRPNet</mark></samp> - это аббревиатура к "<samp><mark>I</mark></samp>s <samp><mark>R</mark></samp>eview <samp><mark>P</mark></samp>ositive?"-determining <samp><mark>Net</mark></samp>work (нейросеть, определяющая, является ли отзыв положительным).

## Структура репозитория
Репозиторий состоит из двух папок. В одной из них лежат все ноутбкуки, в которых производилась обработка данных и обучение модели, во второй - реализация пользовательского интерфейса для демонстрации работы модели:
- data processing:
  - `Parsing.ipynb` - парсинг Кинопоиска с использованием api (извлечение массива рецензий);
  - `Embedding.ipynb` - обучение модели Word2Vec на всей выборке рецензий из Кинопоиска;
  - `Preprocessing.ipynb` - формирование качественной обучающей выборки для нейронной сети;
  - `Training.ipynb` - обучение нейронной сети на видеокарте (через Google Colab);
  - `utils.py` - некоторые утилиты, например, таймер и фукнция для вывода прогресс-бара;
- interface:
  - `main.py` - пользовательский интерфейс (CLI);
  - `model.py` - класс интерфейса модели;
  - `utils.py` - некоторые утилиты для пользовательского интерфейса;
  - `parameters/` - параметры нейронной сети (таблица эмбеддинга, словарь токенов, веса и смещения модели).

## Архитектура модели
![](https://github.com/Ostrill/IRPNet/blob/master/assets/architecture_ru.png?raw=true)

## Метрики качества
Все метрики были рассчитаны на выборке из более чем 200К рецензий Кинопоиска:
|   Метрика | Значение           |
|----------:|:-------------------|
|  Accuracy | 0.9134621659162305 |
| Precision | 0.9914457491022066 |
|    Recall | 0.909656810116406  |
|   F1-мера | 0.9487919240454142 |

## Стек технологий
- [Kinopoisk Api Unofficial](https://kinopoiskapiunofficial.tech/) `[2.0.1]` - парсинг рецензий из Кинопоиска;
- [Pandas](https://pandas.pydata.org/) `[1.4.2]` - работа с данными;
- [Matplotlib](https://matplotlib.org/) `[3.4.3]` - визуализация;
- [PyTorch](https://pytorch.org/) `[1.11.0]` - нейронная сеть;
- [Gensim](https://radimrehurek.com/gensim/) `[4.2.0]` - модель Word2Vec;
- [Jupyter Notebook](https://jupyter.org/) - интерактивная среда для Python;
- [Google Colab](https://colab.research.google.com/) - обучение модели на GPU.

## Использование модели
В первую очередь необходимо установить PyTorch:

```bash
$ pip install torch
```

Сразу после этого можно [скачать](https://github.com/Ostrill/IRPNet/releases/tag/v1.0.0) модуль, который состоит из файла `model.py` и папки с параметрами модели, а затем вставить его в Ваш проект.

Пример использования:

```Python
from model import Model


model = Model()

example_reviews = [
    'Все плохо, не советую',   # Negative 99.392%
    'Все отлично, рекомендую', # Positive 99.996%
    'В целом пойдет'           # Positive 64.878%
]

for review in example_reviews:
    pos, neg = model.process_review(review)
    print(review + ':')
    print(' Positive:', pos)
    print(' Negative:', neg)
```