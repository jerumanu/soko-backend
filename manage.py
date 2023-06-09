import os
import unittest
from flask_migrate        import Migrate, MigrateCommand
from app.main                 import create_app, db
from app                      import blueprint
from app.main.ecommerce.views.home_view import home
from flask_script import Manager
from app.main.ecommerce.views.ratings import rate



app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.register_blueprint(home)
app.register_blueprint(rate)
app.app_context().push()



manager = Manager(app)
migrate = Migrate(app, db, command='migrate')

manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)



@manager.command
def run():
    app.run(host='127.0.0.1', port=8080, debug=False)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()



