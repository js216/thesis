.PHONY: all clean

all: polarize.pdf polarizeTlF.pdf SOF.pdf SOF2.pdf slope.pdf Ptrans1.pdf Ptrans2.pdf dressed.pdf

# additional dependencies

polarizeTlF.pdf: P_arr.csv Ez_arr.csv

SOF.pdf: SOF.csv

SOF2.pdf: SOF2.csv

slope.pdf: slope.csv all_B_slopes.csv

Ptrans1.pdf: Ptrans1.csv

Ptrans2.pdf: Ptrans2.csv

# generic rules

%.svg: %.py
	python $<

%.pdf: %.svg
	inkscape -D --export-filename=$@ --export-latex $<
	sed -i 's/$@/figs\/matplotlib\/$@/g' $@_tex

clean:
	rm -f *.pdf *.svg *.pdf_tex
