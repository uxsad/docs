PDFS = design.pdf

all: $(PDFS)

%.pdf: %.roff
	groff -Tpdf -mspdf -ept < $< > $@

clean:
	rm -f $(PDFS)

.PHONY: clean
