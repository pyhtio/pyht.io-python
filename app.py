from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
  return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>pyht.io</title>
    </head>
    <body>
        <h1>pyht.io</h1>
        <p>you have reached pyht.io</p>
        <p>This site is under construction.</p>
    </body>
    </html>
'''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8001)
