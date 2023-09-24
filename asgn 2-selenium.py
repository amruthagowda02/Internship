#!/usr/bin/env python
# coding: utf-8

# In[57]:


import selenium
import pandas as pd
import numpy as np
from selenium import webdriver
import warnings
warnings.filterwarnings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# # Q1
# 

# In[273]:


driver=webdriver.Chrome()


# In[274]:


driver.get('https://www.shine.com/')


# In[278]:


slct=driver.find_element(By.CLASS_NAME,"searchBarInput")
slct.click()


# In[279]:


job=driver.find_element(By.CLASS_NAME,"form-control  ")
job.send_keys('Data Analyst')


# In[280]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[285]:


search_button = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search_button.click()


# In[286]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[287]:


title_tags = driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)

location_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)

company_tags = driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)

exp_tags = driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in exp_tags[0:10]:
    exp = i.text
    experience_required.append(exp)


# In[288]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[289]:


import pandas as pd
df=pd.DataFrame({'TITLE':job_title,'LOCATION':job_location,'COMPANY NAME':company_name,'EXPERIENCE REQUIRED':experience_required})
df


# # Q2

# In[293]:


driver=webdriver.Chrome()
driver.get('https://www.shine.com/')


# In[297]:


slct=driver.find_element(By.CLASS_NAME,"searchBarInput")
slct.click()


# In[298]:


job=driver.find_element(By.CLASS_NAME,"form-control  ")
job.send_keys('Data scientist')


# In[299]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[301]:


search_button = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search_button.click()


# In[302]:


job_title=[]
job_location=[]
company_name=[]


# In[303]:


title_tags = driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)

location_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)

company_tags = driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)


# In[304]:


df=pd.DataFrame({'TITLE':job_title,'LOCATION':job_location,'COMPANY NAME':company_name,'EXPERIENCE REQUIRED':experience_required})
df


# # Q3

# In[328]:


driver=webdriver.Chrome()
driver.get('https://www.shine.com/')


# In[332]:


slct=driver.find_element(By.CLASS_NAME,"searchBarInput")
slct.click()


# In[333]:


job=driver.find_element(By.CLASS_NAME,"form-control  ")
job.send_keys('Data scientist')


# In[335]:


search_button = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search_button.click()


# In[336]:


slct_loc=driver.find_element(By.CLASS_NAME,"filter_filter_lists_items__wlFfo")
slct_loc.click()


# In[347]:


delhi_option = driver.find_element(By.XPATH,'//li[@class="filter_filter_option_item__bvdpQ"][7]')
delhi_option.click()


# In[350]:


slct_=driver.find_element(By.XPATH,'//div[@class="filter_btnWrap__5ToWy"]//button[2]')
slct_.click()


# In[ ]:


slct_sal=driver.find_element(By.CLASS_NAME,)
slct_sal.click()


# In[357]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[358]:


title_tags = driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)

location_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)

company_tags = driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)

exp_tags = driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in exp_tags[0:10]:
    exp = i.text
    experience_required.append(exp)


# In[359]:


df=pd.DataFrame({'TITLE':job_title,'LOCATION':job_location,'COMPANY NAME':company_name,'EXPERIENCE REQUIRED':experience_required})
df


# # Q4

# In[246]:


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")


# In[247]:


sr=driver.find_element(By.CLASS_NAME,"Pke_EE")
sr.send_keys('sunglasses')


# In[248]:


search_button = driver.find_element(By.CLASS_NAME,"_2iLD__" )
search_button.click()


# In[249]:


B=[]
D=[]
P=[]


# In[251]:


B_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in B_tags:
    BB = i.text
    B.append(BB)
P_tags = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in P_tags:
    PP = i.text
    P.append(PP)
    
D_tags = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in D_tags:
    DD = i.text
    D.append(DD)


# In[252]:


print(len(P),len(B),len(D)) 


# In[253]:


min_ = min(len(P), len(B), len(D))
P = P[:min_]
B = B[:min_]
D = D[:min_]
df=pd.DataFrame({'TITLE':B,'RATING':D,"PRICE":P})
df


# # Q5

# In[237]:


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market")


# In[240]:


rat=[]
sm=[]
fl=[]


# In[244]:


R_tags = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in R_tags:
    RE = i.text
    rat.append(RE)
    
    
sm_tags = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in sm_tags:
    SM = i.text
    sm.append(SM)
    
fl_tags = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in fl_tags:
    FULL = i.text
    fl.append(FULL)


# In[245]:


df=pd.DataFrame({'TITLE':rat,'RATING':sm,"PRICE":fl})
df


# # Q6

# In[221]:


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")


# In[223]:


sr=driver.find_element(By.CLASS_NAME,"Pke_EE")
sr.send_keys('sneakers')


# In[225]:


search_button = driver.find_element(By.CLASS_NAME,"_2iLD__" )
search_button.click()


# In[226]:


B=[]
D=[]
P=[]


