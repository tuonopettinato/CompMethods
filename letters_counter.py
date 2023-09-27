import numpy as np
import argparse
from loguru import logger
import matplotlib.pyplot as plt
import time

start_time = time.time()


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cap_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

parser = argparse.ArgumentParser(prog='wordcount',
    description='Count the letter frequency in a text. The first positional argument is the .txt file you want to submit, whereas if the second argument is y, the histogram will be shown.')
parser.add_argument('infile')
parser.add_argument('histogram_choice')

def process_file(infile, histogram_choice):
    """
    """
    logger.info(f'Opening input file {infile}...')
    data = open(infile, encoding= 'utf-8').read()
    total_characters = len(data)
    print(total_characters)
    logger.info(f'Done, {total_characters} character(s) found.')
    histogram = np.array([])
    for letter,cap_letter in zip(alphabet, cap_alphabet):
        letter_frequency = 100*(data.count(letter) + data.count(cap_letter))/total_characters
        histogram = np.append(histogram, letter_frequency)
        print(cap_letter, ':',  letter_frequency, '%' )
    ordering = np.argsort(histogram)[::-1]
    histogram = np.sort(histogram)[::-1]
    label_letters = [alphabet[i] for i in ordering]
    if histogram_choice  == 'y':
        plt.figure(f'Letter frequency in {infile}')
        plt.bar(label_letters, histogram, width=0.5, color='tab:blue')
        plt.ylabel('Frequency (%)')
        end_time = time.time()
        runtime = end_time - start_time
        logger.info(f'Runtime is: {runtime:.2f} seconds')
        plt.show()
    else: None

if __name__== '__main__':
    args = parser.parse_args()
    process_file(args.infile, args.histogram_choice)




