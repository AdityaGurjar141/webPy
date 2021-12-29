import requests
from bs4 import BeautifulSoup as bs
import os
import img2pdf
from PIL import Image
from fpdf import FPDF
tag = input("Enter Doujin ID: ")

try:
    os.mkdir(os.path.join(os.getcwd(), tag))
except:
    pass
os.chdir(os.path.join(os.getcwd(), tag))
url = "%s%s/"%("https://nhentai.net/g/",tag)
page= requests.get(url)
#html=page.text
#print(html)
#results = bs.find(class_="thumb-container")
soup = bs(page.content, "html.parser")
pages=soup.find_all("a", class_="gallerythumb")
max_page=(len(pages))

for x in pages:
    url2 = "%s%s/%s/"%("https://nhentai.net/g/",tag,str(pages.index(x)+1))
    #print(url2)
    page= requests.get(url2)
    soup = bs(page.content, "html.parser")
    p_imag=soup.find("section", id = "image-container")
    p_imag2= p_imag.find("img")
    img_link=p_imag2['src']
    #print(img_link)
    with open(str(pages.index(x)+1)+'.jpg','wb') as f:
        im = requests.get(img_link)
        f.write(im.content)



file = open("%s%s"%(tag,'.pdf'), "wb")
pdf = FPDF()
for x in pages:
    #image = Image.open("%s%s"%(str(pages.index(x)+1),'.jpg'))
    pdf.add_page()
    pdf.image("%s%s"%(str(pages.index(x)+1),'.jpg'), x=0, y=0, w=210)
pdf.output("%s%s"%(tag,'.pdf'))
file.close()







