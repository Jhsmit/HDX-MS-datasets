# HDX-MS-datasets
Repository for HDX-MS datasets

NOTE: This is not the HDX XML dataset format proposed at the HDX-MS 2022 conference, but a .yaml based format currently used in PyHDX. 
The aim is for thseet formats to converge.

The aim of this repository is to collect curated bottom-up HDX-MS datasets for automated
processing, data mining and interactive visualization.
The repository is a work-in-progress.

One dataset / jobfile is added for testing purposes. This currently uses the PyHDX 0.4.0b9
state data yaml spec and jobfile API. Jobfiles might be better suited to placed in seperate 
repositories at a later data such that this database can be downstream-software agnostic
and only features as a curated and annotated database.

Datasets should consist of .csv D-uptake/exposure peptide tables. Each dataset is described by
a `metadata.yaml` file and a `protein_states.yaml` file. 

Ideally, datasets should include more information, such as peptide envelopes or raw MS spectra. 

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
                   
jobfile.yaml
------------

An alpha implementation of this file was added in PyHDX 0.4.0b9

- Version of PyHDX to use
- Pipeline specification of fitting procedures to run
- ΔG fit settings hyperparameters (optimizer, stop_loss, patience)

Ultimately, users should be able to query the database through and API and obtain ΔGs for specified
proteins / protein states. 

