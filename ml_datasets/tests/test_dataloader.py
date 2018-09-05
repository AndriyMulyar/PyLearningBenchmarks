from unittest import TestCase
from ml_datasets import DataLoader

class TestDataLoader(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = DataLoader()

    @classmethod
    def tearDownClass(cls):
        cls.data.__exit__(None, None, None)

    def test_init(self):
        data = self.data
        self.assertIsInstance(data, DataLoader)

    def test_keel(self):
        data = self.data
        query = data(filters=[('dataset_provider', '=', 'keel')])
        self.assertEquals(sum(1 for _ in query), 100,
                          msg="Currently 100 datasets from KEEL, update test if this has changed")

    def test_dataset_retrieval(self):
        data = self.data
        query = data(filters=[('dataset_provider', '=', 'keel')])



        for metadata, folds in query:
            for train, test in folds:
                X_train, y_train = train
                X_test, y_test = test

        pass





