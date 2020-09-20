from flask import Flask, render_template, url_for, request
import string
import random
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html', page='frontpage')

@app.route('/contact')
def contact():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        captcha = request.form["captcha"]


    captcha_str = get_random_string(8)
    n = random.randint(0,41)

    captcha_filename = 'captcha' + str(n) + '.png'
    captcha_path = './static/captcha/' + captcha_filename

    if os.path.isfile(captcha_path):
        os.remove(captcha_path)

    generate_new_captcha(captcha_str, captcha_path)

    return render_template('./contact.html', page='contact', 
                            captcha_path=captcha_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Random color 1:
def rand_color_one():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

# 2:
def rand_color_two():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

def generate_new_captcha(text, path):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # Create a Font object:
    font = ImageFont.truetype("./static/fonts/NotoSansGurmukhi-Regular.ttf", 50)

    # Create a Draw object:
    draw = ImageDraw.Draw(image)

    # Fill each pixel:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rand_color_one())

    # Output text:
    for t in range(4):
        draw.text((60 * t + 10, 10), text, font=font, fill=rand_color_two())

    # blurry:
    image = image.filter(ImageFilter.BLUR)
    image.save(path, 'png')