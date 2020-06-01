# coding:UTF-8

"""使用SQLAlchemy实现ORM技术，Object-Relational Mapping"""
# https://blog.csdn.net/q370835062/article/details/84974951?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1

# 导入:
from sqlalchemy import Table, Column, String, Integer, create_engine, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 连接数据库,echo 参数为 True，程序运行时调试信息会打印出来
engine = create_engine('mysql+mysqlconnector://root:rootroot@localhost:3306/test', echo=True)

# 绑定引擎(第二种创建表方式)
metadata = MetaData(engine)

# 创建基类
Base = declarative_base()


# 定义User类
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

    def __str__(self):
        return "%s %s" % (self.id, self.name)

    __repr__ = __str__


class Manager(Base):
    __tablename__ = 'manager'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), ForeignKey('uesr.name'))

    def __str__(self):
        return "%s %s" % (self.id, self.name)

    __repr__ = __str__


# # 创建表
# Base.metadata.create_all(engine)
# Base.metadata.drop_all()

# 创建表(第二种创建表方式)
metadata.create_all()


def connect_db_table():
    # 连接数据库的这个表，打开之后可以进行增加行，约束等操作
    user_table = Table('user', metadata, autoload=True)
    # # 增加约束
    # user_table.append_constraint()

    # 如果 MetaData 没有绑定引擎，则另需指定 autoload_with 参数
    user_table1 = Table('user', metadata, autoload=True, autoload_with=engine)


def session_connect():
    # 创建会话
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # user = User(id=1, name='joey')
    # manager = Manager(id=1, name='joey')
    user = User(name='joey')
    manager = Manager(name='joey')
    # 增加数据
    session.add(user)
    session.add(manager)
    # session.add([user, manager])
    session.commit()

    # 查询数据
    user_result = session.query(User).filter(User.id == 1).one()
    allresult = session.query(User).all()
    # allresult = session.query(User).first()///.order_by(User.id)
    print('allresult:', allresult)
    print('type:', type(user_result))
    print('name:', user_result.name)

    # 删除数据
    del_result = session.query(User).first()
    session.delete(del_result)
    session.commit()

    # 修改数据
    alter_result = session.query(User).first()
    alter_result.name = 'joey1'
    print(session.dirty)  # 显示修改的内容
    session.commit()

    session.close()
