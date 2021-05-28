# coding:utf-8

from flask import Blueprint,current_app

# 初始化提供静态文件的蓝图
html = Blueprint('web_html', __name__)


# 127.0.0.1:5000/static/html/auth.html 这样访问并不友好，如何优化成：
# 127.0.0.1:5000/auth.html
# 127.0.0.1:5000/ 主页
# 127.0.0.1:5000/favicon.ico flask默认加载的网站标识

# 在flask如何提取路由参数参数
# <html_file_name> 无法匹配到127.0.0.1:5000/后为空的情况
# 使用自定义路由rex，html_file_name路由变量

@html.route("/<rex(r'.*'):html_file_name>")
def get_html(html_file_name):
    """提供静态文件"""
    # 为空，请求的是主页
    if not html_file_name:
        html_file_name = "index.html"

    # 网站标识，在2.0是失效的
    if html_file_name != 'favicon.ico':
        html_file_name = "html/" + html_file_name

    print(html_file_name)
    return current_app.send_static_file(html_file_name)

