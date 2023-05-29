TeX = pdflatex

CHAPTERS = absorbers.tex apparatus.tex bibliography.tex circuits.tex conclusion.tex francium.tex glossaries.tex hamiltonian.tex HVcontrol.tex introduction.tex laser_power.tex lens.tex magneticshield.tex PMT.tex simulations.tex systematics.tex target_making.tex test_interaction.tex thesis.tex titlepage.tex

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
