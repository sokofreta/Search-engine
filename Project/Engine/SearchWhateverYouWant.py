import re
from Testing_engine import Testing_engine
from ReversedIndexing import ReverIndex
import numpy as np

class Search():

    def __init__(self,EXT=False):
        self.Extended = EXT
        self.rev_index = ReverIndex(EXT)
        self.df = Testing_engine().get_testing_data()
        self.search_query  = ""
        self.tf_idf = {}
        

    def BasicSearch(self,word_to_search) :
        data = self.rev_index.SortReversedIndexMatrix()
        if (word_to_search in data ): # exteded if contion per word ---> or word_to_search in data
            clean_data = re.sub("[},{]","",str(data.get(word_to_search))).split(" ")
            formated_data = {int(item) for item in clean_data}
    
            
            self.idf = np.log10(len(self.rev_index.tokens)/len(formated_data)) 

            self.tf = {}
            self.tf_idf = {}

            # Calculate the tf and   
            for doc in formated_data :
                total_terms = len(self.rev_index.tokens.get(doc))
                freq_of_query_word = self.rev_index.tokens.get(doc).count(word_to_search)
                term_freq = freq_of_query_word/total_terms
                self.tf.update({doc: term_freq})
                self.tf_idf.update({doc: term_freq*self.idf})

            return formated_data 


    def AdvancedSearch(self) :
    
        documents = []
        for word in self.search_query :
            documents.append(self.BasicSearch(word)) 
        sorted_tf_idf_docs = sorted(self.tf_idf.items(), key=lambda x:x[1],reverse=True)
        best_docs = dict(sorted_tf_idf_docs)
        return list(best_docs.keys())


    def Get_results(self,query:list):
        self.search_query = query
        docs_ordered_by_relativity = self.AdvancedSearch() 
        docs_to_be_displayed = self.df.iloc[docs_ordered_by_relativity] 
        return docs_to_be_displayed
                 
if __name__ == "__main__":
    print(Search(EXT=False).Get_results("war"))