from flask import Flask, render_template, url_for, request
from captcha.image import ImageCaptcha
import string
import random
import os

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

    image = ImageCaptcha(fonts=['./static/fonts/Roboto-ThinItalic.ttf'])

    result_str = get_random_string(8)
    n = random.randint(0,41)

    data = image.generate(result_str)

    captcha_filename = 'captcha' + str(n) + '.png'
    captcha_path = './static/img/' + captcha_filename

    if os.path.isfile(captcha_path):
        os.remove(captcha_path)

    image.write(result_str, captcha_path)

    return render_template('./contact.html', page='contact', 
                            captcha_path=captcha_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str