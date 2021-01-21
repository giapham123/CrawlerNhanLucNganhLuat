import requests  #requests module is used to fetch the HTML code from a webpage
import bs4 #beautiful soup is a module used to parse HTML code using its various functions
import re  #re is a module used to implement various functionalities of regualar expressions
import os
import urllib.request
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
fp=open('data.txt','w+',encoding="utf-8")
for i in range(1,2):
    root_url = 'https://nhanlucnganhluat.vn/'
    page_url = root_url + 'tim-viec-lam/tat-ca-viec-lam+vn.html'
    pages = page_url + '?trang='+str(i)
    r = requests.get(pages)
    soup = bs4.BeautifulSoup(r.content)

    # direct folder to save image
    path = '.\\tempDir'
    files = os.listdir(path)
    # end
    arImages = []
    # get image
    for j in range(len(soup.select('ul li a img'))): 
        arImages.append("local-filename1"+str(j)+str(i)+".jpg")
        fullfilename = os.path.join('.\\tempDir', "local-filename1"+str(j)+str(i)+".jpg")
        urllib.request.urlretrieve(soup.select('ul li a img')[j]['data-src'].replace(" ", "%20").encode('ascii', 'ignore').decode('ascii'), fullfilename)
    # end get image
    arData = []
    # save data to text
    for j in range(len(soup.select('ul li div div'))):
        if(j %2 == 0):
            # print (soup.select('ul li div div')[j].get_text())
            arData.append([soup.select('ul li div div')[j].get_text()])
            fp.write(soup.select('ul li div div')[j].get_text()+ '|'+ "local-filename1"+str(j)+str(i)+".jpg" + '\n')
    # end save data to text
    for j in range (len(arData)):
        print((arData[j][0] + "|"+arImages[j]).split('|'))

        # ws.append(arData[j][0]+ "|"+arImages[j].split('|')) 
    fp.write('\n\n')
wb.save("sample.xlsx")
fp.close()
    
    
    
    
    
