import datetime
from flask_script import Manager
from rent import db

from rent import create_app

app = create_app("develop")
manage = Manager(app)


if __name__ == '__main__':

    app.run()