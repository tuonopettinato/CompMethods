import numpy as np
import argparse
from loguru import logger
import matplotlib.pyplot as plt
import time

start_time = time.time() #Here the clock starts

#We define letters of alphabet. We don't distinguish between uppercase and lowercase.
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cap_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#We create the parser variable giving the nameprogram and a description of what it does
parser = argparse.ArgumentParser(prog='wordcount',
    description="This program counts the letter occurrences in a given text . There are two valid arguments we can give to the program. First argument is necessary and is the file we want to read; it has to be in the same folder as the program. The second argument is optional and his value will determine if the plot will be shown or not: keep it empty if you want see the plot, insert 'n' if you are not interested in the plot.")
parser.add_argument('infile') #First argument: input file txt
parser.add_argument('histogram_choice', nargs='?', default='y') #Second argument. Printing the istogram. It is an optional value




def process_file(infile, histogram_choice):
    """
    This function will count and print the number of letters contained in the infile. It has been
    implemented the possibility to plot an histogram
    of letters occurrences.
    """
    logger.info(f'Opening input file {infile}...')
    data = open(infile, encoding= 'utf-8').read() #Data reading
    total_characters = len(data)
    logger.info(f'Done, {total_characters} character(s) found.')
    histogram = np.array([])

    '''
    We start a for cycle that will search each letter (lowercase and uppercase) in the text. The sum
    of the two cases will be stacked in the
    histogram empty array. In order to make an histogram with decreasing order
    of occurrences we have associated the occurrences with
    their alphabet letter.
    '''

    for letter,cap_letter in zip(alphabet, cap_alphabet):
        letter_frequency = 100*(data.count(letter) + data.count(cap_letter))/total_characters
        histogram = np.append(histogram, letter_frequency)
        print(cap_letter, ':',  np.round(letter_frequency, 2), '%' )
    ordering = np.argsort(histogram)[::-1] #It creates an array of indexes that are keeping track of the position changes in order to give the decreasing order
    histogram = np.sort(histogram)[::-1] #It creates a sorted array in decreasing order
    label_letters = [alphabet[i] for i in ordering] #Reordering the alphabet letters

    #If choice for plotting the histogram

    if histogram_choice  == 'y':
        plt.figure(f'Letter frequency in {infile}')
        plt.bar(label_letters, histogram, width=0.5, color='tab:blue')
        plt.ylabel('Frequency (%)')
        end_time = time.time() #stopwatch
        runtime = end_time - start_time
        logger.info(f'Runtime is: {runtime:.2f} seconds')
        plt.show()
    elif histogram_choice  == 'n':
        end_time = time.time() #stopwatch
    else:
        logger.error("Invalid value for histogram_choice. Please enter 'n' if you don't want to see the plot ")


if __name__== '__main__':
    args = parser.parse_args()
    process_file(args.infile, args.histogram_choice)



