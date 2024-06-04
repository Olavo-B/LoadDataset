import os
import io
import gzip
import zipfile
import requests
import pandas as pd
from tqdm import tqdm


def load_susy(debug=False, save_path=None, load_path=None):
    """
    Load the SUSY dataset from the UCI Machine Learning Repository.


    :param debug: If True, only load a subset of the dataset for faster testing
    :param save_path: If provided, save the dataset to this path
    :param load_path: If provided, load the dataset from this path

    :return: A tuple containing the data and target variables


    """

    if load_path and os.path.exists(load_path):
        print(f"Loading dataset from {load_path}")
        df = pd.read_csv(os.path.join(load_path, 'susy.csv'))
 

        # Rename the first column to 'target' and separate it as a Series
        target = df.iloc[:, 0]
        target.name = 'target'

        # Get the remaining columns as a DataFrame
        data = df.iloc[:, 1:]

        if debug:

            print("Loaded SUSY dataset successfully. Returning data and target variables.")
            print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/SUSY")
            print(f"Data: {data.shape}")
            print(f"Target: {target.shape}")

        return data,target


    url = 'https://archive.ics.uci.edu/static/public/279/susy.zip'
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm(total=total_size, unit='iB', unit_scale=True, desc='Download Susy Dataset')

        file_buffer = io.BytesIO()
        for data in response.iter_content(block_size):
            t.update(len(data))
            file_buffer.write(data)
        t.close()

        file_buffer.seek(0)

        with zipfile.ZipFile(file_buffer) as the_zip:
            with the_zip.open('SUSY.csv.gz') as gz_file:
                with gzip.open(gz_file) as the_file:
                    # Load the full CSV into a DataFrame
                    print("Load CSV into DataFrame")
                    the_file.seek(0)
                    df = pd.read_csv(the_file, names=[i for i in range(0, 19)])

                    # Rename the first column to 'target' and separate it as a Series
                    target = df.iloc[:, 0]
                    target.name = 'target'

                    # Get the remaining columns as a DataFrame
                    data = df.iloc[:, 1:]

                    if save_path:
                        # Ensure the save path exists
                        os.makedirs(save_path, exist_ok=True)

                        if debug:
                            print(f"Saving dataset to {save_path}")
                       
                        df.to_csv(os.path.join(save_path, 'susy.csv'), index=False)
           

                        
                    if debug:
                        print("="*100)
                        print("Loaded SUSY dataset successfully. Returning data and target variables.")
                        print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/SUSY")
                        print(f"Data: {data.shape}")
                        print(f"Target: {target.shape}")
                        print("="*100)
                        



                    return data, target

    else:
        ValueError(f"Failed to download dataset from {url}. Status code: {response.status_code}")
        return None

def load_higgs(debug=False, save_path=None, load_path=None):
    """
    Load the HIGGS dataset from the UCI Machine Learning Repository.


    :param debug: If True, only load a subset of the dataset for faster testing
    :param save_path: If provided, save the dataset to this path
    :param load_path: If provided, load the dataset from this path

    :return: A tuple containing the data and target variables


    """

    if load_path and os.path.exists(load_path):
        print(f"Loading dataset from {load_path}")
        df = pd.read_csv(os.path.join(load_path, 'higgs.csv'))
 

        # Rename the first column to 'target' and separate it as a Series
        target = df.iloc[:, 0]
        target.name = 'target'

        # Get the remaining columns as a DataFrame
        data = df.iloc[:, 1:]

        if debug:

            print("Loaded HIGGS dataset successfully. Returning data and target variables.")
            print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/HIGGS")
            print(f"Data: {data.shape}")
            print(f"Target: {target.shape}")

        return data,target


    url = 'https://archive.ics.uci.edu/static/public/280/higgs.zip'
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm(total=total_size, unit='iB', unit_scale=True, desc='Download Higgs Dataset')

        file_buffer = io.BytesIO()
        for data in response.iter_content(block_size):
            t.update(len(data))
            file_buffer.write(data)
        t.close()

        file_buffer.seek(0)

        with zipfile.ZipFile(file_buffer) as the_zip:
            with the_zip.open('HIGGS.csv.gz') as gz_file:
                with gzip.open(gz_file) as the_file:
                    # Load the full CSV into a DataFrame
                    print("Load CSV into DataFrame")
                    the_file.seek(0)
                    df = pd.read_csv(the_file, names=[i for i in range(0, 29)])

                    # Rename the first column to 'target' and separate it as a Series
                    target = df.iloc[:, 0]
                    target.name = 'target'

                    # Get the remaining columns as a DataFrame
                    data = df.iloc[:, 1:]

                    if save_path:
                        # Ensure the save path exists
                        os.makedirs(save_path, exist_ok=True)


                        if debug:
                            print(f"Saving dataset to {save_path}")
                       
                        df.to_csv(os.path.join(save_path, 'higgs.csv'), index=False)
           
                    
                    if debug:
                        print("="*100)
                        print("Loaded HIGGS dataset successfully. Returning data and target variables.")
                        print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/HIGGS")
                        print(f"Data: {data.shape}")
                        print(f"Target: {target.shape}")
                        print("="*100)
                    
                    return data, target
                
    else:
        ValueError(f"Failed to download dataset from {url}. Status code: {response.status_code}")
        return None
    
