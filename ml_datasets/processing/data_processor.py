from scipy.io import arff
from scipy.io.arff.arffread import ParseArffError
from pandas import DataFrame
import numpy as np
import pkg_resources, fileinput
"""
A class to process a given dataset
"""


class DataProcessor:

    def __init__(self):
        self.arff_reader = ARFFReader()





    def __call__(self, dataset_metadata, return_folds=True):
        """
        Takes in a given meta-data dict that contains the relative path to the dataset
        :return:
        """
        arff = self.arff_reader
        if 'directory' not in dataset_metadata:
            raise KeyError("'directory' key not in dataset metadata dictionary: "+dataset_metadata)

        resource_path = dataset_metadata['directory']

        if return_folds:
            for i in range(1,5):
                train_file = dataset_metadata['name']+"-5-%itra.dat" %i
                test_file = dataset_metadata['name'] + "-5-%itst.dat" %i

                yield (arff.read(resource_path+"/"+train_file), arff.read(resource_path+"/"+test_file))
        else:
            yield arff.read(resource_path+"/"+dataset_metadata['name']+".dat")



class ARFFReader():

    def __init__(self, pre_process = True):
        self.pre_process = pre_process

    def _removeUnneccessaryTags(self,filename):
        """
        Removes extra content from files to insure that it follows arff format.
        :param filename:
        :return:
        """
        for line in fileinput.FileInput(filename, inplace=1):
            if '@inputs' in line or '@input' in line or '@outputs' in line or '@output' in line or line == "":
                print("".rstrip())
            else:
                print(line.rstrip())

    def load_ARFF(self, filename):
        try:
            data, meta = arff.loadarff(filename)
        except ParseArffError:
            self._removeUnneccessaryTags(filename)
            data, meta = arff.loadarff(filename)

        df = DataFrame(data=data, columns=meta.names())

        if self.pre_process:
            self._pre_process(df, meta)

        print(df.columns)
        y = df[meta.names()[-1]]
        X = df.drop([meta.names()[-1]], axis=1)
        return (X.values, y.values)


    def _pre_process(self, df, meta):
        """
        Converts discrete feature into psuedo-continous versios.
        One hot encodes features that take on multiple discrete values.
        :param df:
        :param meta:
        :return:
        """
        for name, type in zip(meta.names(), meta.types()):
            if type == 'nominal':
                _, values = meta[name]

                if len(values) == 2:
                    uniq = np.unique(values)
                    df[name] = df[name].map({uniq[0].encode(): 0, uniq[1].encode(): 1})
                else:
                    # one-hot-encodes discrete feature values into multiple features
                    for value in values:
                        df[name+"_"+value] = [1 if x == value.encode() else 0 for x in df[name]]
                    df.drop(name, axis=1, inplace=True)




    def read(self, resource_path):
        file = pkg_resources.resource_filename('datasets', resource_path)
        return self.load_ARFF(file)



