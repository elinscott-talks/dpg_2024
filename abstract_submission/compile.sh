#!/bin/bash
mv ~/Downloads/contribution.tex .
sed -i 's/_synopsis//g' contribution.tex && sed -i 's/\scKeywords/%/g' contribution.tex && pdflatex contribution.tex && evince contribution.pdf
