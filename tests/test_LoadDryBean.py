import unittest
import context as LoadDataset

class TestLoadDryBean(unittest.TestCase):
    def test_load_dry_bean(self):
        # Test saving the dataset to a provided path
        data, target = LoadDataset.load_drybean(debug=True, save_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)

        # Test loading the dataset from a provided path
        data, target = LoadDataset.load_drybean(load_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)
if __name__ == '__main__':
    unittest.main()