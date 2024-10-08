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
    
    def test_load_iris(self):
                
                # Test saving the dataset to a provided path
                data, target = LoadDataset.load_iris(debug=True, save_path='./misc/data')
                self.assertIsNotNone(data)
                self.assertIsNotNone(target)
        
                # Test loading the dataset from a provided path
                data, target = LoadDataset.load_iris(load_path='./misc/data')
                self.assertIsNotNone(data)
                self.assertIsNotNone(target)

            
    def test_load_kdd99(self):
                    
                    # Test saving the dataset to a provided path
                    data, target = LoadDataset.load_kdd99(debug=True, save_path='./misc/data')
                    self.assertIsNotNone(data)
                    self.assertIsNotNone(target)
            
                    # Test loading the dataset from a provided path
                    data, target = LoadDataset.load_kdd99(load_path='./misc/data')
                    self.assertIsNotNone(data)
                    self.assertIsNotNone(target)

    def test_load_spambase(self):

        # Test saving the dataset to a provided path
        data, target = LoadDataset.load_spambase(debug=True, save_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)

        # Test loading the dataset from a provided path
        data, target = LoadDataset.load_spambase(load_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)


if __name__ == '__main__':
    unittest.main()