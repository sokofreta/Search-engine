import pandas as pd
import string

class Convertor():
    """
        This class is a trasformer which formats the data to a wanted state.
        This step helps on the future because the data it is formated and can easily
        and effortlessly be used on the the next actions.
    """
    def __init__(self):
        self.dates =[]
        self.urls =[]
        self.text = []
        self.df = pd.read_csv("Engine/Test_dataset.csv")

        for row in  self.df.itertuples() :
        
            self.text.append(str(row.title)  + "{% %}" + str(row.description))
            self.urls.append(row.guid) # guid-> gloabl unique identifier for new 
            self.dates.append(row.pubDate) 

    def Get_ftext(self,des:bool) -> list[dict]:
        """
            This fuction return a list of terms without punduations,  
            for futher actions such as Tokenization, Lemming, Stemming.

            Parameters
            ----------
            bool: EXT ==> 
                If True, return the title and the description. 
                If False, return only the title. 

            Examples
            ---------- 
            >>> self.text = ["Terms of the first new;","Terms of the second !"]

            The above will formated as 
            >>> self.text2 =   [{'Doc_id': 0, 'Terms': 
                                    'Terms of the first new'}, # ; -> removed
                                {'Doc_id': 1, 'Terms': 
                                    'Terms of the second'}]    # ! -> removed
        """

        title =[]
        terms_per_doc = []


        # Here the title it is seperared from description so if the user wants
        # a quick search this will be made at the titles and not the description.
        # If the user wanted a more advanced search then the engine will look at
        # the text that the description has.

        for index,item in enumerate(self.text):
            title = str(item.split("{% %}")[0])
            description = str(item.split("{% %}")[1])

            if(des):
                text = title  +  description
            else :
                text= title

            formated_text = {
                "Doc_id":index,
                "Terms": text.translate(str.maketrans('','',string.punctuation))
            }
            terms_per_doc.append(formated_text)
        return terms_per_doc

    def Get_furls(self)  -> list[dict]:
        """
            This fuction return a dictionary of the urls in term of categories 
            and by domain.

            Examples
            ------- 
            >>> given url = "www.bbc.co.uk/news/business-60509453"
                formated_date = {"Doc_id":0,
                                 "domain" : "bbc.co.uk",
                                 "category" : "news",
                                 "sub_category" : "business"}
        """
        #  https://www.bbc.co.uk/news/technology-60608222
        self.furls = []
        # print(self.urls[21].split("/")[2:4]) # -> ['www.bbc.co.uk', 'news']
        
        for i in range(20):
            url_info = self.urls[i].split("/")
            mydict =  { 
                            "Doc_id":i,
                            "domain" : url_info[2],
                            "category" : url_info[3],
                            "sub_category" : url_info[4].split("-")[0]
                        }
            self.furls.append(mydict)
        
        print(self.furls)

    def Get_fdates(self) -> list[dict]:
        """
            This fuction formated the given dates into more readable from the 
            computer dates to easily organize them.

            Example 
            ----
            >>> given date = 'Mon, 07 Mar 2022 00:14:42 GMT' 
                formated_date ={"Doc_id":13,
                                "Year"  :2022,
                                "Month" :3,
                                "Day"   :7}
        """
        dates = []
        for index,_ in enumerate(self.dates):
            # self.dates[index].split(" ")[1:5]

            # convert every month into a number using switch.
            date = self.dates[index].split(" ")[1:5]
            # print(date[])
            month = 0 
            match date[1]:
                case "Jan": 
                    month = 1
                case "Feb": 
                    month = 2          
                case "Mar": 
                    month = 3                   
                case "Apr": 
                    month = 4   
                case "May": 
                    month = 5                   
                case "Jun": 
                    month = 6                   
                case "Jul": 
                    month = 7                  
                case "Aug": 
                    month = 8                  
                case "Sep": 
                    month = 9               
                case "Oct": 
                    month = 10               
                case "Nov": 
                    month = 11            
                case "Dec": 
                    month = 12                    
                case _:
                    pass

            formated_date = {
                "Doc_id":index,
                "Year":date[2],
                "Month":month,
                "Day":int(date[0])
            }
            
            dates.append(formated_date)
        return dates

if __name__ == "__main__":
    print("==============================TERMS==============================")
    print(f"formated text : {Convertor().Get_ftext()}")

    print("==============================DATES==============================")
    print(f"formated date : {Convertor().Get_fdates()}")

    print("==============================URLS==============================")
    print(f"formated url : {Convertor().Get_furls()}")