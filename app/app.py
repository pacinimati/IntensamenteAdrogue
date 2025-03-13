from flask import Flask, render_template

# cd "c:/Users/matia/OneDrive/Documentos/PROGRAMACION/PAG CONSUL/app"
# python app.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/profesionales')
def profesionales():
    return render_template('profesionales.html')

@app.route('/especialidades')
def especialidades():
    return render_template('especialidades.html')

@app.route('/talleres')
def talleres():
    return render_template('talleres.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)


