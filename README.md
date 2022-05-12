# IRPNet
IRPNet is a model for classifying textual reviews into positive and negative. Completed as a bachelor's graduation work by a student of RTU MIREA Zhuravlev V. E.

## Repository structure
There are two folders in repository. One is for working with data and training the model, the second is a user interface for interacting with the trained model:
- data processing:
  - `Parsing.ipynb` - parsing KinoPoisk using API to extract labeled reviews
  - `Embedding.ipynb` - training a Word2Vec model based on all extracted KinoPoisk reviews
  - `Preprocessing.ipynb` - forming of qualitative training dataset for a neural network
  - `Training.ipynb` - training a neural network on a GPU using Google Colab
  - `utils.py` - some features like timer and progress bar printing
- interface:
  - `main.py` - CLI implementation
  - `model.py` - classification model implementation
  - `utils.py` - some features like colored output in CLI
  - `parameters` - parameters of neural network (embedding, dictionary of tokens, weights and biases)

## Model architecture
![](https://github.com/Ostrill/IRPNet/blob/master/assets/architecture.png?raw=true)

## Quality metrics
Metrics calculated for a dataset of more than 200'000 KinoPoisk reviews:
|    Metric | Value              |
|----------:|:-------------------|
|  Accuracy | 0.9134621659162305 |
| Precision | 0.9914457491022066 |
|    Recall | 0.909656810116406  |
|  F1-score | 0.9487919240454142 |

## Technologies
- [Kinopoisk Api Unofficial](https://kinopoiskapiunofficial.tech/) - parsing reviews
- [Pandas](https://pandas.pydata.org/) - working with data
- [Matplotlib](https://matplotlib.org/) - visualization
- [PyTorch](https://pytorch.org/) - neural network
- [Gensim](https://radimrehurek.com/gensim/) - Word2Vec model
- [Google Colab](https://colab.research.google.com/) - GPU training

## Usage
First of all, you need to install PyTorch:

```bash
$ pip install torch
```

Next, you need to [download]() a module consisting of model.py and a folder with model parameters, and then insert these files into your project.

After that you can use IRPNet:

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