quick: thesis.tex figs
	pdflatex thesis

xelatex: thesis.tex figs
	xelatex thesis

full: thesis.tex references.bib figs
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.pdf
	$(MAKE) clean -C figs

.PHONY: figs
figs:
	$(MAKE) -C figs
