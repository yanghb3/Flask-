## 配置数据库
HOSTNAME = '82.157.254.237'
PORT = '3306'
DATABASE = 'flask_test'
USERNAME = 'root'
PASSWD = 'Yang200371.'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI =DB_URI


## 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_TLS = True
MAIL_PORT = 25
MAIL_USERNAME = '3242950010@qq.com'
MAIL_PASSWORD = 'vvanaqdtslexchdh'
MAIL_DEFAULT_SENDER = '3242950010@qq.com'

SECRET_KEY='abihibhkdu_hizbkw'