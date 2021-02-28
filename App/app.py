from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/testing')
    def testing():
        return 'This is only a test'

    return app

if __name__ == '__main__':
    application = create_app()
    application.run()
