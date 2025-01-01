import sys
import re

def RelativeDocs(docs: list[list[int]]) -> list[int] :
    '''

    `Params`
        Takes a list of the documents that it is relevand for each keyword in search query\n

    `Output`
        Gives a list of documents that is relative to ALL of the keywords.\n
        (aka. the documents that contain every keyword). 
    '''
   
    search_docs = []

    # Delete empty list of documents. 
    # (When no document is there for a keyword the list of it contain a 0) 
    for doc in docs :
        if doc[0] == 0 :
            continue
        else :
            search_docs.append(doc)

    # try and find the relative document(s) that contain all of the keywords.
    rel_docs = []
    for doc in search_docs :
        for value in doc :
            rel_docs.append(value)

    return rel_docs

def BasicSearch(search_word) :
    falo = False # 
    
    with open("DATA/ReversedIndex","r+") as f :    
        for line in f :
            word  = line.split('~')[0]
            doc_s = line.split('~')[1]
            if word.__eq__(search_word) :
                falo = True
                documents = re.sub("[{}]","",doc_s)
                documents = re.sub("\s","",documents)
                documents = re.split(",",documents)
    if falo :
        return documents
    else: 
        return [0]   

def AdvancedSearch() :
    search_query = sys.argv[1:]

    documents = []
    for word in search_query :
        documents.append(list(BasicSearch(word)))

    if documents[0][0]== 0 :
        print(f"There is no documents with {search_query[0]} in it.")
        pass
    else :
        relative_docs = RelativeDocs(documents)

        for value in relative_docs :
            with open(f"DATA/News/file-{value}","r") as f :
                for line in f :
                    print (re.sub("\n","",line.split("~")[1]))
                        

AdvancedSearch()