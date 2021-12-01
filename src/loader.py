import yaml
from pyhdx.fileIO import csv_to_dataframe, read_dynamx
from pyhdx.models import PeptideMasterTable
from pathlib import Path


def load_dataset(pth):
    state_dict = yaml.safe_load((pth / 'protein_states.yaml').read_text())

    data_files_dict = state_dict['data_files']
    data_files = {}
    for file_name, spec in data_files_dict.items():
        file_pth = pth / spec['filename']
        fmt = spec['format']
        if fmt.lower() == 'dynamx':
            df = read_dynamx(file_pth)  # lazy?
            data_files[file_name] = df
        elif fmt.lower == 'pdb':
            data_files[file_name] = file_pth.read_text()



# filters are applied on the state data DataFrame before creating the HDXMeasurement object
PREPROCESS_FILTERS = {
    'remove_zero_exchange': lambda data: data.query('exposure != 0.'),
    'postive_uptake': lambda data: data.query('uptake_corrected >= 0')
}
