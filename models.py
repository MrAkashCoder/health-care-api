from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'tblpost'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    short_description = Column(Text)
    description = Column(Text)
    category_id = Column(Integer)
    author_id = Column(Integer)
    date = Column(Date)
    viewer_count = Column(Integer)
    comments = Column(Text)
    image_URL = Column(Text)
    tags = Column(Text)
    post_url = Column(Text)
    # user_id = Column(Integer, ForeignKey('users.id'))

    # creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'tblusers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    email = Column(Text)
    password = Column(Text)

    # blogs = relationship("Blog", back_populates="creator")
    