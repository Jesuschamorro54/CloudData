import os
from flask import Flask  
from views import main

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom( 50 )



app.register_blueprint(main)

#if __name__ == '__main__':
#    app.run()