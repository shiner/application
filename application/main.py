import os
from application import app

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

