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



if __name__ == '__main__':
    unittest.main()