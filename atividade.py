import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    email = Column("Email", String)
    idade = Column("Idade", String)
    ra = Column("RA", String)

    def __init__ (self, nome: str, email: str, idade: str, ra: str):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.ra = ra
        
Base.metadata.create_all(bind=db)

for i in range(2):
    ra = input("Digite seu R.A.: ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    idade = input("Digite sua idade: ")

aluno = Aluno(nome="Davi", email="davi@gmail.com", idade="18", ra="012413")
session.add(aluno)
session.commit()

lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.idade} - {aluno.ra}")

# Deletando um usuário
print("\nExcluindo usuário no banco de dados.")
email_aluno = input("Informe o email do aluno: ")
aluno - session.query(Aluno).filter_by(email = email_aluno).first()
session.delete(Aluno)
session.commit()
print("\nEmail apagado com sucesso!")

# Atualizar um usuário
print("\nAtualizando os dados de um usuário: ")

email_aluno = input("Informe o email do aluno: ")

aluno - session.query(Aluno).filter_by(email = email_aluno).first()

print(f"{aluno.id} - {aluno.nome} - {aluno.email}")

# Fechando conexão
session.close()