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
--------------------

- Describes the protein of interest 
- Information on the protein state (mutations, ligands, oligomeric state, buffer conditions)
- HDX specific experimental conditions (deuteration percentage, pH, temperature)
- Specification of .csv file format
- Definition of peptide sets per protein state (FD control / ND control / experiment)


