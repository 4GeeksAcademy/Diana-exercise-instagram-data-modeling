import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
   
    
class User(Base): 
    __tablename__ = "user"
    ID = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, index=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(30), unique=True, nullable=False)

class Follower(Base):
    __tablename__ = "follower"
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)

class Direct_Message(Base):
    __tablename__ = "direct_message"
    ID = Column(Integer, primary_key=True)
    message_text = Column(String(300), nullable=False)
    sender_id = Column(Integer, ForeignKey('user.ID'), unique=True)
    user = relationship(User)

class Post(Base):
    __tablename__ = "post"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'), unique=True)
    user = relationship(User)


class Comment(Base):
    __tablename__ = "comment"
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship(Post)

class Media(Base):
    __tablename__ = "media"
    ID = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(200))
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship(Post)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
