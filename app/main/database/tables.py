from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(16), nullable=False)
    password = Column(String(200), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)


    def set_password(self, password):
        '''Create hashed password.'''
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def check_password(self, password):
        '''Check hashed password.'''
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
