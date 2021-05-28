# coding:utf-8

# 导入蓝图对象
import string
import random
from . import api

from ihome import redis_store
from ihome import constants
from captcha.image import ImageCaptcha

from flask import current_app, jsonify, make_response
from ihome.ultils.response_code import RET


# 127.0.0.1/api/v1.0/image_codes?id=xx
# 定义视图函数
# 用默认的路由转换器
@api.route("/image_codes/<image_code_id>")
def generate_image_code(image_code_id):
    """
    获取图片验证码
    :param image_code_id: 验证码编号
    :return:正常:验证码图片, 异常返回json
    """
    # 业务逻辑处理
    # 生成四位数验证码图片
    image = ImageCaptcha()
    chr_all = string.ascii_letters + string.digits
    text = ''.join(random.sample(chr_all, 4))
    # data = image.generate_image(text)
    out = image.generate(text)
    image_data = out.getvalue()

    # 将图片验证码真实值和编号保存在redis中
    # setex:设置值同时设置有效期
    try:
        redis_store.setex("image_code_%s" % image_code_id, constants.IMAGG_CODE_REDIS_EXPIRE, text)
    # 捕获所有异常
    except Exception as e:
        # 异常处理
        current_app.logger.error(e)
        return jsonify(errno=RET.REQERR, errmsg="save image code failed")

    # 返回图片
    res = make_response(image_data)
    res.headers["Content-Type"] = "image/jpg"
    return res




