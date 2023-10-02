#!/usr/bin/env python
# coding: utf-8

# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
import numpy as np
import re
import requests



# In[88]:


from selenium.common.exceptions import NoSuchElementException


# # Q1

# In[3]:


val=input("enter your item ")


# In[ ]:





# In[96]:


driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")


# In[97]:


slct=driver.find_element(By.CLASS_NAME,"nav-search-field ")
slct.click()


# In[98]:


srch = driver.find_element(By.ID, "twotabsearchtextbox")
srch.send_keys('guitar')


# In[99]:


go=driver.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]//span')
go.click()


# In[100]:


urls = []
start = 0
end = 3

for page in range(start, end):
   
    elements = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for element in elements:
        urls.append(element.get_attribute('href'))
    
for url in urls:
    print(url)


# In[91]:


len(urls)


# In[21]:


brand=[]
for url in urls:
    driver.get(url)
    time.sleep(2)
    try:
        brands = driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-medium brand-snapshot-flex-row"]/p/span')
        for brand_element in brands:
            brand.append(brand_element.text)
    except NoSuchElementException:
        brand.append('-')

print(brand)   


# In[22]:


len(brand)


# # Q2

# In[ ]:


"brand name", "name of product","price","return/exchange","expected delivery","availability"


# In[93]:


brand=[]
product=[]
price=[]
rtex=[]
deli=[]
avail=[]
purl=[]


# In[101]:


for url in urls:
    driver.get(url)
    
    try:
        brands = driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-medium brand-snapshot-flex-row"]/p/span')
        for brand_element in brands:
            brand.append(brand_element.text)
    except NoSuchElementException:
        brand.append('-')
        
    try:
        products = driver.find_elements(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        for i in products:
            PP = i.text
            product.append(PP)
    except NoSuchElementException:
        product.append('-')
        
    try:
        prices = driver.find_elements(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]/span[2]/span[2]')
        for i in prices:
            P = i.text
            price.append(P)
    except NoSuchElementException:
        price.append('-')
        
    try:
        rtexs = driver.find_elements(By.XPATH,'//li[3][@class="a-carousel-card tw-scroll-carousel-element"]/div/span/div[2]/span')
        for i in rtexs:
            r = i.text
            rtex.append(r)
    except NoSuchElementException:
        rtex.append('-')
        
    try:
        deliv= driver.find_elements(By.XPATH,'//div[@class="a-spacing-base"]//span[@class="a-text-bold"]')
        for i in deliv:
            d = i.text
            deli.append(d)
    except NoSuchElementException:
        deli.append('-')
        
    try:
        avails= driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-none a-spacing-top-micro }"]')
        for i in avails:
            a = i.text
            avail.append(a)
    except NoSuchElementException:
        avail.append('-')


# In[104]:


print(len(brand), len(product), len(price), len(rtex), len(deli), len(avail))


# In[105]:


df = pd.DataFrame({'BRAND': brand[:177], 'PRODUCT': product[:177], 'PRICE': price[:177], 'RETURN': rtex[:177], 'DELIVERY': deli[:177], 'AVAILABILITY': avail[:177]})
df


# In[103]:


print(len(brand), len(product), len(price), len(rtex), len(deli), len(avail))


# # Q3

# In[39]:


driver=webdriver.Chrome()
driver.get("https://images.google.com/")


# In[40]:


slct=driver.find_element(By.CLASS_NAME,"gLFyf")
slct.click()


# In[41]:


srch = driver.find_element(By.CLASS_NAME,"gLFyf")
srch.send_keys('fruits')


# In[44]:


go=driver.find_element(By.CLASS_NAME,"zgAlFc")
go.click()


# In[51]:


for _ in range(20): # scroll 20 times till 100 images are obtained
    driver.execute_script("window.scrollBy(0,100)")
images=driver.find_elements(By.CLASS_NAME,'rg_i.Q4LuWd')
url=[]
for i in images:
    source=i.get_attribute('src')# src for image class
    if source is not None:
        if(source[0:4]=='http'):
            url.append(source)
for i in range(len(url)):
    if i >10:
        breakBy.XPATH,
    print("dwld {0} of {1} img".format(i,10))
    response=requests.get(url[i])
    file=open(r'C:\Users\LENOVO\OneDrive\Desktop\data trained'+str(i)+".jpg","wb")
    file.write(response.content)


# In[49]:





# # Q4

# In[13]:


driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")


# In[95]:


slct=driver.find_element(By.CLASS_NAME,"_2SmNnR")
slct.click()


# In[14]:


srch = driver.find_element(By.CLASS_NAME,"Pke_EE")
srch.send_keys('Oneplus Nord')


# In[97]:


go=driver.find_element(By.CLASS_NAME,"_2iLD__")
go.click()


# In[173]:


# brand=[]
name=[]
col=[]
ram=[]
rom=[]
Pcam=[]
Scam=[]
size=[]
bat=[]
P=[]
url=[]


# In[175]:


names = driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
for i in names:
    bb = i.text
    name.append(bb)

colors = driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')
for i in colors:
    cc = i.text
    match = re.search(r'\(([^,]+),', cc) 
    if match:
        text = match.group(1).strip()
        col.append(text)

ra = driver.find_elements(By.XPATH, '//ul[@class="_1xgFaf"]/li[1]')
for i in ra:
    rr = i.text
    match = re.search(r'(\d+\s*GB\s*RAM)', rr)
    if match:
        text = match.group(0).strip()
        ram.append(text) 

ro = driver.find_elements(By.XPATH, '//ul[@class="_1xgFaf"]/li[1]')
for i in ro:
    rrr = i  
    match = re.search(r'(\d+\s*GB\s*ROM)', rrr.text)
    if match:
        text = match.group(0).strip()
        rom.append(text)  

prim = driver.find_elements(By.XPATH,'//ul[@class="_1xgFaf"]/li[3]')
for i in prim:
    pp = i.text
    Pcam.append(pp)
BAT = driver.find_elements(By.XPATH,'//ul[@class="_1xgFaf"]/li[4]')
for i in BAT:
    bats = i.text
    bat.append(bats)
SIZ = driver.find_elements(By.XPATH,'//ul[@class="_1xgFaf"]/li[2]')
for i in SIZ:
    siz = i.text
    size.append(siz)
P=[]
PRI = driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for element in PRI:
    pri = element.text
    P.append(pri)


# In[176]:


print(len(name),len(col),len(ram),len(rom),len(Pcam),len(bat),len(size),len(P))


# In[177]:


df=pd.DataFrame({'NaME':name,'colour':col,'RAM':ram,'ROM':rom,'camera':Pcam,'Battery':bat,"SIZE":size,'Price':P})
df


# In[180]:


path = 'Phoneoutput.csv'
df.to_csv(path, index=True) 
print(f'DataFrame saved to ',path)


# # Q5

# In[ ]:


#Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. 


# In[57]:


driver=webdriver.Chrome()
driver.get("https://www.google.com/maps/")


# In[58]:


srch = driver.find_element(By.ID,"searchboxinput")
srch.send_keys('bangalore')


# In[59]:


go=driver.find_element(By.CLASS_NAME,"pzfvzf")
go.click()


# In[62]:


try:
    url = driver.current_url
    print("Extracted URL:", url)
    lat_lng = re.findall(r'@([-0-9.]+),([-0-9.]+)', url)
    if lat_lng:
        latitude, longitude = lat_lng[0]
        print("Latitude:", latitude)
        print("Longitude:", longitude)
except Exception as e:
    print("An error occurred:", str(e))



# # Q6

# In[111]:


driver=webdriver.Chrome()
driver.get("https://www.digit.in/")


# In[112]:


go=driver.find_element(By.XPATH,'//li[@class="rh-subitem-menus rh-megamenu menu-item menu-item-type-post_type_archive menu-item-object-top-products"]')
go.click()


# In[114]:


go=driver.find_element(By.XPATH,'//div[@class="main-side clearfix full_width"]/div/div[2]/div[6]/p/a')
go.click()


# In[122]:


try:
    name=[]
    names = driver.find_elements(By.XPATH,'//h3[@class="font130 mt0 mb10 mobilesblockdisplay "]')
    for i in names:
        bb = i.text
        name.append(bb)
except NoSuchElementException:
    name.append('-')
try:
    os=[]
    oss = driver.find_elements(By.XPATH,'//div[@class="woo_code_zone_loop clearbox"]/div[1]/div/span[2]')
    for i in oss:
        ss = i.text
        os.append(ss)
except NoSuchElementException:
    os.append('-')
try:
    dis=[]
    disps = driver.find_elements(By.XPATH,'//div[@class="woo_code_zone_loop clearbox"]/div[2]/div/span[2]')
    for i in disps:
        pp = i.text
        dis.append(pp)
except NoSuchElementException:
    dis.append('-')
try:
    res=[]
    ress = driver.find_elements(By.XPATH,'//div[@class="woo_code_zone_loop clearbox"]/div[3]/div/span[2]')
    for i in ress:
        s = i.text
        res.append(s)
except NoSuchElementException:
    res.append('-')

try:
    pro=[]
    pros = driver.find_elements(By.XPATH,'//div[@class="woo_code_zone_loop clearbox"]/div[3]/div/span[2]')
    for i in pros:
        b = i.text
        pro.append(b)
except NoSuchElementException:
    pro.append('-')
try:
    des=[]
    dess = driver.find_elements(By.XPATH,'//div[@class="cegg-no-top-margin cegg-list-logo-title"]/a')
    for i in dess:
        d = i.text
        des.append(d)
except NoSuchElementException:
    des.append('-')
try:
    pri=[]
    pris = driver.find_elements(By.XPATH,'//div[@class="cegg-price cegg-price-color cegg-price-instock"]')
    for i in pris:
        pr = i.text
        pri.append(pr)
