from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
from nltk.corpus import stopwords
import os

#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


#Tokenze all the contect for each file.
def TokenizeAndStemmingFiles() :
    '''
        Tokenize every file from 'DATA/News' and save into 'Θα δώ'.
    '''
    
    AllTokens = {}
    #Find all of the files.
    files = os.listdir("DATA/News")
    #Loop to take every file.
    for file in files :
        #open the file and read.
        with open(f"DATA/News/{file}","r+") as f:
            #loop every line of the file.
            file_tokens = []
            for line in f :
                newline = line.split("~")[1]  #Take the wanted data.
                tokens = word_tokenize(newline)  #Tokenize the data.
                line_tokens = ""
                for token in tokens :
                    word = stemmer.stem(token)
                    if word not in stop_words :
                        line_tokens += word + " "

                file_tokens.append(line_tokens)
        AllTokens[file.split("-")[1]] = file_tokens
    return AllTokens

                          

if __name__ == "__main__" :
    a = TokenizeAndStemmingFiles()
    print(a)
    pass

