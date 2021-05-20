import sqlalchemy.exc

from app import db
from datetime import datetime
from json import dumps
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s).lower()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tg_id = db.Column(db.String(15), unique=True)
    subscription = db.Column(db.Integer, default=0)
    registration = db.Column(db.DateTime, default=datetime.now())
    success = bool()

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def commit(self):
        """
        Void function. Required to save the update on the server.
        :return: Void
        """
        try:
            db.session.commit()
            self.success = True
        except:
            self.success = False
            # raise Exception("Commit failed")

    def create(self, tg_id=None, subscription=None):
        """
        Create new user.
        :param tg_id:
        :param subscription:
        :return: dict{'id', 'tg_id', 'subscription'}
        """
        if tg_id:
            self.tg_id = tg_id
        db.session.add(self)
        self.commit()
        return {'id': self.id, 'tg_id': self.tg_id, 'subscription': self.subscription}

    def update(self, tg_id=None, subscription=None):
        """
        Update user data(tg_id or subscription).
        :param tg_id:
        :param subscription:
        :return: Void
        """
        if tg_id:
            self.tg_id = tg_id
        if subscription:
            self.subscription = subscription
        self.commit()

    def get_user(self, user_id=None, tg_id=None):
        """
        get_user by id or tg_id.
        :param user_id:
        :param tg_id:
        :return: dict{'id', 'tg_id', 'subscription'}

        """
        try:
            if user_id:
                self.id = user_id
                # user = Users.query.filter(Users.id == self.id).one()
            elif tg_id:
                self.tg_id = tg_id
                user = Users.query.filter(Users.tg_id == self.tg_id).one()
            else:
                return dict()
            self.success = True
        except sqlalchemy.exc.NoResultFound:
            self.success = False

        if self.success:
            self.id = user.id
            self.tg_id = user.tg_id
            self.subscription = user.subscription

        return {'id': self.id, 'tg_id': self.tg_id, 'subscription': self.subscription}

    def get_json(self):
        """
        Get user data in json format.
        :return: dict{'id', 'tg_id', 'subscription'}
        """
        return {'id': self.id, 'tg_id': self.tg_id, 'subscription': self.subscription}

    def __repr__(self):
        return "<User id: {}, tg_id: {}, subscription: {}>".format(self.id, self.tg_id, self.subscription)



class Site(db.Model):
    """
    Column:
        id         : page id            \n
        member_id  : page member id     \n
        slug       : page url           \n
        style      : css style name     \n
        pattern    : HTML pattern name  \n
        title      : page title  (str)  \n
        head       : page head   (str)  \n
        body       : page body   (dict) \n
        side_bar   : side bar    (list) \n
        create     : date of create     \n
        last_update: date of last update\n
    """
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    slug = db.Column(db.String(50), unique=True)
    style = db.Column(db.String(50))
    pattern = db.Column(db.String(50))
    title = db.Column(db.String(140))
    head = db.Column(db.String(250))
    body = db.Column(db.String(2500))
    side_bar = db.Column(db.String(2500))
    photo1 = db.Column(db.String(140))
    photo2 = db.Column(db.String(140))
    create = db.Column(db.DateTime, default=datetime.now())
    last_update = db.Column(db.DateTime, default=datetime.now())
    raw_body = dict()
    raw_side_bar = list()

    def __init__(self, *args, **kwargs):
        super(Site, self).__init__(*args, **kwargs)
        self.generate_slug()
        self.generate_body()
        self.generate_side()

    def generate_slug(self):
        """
        This function generate URL
        :return: Void
        """
        if self.title:
            self.slug = slugify(self.title)
    
    def generate_body(self):
        '''
        Transformate array to string-json. Required to saving to the DB.
        :return: Void
        '''
        if self.raw_body:
            self.body = dumps(self.raw_body)

    def generate_side(self):
        '''
        Transformate array to string-json. Required to saving to the DB.
        :return: Void
        '''
        if self.raw_side_bar:
            self.side_bar = dumps(self.raw_side_bar)

    def commit(self):
        db.session.commit()

    def __repr__(self):
        return 'Site id: {}, member: {}, title: {}>'.format(self.id, self.member_id, self.title)

