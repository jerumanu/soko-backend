import unittest
import datetime as dt

from app.main import db
from app.main.model.category_model import CategoryModel
from manage import app

from app.test.base import BaseTestCase


class TestCategoryModel(BaseTestCase):
   def test_new_category(self):
        app.config.from_object('app.main.config.TestingConfig')
        category = CategoryModel("Solar")
        db.session.add(category)
        db.session.commit()
        print(category)
        assert category.name      == "Solar"
        assert category.id        == 1
        assert category.createdAt == dt.datetime(2022, 10, 3, 0, 0)
    

        





if __name__ == '__main__':
    unittest.main()

