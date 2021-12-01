# HDX-MS-datasets
Repository for HDX-MS datasets

The repository is a work-in-progress.

The aim of this repository is to collect curated bottom-up HDX-MS datasets for automated
processing, data mining and interactive visualization. 

Datasets should consist of .csv D-uptake/exposure peptide tables. Each dataset is described by
a `metadata.yaml` file and a `protein_states.yaml` file. Calculation of ΔG values and protection
factors are scheduled automatically from a `pyhdx_jobs.yaml` file. 

metadata.yaml
-------------

- Describes which protein was used in the HDX-MS experiment with identifiers (PDB id, etc). 
- Contains a list of authors (and contact email, ORCID, affiliations, ...)
- List of associated publications with the datasets
- List of repositories where raw data or associated data can be found

protein_states.yaml
--------------------

- Experimental conditions relevant for calculating ΔG values (pH, temperature, D percentage)
- labels of each state in the .csv uptake files and which files are used
- Information on the protein state (mutations, ligands, oligomeric state, buffer conditions)
                   
pyhdx_jobs.yaml
---------------
- Version of PyHDX to use
- Pipeline specification of fitting procedures to run
- ΔG fit settings hyperparameters (optimizer, stop_loss, patience)

Ultimately, users should be able to query the database through and API and obtain ΔGs for specified
proteins / protein states. 

