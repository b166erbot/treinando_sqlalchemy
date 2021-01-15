from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///banco.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class Pessoa(Base):
    __tablename__ =  'pessoas'

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(Integer)

    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade = {self.idade})"


Base.metadata.create_all(engine)
