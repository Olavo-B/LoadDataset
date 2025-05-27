# LoadDataset

A Python library for automatically importing conventional machine learning datasets with built-in download, caching, and preprocessing capabilities.

## 📊 Available Datasets

The library currently supports the following popular machine learning datasets:

- **SUSY** - Supersymmetric particle classification dataset
- **HIGGS** - Higgs boson detection dataset  
- **Covertype** - Forest cover type prediction dataset
- **Adult** - Census income prediction dataset

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
from LoadDataset.LoadDataset import load_higgs, load_covertype, load_adult

# Load HIGGS dataset
higgs_data, higgs_target = load_higgs(debug=True)

# Load Covertype dataset
cover_data, cover_target = load_covertype(save_path='datasets/covertype.csv')

# Load Adult dataset
adult_data, adult_target = load_adult(load_path='datasets/adult.csv')
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
```

> [!IMPORTANT]
> Python 3.7+ is required. The library has been tested with Python 3.7, 3.8, 3.9, 3.10, and 3.11.

## 🐛 Troubleshooting

### Common Issues

**Dataset won't download:**
- Check your internet connection
- Verify you have write permissions to the save directory
- Some datasets may be temporarily unavailable from their original sources

**Out of memory errors:**
- Large datasets like HIGGS may require significant RAM
- Consider using a machine with at least 8GB RAM for larger datasets

**File permission errors:**
- Ensure the script has write permissions to the specified directories
- On Unix systems, you may need to use `chmod` to set proper permissions

> [!TIP]
> Use the `debug=True` parameter to get detailed information about what the library is doing during the loading process.

## 📈 Dataset Information

| Dataset | Size | Features | Samples | Task Type |
|---------|------|----------|---------|-----------|
| SUSY | ~2.6GB | 18 | 5M | Binary Classification |
| HIGGS | ~7.4GB | 28 | 11M | Binary Classification |
| Covertype | ~73MB | 54 | 581K | Multi-class Classification |
| Adult | ~5MB | 14 | 48K | Binary Classification |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Adding new datasets
- Improving existing functionality
- Bug fixes
- Documentation improvements

## 📄 License

This project is open source. Please check the repository for license details.
