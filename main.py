 # -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from db import docDB
import os



app = Flask(__name__)

#############################################
@app.route('/<string:arg>',methods = ['GET'])
def get_Api_search(arg):
    data = docDB()

    false = [{"email" : False}]
    search = [i for i in data if i["email"] == arg ]
    if(len(search)==0):
        return jsonify(false[0])


    return jsonify(search[0])






    # inicia o codigo
#############################################
if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
