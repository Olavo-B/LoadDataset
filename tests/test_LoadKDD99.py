import unittest
import context as LoadDataset

class TestLoadKDD99(unittest.TestCase):

            
    def test_load_kdd99(self):
                    
                    # Test saving the dataset to a provided path
                    data, target = LoadDataset.load_kdd99(debug=True, save_path='./misc/data')
                    self.assertIsNotNone(data)
                    self.assertIsNotNone(target)
            
                    # Test loading the dataset from a provided path
                    data, target = LoadDataset.load_kdd99(load_path='./misc/data')
                    self.assertIsNotNone(data)
                    self.assertIsNotNone(target)



if __name__ == '__main__':
    unittest.main()