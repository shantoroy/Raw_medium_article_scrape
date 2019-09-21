#!/usr/bin/env python
# coding: utf-8

# In[30]:


import urllib.request
import requests
import bs4
from bs4 import BeautifulSoup


# In[31]:


ethereum = "https://medium.com/search?q=ethereum"


# In[32]:


from selenium import webdriver
driver = webdriver.Chrome('/home/mrx/Downloads/chromedriver')
driver.get(ethereum)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(res, 'lxml')


# In[9]:


work=[]
for my_tag in soup.find_all(class_="ds-link ds-link--styleSubtle link--darken link--accent u-accentColor--textNormal"):
    work.append(my_tag.text)
work


# In[11]:


para=[]
for my_tag in soup.find_all(True,{'class':['graf graf--h4 graf-after--h3 graf--trailing graf--subtitle','graf graf--p graf-after--figure','graf graf--p graf-after--h3 graf--trailing']}):
    para.append(my_tag.text)
para


# In[13]:


title=[]
for my_tag in soup.find_all(True,{'class':['graf graf--h3 graf-after--figure graf--title','graf graf--h3 graf--leading graf--title','graf graf--h3 graf-after--figure graf--trailing graf--title']}):
    title.append(my_tag.text)
title


# In[14]:


read=[]
for my_tag in soup.find_all(class_="readingTime"):
    read.append(my_tag.get('title'))
read


# In[15]:


upvotes=[]
for my_tag in soup.find_all('span',{'class':'u-relative u-background js-actionMultirecommendCount u-marginLeft5'}):
    upvotes.append(my_tag.text)
upvotes


# In[16]:


date=[]
for my_tag in soup.find_all('time'):
    date.append(my_tag.text)
date


# In[17]:


name = []
for my_tag in soup.find_all(class_="ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken"):
    name.append(my_tag.text)
name


# In[23]:


content=[]
alllink=[]
for my_tag in soup.find_all(class_="postArticle postArticle--short js-postArticle js-trackPostPresentation"):
    content.append(my_tag.text)
    for link in my_tag.find_all('a'):
        alllink.append(link.get('href'))
for i in range(0,len(content)):
    content[i]=content[i].replace(name[i],'')
    content[i]=content[i].replace(date[i],'')
    content[i]=content[i].replace(upvotes[i],'')
    content[i]=content[i].replace(title[i],'')
    content[i]=content[i].replace('…Read more…','*')
    content[i]=content[i].replace('Read more…','*')
    content[i]=content[i].replace('\xa0',' ')
    content[i]=content[i].replace(' in ', '')
    for tag in work:
        content[i] = content[i].replace(tag, '')
    content[i]=content[i].split('*')


# In[26]:


body=[]
for i in range(0,len(content)):
    body.append(content[i][0])

res =[]
for i in range(0,len(content)):
    if (len(content[i]) == 1):
        res.append('')
    else:
        res.append(content[i][1])

links=[]
for my_tag in soup.find_all(class_="button button--smaller button--chromeless u-baseColor--buttonNormal"):
        links.append(my_tag.get('href'))


# In[27]:


import pandas as pd
data1 = pd.DataFrame({'1.Tag':'Ethereum','2.Name':name,'3.Title':title,'4.Body':body,'5.Upvotes':upvotes,'6.Date':date,'7.Comments':res,'8.Link':links}) 


# In[28]:


data1.head()


# In[29]:


len(data1)


# In[ ]:




