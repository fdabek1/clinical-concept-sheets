import pandas as pd
import pkgutil
import io
import os


class EHRCodeMappingNotFound(Exception):
    pass


class InvalidEHRCodeMappingVersion(Exception):
    pass


def load_mapping(name, version=None):
    all_mappings = pd.read_csv(io.BytesIO(pkgutil.get_data(__name__, os.path.join('data', 'mappings.csv'))))

    result = all_mappings[all_mappings['ID'] == name]
    if result.shape[0] == 0:
        raise EHRCodeMappingNotFound

    result = result.iloc[0]
    if version is None:
        version = result['CurrentVersion']
    else:
        if result['CurrentVersion'] > version:
            raise InvalidEHRCodeMappingVersion

    filename = result['ID'] + '.v' + str(version) + '.csv'

    return pd.read_csv(io.BytesIO(pkgutil.get_data(__name__, os.path.join('mappings', filename))))
