
# coding: utf-8

# In[16]:

from selenium import webdriver


# In[17]:

import time
import os
from os import listdir


# In[18]:

import jieba


# In[19]:

from sklearn import feature_extraction


# In[20]:

from sklearn.feature_extraction.text import TfidfTransformer


# In[21]:

from sklearn.feature_extraction.text import CountVectorizer


# In[22]:

from sklearn.cluster import KMeans


# In[8]:

def is_element_exist(css):
    try:
        browser.find_element_by_tag_name(css)
        return True
    except:
        return False
def is_class_para(classname):
    elems_div=browser.find_elements_by_tag_name('div')
    for elem_div in elems_div:
        if elem_div.get_attribute('class')==classname: return True
    return False


# In[13]:

if __name__ == "__main__":
    if not os.path.exists("D:\\PythonPersonal"):
            os.mkdir("D:\\PythonPersonal")     
    browser=webdriver.Chrome()
    browser.get('https://www.baidu.com/s?wd=%E6%AD%A6%E5%B3%B0&rsv_spt=1&rsv_iqid=0x9952ff8a0005da91&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=6&rsv_sug7=100')
    i=0
    while(i<20):    
        i=i+1
        '''开始依次抓取'''
        elems=browser.find_elements_by_class_name('t')
        for elem in elems:
            print("正在抓取文章："+elem.text+"...")   
            title=elem.text
            title=title.replace('?','').replace('/','').replace('<','').replace('>','').replace('|','').replace('*','').replace('"','')    #避免文件名禁用符
            elem.find_element_by_tag_name('a').click()
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[-1])
            if is_class_para('para'):
                elems_div=browser.find_elements_by_class_name('para')
                for elem_div in elems_div:
                    #print(elem_div.text)
                    with open('D:\\PythonPersonal/'+title+'.txt',"a",encoding='utf-8') as f:  
                        f.write(elem_div.text)
                        f.write('\n')
            elif is_element_exist('p'):
                elems_p=browser.find_elements_by_tag_name('p')
                for elem_p in elems_p:
                    #print(elem_p.text)
                    with open('D:\\PythonPersonal/'+title+'.txt',"a",encoding='utf-8') as f:  
                        f.write(elem_p.text)
                        f.write('\n')
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
        browser.find_elements_by_class_name('n')[-1].click()
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[0])


# In[26]:

all_file=listdir('D:/PythonPersonal')
for file in all_file:
        if os.path.getsize(os.path.join("D:/PythonPersonal", file)) == 0:  
             os.remove(os.path.join("D:/PythonPersonal", file)
labels=[] 
corpus=[] 


# In[30]:

typetxt=open('D:/PythonPersonal/stop.txt')
texts=['\u3000','\n',' ']


# In[31]:

for word in typetxt:
        word=word.strip()
        texts.append(word)


# In[33]:

for i in range(0,len(all_file)):
        filename=all_file[i]
        filelabel=filename.split('.')[0]
        labels.append(filelabel)
        file_add='D:/PythonPersonal/'+ filename
        print(file_add)
        doc=open(file_add,encoding='utf-8').read()
        data=jieba.cut(doc,cut_all=True) 
        data_adj=''
        delete_word=[]
        for item in data:
            if item not in texts: 
                data_adj+=item+' '
            else:
                delete_word.append(item)
        corpus.append(data_adj)


# In[37]:

vectorizer=CountVectorizer()    
transformer=TfidfTransformer()  
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))   
weight=tfidf.toarray()     
word=vectorizer.get_feature_names()     
mykms=KMeans(n_clusters=10)
y=mykms.fit_predict(weight)
for i in range(0,10):
    label_i=[]
    for j in range(0,len(y)):
        if y[j]==i:
            label_i.append(labels[j])
    print('label_'+str(i)+':'+str(label_i))


# In[ ]:



