TeX = xelatex

CHAPTERS = apparatus.tex introduction.tex outlook.tex preliminary.tex simulations.tex systematics.tex

.PHONY: full clean figs

thesis.pdf: thesis.tex $(CHAPTERS) | figs
	$(TeX) thesis

full: thesis.tex references.bib $(CHAPTERS) | figs
	$(TeX) thesis
	bibtex thesis
	$(TeX) thesis
	$(TeX) thesis

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.pdf
	$(MAKE) clean -C figs

figs:
	$(MAKE) -C figs
