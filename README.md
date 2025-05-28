# LoadDataset

A Python library for automatically importing conventional machine learning datasets with built-in download, caching, and preprocessing capabilities.

## 📊 Available Datasets

The library currently supports the following popular machine learning datasets:

- **SUSY** - Supersymmetric particle classification dataset
- **HIGGS** - Higgs boson detection dataset  
- **Covertype** - Forest cover type prediction dataset
- **Adult** - Census income prediction dataset
- **Iris** - Classic flower species classification dataset
- **KDD99** - Network intrusion detection dataset
- **Spambase** - Email spam detection dataset
- **DryBean** - Dry bean classification dataset

> [!TIP]
> All datasets are automatically downloaded on first use and cached locally for faster subsequent access.

## 🚀 Installation

Install directly from GitHub using pip:

```bash
pip install git+https://github.com/Olavo-B/LoadDataset
```

> [!WARNING]
> Make sure you have a stable internet connection for the initial dataset downloads, as some files can be quite large (HIGGS dataset is ~7GB).

## 💻 Usage

### Basic Usage

```python
from LoadDataset.LoadDataset import load_susy

# Load SUSY dataset with default settings
data, target = load_susy()
```

### Advanced Usage with Parameters

```python
from LoadDataset.LoadDataset import load_susy

# Load with custom settings
data, target = load_susy(
    debug=True,                    # Enable debug output
    save_path='data/susy.csv',     # Custom save location
    load_path='data/susy.csv'      # Custom load location
)
```

### Loading Other Datasets

```python
from LoadDataset.LoadDataset import (
    load_higgs, load_covtype, load_adult, 
    load_iris, load_kdd99, load_spambase
)

# Load HIGGS dataset
higgs_data, higgs_target = load_higgs(debug=True)

# Load Covertype dataset (note: function name is load_covtype, not load_covertype)
cover_data, cover_target = load_covtype(save_path='datasets/covertype.csv')

# Load Adult dataset
adult_data, adult_target = load_adult(load_path='datasets/adult.csv')

# Load Iris dataset
iris_data, iris_target = load_iris(debug=True)

# Load KDD99 dataset
kdd_data, kdd_target = load_kdd99(save_path='datasets/kdd99.csv')

# Load Spambase dataset
spam_data, spam_target = load_spambase(debug=True)
```

## ⚙️ How It Works

The library follows a simple workflow:

1. **Check Local Cache**: First checks if the dataset already exists at the specified `load_path`
2. **Download**: If not found locally, downloads the dataset from the original source
3. **Process**: Automatically handles decompression and data formatting
4. **Cache**: Saves the processed dataset to the specified `save_path` for future use
5. **Return**: Returns the data as pandas DataFrames split into features and target variables

> [!NOTE]
> The library automatically handles different file formats (CSV, compressed files, etc.) and preprocessing steps specific to each dataset.

## 📋 Function Parameters

All dataset loading functions support the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `debug` | bool | `False` | Enable verbose output during loading |
| `save_path` | str | `None` | Path where to save the downloaded dataset |
| `load_path` | str | `None` | Path where to look for existing dataset |

> [!CAUTION]
> If `save_path` and `load_path` are different, the library will save to `save_path` but load from `load_path` on subsequent runs. Make sure these paths are consistent to avoid re-downloading.

## 🔧 Requirements

```
pandas==2.2.2
requests==2.25.1
tqdm==4.65.0
pytest==6.2.4
ucimlrepo>=0.0.3
scikit-learn>=1.0.0
```

> [!IMPORTANT]
> Python 3.7+ is required. The library has been tested with Python 3.7, 3.8, 3.9, 3.10, and 3.11.

## 🐛 Troubleshooting

### Common Issues

> [!CAUTION]
> There's currently a bug in the `load_spambase` function where it incorrectly references 'iris.csv' in the load_path section. This will be fixed in a future update.

**Dataset won't download:**
- Check your internet connection
- Verify you have write permissions to the save directory
- Some datasets may be temporarily unavailable from their original sources
- For UCI ML Repo datasets (Adult, Iris, Covertype, KDD99, Spambase), ensure `ucimlrepo` is installed

**Out of memory errors:**
- Large datasets like HIGGS and KDD99 may require significant RAM
- Consider using a machine with at least 8GB RAM for larger datasets

**Import errors:**
- Make sure all required dependencies are installed: `ucimlrepo`, `scikit-learn`
- Some datasets require additional preprocessing libraries

**File permission errors:**
- Ensure the script has write permissions to the specified directories
- On Unix systems, you may need to use `chmod` to set proper permissions

> [!TIP]
> Use the `debug=True` parameter to get detailed information about what the library is doing during the loading process.

## 📈 Dataset Information

| Dataset | Size | Features | Samples | Task Type | Source Method |
|---------|------|----------|---------|-----------|---------------|
| SUSY | ~2.6GB | 18 | 5M | Binary Classification | Direct Download |
| HIGGS | ~7.4GB | 28 | 11M | Binary Classification | Direct Download |
| Covertype | ~73MB | 54 | 581K | Multi-class Classification | UCI ML Repo API |
| Adult | ~5MB | 14 | 48K | Binary Classification | UCI ML Repo API |
| Iris | ~5KB | 4 | 150 | Multi-class Classification | UCI ML Repo API |
| KDD99 | ~75MB | 41 | 4.9M | Multi-class Classification | Direct Download |
| Spambase | ~350KB | 57 | 4.6K | Binary Classification | UCI ML Repo API |
| DryBean | ~2.4MB | 16 | 13K | Multi-class Classification | UCI ML Repo API |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Adding new datasets
- Improving existing functionality
- Bug fixes
- Documentation improvements

## 📄 License

This project is open source. Please check the repository for license details.
