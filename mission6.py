
# coding: utf-8

# In[6]:


get_ipython().system('pip install flask')


# In[ ]:


"""
get 時 回傳json

"""
#引用套件
from flask import Flask, request, abort, jsonify
#flask這個應用的啟動點
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#為這個啟動點增加訪問路徑'/'
@app.route('/',methods=['GET'])
def hello_world():
    t = {'userId':1,'userName':'xiaoming'}
    return jsonify(t)
#啟用app
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
#請訪問192.168.114.10:5000/

