from Tokenzation import TokenizeAndStemmingFiles


#Reveresed indexing techingue
def ReversedIndexMatrix() :
    '''
        Takes the basic index matrix (Doc --> words) and converting it into \n
        a reversed index matrix (words --> Doc).
    '''
    index = {}
    tokens = TokenizeAndStemmingFiles()
    for i in tokens.keys() :
        doc = tokens[i] 
        for line in doc:
            for word in line.split(" ") :
                if word not in index:
                    index[word] = set({})
                index[word].add(i)
    return index

def SortReversedIndexMatrix() :
    '''
        Sort and display a Reversed indexed matrix.
    '''
    indexes = ReversedIndexMatrix()
    keys = list(indexes.keys())
    keys.sort()

    # Sorted Dictionary
    sd = {i: indexes[i] for i in keys}

    for key in keys :
        print(sd[key])


    # Display a more readable way of the Sorted Dictionary 
    # for key in keys :
    #     print(f"{key} : {sd[key]}")

    return sd
    
def PrettifyRI() -> str :
    Data = SortReversedIndexMatrix()
    keys = Data.keys()
    pretty = ""

    for key in keys :
        pretty += f"{key}~{Data[key]} \n"

    with open("DATA/ReversedIndex","a+") as ri:
        ri.write(pretty)
    return pretty
if __name__ == "__main__" :
    PrettifyRI()
    pass
                
                
      