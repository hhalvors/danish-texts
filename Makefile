# ============================================================
#  Makefile — danish-texts
#
#  Builds PDFs from all .tex source files in texts/.
#  After building, run sync-pdfs.sh to push PDFs to phi423.
#
#  Usage:
#    make              rebuild all out-of-date PDFs
#    make all          same as above
#    make clean        remove LaTeX auxiliary files (keep PDFs)
#    make cleanall     remove auxiliary files and compiled PDFs
#    make list         list all .tex sources and their PDF status
#    make help         show this message
#    make -j4          parallel build with 4 jobs
# ============================================================

# Discover all .tex sources and derive PDF targets.
# Excludes .parts/ — transcription batches that are still fragments are staged there
# before being spliced into the main document. A fragment has no preamble and no
# \begin{document}, so trying to build it standalone fails with "Missing \begin{document}".
# Fragments also carry a .texfrag extension for the same reason; this is belt and braces.
TEXFILES := $(shell find texts -name '*.tex' -not -path '*/.parts/*' | sort)
PDFFILES  := $(TEXFILES:.tex=.pdf)

# latexmk flags: pdf mode, non-interactive, stop on first error
LATEXMK   := latexmk -pdf -interaction=nonstopmode -halt-on-error
LATEXMKLUA := latexmk -lualatex -interaction=nonstopmode -halt-on-error

.PHONY: all clean cleanall list help

all: $(PDFFILES)

# LuaLaTeX overrides for files using fontspec/unicode-math
# (must come before the general pattern rule)
texts/hoeffding/relation-som-kategori/transcription.pdf: \
  texts/hoeffding/relation-som-kategori/transcription.tex
	cd $(dir $<) && $(LATEXMKLUA) $(notdir $<)

texts/hoeffding/relation-som-kategori/translation.pdf: \
  texts/hoeffding/relation-som-kategori/translation.tex
	cd $(dir $<) && $(LATEXMKLUA) $(notdir $<)

texts/hoeffding/personlighedsprincippet/translation.pdf: \
  texts/hoeffding/personlighedsprincippet/translation.tex
	cd $(dir $<) && $(LATEXMKLUA) $(notdir $<)

# Brøchner, Bidrag til Opfattelsen af Philosophiens historiske Udvikling (1869).
# LuaLaTeX, not pdfLaTeX, and deliberately: the book carries 400--600 words of
# polytonic Greek. Under pdfLaTeX the Greek goes through LGR, for which
# Libertinus has no Type1 face, so it falls back to CB Greek -- a Computer
# Modern Greek that clashes with the Libertinus text and sets upright, where
# the book's Greek fount is a cursive. Under LuaLaTeX the Greek comes from
# Libertinus Serif itself, with the iota subscript the book needs (ἐνεργείᾳ,
# p. 99 and the errata leaf). Reasoning is repeated in the file's own header §6.
texts/brochner/philosophiens-udvikling/transcription.pdf: \
  texts/brochner/philosophiens-udvikling/transcription.tex
	cd $(dir $<) && $(LATEXMKLUA) $(notdir $<)

# Brøchner, Philosophiens Historie i Grundrids, 1. and 2. Deel (1873--74).
# LuaLaTeX for the same reason as the 1869 Bidrag above, and more so: 1. Deel
# alone carries 8194 Greek characters on 163 of its 274 pages, including the
# variant sorts and the iota subscript. Both parts load fontspec, so the
# generic pdfLaTeX rule below cannot build them at all -- it dies at
# fontspec's "cannot-use-pdftex".
texts/brochner/philosophiens-historie-1/transcription.pdf: \
  texts/brochner/philosophiens-historie-1/transcription.tex
	cd $(dir $<) && $(LATEXMKLUA) $(notdir $<)

texts/brochner/philosophiens-historie-2/transcription.pdf: \
  texts/brochner/philosophiens-historie-2/transcription.tex
	cd $(dir $<) && $(LATEXMKLUA) $(notdir $<)

# Compile each .tex to PDF.
# cd into the source directory first so relative paths resolve correctly.
# latexmk detects how many pdflatex passes are needed (typically 2 for
# files with a table of contents or cross-references).
%.pdf: %.tex
	cd $(dir $<) && $(LATEXMK) $(notdir $<)

# Remove LaTeX auxiliary files, leaving PDFs intact.
clean:
	@find texts \( \
	  -name '*.aux'            \
	  -o -name '*.fdb_latexmk' \
	  -o -name '*.fls'         \
	  -o -name '*.log'         \
	  -o -name '*.out'         \
	  -o -name '*.synctex.gz'  \
	  -o -name '*.toc'         \
	  -o -name '*.xdv'         \
	\) -delete
	@echo "Auxiliary files removed."

# Remove auxiliary files and all locally-compiled PDFs.
# Does not touch PDFs that have no .tex source (sync-pdfs.sh handles those).
cleanall: clean
	@rm -f $(PDFFILES)
	@echo "Auxiliary files and compiled PDFs removed."

# Show each .tex source and whether its PDF is up to date.
list:
	@echo ""
	@echo "Source files and PDF status:"
	@echo "-----------------------------"
	@for tex in $(TEXFILES); do \
	  pdf=$${tex%.tex}.pdf; \
	  if [ ! -f "$$pdf" ]; then \
	    echo "  MISSING  $$tex"; \
	  elif [ "$$tex" -nt "$$pdf" ]; then \
	    echo "  STALE    $$tex"; \
	  else \
	    echo "  ok       $$tex"; \
	  fi; \
	done
	@echo ""

help:
	@echo ""
	@echo "  make           rebuild all out-of-date PDFs"
	@echo "  make clean     remove LaTeX auxiliary files"
	@echo "  make cleanall  remove auxiliary files and compiled PDFs"
	@echo "  make list      show PDF status for each source file"
	@echo "  make -j4       parallel build with 4 jobs"
	@echo ""
	@echo "  After building, run 'bash sync-pdfs.sh' to push PDFs to phi423."
	@echo ""
