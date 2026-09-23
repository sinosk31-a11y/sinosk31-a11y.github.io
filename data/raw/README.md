# Project 02 — Raw Dataset

## Dataset

**UCI Online Retail II**

Source:

https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii

The dataset contains transaction-level information from a UK-based
online retail business covering transactions from December 2009 through
December 2011.

## Raw file

The original downloaded file is:

`online_retail_II.xlsx`

The workbook contains two sheets:

- `Year 2009-2010`
- `Year 2010-2011`

The combined dataset contains approximately 1.07 million transaction
records.

## Why the raw file is not stored in this repository

The original Excel workbook is approximately 43 MB.

To keep the Git repository lightweight and focused on reproducible
analysis, the original raw workbook is not committed to the repository.

Users can obtain the original dataset directly from the official UCI
Machine Learning Repository using the source above.

## Reproduction

After downloading the dataset, place the file locally at:

`data/raw/online_retail_II.xlsx`

The analytical scripts in this project use that path as their raw-data
input.

The raw dataset is preserved locally and is not modified during the
analysis.

## License

The dataset is provided by the UCI Machine Learning Repository under
the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

Dataset attribution:

Chen, D. (2019). Online Retail II. UCI Machine Learning Repository.
https://doi.org/10.24432/C5CG6D
