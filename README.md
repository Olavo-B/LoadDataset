# LoadDataset

Biblioteca para importar datasets convencionais automaticamente

Datasets presentes:

- SUSY
- HIGGS
- Covertype
- Adult

## Installation

```python
!pip install git+https://github.com/Olavo-B/LoadDataset
```


## Usage

```python

from LoadDataset.LoadDataset import load_susy

data,target = load_susy(debug=True, save_path='data/susy.csv', load_path='data/susy.csv')

```

## Requirements

 - pandas==2.2.2
 - requests==2.25.1
 - tqdm==4.65.0
 - pytest==6.2.4