def load_covtype(debug=False, save_path=None, load_path=None):
    """
    Load the Covertype dataset from the UCI Machine Learning Repository.

    :param debug: If True, only load a subset of the dataset for faster testing
    :param save_path: If provided, save the dataset to this path
    :param load_path: If provided, load the dataset from this path

    :return: A tuple containing the data and target variables


    """

    if load_path and os.path.exists(load_path):
        print(f"Loading dataset from {load_path}")
        df = pd.read_csv(os.path.join(load_path, 'covtype.csv'))
 

        # Rename the first column to 'target' and separate it as a Series
        target = df.iloc[:, 0]
        target.name = 'target'

        # Get the remaining columns as a DataFrame
        data = df.iloc[:, 1:]

        if debug:

            print("Loaded Covertype dataset successfully. Returning data and target variables.")
            print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/Covertype")
            print(f"Data: {data.shape}")
            print(f"Target: {target.shape}")

        return data,target

    from ucimlrepo import fetch_ucirepo 
    
    # fetch dataset 
    covertype = fetch_ucirepo(id=31) 

    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    covertype.data.targets = le.fit_transform(covertype.data.targets.values.ravel())


 
    # data (as pandas dataframes) 
    X = covertype.data.features 
    y = pd.Series(covertype.data.targets, name='target')
    

    if save_path:
        # Ensure the save path exists
        os.makedirs(save_path, exist_ok=True)

        df = pd.concat([y, X], axis=1)

        if debug:
            print(f"Saving dataset to {save_path}")
    
        # Save the dataset to the save path
        df.to_csv(os.path.join(save_path, 'covtype.csv'), index=False)

    if debug:
        print("="*100)
        print("Loaded Covertype dataset successfully. Returning data and target variables.")
        print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/Covertype")
        print(f"Data: {X.shape}")
        print(f"Target: {y.shape}")
        print("="*100)
    


    return X,y

def load_adult(debug=False, save_path=None, load_path=None):
    """
    Load the Adult dataset from the UCI Machine Learning Repository.

    :param debug: If True, only load a subset of the dataset for faster testing
    :param save_path: If provided, save the dataset to this path
    :param load_path: If provided, load the dataset from this path

    :return: A tuple containing the data and target variables


    """

    if load_path and os.path.exists(load_path):
        print(f"Loading dataset from {load_path}")
        df = pd.read_csv(os.path.join(load_path, 'adult.csv'))


 

        # Rename the first column to 'target' and separate it as a Series
        target = df.iloc[:, 0]
        target.name = 'target'

        # Get the remaining columns as a DataFrame
        data = df.iloc[:, 1:]

        if debug:

            print("Loaded Adult dataset successfully. Returning data and target variables.")
            print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/Adult")
            print(f"Data: {data.shape}")
            print(f"Target: {target.shape}")

        return data,target

    from ucimlrepo import fetch_ucirepo 
    
    # fetch dataset 
    adult = fetch_ucirepo(id=2) 

    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    adult.data.targets = le.fit_transform(adult.data.targets.values.ravel())

        
    # data (as pandas dataframes) 
    X = adult.data.features 
    y = pd.Series(adult.data.targets, name='target')
    y.name = 'target'



    if save_path:
        # Ensure the save path exists
        os.makedirs(save_path, exist_ok=True)

        df = pd.concat([y, X], axis=1)

        if debug:
            print(f"Saving dataset to {save_path}")
    
        # Save the dataset to the save path
        df.to_csv(os.path.join(save_path, 'adult.csv'), index=False)

    if debug:
        print("="*100)
        print("Loaded Adult dataset successfully. Returning data and target variables.")
        print("Link to dataset: https://archive.ics.uci.edu/ml/datasets/Adult")
        print(f"Data: {X.shape}")
        print(f"Target: {y.shape}")
        print("="*100)
    


    return X,y