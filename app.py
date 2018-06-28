import base64
from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/saveImg64DataAsImageFile/', methods=['GET', 'POST'])
# Function for retrieving all the added items:
def saveImg64DataAsImageFile():
    #with open("imageToSave.png", "wb") as fh:
    #    return ";>"

    if request.method == 'GET':
        return render_template('load_and_resize_picture.html')
    else:
        image_64_encode = (str(request.form['id2'])[23:])

        imgstring = image_64_encode # the full string goes here
        imgdata = base64.b64decode(imgstring)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        return render_template('image_saved.html')
