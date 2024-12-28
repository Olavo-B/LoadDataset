import unittest
import context as LoadDataset

class TestLoadIris(unittest.TestCase):

    def test_load_iris(self):
                
                # Test saving the dataset to a provided path
                data, target = LoadDataset.load_iris(debug=True, save_path='./misc/data')
                self.assertIsNotNone(data)
                self.assertIsNotNone(target)
        
                # Test loading the dataset from a provided path
                data, target = LoadDataset.load_iris(load_path='./misc/data')
                self.assertIsNotNone(data)
                self.assertIsNotNone(target)


if __name__ == '__main__':
    unittest.main()