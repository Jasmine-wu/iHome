# coding:utf-8

import redis
import datetime

class Config():

    # DEBUG = True
    SECRET_KEY='13333xxxxx4444444'

    # 数据库
    SQLALCHEMY_DATABASE_URI='mysql://root:changsha123@127.0.0.1:8888/ihome_python04'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST='127.0.0.1'
    REDIS_PORT= 6379

    # flask-session配置，将session保存在redis中
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'lqz'
    SESSION_REDIS =redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 对session id进行隐藏显示
    SESSION_USE_SIGNER=True
    # 设置session有效期
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7)

class DevelopementConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    pass

# 构建映射关系
config_map = {
    "develop": DevelopementConfig,
    "product": ProductConfig

}