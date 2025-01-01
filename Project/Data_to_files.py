
#Global + Local imports.
import pandas as pd
import os


def CreateDataFiles():
    '''
    This function converts the data from dataset into files.\n
    Also it creating a structure to help accesing the files more easily and make it more readable to humans.\n   
    '''

    try :
        os.mkdir("DATA")
    except :
        print("We are cooked")

    #Try creating the 'News' Directory that contain the core information.
    try :
        os.mkdir('DATA/News')
        #First_initianalzation()
        CreateFiles()
    except:
        print('Directory "News" already exist.')


    ''' 
        The purpose of the following functions is to create a structure
        and made the access to core information faster.
        this also helps to make filtering easier.
    '''

    #Try creating the 'Titles' Directory that contain the only the titles of each news.
    try :
        os.mkdir("DATA/Titles")
        CreateTitles()
    except:
       print('Directory "Titles" already exist.')

    #Try creating the 'Dates' Directory that contain the only the publicition date of each news.
    try :
        os.mkdir('DATA/Dates')
        CreateDates()
    except:
        print('Directory "Dates" already exist.')

    #Try creating the 'Links' Directory that contain the only the link of each news. 
    try :
        os.mkdir('DATA/Links')
        CreateLinks()
    except:
        print('Directory "Links" already exist.')

def First_initianalzation() :
    df = pd.read_csv("Original-Dataset/bbc_news.csv")
    df = df.iloc[:15]

    # Stable Dataset (Only for testing) 
    df.to_csv("Test_Dataset.csv" , index=False) 


#Greate a file for each of the row of the dataset.
def CreateFiles() :
    df = pd.read_csv("Test_Dataset.csv",index_col=False)
        
    #Read the amount of Columnds that Dataframe has
    for source in df :  
        #Create file for each row of the dataframe
        i=0
        while i < len(df) :

            #Creation of the file
            with open(f"DATA/News/file-{i}","a+",encoding="utf8") as f :
                f.write(f'{source}~'  + df[source].iloc[i] + '\n')
            i+=1


#Creation of the titles to easily access the core information.
def CreateTitles() :
    for file in os.listdir('DATA/News'):
            with open(f"DATA/News/{file}","r") as f:
                for line in f :
                    Cat_Data = line.split("~")
                    if Cat_Data[0] == "title":
                        title = Cat_Data[1].strip()
                        with open(f"DATA/Titles/{file}","w") as tf : #tf reference af title file.
                            tf.write(title)
                            break


#Creation of the date to easily access the core information.
def CreateDates() :
    for file in os.listdir('DATA/News'):
            with open(f"DATA/News/{file}","r") as f:
                for line in f :
                    Cat_Data = line.split("~")
                    if Cat_Data[0] == "pubDate":
                        date = Cat_Data[1].strip()
                        with open(f"DATA/Dates/{file}","w") as df : #df referce as date file.
                            df.write(date)
                            break


#Creation of the links to easily access the core information.
def CreateLinks() :
    for file in os.listdir('DATA/News'):
            with open(f"DATA/News/{file}","r") as f:
                for line in f :
                    Cat_Data = line.split("~")
                    if Cat_Data[0] == "link":
                        link = Cat_Data[1].strip()
                        with open(f"DATA/Links/{file}","w") as lf : #lf refers as link file.
                            lf.write(link)
                            break
                    


if __name__ == "__main__" :

    # #Create the test sample from data.
    # First_initianalzation()

    #Converting the data into files and store them into several dictionaries. 
    CreateDataFiles()
    
