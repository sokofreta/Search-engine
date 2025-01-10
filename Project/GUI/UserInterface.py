import tkinter as tk
import sys
sys.path.insert(0, 'C:/Users/seita/Documents/GitHub/Search-engine/Project/Engine')

from SearchWhateverYouWant import Search
from Tokenzation import My_Tokenizer


class GUI():

    def __init__(self):
        self.results_of_search = Search()
        self.tokenizer = My_Tokenizer()
        self.labels = tk.StringVar()

    def DataDisplay(self) :
        query = entry.get()
        keywords = self.tokenizer.Tokenize_query(query,lemm =True)
        results = self.results_of_search.Get_results(keywords) # results is dataframe

        label = tk.Label(root,textvariable=self.labels, justify=tk.LEFT,
                         fg="black",font=("Arial", 16, "bold"),padx=20)
        for row in results.itertuples() :
           self.labels.set(row._1)
        label.pack()
        


class CLI():

    def __init__(self):
        self.results_of_search = Search()
        self.tokenizer = My_Tokenizer()

    def show_data(self):
        unassembled_query = sys.argv[1:]
        query = ""
        for value in unassembled_query:
            query += str(value) + " "
        keywords = self.tokenizer.Tokenize_query(query,lemm =True)
        results = self.results_of_search.Get_results(keywords) # results is dataframe
        print(f"Looking for {keywords}")
        for row in results.itertuples() :
            print("---"*20 + f"FILE {row.Index}" + "---"*20)
            print(f"TF-IDF value: {self.results_of_search.tf_idf[row.Index]}")
            print(f"It has:\n\t Title -> '{str(row.title).lstrip()}'")
            print(f"\t It is posted at -> '{str(row.pubDate).lstrip()}'")
            print(f"\t Unique url indetifier -> '{str(row.guid).lstrip()}'")
            print(f"\t And description -> '{str(row.description).lstrip()}' \n")
        
    
if __name__ == "__main__" :

    CLI().show_data()
    # root = tk.Tk()
    # root.geometry("600x600")
    # entry = tk.Entry(root,textvariable="search",font="Arial 25",fg="black")
    # entry.pack(side="top")
    # button = tk.Button(root,command=GUI().DataDisplay,text="Search :)")
    # button.pack()         
    # root.mainloop()