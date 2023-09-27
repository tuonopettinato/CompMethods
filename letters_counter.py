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
    print(len(data))
    logger.info(f'Done, {len(data)} character(s) found.')
    histogram = np.array([])
    for letter,cap_letter in zip(alphabet, cap_alphabet):
        letter_occurrence = data.count(letter) + data.count(cap_letter)
        histogram = np.append(histogram, letter_occurrence)
        print(cap_letter,':  ', letter_occurrence)
    plt.figure('Letter occurrences')
    plt.bar(alphabet, histogram/np.sum(histogram), width=0.5, color='tab:blue')
    end_time = time.time()
    runtime = end_time - start_time
    logger.info(f'Runtime is: {runtime:.2f} seconds')
    if histogram_choice  == 'y':
        plt.show()
    else: None

if __name__== '__main__':
args = parser.parse_args()
process_file(args.infile, args.histogram_choice)




