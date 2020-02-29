import click
from blog import db,app
from blog.models import User,Ariticles
# 自定义initdb
@app.cli.command()
@click.option('--drop',is_flag=True,help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')

# 自定义命令forge，把数据写入数据库
@app.cli.command()
def forge():
    db.create_all()
    name = "Bruce"
    ariticles = [
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'},
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'},
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'},
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'},
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'},
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'},
        {'title':'如何防治蝗灾','content':'xxxxxxxxx','author':'晓红'}
    ]
    user = User(name=name)
    db.session.add(user)
    for m in ariticles:
        ariticle = Ariticles(title=m['title'],content=m['content'],author=m['author'])
        db.session.add(ariticle)
    db.session.commit()
    click.echo('数据导入完成')

# 生成admin账号的函数
@app.cli.command()
@click.option('--username',prompt=True,help="用来登录的用户名")
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True,help="用来登录的密码")
def admin(username,password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户')
        user = User(username=username,name="雷洛")
        user.set_password(password)
        db.session.add(user)
    
    db.session.commit()
    click.echo('创建管理员账号完成')