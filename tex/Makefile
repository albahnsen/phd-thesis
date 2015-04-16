thesis.pdf: bibliography.bib thesis.tex classicthesis-config.tex chapters/*.tex frontback/*.tex 
	pdflatex -shell-escape thesis
	bibtex thesis
	pdflatex -shell-escape thesis
	pdflatex -shell-escape thesis
	rm -f *.lot *.lof *.lol *.toc *.log *.out *.aux *.blg *.bbl thesis.brf chapters/*.aux frontback/*.aux chapters/*.backup frontback/*.backup *.pyg *.backup figures/src/*.aux figures/src/*.backup

partial:
	bibtex thesis
	pdflatex -shell-escape thesis

clean:
	rm -f *.lot *.lof *.lol *.toc *.log *.out *.aux *.blg *.bbl thesis.pdf thesis.brf chapters/*.aux frontback/*.aux chapters/*.backup frontback/*.backup *.pyg *.backup figures/src/*.aux figures/src/*.backup

rebuild: clean thesis.pdf
