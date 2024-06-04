import unittest
import context as LoadDataset

class TestLoadSusy(unittest.TestCase):
    def test_load_susy(self):


        # Test saving the dataset to a provided path
        data, target = LoadDataset.load_susy(debug=True, save_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)

        # Test loading the dataset from a provided path
        data, target = LoadDataset.load_susy(load_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)
    
    def test_load_higgs(self):

        # Test saving the dataset to a provided path
        data, target = LoadDataset.load_higgs(debug=True, save_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)

        # Test loading the dataset from a provided path
        data, target = LoadDataset.load_higgs(load_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)
    
    def test_load_covtype(self):
            
            # Test saving the dataset to a provided path
            data, target = LoadDataset.load_covtype(debug=True, save_path='./misc/data')
            self.assertIsNotNone(data)
            self.assertIsNotNone(target)
    
            # Test loading the dataset from a provided path
            data, target = LoadDataset.load_covtype(load_path='./misc/data')
            self.assertIsNotNone(data)
            self.assertIsNotNone(target)
    
    def test_load_adult(self):
            
            # Test saving the dataset to a provided path
            data, target = LoadDataset.load_adult(debug=True, save_path='./misc/data')
            self.assertIsNotNone(data)
            self.assertIsNotNone(target)
    
            # Test loading the dataset from a provided path
            data, target = LoadDataset.load_adult(load_path='./misc/data')
            self.assertIsNotNone(data)
            self.assertIsNotNone(target)



if __name__ == '__main__':
    unittest.main()