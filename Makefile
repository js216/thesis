TeX = xelatex

quick: thesis.tex figs
	$(TeX) thesis

full: thesis.tex references.bib figs
	$(TeX) thesis
	bibtex thesis
	$(TeX) thesis
	$(TeX) thesis

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.pdf
	$(MAKE) clean -C figs

.PHONY: figs
figs:
	$(MAKE) -C figs
