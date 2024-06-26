# ATAT

Antibody daTa Analysis Tool

A truly terrible acronym but no worse than those listed in [DOOFAAS](https://lweb.cfa.harvard.edu/~gpetitpas/Links/Astroacro.html).

## Description

CLI tool for plotting and returning statistics from antibody data.

#### This tool accepts:

* Input is in the form of a comma-separated file (CSV) in which rows are
  separated by newline characters and the value of each column within a row
  is separated by a comma.

#### This tool will create:

* A histogram of optical densities with clear annotations as a PNG file.
* a csv with the following statistics: min, max and mean optical density for amino acid groups to an accuracy of 1 decimal place.

### How To:

This would be distributed via PyPI and/or conda-forge and would be installable that way.

Once installed, the tool can be accessed via, the command line using the following arguments:

`atat -i INPUT_FILE [-o OUTPUT_DIRECTORY] [-n OUTPUT_NAME] [-dp DECIMAL_PLACES] [-im {PNG,JPEG,TIFF}]`

Arguments in square brackets are optional.
