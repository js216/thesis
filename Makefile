TeX = pdflatex

CHAPTERS = apparatus.tex HVcontrol.tex PMT.tex systematics.tex titlepage.tex bibliography.tex introduction.tex serrodyne.tex test_interaction.tex glossaries.tex magneticshield.tex simulations.tex thesis.tex

.PHONY: full figs

thesis.pdf: thesis.tex $(CHAPTERS) figs
	$(TeX) thesis

full: thesis.tex references.bib $(CHAPTERS) figs
	$(TeX) thesis
	bibtex thesis
	makeglossaries thesis
	$(TeX) thesis
	$(TeX) thesis

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.pdf
	$(MAKE) clean -C figs

figs:
	$(MAKE) -C figs
