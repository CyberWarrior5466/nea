#!/bin/bash

echo "compiling"

cp report/report.md report/temp_report.md
python report/add_code.py report/temp_report.md -no_font
cd report

pandoc metadata_no_font.yaml temp_report.md \
    --output=out.pdf \
    --syntax-definition=aqa.xml \
    --number-sections \
    # --table-of-contents

rm temp_report.md

cd ..

# echo report/report.md | entr report/compile_report_no_font.sh
