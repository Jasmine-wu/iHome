# coding:utf-8
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
from ihome.ultils.commons import ReConverter

import pymysql


# 数据库
db = SQLAlchemy()

# 为了方便外部调用
# 创建redis连接对象
redis_store = None

def create_app(config_name):
    """
    :param config_name: 创建app类型的类型名（"develpo","product"）
    :return:
    """
    # 替换默认的数据驱动MySQLdb为pymysql
    # MySQLdb支持python2
    pymysql.install_as_MySQLdb()

    # static_url_path='/static' ,static_folder='static'默认
    app = Flask(__name__)

    # 根据映射关系给app配置不同环境的config
    config_class = config_map[config_name]
    app.config.from_object(config_class)

    #  创建数据库
    db.init_app(app)

    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 用flask-sesison将session保存在redis中
    Session(app)

    # 为flask添加csr防护(只是添加防护，还未设置csr_token值)
    CSRFProtect(app)

    # 为flask添加自定义的正则转换器rex
    app.url_map.converters['rex'] = ReConverter


    # 注册蓝图
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')

    from ihome import web_html
    app.register_blueprint(web_html.html)

    return app



