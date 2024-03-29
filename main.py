from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
  <!DOCTYPE html>

<html>
    <head>
        <style>

            input {{
                display:inline-block;
            }}

            label {{
                display:inline-block;
            }}

            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method = "POST">
            <label for="rot" ><h3>Rotate by:</h3></label>
            <input type="text" name="rot" value="0" id="rot"/>
            <textarea name="text" rows="5" col="30">{0}</textarea>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/" , methods=["POST"])
def encrypt():
    text = request.form['text']
    rot = int(request.form["rot"])
    rotated_string = rotate_string(text, rot)
    return form.format(rotated_string)


app.run()    
