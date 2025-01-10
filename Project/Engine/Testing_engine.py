import pandas as pd
from Data_to_files import Data

class Testing_engine():
    """
        This class reduce the rows of a dataframe for easier debugging. 
    """
    # Only keep the first 20 lines for testing.
    # Αdditional test will select random (or all dataset) for testing.
    def __init__(self):
        self.df = Data().Get_df()
        self.testing_data = self.df.iloc[:20]
        self.testing_data.to_csv("Test_dataset.csv",index=False)

    def get_testing_data(self):
        return self.testing_data


if __name__=="__main__":
    test = Testing_engine().get_testing_data()
    print(test)
