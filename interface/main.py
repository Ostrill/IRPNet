from model import Model
from utils import *


model = Model()
EXIT_WORD = '-'
print(f' Для выхода введите {YEL}[{EXIT_WORD}]\n')
while True:
    review = input(f'{CYN} > {WHT}')
    if not review:
        continue
    elif review == EXIT_WORD:
        exit()
    try:
        result = model.process_review(review)
        print(beauty_output(*result))
    finally:
        continue
