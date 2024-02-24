# import libraries

import chardet 
import csv

# identifying the encoding

def find_encoding(file):
    with open(file,'rb') as file_enc:
        encoding_file = chardet.detect(file_enc.read())

        encoding_detected = encoding_file['encoding']
    return encoding_detected


# identifying the delimiter

def find_delimeter(file):
    with open(file, 'r', newline='') as file_delimiter:

        delim_detect = csv.Sniffer()

        sample_delim = file_delimiter.read(1024)

        delimiter = delim_detect.sniff(sample_delim).delimiter
    return delimiter


def remove_accents (param_to_remove):

    #variables
    string_from = 'áéíóúàèìòùâêîôûãõäëïöüçñÿýÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÇÑŸÝ'
    string_to = 'aeiouaeiouaeiouaoaeioucnyyAEIOUAEIOUAEIOUAOAEIOUCNYY'
    result = ''
    count = 0

    while count < len(param_to_remove):

        word = param_to_remove[count]
        count+=1
        index = string_from.find(word)

        if index == -1:
            result += word
        else:
            result += string_to[index] 
    return result
