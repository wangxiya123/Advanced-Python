
# coding: utf-8

# In[34]:

def get_data(url):
    res = requests.get(url)
    from pyquery import PyQuery as pq
    doc = pq(res.content)
    return doc

def content_write(content,filename):
    #将文字写入文件
        with open(filename,"w",encoding='utf-8') as f:
            for i in range (len(content)): 
                f.write(content[i])
                f.write('\n')
                f.write('\n')
            f.close()
def pic_write(content,filename):
    #将图片写入txt文件
    file = open(filename,'w+')
    for k in range (len(content)):    
        file.write(content[k][24:-1]+'\n')
    file.close()
    
def mkdir(new_path):
       # new_path=path+title[j]
        if not os.path.exists(new_path):  
            try:
                os.mkdir(new_path)
            except FileNotFoundError:
                pass


# In[2]:

import requests
import os
import re
from pyquery import PyQuery as pq


# In[ ]:

root='http://skqs.guoxuedashi.com'
doc=get_data(root)
url=[pq(sq).attr('href') for sq in doc('.dd3 a')]
title=[pq(st).text() for st in doc('.clearfix .dd3 a')]
for h in range(4):
    path = "F:\\pc\\"
    new_path=path+title[h]
    mkdir(new_path)
    urll=root+url[h]
    doc=get_data(urll)
    url1=[pq(sq).attr('href') for sq in doc('.dd3 a')]
    title1=[pq(st).text() for st in doc('.dd3 a')]
    for j in range(len(url1)):
        new_path1=new_path+"\\"+title1[j]
        mkdir(new_path1)
        url2=root+url1[j]
        docc=get_data(url2)
        url3=[pq(sq).attr('href') for sq in docc('.info_cate a')]
        title2=[pq(st).text() for st in docc('.info_cate a')]
        for i in range(len(url3)):
            new_path2=new_path1+"\\"+title2[i]
            mkdir(new_path2) 
            url4=root+url3[i]
            doccc=get_data(url4)
            #name=doccc(".info_tree a").text()
            text_name=title2[i]
            cc=doccc('.tline').text()
            content=re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", cc)
            ccc=content.split('-') #文字
            pq(doccc('script')[-6]).text()
            aaaa = pq(doccc('script')[-6]).text()
            m=re.search('imglist.+png\'\;',aaaa)
            try:
                n=m.group(0).split(';')
                filename_text=new_path2+"\\"+text_name+'.txt'
                filename_pic=new_path2+"\\"+text_name+'_picsource.txt'
                content_write(ccc, filename_text)
                pic_write(n, filename_pic)
            except AttributeError:
                pass
            continue


# In[ ]:

url2=root+url1[j]
        docc=get_data(url2)
        url3=[pq(sq).attr('href') for sq in docc('.info_cate a')]
        title2=[pq(st).text() for st in docc('.info_cate a')]
        for i in range(len(url3)):
            path2=path1+title[j]+"\\"
            mkdir(title2,i,path2) 
            url4=root+url3[i]
            doccc=get_data(url4)
            #name=doccc(".info_tree a").text()
            text_name=title2[i]+'.txt'
            cc=doccc('.tline').text()
            content=re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", cc)
            ccc=content.split('-') #文字
            pq(doccc('script')[-6]).text()
            aaaa = pq(doccc('script')[-6]).text()
            m=re.search('imglist.+png\'\;',aaaa)
            try:
                n=m.group(0).split(';')
                filename_text=path2+title2[i]+"\\"+text_name
                filename_pic=path2+title2[i]+"\\pic_url.txt"
                content_write(content, filename_text)
                pic_write(n, filename_pic)
            except AttributeError:
                pass
            continue


# In[ ]:

url2=root+url1[j]
        docc=get_data(url2)
        url3=[pq(sq).attr('href') for sq in docc('.info_cate a')]
        title2=[pq(st).text() for st in docc('.info_cate a')]
        for i in range(len(url3)):
            path2=path1+title[j]+"\\"
            mkdir(title2,i,path2) 
            url4=root+url3[i]
            doccc=get_data(url4)
            #name=doccc(".info_tree a").text()
            text_name=title2[i]+'.txt'
            cc=doccc('.tline').text()
            content=re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", cc)
            ccc=content.split('-') #文字
            pq(doccc('script')[-6]).text()
            aaaa = pq(doccc('script')[-6]).text()
            m=re.search('imglist.+png\'\;',aaaa)
            try:
                n=m.group(0).split(';')
                filename_text=path2+title2[i]+"\\"+text_name
                filename_pic=path2+title2[i]+"\\pic_url.txt"
                content_write(content, filename_text)
                pic_write(n, filename_pic)
            except AttributeError:
                pass
            continue

