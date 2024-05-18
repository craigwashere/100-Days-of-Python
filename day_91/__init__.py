#flask --app main --debug run
#https://www.geeksforgeeks.org/how-to-upload-file-in-python-flask/

from flask import *
import os
from PIL import Image # for reading image files
import base64
import io

app = Flask(__name__)

def get_colors(im):
    colors = im.getcolors(im.size[0]*im.size[1])
    colors.sort(reverse=True)
    return colors[:10]
    
@app.route('/', methods = ['GET', 'POST'])
def main():
    global f
    colors = None;
    encoded_img_data = None;
    file_name = None
    if request.method == 'POST':
        f = request.files['file']
        im = Image.open(f.stream)
        colors = get_colors(im)
        
        data = io.BytesIO()
        im.save(data, "PNG")
        encoded_img_data = base64.b64encode(data.getvalue()).decode('utf-8')
        
        file_name = f.filename
    return render_template("index.html", file=encoded_img_data, colors=colors, filename=file_name)
            
if __name__ == '__main__':
	app.run(debug=True)

