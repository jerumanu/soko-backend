from  ....main import db
from typing import List
import datetime as dt

class BlogModel(db.Model):
    __tablename__ = "blog"

    id          = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    text        = db.Column(db.String(255), nullable=False)
    title       = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    blog_img    = db.Column(db.String)
    createAt    = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())
    author      = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # comments    = db.Column()

    def __init__(self, title, text, description):
        self.createAt    = dt.datetime.now()
        self.title       = title
        self.text        = text
        self.description = description

    def __repr__(self) -> str:
        return 'Blog(name=%s)' % self.title

    @classmethod
    def find_all(cls) -> List["BlogModel"]:
        return cls.query.all()