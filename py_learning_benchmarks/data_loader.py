"""
Loads datasets one at a time for experimentation purposes
"""
from datasets import ClassificationLoader
from .processing.data_processor import DataProcessor
from pprint import pprint
class DataLoader:

    def __init__(self, return_folds=True, filters=[], pre_process=True):
        self.classification = ClassificationLoader(filters=filters)
        self.process = DataProcessor(pre_process)
        self.return_folds = return_folds


    def reset_filters(self, filters=[]):
        self.classification.reset_filters(filters)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, filters=None, sort_by="IR"):
        """
        Returns a generator of the specified collection of data-sets to load with metadata.
        Each dataset is a tuple containing a meta-data dict and a generator of each fold
        :return:
        """

        #yields a generator on call containing either the whole dataset or each fold.
        process = self.process


        if filters is not None:
            self.reset_filters(filters=filters)

        dataset_metadata = self.classification.load_meta()

        dataset_metadata = sorted(dataset_metadata, key=lambda k: k[sort_by])
        for metadata in dataset_metadata:
            yield (metadata, process(metadata, return_folds=self.return_folds))









