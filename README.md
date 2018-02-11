# PranitRox
Project for coding culture hackathon. And yes, Pranit really rox.

## Code

filterdb.py - To clean MET database and extract only public domain page links relevant to India

Usage:

>python3 filterdb.py filename.csv > linkfilename.csv

downloadmet.py - Script to extract image URLs from webpages found by filterdb.py

Usage:

>cat linkfilename.csv | python3 downloadmet.py imglinkfilename.csv

imageconverter.py - Script to convert images to black and white template image from a given folder

Usage:

>python3 imageconverter.py pathname

## Datasets

[Harvard Art Museum](https://www.harvardartmuseums.org/) - API key will be emailed to all.

[MET Museum](https://www.metmuseum.org/)

[WikiArt](https://www.wikiart.org/) [WikiArt data retriever](https://github.com/lucasdavid/wikiart)

## Useful Links

[AR.js-Efficient AR for the web](https://jeromeetienne.github.io/AR.js/)

[NativeScript - Developing native JS mobile apps](https://docs.nativescript.org/)

[Artistic Style Transfer - Excellent Neural Network Explanation](https://harishnarayanan.org/writing/artistic-style-transfer/)
