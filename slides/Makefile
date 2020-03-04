slides.pdf: frames.tex preface.tex
	cd latex && latexmk -quiet slides.tex

clean:
	cd latex && latexmk -c && rm *~

veryclean:
	cd latex && latexmk -C && rm ../*~
