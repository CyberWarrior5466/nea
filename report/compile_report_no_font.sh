#!/bin/bash

cp report/report.md report/temp_report.md
python report/add_code.py report/temp_report.md -no_font
cd report


pandoc metadata_no_font.yaml temp_report.md \
        --output=out.pdf \
        --syntax-definition=aqa.xml \
        --table-of-contents \
        --number-sections

rm temp_report.md

cd ..

xdg-open report/out.pdf
