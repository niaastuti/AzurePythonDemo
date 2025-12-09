from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Halo dari Aplikasi Python PaaS Pertama Saya!</h1><p>Deployment Sukses ke Azure App Service.</p>'

if __name__ == '__main__':
    app.run()