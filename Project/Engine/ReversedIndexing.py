from Tokenzation import My_Tokenizer 

class ReverIndex():

    def __init__(self,EXT=False):
        self.tokens = My_Tokenizer(EXT).Get_cleanse_tokes()

    #Reveresed indexing techingue
    def ReversedIndexMatrix(self) -> dict:
        '''
            Takes the basic index matrix (Doc --> words) and converting it into \n
            a reversed index matrix (words --> Doc).
        '''
        index = {}
        
        self.tokens
        for i in self.tokens:
            doc = i
            for word in self.tokens[doc]:
                
                if word not in index:
                    index[word] = set({})
                index[word].add(i)
        return index

    def SortReversedIndexMatrix(self) -> dict:
        '''
            Sort and display a Reversed indexed matrix.
        '''
        indexes = self.ReversedIndexMatrix()
        keys = list(indexes.keys())
        keys.sort()

        # Sorted Dictionary
        sd = {i: indexes[i] for i in keys}
        # Display a more readable way of the Sorted Dictionary 
        # for key in keys :
        #     print(f"{key} : {sd[key]}")

        return sd
        
    def PrettifyRI(self) -> str :
        Data = self.SortReversedIndexMatrix()
        keys = Data.keys()
        pretty = ""

        for key in keys :
            pretty += f"{key}: {Data[key]} \n"

        with open("Reversed_index.txt","w+") as file :
            file.write(pretty)
        return pretty


if __name__ == "__main__" :
    print((ReverIndex(EXT=False).PrettifyRI()))
            
                
      