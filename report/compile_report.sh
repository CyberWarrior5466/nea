#!/bin/bash

cd report/assets/input

for i in *.mmd; do
    ~/.yarn/bin/mmdc -c ../mermaid_config.json \
         -i "$i" \
         -o "../${i%.*}.svg"
done

for i in *.pikchr; do
    fossil pikchr "$i" "../${i%.*}.svg"
done

cd ../../..

cd report
cp report.md temp_report.md
pandoc metadata.yaml report.md \
        --output=out.pdf \
        --syntax-definition=aqa.xml \
        --pdf-engine=xelatex \
        --table-of-contents \
        --number-sections

cd ..

python report/add_code.py > 

# xdg-open report/out.pdf