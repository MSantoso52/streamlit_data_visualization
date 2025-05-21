import pandas as pd

def read_data():
    
    file_path = "revenue_data.csv"

    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error while readind CSV file {e}")
        return None

if __name__=="__main__":

    df = csvToPandas()

    df.info()

    print(df.head())


