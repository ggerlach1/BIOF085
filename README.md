[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/araastat/BIOF085/master?filepath=index.md)


# Introduction to Data Science using Python

This repository contains teaching materials for a 3-day workshop on using 
Python for data science. 

## Computational environment

This workshop is run using the [Anaconda Python distribution](https;//www.anaconda.com). A `conda` environment to run all the materials can be created using 

```python
conda create -n ds_python python=3.7 anaconda
```

The packages `plotly` and `altair` are needed for one document, but are otherwise not covered in the materials. 

## Teaching materials and documents

Long-form manuals for the material covered in this workshop are available in the top folder, and administrative materials for running the workshop are in the `workshop_documents` folder. The workshop is conducted by live-coding, choosing select materials in sequence form the long-form manuals. This can be adapted depending on the audience and the available time. 

The teaching materials are stored primarily as synchronized Python
and RMarkdown files. These seem an interesting choice for a Python workshop, 
but it enabled me to use RStudio, `bookdown` and some of it's editing tools as my IDE when needed. These materials can also be synced to Jupyter notebooks using the `jupytext` package (see below). I wrote the materials with a combination of RMarkdown and Jupyter notebook, synced using `jupytext`, which was a nice workflow for me. 

These materials can also be consumed as live notebooks using the Binder link above. This connects this repository to [Binder](https://mybinder.org), where the RMarkdown files are converted to Jupyter notebooks on-the-fly and deployed as live notebooks on the web. 

## Converting materials to Jupyter notebooks for local consumption

All the RMarkdown files can be converted to Jupyter notebooks using the 
`jupytext` Python package. To do this, first install the `jupytext` package.

```
conda install -c conda-forge jupytext
```

Then, from the terminal, go to the `docs` folder and type

```
jupytext --sync *.Rmd
```

This will generate all the corresponding Jupyter notebook files. Now you can edit either
the notebooks or the Rmd files, and it will be reflected in the other. See the [jupytext documentation](https://jupytext.readthedocs.io/en/latest/introduction.html) for more details. 

