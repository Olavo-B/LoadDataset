import unittest
import context as LoadDataset

class TestLoadCovtype(unittest.TestCase):

    def test_load_covtype(self):
            
            # Test saving the dataset to a provided path
            data, target = LoadDataset.load_covtype(debug=True, save_path='./misc/data')
            self.assertIsNotNone(data)
            self.assertIsNotNone(target)
    
            # Test loading the dataset from a provided path
            data, target = LoadDataset.load_covtype(load_path='./misc/data')
            self.assertIsNotNone(data)
            self.assertIsNotNone(target)


if __name__ == '__main__':
    unittest.main()