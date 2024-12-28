import unittest
import context as LoadDataset

class TestLoadHiggs(unittest.TestCase):

    def test_load_higgs(self):

        # Test saving the dataset to a provided path
        data, target = LoadDataset.load_higgs(debug=True, save_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)

        # Test loading the dataset from a provided path
        data, target = LoadDataset.load_higgs(load_path='./misc/data')
        self.assertIsNotNone(data)
        self.assertIsNotNone(target)

if __name__ == '__main__':
    unittest.main()