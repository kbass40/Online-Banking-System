import Apple

app = Apple.app

#gunicorn automatically searches for the app var and binds
#an address to it

if __name__ == '__main__':
    app.run(host='0.0.0.0')
