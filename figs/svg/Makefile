.PHONY: all clean

%.pdf: %.svg
	inkscape -D --export-filename=$@ --export-latex $<
	sed -i 's/$@/figs\/svg\/$@/g' $@_tex

all: lasers1.pdf lasers2.pdf

clean:
	rm -f *.pdf *.pdf_tex
