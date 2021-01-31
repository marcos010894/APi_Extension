# -- coding: utf-8 --
from flask import Flask,request,jsonify
from flask_cors import CORS
from db import docDB
import os



app = Flask(_name_)
CORS(app)

#############################################
@app.route('/<string:arg>',methods = ['GET'])
def get_Api_search(arg):
    data = docDB()

    false = [{"status" : 4001}]
    search = [i for i in data if i["email"] == arg ]
    if(len(search)==0):
        return jsonify(false)


    return jsonify(search)






    # inicia o codigo
#############################################
if _name== 'main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
