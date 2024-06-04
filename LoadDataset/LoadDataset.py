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

                        df.to_csv(os.path.join(save_path, 'susy.csv'), index=False)

                    return data, target

    else:
        ValueError(f"Failed to download dataset from {url}. Status code: {response.status_code}")
        return None