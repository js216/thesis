quick: thesis.tex
	pdflatex thesis

full: thesis.tex references.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
