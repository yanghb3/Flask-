from flask import Flask
from exts import db
from blueprint.cms import bp as cms_bp
from blueprint.front import bp as front_bp
from blueprint.users import bp as user_bp
import config

app = Flask(__name__)
app.config.from_object(config)

#注册数据库对象
db.init_app(app)

#注册蓝图
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
