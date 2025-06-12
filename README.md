# HDX-MS-datasets
Repository for HDX-MS datasets

NOTE: This is not the HDX dataset format proposed at the HDX-MS 2022 conference, which includes isotopic envelopes, but a .yaml based format containing metadata and peptide-average deuterium uptake. 

The aim of this repository is to collect curated bottom-up HDX-MS datasets for automated
processing, data mining and interactive visualization.

Datasets should consist of .csv D-uptake/exposure peptide tables. Each dataset is described by
a `metadata.yaml` file and a `hdx_spec.yaml` file. 

Repository for downloading and loading datasets in python: [hdxms-datasets](https://github.com/Jhsmit/hdxms-datasets)

metadata.yaml
-------------

- Contains a list of authors (and contact email, ORCID, affiliations, ...)
- List of associated publications with the datasets
- List of repositories where raw data or associated data can be found

hdx_spec.yaml
-------------

The hdx spec file describes protein states in  the HDX-MS dataset in detail. It contains the following sections:

### data_files

Dictionary of datafiles, with the following keys: `filename`, `format`, `type`.

### structures
Dictionary of structures. Typically, one datasets should contain only one protein structure, where different protein states can be mutants or liganded states of the same protein. However, it is possible to specify multiple structures, e.g. for different conformational states of the same protein. 
Possible keys are:
 - `data_file` (str): Link to a file in the `data_files` section, which contains the structure.
 - `chain` (list): Chain or chains (in case of homomultimeric proteins) of the structure that are relevant for the HDX-MS dataset.


### protein
Dictionary (keys are protein states) of protein information. Each element has the following keys:
 - `sequence` (str): FASTA sequence of the protein, including mutations
 - `n_term`: (int): Residue number of the N-terminal residue in the sequence. Typically 1, can be negative in case of affinity tags. 
 - `c_term`: (int): Residue number of the C-terminal residue in the sequence. 
 - `oligomeric_state` (int): Oligomeric state of the protein. 
 - `ligands` (list): Format TBD.
 - `mutations` (list): List of mutations that are present in the structure, e.g. `["A123T", "G456D"]`.
 - `concentration` (str): Concentration of the protein, with units. e.g. "10 µM".

The keys `sequence`, `n_term`, `c_term` are mandatory.

### peptides
Dictionary (keys are protein states) of peptides. Each element can have one of the following peptide types: `fully_deuterated`, `non_deuterated`, `partially_deuterated`. 

Each element has the following keys:
- `data_file` (str): Link to a file in the `data_files` section, which contains the peptide data.
- `filters` (dict): Dictionary of filters that are applied the peptide table to obtain the peptides only in this peptide set. 
- metadata (dict): Dictionary of metadata for the peptide set, with keys: 
    - `pH` (float): Uncorrected pH (pH read) of the exchange buffer. 
    - `temperature` (float): Temperature of the exchange buffer in Kelvin.
    - `d_percentage` (float): Percentage of deuterium in the exchange buffer.




