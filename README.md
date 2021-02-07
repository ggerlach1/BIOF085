

# Introduction to Data Science using Python

This repository contains teaching materials for a 3-day workshop on using 
Python for data science. 

## Computational environment

This workshop is run using the [Anaconda Python distribution](https;//www.anaconda.com). A `conda` environment to run all the materials can be created using 

```python
conda create -n ds_python python=3.7 anaconda
```
The necessary packages: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `sklearn`, `biopython`, `statsmodels`
The packages `plotly` and `altair` are needed for one document, but are otherwise not covered in the materials. 

## Teaching materials and documents

All the data files used in the workshop are contained in `data`.  The homework
assignments and solutions are contained in `homeworks`.  The introduction
document, all sides, and a schedule for the three days are in
`workshop_documents`. Administrative materials for running the workshop are in
the `workshop_documents` folder. The `docs` folder contains `.pdf` and `.html`
book like versions of the material covered in the workshop. 

The material covered during the workshop is in `jupyter notebooks` as they allow the use of Markdown and embedding for figures. During the workshop most material is covered via live-coding using either `Spyder`, `jupyter`, or `google-colab`. The other component of the class is work from screen cast videos allowing independent work. 

The data and notebooks are also contained in a google drive [folder](https://drive.google.com/drive/folders/1b34gkpGXjP8LDLq5rMJ7mUoCJX8pMt4d?usp=sharing) which provides easy access to the notebooks and data for students unfamiliar with coding in general. We found fewer issues with this than other methods of providing the data and live notebooks.

## TODO:

1. Clean up the data folder and make sure it only has the material we actually use, the folder `new_march` has the data we will provide for the March Workshop I believe it has all of it.
2. Better file system/work setup explanation at the beginning - see day 0 slides
4. Adjust Genomics project work


## Licenses

All software code in this repository is licensed under the MIT License (see LICENSE)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />All textual and written material in this repository is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
