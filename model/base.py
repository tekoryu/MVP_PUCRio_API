"""
File: base.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Anchor to call all models?
"""

from sqlalchemy.ext.declarative import declarative_base

# cria uma classe Base para o instanciamento de novos objetos/tabelas
Base = declarative_base()
