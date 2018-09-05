"""
Loads classification data sets
"""
from pathlib import Path
import pkg_resources
import re, operator

class ClassificationLoader:

    def __init__(self, filters=[]):
        self.datasets_metadata = []
        self._load_keel()
        self.reset_filters(filters)


    def reset_filters(self, filters):
        self.conditions = filters

    def load_meta(self):
        filtered = self.filter(self.conditions)

        return filtered

    def _load_keel(self):
        for directory in pkg_resources.resource_listdir('datasets', 'classification/data/keel'):
            for dataset_directory in pkg_resources.resource_listdir('datasets', 'classification/data/keel'+'/'+directory):
                metadata_file = pkg_resources.resource_filename('datasets', 'classification/data/keel'+'/'+directory+'/'+dataset_directory+'/'+dataset_directory+'-names.txt')
                dataset_metadata = {'name':dataset_directory, 'directory': 'classification/data/keel'+'/'+directory+'/'+dataset_directory}
                file = open(metadata_file, 'r')
                text = file.read()
                matches = re.finditer(r"\d:\s([\w ]*)[.:\s]*([A-Za-z0-9.,]+(?:\s+[A-Za-z0-9.,]+)*\s*$)", text, re.MULTILINE)
                for match in matches:
                    dataset_metadata[match.group(1).strip()] = self._parse_float(match.group(2).strip().replace(',', '.'))
                    if "Description" in dataset_metadata:
                        dataset_metadata.pop('Description')
                    if "Header" in dataset_metadata:
                        dataset_metadata.pop('Header')
                dataset_metadata["dataset_provider"] =  'keel'
                self.datasets_metadata.append(dataset_metadata)

    def _parse_float(self, value):
        try:
            x = float(value)
            return x
        except:
            return value

    def filter_single(self, filter_this_dict, key, operation, value):
        ops = {'>': operator.gt,
               '<': operator.lt,
               '>=': operator.ge,
               '<=': operator.le,
               '=': operator.eq,
               'contains': operator.contains}
        return [x for x in filter_this_dict if ops[operation](x[key], value)]

    def filter(self, conditions = []):
        filtered = self.datasets_metadata

        if not conditions:
            return filtered

        for key, operation, value in conditions:
            filtered = self.filter_single(filtered, key, operation, value)

        return filtered



