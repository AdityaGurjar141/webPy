# webPy

## python scraping
The code is used to scrape bulk images from a specific website. The website uses a six-digit code to index different catalogs.
The code takes that six-digit number, downloads that specific catalog, and compiles it into a pdf.

It works in the current working directory of the PC and doesn't have a specific download location.

## Dependencies
The code uses these libraries to perform its function.
Requests
BeautifulSoup
os
img2pdf *deprecated*
Pillow
FPDF
