
# coding: utf-8

# In[ ]:


"""
flask get結合query string

使用時，查詢http://192.168.114.10:5000?hello=iii

"""
#引用套件
from flask import Flask, request, abort, jsonify
#flask這個應用的啟動點
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#為這個啟動點增加訪問路徑'/'
@app.route('/',methods=['GET'])
def hello_world():
    #取用用戶的querystring,用戶欄位輸入的是hello的內容直
    #192.168.114.10:5000?hello=sdjfydj
    t = request.args.get('userId')
    #轉成dict
    jsonDict = {'userId':t}
    #把dict轉成json,並回傳給用戶
    return jsonify(jsonDict)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

