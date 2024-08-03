<h1><div align="right">
<code>🇺🇸</code> 
<a href="README-RU.md">🇷🇺</a>
</div>
IRPNet
</h1>

IRPNet is a model for classifying textual reviews into positive and negative. Completed as a bachelor's diploma work.

> <samp><mark>IRPNet</mark></samp> is an abbrevation for "<samp><mark>I</mark></samp>s <samp><mark>R</mark></samp>eview <samp><mark>P</mark></samp>ositive?"-determining <samp><mark>Net</mark></samp>work.

## Repository structure
There are two folders in repository. One is for working with data and training the model, the second is a user interface for interacting with the trained model:
- data processing:
  - `Parsing.ipynb` - parsing KinoPoisk using API to extract labeled reviews;
  - `Embedding.ipynb` - training a Word2Vec model based on all extracted KinoPoisk reviews;
  - `Preprocessing.ipynb` - forming of qualitative training dataset for a neural network;
  - `Training.ipynb` - training a neural network on a GPU using Google Colab;
  - `utils.py` - some features like timer and progress bar printing;
- interface:
  - `main.py` - CLI implementation;
  - `model.py` - classification model implementation;
  - `utils.py` - some features like colored output in CLI;
  - `parameters/` - parameters of neural network (embedding, dictionary of tokens, weights and biases).

## Model architecture
![](https://github.com/Ostrill/IRPNet/blob/master/assets/architecture.png?raw=true)

## Quality metrics
Metrics calculated for a dataset of more than 200K KinoPoisk reviews:
|    Metric | Value              |
|----------:|:-------------------|
|  Accuracy | 0.9134621659162305 |
| Precision | 0.9914457491022066 |
|    Recall | 0.909656810116406  |
|  F1-score | 0.9487919240454142 |

## Technologies
- [Kinopoisk Api Unofficial](https://kinopoiskapiunofficial.tech/) `[2.0.1]` - parsing reviews;
- [Pandas](https://pandas.pydata.org/) `[1.4.2]` - working with data;
- [Matplotlib](https://matplotlib.org/) `[3.4.3]` - visualization;
- [PyTorch](https://pytorch.org/) `[1.11.0]` - neural network;
- [Gensim](https://radimrehurek.com/gensim/) `[4.2.0]` - Word2Vec model;
- [Jupyter Notebook](https://jupyter.org/) - interactive environment for Python;
- [Google Colab](https://colab.research.google.com/) - GPU training.

## Usage
First of all, you need to install PyTorch:

```bash
$ pip install torch
```

Next, you need to [download](https://github.com/Ostrill/IRPNet/releases/tag/v1.0.0) a module consisting of `model.py` and a folder with model parameters, and then insert these files into your project.

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