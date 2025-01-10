import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Store_categories import Convertor
from nltk.stem import PorterStemmer ,WordNetLemmatizer 


# # Downloads for stemming
# nltk.download("punkt")

# # Downloads for lemming
# nltk.download("wordnet")
# nltk.download("omw-1.4")


class My_Tokenizer():
    """ 
        Takes data and tokenize them.
    """
    #Every time that the engine starts it is import the new dataset of stopwords
    def __init__(self,EXT=False):
        # import nltk
        # nltk.download('stopwords')

        self.stop_words = set(stopwords.words('english'))
        data_to_tokenize = Convertor()
        self.Terms ={}
        for value in data_to_tokenize.Get_ftext(des=EXT) :
           self.Terms.update({value.get("Doc_id") : value.get("Terms")})

           
        self.Tokenized_texts = {}
        self.Tokenize() # Tokenize the given text.

        self.cleanshed_tokens = self.Get_cleanse_tokes()
        

    # Tokenze all the contect for each file.
    def Tokenize(self) :
        '''
            Here is where the data get Tokenized
            
        '''
        for key in self.Terms :
            self.Tokenized_texts.update({key:word_tokenize(self.Terms.get(key))})


    # Tokenze all the contect for each file.
    def Get_stemmed_tokens(self) -> dict :
        """
            This fuction return a list of dictionaries. \n
            The key is the Doc_id. \n
            The Value is a list that contains tokens that is Stemmed.  

            Examples
            -------- 
            >>> Stemmed_tokens = {0: ['Stemmed','Tokens' ,'of' ,'the', 'first' ,'new'], 
                                  1: ['Stemmed','Tokens' ,'of' ,'the', 'second']}
        """
         
        ps = PorterStemmer()

        stemmed_tokens = {}
        for key in self.cleanshed_tokens:
            UNformated_stemmed_tokens = []
            # go throught every word.
            for value in self.cleanshed_tokens[key]:
                UNformated_stemmed_tokens.append(ps.stem(value))
            stemmed_tokens.update({key : UNformated_stemmed_tokens})

        return stemmed_tokens


    # Tokenze all the contect for each file.
    def Get_lemmatized_tokens(self) -> dict :
        """
            This fuction return a list of dictionaries. \n
            The key is the Doc_id \n
            The Value is a list that contains tokens that is lemmatized  

            Examples
            -------- 
            >>> lemmed_tokens = {0: ['Lemmatized','Tokens' ,'of' ,'the', 'first' ,'new'], 
                                 1: ['Lemmatized','Tokens' ,'of' ,'the', 'second']}
        """
        wnl = WordNetLemmatizer()

        lemmed_tokens = {}
        for key in self.cleanshed_tokens:
            UNformated_lemmed_tokens = []
            # go throught every word.
            for value in self.cleanshed_tokens[key]:
               UNformated_lemmed_tokens.append(wnl.lemmatize(value))
            lemmed_tokens.update({key : UNformated_lemmed_tokens})

        return lemmed_tokens


    # Tokenze all the contect for each file.
    def Get_cleanse_tokes(self) -> dict :
        """
            Take tokenized text and removes stopwords\n

            Examples
            -------- 
            >>> cleansed_tokes = {0: ['Cleansed','Tokens' ,'of' ,'the', 'first' ,'new'], 
                                  1: ['Cleansed','Tokens' ,'of' ,'the', 'second']}
        """
        clean_data = {}
        for key in self.Tokenized_texts:
            semi_cleaned_data = []

            # go throught every word.
            for value in self.Tokenized_texts[key]:
                if value not in self.stop_words:
                    semi_cleaned_data.append(value.lower())
            clean_data.update({key : semi_cleaned_data})

        return clean_data


    def Tokenize_query(self,query : str , lemm = False):
        
        query.translate(str.maketrans('','',string.punctuation))

        raw_search_words = word_tokenize(query)
        search_words_without_stopwords = []
        for value in raw_search_words:
                if value not in self.stop_words:
                    search_words_without_stopwords.append(value.lower())
         
        stemmed_words = []
        lemmed_words = []
        for word in search_words_without_stopwords:
            stemmed_words.append(PorterStemmer().stem(word))
            lemmed_words.append(WordNetLemmatizer().lemmatize(word))
        if lemm :
            return lemmed_words
        else :
            return stemmed_words

if __name__ == "__main__" :
    print(My_Tokenizer(EXT=False).Get_cleanse_tokes())
    pass

