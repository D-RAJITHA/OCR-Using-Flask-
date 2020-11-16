#!flask/bin/python
import werkzeug
import base64
import requests
import json
import jsonpickle
import pytesseract
import re
import numpy as np
import cv2 
import time
import os , io , sys
from datetime import date
from PIL import Image
import pytesseract
import cv2
from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['TEMP_UPLOAD_FOLDER'] = "images" 
app.config["DEBUG"] = True
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def home():
    imagefile = request.files['nationalid']
    language = request.form['language']
    if imagefile and allowed_file(imagefile.filename):
        file_name = werkzeug.utils.secure_filename(imagefile.filename)
        print("\nReceived image File name : " + file_name)
        imagefile.save(os.path.join(app.config['TEMP_UPLOAD_FOLDER'],file_name))
        img = Image.open(imagefile)
        print(language)
        text = pytesseract.image_to_string(img,lang=language)
        print(text)
    return jsonify({"data":text,"statusCode":"200"})


if __name__ == '__main__':
    app.run("0.0.0.0",port=5000, debug=True)
