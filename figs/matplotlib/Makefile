.PHONY: all clean

all: polarize.pdf

%.svg: %.py
	python3 $<

%.pdf: %.svg
	inkscape -D -z --file=$< --export-pdf=$@ --export-latex
	sed -i 's/$@/figs\/matplotlib\/$@/g' $@_tex

clean:
	rm -f *.pdf *.svg *.pdf_tex
