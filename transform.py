import pandas as pd
from datetime import datetime 
import sys

def transform_data(input_file):
        df=pd.read_csv(input_file) #load the data
        df.drop_duplicates(subset=['symbol','date'],inplace=True) # drop duplicates
        df.fillna(0, inplace=True)# replacing null values with 0
        df['date']=pd.to_datetime(df['date'],utc=True) # ttransform it to date to time 
        df=df.sort_values(by=['date','symbol'],ascending =True) #sorting the date 

        transformed_file=f"transformed_stock_data{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        df.to_csv(transformed_file, index=False)

        print(f"✅ Transformed data saved to {transformed_file}")
        return transformed_file

    
if __name__ =="__main__":
        if len(sys.argv) != 2:
          print("Usage: python transform_data.py <input_csv_file>") #in terminal run python transform.py <input_raw_data_csv_file>
        else:
          transform_data(sys.argv[1])


