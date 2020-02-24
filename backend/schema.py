"""Esquemas de classes e banco de dados do sistema."""
from pydantic import BaseModel


class Pesquisa(BaseModel):
    """
    classe que mantém as informações de busca dos elementos no banco de dados.

    atributos: sigla, nome.
    """

    sigla: str
    nome: str
    familia: str


class Elemento():
    """
    Representacao de um elemento.

    atributos: nome, sigla, atomico, m_molar.
    """

    def __init__(self, sigla: str, nome: str, familia: str, atomico: int,
                 m_molar: float):
        """Inicializa a classe que mantém os dados de elementos."""
        self.sigla = sigla
        self.nome = nome
        self.familia = familia
        self.atomico = atomico
        self.m_molar = m_molar

    def __str__(self):
        """Padroniza a saída de string da classe."""

        return '{} {}\nFamilia: {}\nNumero atomico: {}\nMassa Molar {}'.\
            format(self.sigla, self.nome, self.familia,
                   self.atomico, self.m_molar)
