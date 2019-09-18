import os
import pandas as pd

import yaml

__all__ = [
    'load_activities', 'load_locations', 'load_modalities', 'load_datasets',
    'load_csv_data', 'load_features', 'load_transformations', 'load_chains', 'load_yaml',
    'dataset_importer', 'feature_importer', 'transformer_importer', 'load_metadata',
    'build_path'
]


def load_csv_data(fname, astype='list'):
    df = pd.read_csv(
        fname,
        delim_whitespace=True,
        header=None
    )
    
    if astype in {'dataframe', 'pandas', 'pd'}:
        return df
    if astype in {'values', 'np', 'numpy'}:
        return df.values
    if astype == 'list':
        return df.values.ravel().tolist()
    
    raise ValueError


def get_root():
    return os.environ['PROJECT_ROOT']


def build_path(*args):
    return os.path.join(
        get_root(),
        *args
    )


"""
YAML file loaders
"""


def load_yaml(fname):
    return yaml.load(open(build_path(fname)))


def load_metadata(fname):
    return load_yaml(os.path.join('metadata', fname))


"""
Dataset metadata
"""


def load_datasets():
    return load_metadata('datasets.yaml')


def load_activities():
    return load_metadata('activities.yaml')


def load_locations():
    return load_metadata('locations.yaml')


def load_modalities():
    return load_metadata('modalities.yaml')


"""
Coded metadata
"""


def load_features():
    return load_metadata('features.yaml')


def load_chains():
    return load_metadata('chains.yaml')


def load_transformations():
    return load_metadata('transformers.yaml')


def load_models():
    return load_metadata('models.yaml')


"""

"""


def module_importer(module_path, class_name, *args, **kwargs):
    m = __import__(module_path, fromlist=[class_name])
    c = getattr(m, class_name)
    return c(*args, **kwargs)


def dataset_importer(class_name, *args, **kwargs):
    return module_importer(
        module_path='src.datasets',
        class_name=class_name,
        *args, **kwargs
    )


def feature_importer(class_name, *args, **kwargs):
    return module_importer(
        module_path='src.features',
        class_name=class_name,
        *args, **kwargs
    )


def transformer_importer(class_name, *args, **kwargs):
    return module_importer(
        module_path='src.transformers',
        class_name=class_name,
        *args, **kwargs
    )
