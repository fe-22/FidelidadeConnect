from waitress import serve
from _init_ import app  # Certifique-se de que 'app' é o nome do seu arquivo principal sem a extensão '.py'

def main():
    serve(app, host='0.0.0.0', port=8000)

if __name__=="_main":
    main()


