slides.pdf: frames.tex preface.tex
	cd latex && latexmk  slides.tex  && mv slides.pdf ..

clean:
	cd latex && latexmk -c && rm *~

veryclean:
	cd latex && latexmk -C && rm ../*~
