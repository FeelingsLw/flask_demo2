from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps import app
from apps.model import db

migrate = Migrate(app, db)
manger = Manager(app)
# 注释下
manger.add_command('db', MigrateCommand)

'''

# 初始化映射仓库 （第一次用）
python manager.py db  init
# 生成映射脚本
python manager.py db migrate
# 映射数据库
python manager.py db upgrade

'''

if __name__ == '__main__':
    manger.run()
