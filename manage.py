from app import create_app, db
from flask_script import Manager, Server
from app.models import Comment

# Creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    print(Comment)
    return dict(db=db,Comment=Comment)


if __name__ == '__main__':
    manager.run()
