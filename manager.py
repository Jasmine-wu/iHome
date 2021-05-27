import datetime
from flask_script import Manager
from ihome import create_app
from flask_migrate import Migrate,MigrateCommand
from ihome import db


# 创建应用对象
app = create_app("develop")
manage = Manager(app)

# 数据库迁移
Migrate(app, db)

# 添加数据库迁移指令
manage.add_command("db",MigrateCommand)


if __name__ == '__main__':

    manage.run()