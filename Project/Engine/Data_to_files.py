
#Global + Local imports.
import pandas as pd

class Data():
    
    def __init__(self):
        self.col = []
        self.df = pd.read_csv("Original-Dataset/bbc_news.csv")
        self.col_len = len(self.df.columns)
        for i in range(self.col_len):
            self.col.append(self.df.columns[i])
    
    def Get_df(self):
        return self.df



if __name__ == "__main__" :

    #Converting the data into dataframe and store it.
    data = Data() 
    