except NoSuchElementException:
    pri.append('-')


# In[125]:


df = pd.DataFrame({'BRAND': name[:4], 'operating system': os[:4], 'PRICE': pri[:4], 'describe': des[:4], 'processor': pro[:4],'resolution':res[:4],'display size':dis[:4]})
df


# # Q7

# In[34]:


driver=webdriver.Chrome()
driver.get("https://www.forbes.com/")


# In[39]:


slct=driver.find_element(By.XPATH,'//div[@class="_8FT-x3t4"]/div')
slct.click()


# In[42]:


go = driver.find_element(By.XPATH, '//li[@class="TjJgrPSg _2bNo56RE secondary"]/a[1]')

go.click()


# In[71]:


rank=[]
name=[]
net=[]
AGE=[]
cnt=[]
src=[]
ind=[]


# In[72]:


ranks = driver.find_elements(By.XPATH,'//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')
for i in ranks:
    rk = i.text
    rank.append(rk)


names = driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[2]')
for i in names:
    bb = i.text
    name.append(bb)


nets = driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[3]')
for i in nets:
    n = i.text
    net.append(n)

ages = driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[4]')
for i in ages:
    age = i.text
    AGE.append(age)



cnts = driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[5]')
for i in cnts:
    c = i.text
    cnt.append(c)

srcs = driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[6]')
for i in srcs:
    s = i.text
    src.append(s)

inds = driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[7]')
for i in inds:
    indus = i.text
    ind.append(indus)


# In[74]:


df=pd.DataFrame({'RANK':rank,'NAME':name,'NET':net,'AGE':AGE,'COUNTRY':cnt,'SOURCE':src,"INDUSTRY":ind})
df


# # Q8

# In[71]:


driver=webdriver.Chrome()
driver.get("https://www.youtube.com/")
slct=driver.find_element(By.CLASS_NAME,"style-scope ytd-rich-grid-media")
slct.click()
cnt=[]
time=[]
vote=[]
for _ in range(1000): 
    driver.execute_script("window.scrollBy(0,1000)")
cnts = driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-comment-renderer"]/div[2]/div[2]')
for i in cnts:
    c = i.text
    cnt.append(c)
times = driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-comment-renderer"]/yt-formatted-string')
for i in times:
    lk = i.text
    time.append(lk)
votes = driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-comment-action-buttons-renderer"]/span[2]')
for i in votes:
    vt = i.text
    vote.append(vt)


# In[78]:


df=pd.DataFrame({'comment':cnt[:120],'uploaded':time[:120],'upvotes':vote[:120]})
df


# # Q9

# In[ ]:


hostel name, distance from city centre, ratings, total reviews, overall
reviews, privates from price, dorms from price, facilities and property description.


# In[43]:


driver=webdriver.Chrome()
driver.get("https://www.hostelworld.com/")


# In[44]:


slct=driver.find_element(By.CLASS_NAME,"native-input")
slct.click()


# In[46]:


srch = driver.find_element(By.CLASS_NAME,"native-input")
srch.send_keys('London')


# In[47]:


slct=driver.find_element(By.CLASS_NAME,"item-text")
slct.click()


# In[48]:


go = driver.find_element(By.XPATH, '//button[@class="btn-content medium-button icon-only"]')
go.click()


# In[23]:


name=[]
names = driver.find_elements(By.XPATH,'//div[@class="property-name"]/span')
for i in names:
    n = i.text
    name.append(n)
dist=[]
dists = driver.find_elements(By.XPATH,'//span[@class="distance-description"]')
for i in dists:
    d = i.text
    dist.append(d)
rate=[]
rates = driver.find_elements(By.XPATH,'//span[@class="number"]')
for i in rates:
    r = i.text
    rate.append(r)
tot=[]
tots = driver.find_elements(By.XPATH,'//div[@class="review"]')
for i in tots:
    t = i.text
    tot.append(t)
pri=[]
pris = driver.find_elements(By.XPATH,'//div[@class="accommodation-price unavailable"]')
for i in pris:
    p = i.text
    pri.append(p)


# In[24]:


print(pri)


# In[52]:


urls = []
start = 0
end = 1

for page in range(start, end):
   
    elements = driver.find_elements(By.XPATH, '//a[@class="property-card-container horizontal"]')
    for element in elements:
        urls.append(element.get_attribute('href'))
for url in urls:
    print(url)


# In[53]:


fac=[]
for url in urls:
    driver.get(url)
    facs= driver.find_elements(By.XPATH,'//ul[@class="facilities"]/li')
    for i in facs:
        bb= i.text
        fac.append(bb)
print(fac)


# In[59]:


print(len(name),len(dist),len(rate),len(tot),len(pri),len(fac))


# In[62]:


df = pd.DataFrame({
    'name': name[:31],'distance': dist[:31],'rate': rate[:31],'totalreview': tot[:31],'price': pri[:31],'facility': fac[:31]})
df


# In[ ]:




