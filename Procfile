# web: gunicorn manage:app

import os
import unittest
from flask_migrate            import Migrate, MigrateCommand
from flask.cli                import FlaskGroup
from app.main                 import create_app, db
from app                      import blueprint


# from app.main.model       import product_model, subscribe_model, comment_model, timming_model
# from app.main.auth.models import user, blacklist

from app.main import create_app, db
from app import blueprint




app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)


app.app_context().push()

cli = FlaskGroup(app)
migrate = Migrate(app, db)

cli.add_command('db', MigrateCommand)



@cli.command
def run():


    app.run(Debug=True)


@cli.command
def test():


    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)


    if result.wasSuccessful():


        return 0


    return 1

if __name__ == '__main__':


    app.run()
