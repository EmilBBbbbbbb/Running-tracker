from sqlalchemy import Column, Integer, String

from user_info.models.database import Base


# Table for storing user information

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return (f'User [ID: {self.id} '
                f', Name: {self.name}, '
                f'E-mail: {self.email}], '
                f'Password: {self.password}')
