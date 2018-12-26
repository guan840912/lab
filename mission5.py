
# coding: utf-8

# In[6]:


import requests
responseFromRemote = requests.get('https://jsonplaceholder.typicode.com/users')

# 有時我們想看response的body內容
#print(responseFromRemote.text)

# 若已經能預期傳回的內容為json格式，則可以直接將其轉為python可操作的資料格式
a = responseFromRemote.json()
#print(responseFromRemote.json())
a1 = print(a[2])
b1 = print(a[3])
c1 = print(a[4])
d1 = print(a[5])


# In[9]:


print(a[2])


# In[3]:


import datetime
nowTime = datetime.datetime.utcnow().strftime("%Y-%m-%d")
print(nowTime)


# In[15]:


import os
import shutil

abc = open(nowTime+'.txt','w')
 # 將資料寫入檔案
abc.write(str(a[2]))
abc.write(str(a[3]))
abc.write(str(a[4]))
abc.write(str(a[5]))
# 將檔案關閉
abc.close()

