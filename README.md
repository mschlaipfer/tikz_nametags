# tikz_nametags
Python script to generate name tags with logos via TikZ for HERMA 4420

## Run:
Adjust the parameters in the preamble of mk_nametags.py. If necessary, create
subdirectories.

`python mk_nametags.py`

You can then create the PDFs using `latexmk -pdf` and create a single PDF using
`pdfunite`.


## Notes:
Measurements work with Evince, but seem to be off with Okular.
