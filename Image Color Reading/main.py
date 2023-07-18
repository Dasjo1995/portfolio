import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import time

import pandas as pd
import matplotlib.patches as patches
import matplotlib.image as mpimg

import cv2
import extcolors

from colormap import rgb2hex

#pip install easydev, colormap, opencv-python, colorgram.py, extcolors

from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from functools import wraps
import sqlite3

from forms import Upload

app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf' # used for securely signing the session cookie
ckeditor = CKEditor(app)
Bootstrap(app)


def color_to_df(input):
    colors_pre_list = str(input).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]

    # convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                           int(i.split(", ")[1]),
                           int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]

    df = pd.DataFrame(zip(df_color_up, df_percent), columns=['c_code', 'occurence'])
    return df

def pie_chart(input):
    plt.pie(input['occurence'], colors=input['c_code'], labels=input['c_code'],
            autopct='%1.1f%%', pctdistance=0.85)
    time.sleep(30)
    plt.savefig('static/pie-chart.jpg')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=["GET", "POST"])
def upload():
    form = Upload()
    image_list = []
    if form.validate_on_submit():
        image = Image.open(form.file.data)
        image.save("static/new-img.jpg")
        img_url = "static/new-img.jpg"

        # Extract colors from the image:
        colors_x = extcolors.extract_from_path(img_url, tolerance=12, limit=12)

        # Function to extract hexcodes from  the extracted colors:

        # Store values in a data table
        df_color = color_to_df(colors_x)

        # Create pie chart:
        pie_chart(df_color)

        return render_template('color_display.html', form=form)
    return render_template('upload.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)