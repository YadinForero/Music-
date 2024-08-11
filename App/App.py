
from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def gsdg():
    return '¡Hola, Hoy es sabados'

@app.route('/F')
def Fauna():
    return render_template ('Fauna.html')
@app.route('/Fl')
def Flor():
    return render_template ('Flora.html')
  
if __name__ == '__main__':
    app.run(debug=True)