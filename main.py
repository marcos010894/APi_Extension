 # -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)

#############################################
@app.route('/<string:arg>',methods = ['GET'])
def get_Api_search(arg):

    false = [{"pago" : True}]
  
    return jsonify(false[0])






    # inicia o codigo
#############################################
if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port) # -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)

#############################################
@app.route('/<string:arg>',methods = ['GET'])
def get_Api_search(arg):

    false = [{"pago" : True}]
  
    return jsonify(false[0])






    # inicia o codigo
#############################################
if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