# In[231]:


B_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in B_tags:
    BB = i.text
    B.append(BB)
    
P_tags = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in P_tags:
    PP = i.text
    P.append(PP)
    
D_tags = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in D_tags:
    DD = i.text
    D.append(DD)


# In[234]:


print(len(P),len(B),len(D)) 


# In[236]:


min_ = min(len(P), len(B), len(D))
P = P[:min_]
B = B[:min_]
D = D[:min_]
df=pd.DataFrame({'TITLE':B,'RATING':D,"PRICE":P})
df


# # Q7

# In[200]:


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")


# In[201]:


sr=driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute")
sr.send_keys('laptop')


# In[202]:


search_button = driver.find_element(By.CLASS_NAME, "nav-search-submit.nav-sprite")
search_button.click()


# In[204]:


cpu_type = driver.find_element(By.ID, "p_n_feature_thirteen_browse-bin/12598163031")
cpu_type.click()

option = driver.find_element(By.ID, "p_n_feature_thirteen_browse-bin/16757432031")
option.click()


# In[208]:


T=[]
R=[]
P=[]


# In[218]:


T_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in T_tags:
    TT = i.text
    T.append(TT)
    
R_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-base puis-bold-weight-text"]')
for i in R_tags:
    RR = i.text
    R.append(RR)

P_tags = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in P_tags:
    PP = i.text
    P.append(PP)


# In[220]:


df=pd.DataFrame({'TITLE':T,'RATING':R,"PRICE":P})
df


# # Q8

# In[160]:


driver = webdriver.Chrome()
driver.get("https://www.azquotes.com/")


# In[161]:


elements = driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a") 
elements[0].click()


# In[162]:


Q=[]
A=[]
T=[]


# In[163]:


Q_tags = driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in Q_tags:
    QT = i.text
    Q.append(QT)
A_tags = driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in A_tags:
    AT = i.text
    A.append(AT)

T_tags = driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in T_tags:
    TT = i.text
    T.append(TT)


# In[164]:


print(len(Q),len(A),len(T))


# In[165]:


df=pd.DataFrame({'QUOTE':Q,'AUTHOR':A,"TYPE":T})
df.head(20)


# # Q9 

# In[59]:


driver = webdriver.Chrome()
driver.get("https://www.jagranjosh.com/")


# In[102]:


elements = driver.find_elements(By.XPATH, "/html/body/div/header/nav/div/div/div[3]/ul/li[3]/a")
elements[0].click()


# In[104]:


pm=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a")
pm[0].click()


# In[130]:


names = []
born_dead=[]
TO=[]
rmk=[]
name_tags = driver.find_elements(By.XPATH, '//div[@class="table-box"]//table/tbody/tr/td[2] ')
for i in name_tags:
    name = i.text
    names.append(name)

bd_tags = driver.find_elements(By.XPATH, '//div[@class="table-box"]//table/tbody/tr/td[3] ')
for i in bd_tags:
    BD = i.text
    born_dead.append(BD)

term_tags = driver.find_elements(By.XPATH, '//div[@class="table-box"]//table/tbody/tr/td[4] ')
for i in term_tags:
    title = i.text
    TO.append(title)

rmk_tags = driver.find_elements(By.XPATH, '//div[@class="table-box"]//table/tbody/tr/td[5] ')
for i in rmk_tags:
    rank = i.text
    rmk.append(rank)


# In[125]:


print(len(names),len(born_dead),len(TO))


# In[131]:


max_length = max(len(names), len(born_dead))
names += [np.nan] * (max_length - len(names))
TO += [np.nan] * (max_length-len(TO))
rmk += [np.nan] * (max_length-len(rmk))
born_dead += [np.nan] * (max_length - len(born_dead))
df=pd.DataFrame({'NAME':names,'BORN-DEAD':born_dead,"TERM OF OFC":TO,"rank":rmk})
df


# # Q 10

# In[35]:


driver = webdriver.Chrome()
driver.get('https://www.motor1.com/')
driver.find_elements(By.CLASS_NAME, "m1-search-panel-input.m1-search-form-text")[0].send_keys('50 most expensive cars')


# In[37]:


driver.find_element(By.CLASS_NAME,"m1-search-form-button-wrapper").click()


# In[ ]:


driver.find_element(By.CLASS_NAME./features/308149/most-expensive-new-cars-ever/")


# In[48]:


cars=[]
car_tags = driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_tags:
    list = i.text
    cars.append(list)


# In[53]:


price=[]
rs_tags = driver.find_elements(By.XPATH,"//strong[contains(text(), 'Price: $')]")
for i in rs_tags:
    list = i.text
    price.append(list)


# In[54]:


print(len(cars),len(price))


# In[58]:


max_length = max(len(cars), len(price))
cars += [np.nan] * (max_length - len(cars))
price += [np.nan] * (max_length - len(price))
df=pd.DataFrame({'cars':cars,'price':price})
df


# In[ ]:




