import os
from controllers import itemPosts, designers, categories, auth
from app import app

app.register_blueprint(itemPosts.api, url_prefix='/api')
app.register_blueprint(designers.api, url_prefix='/api')
app.register_blueprint(categories.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    if os.path.isfile('dist/' + path):
        return app.send_static_file(path)

    return app.send_static_file('index.html')
