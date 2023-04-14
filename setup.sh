#!/bin/bash

# # ubuntu
# sudo apt install hatch pandoc texlive-xetex fonts-firacode ttf-mscorefonts-installer npm fossil -y 

# # fedora
# sudo dnf install 'dnf-command(copr)'
# sudo dnf copr enable adrienverge/some-nice-fonts -y
# sudo dnf install hatch pandoc texlive-xetex fira-code-fonts some-nice-fonts npm librsvg2-tools texlive-scheme-medium fossil -y


# cd report
# mkdir mermaid
# cd mermaid
# https://github.com/mermaid-js/mermaid-cli#install-locally
# sudo dnf install yarnpkg
# sudo npm install -g @mermaid-js/mermaid-cli

cd report/assets/diagrams
for i in *.mmd; do
    mmdc -c ../mermaid_config.json \
         -i "$i" \
         -o "..${i%.*}.svg"
done
cd ../../..



# then manually change `==` to `<=` for syntax_tree.svg with inspect element
# becuase otherwise renders as `&lt;`


# # setup project
# hatch shell

# # publish to pypi
# hatch build
# hatch publish -r 
#   # go on https://pypi.org
#   # get a token https://pypi.org/help/#apitoke
#   # copy paste the username and token in this command
