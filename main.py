import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando Banco de dados
# Conexão com o banco de dados
db = create_engine("sqlite:///meubanco.db")

# CREATE DATABASE meubanco
Session = sessionmaker(bind=db)
session = Session()

# I/O
# I = input (Entrada)
# O = output (Saída)

# Abrindo uma conexão

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)

# Salvar no banco de dados
# usuario = Usuário("Davi", "davi@gmail.com", 123)
usuario = Usuario(senha="123", nome="Davi", email="davi@gmail.com")
session.add(usuario)
session.commit()

# Mostrando conteúdo do banco de dados
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")
