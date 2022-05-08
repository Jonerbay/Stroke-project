# Stroke-project
Completed project on detecting stroke using real data from hospital. You get acquainted with all done work via `report.pdf`.

## Data

Original dataset located in Excel file. Data is divided into several sheets. Then, cleaned and filtered data was written to dataset.csv.
Comments.txt contains infromation about data labels for some columns that has multi class values. Most of the data are binary. Y labels are in "Death" column.

## Code implentation

All code implentation was done on Jupyter Notebook - `stroke.ipynb`

## AutoML

AutoGluon was used as alternative approach. Code and requirments are presented in files. Link to tool - `https://auto.gluon.ai/stable/index.html`

## Correct labels in dataset
Stroke diagnosis{ hemorraghic - 0, Ishemic - 1, Mixed - 2 }

Date of Dysrhythmia{ no - 0, yes/single - 1, constant - 2 }

Dysrhythmia{no - 0, yes - 1, Afib - 2, ventricular extrasystoles - 3}

Heart Failure{no - 0, yes Acute - 1, chronic continous I - 2, chronic continous II - 3, chronic continous III - 4}

For other values { happened/has/taken - 1, otherwise - 0}
