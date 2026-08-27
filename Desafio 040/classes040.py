import xml.etree.ElementTree as ET

from openpyxl.descriptors import String


class Aluno:
    def __init__(self, nome:str = "<empty>", curso:str = "<empty>", serie:int = 0):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class Usuario:
    def __init__(self, nome:str = "<empty>", email:str = "<empty>"):
        self.nome = nome
        self.email = email

class JSON:
    def exportar(self, classe):
        pass

class XML:
    def exportar(self, lista):
        root = ""

        if lista[0].__class__.__name__ == "Usuario":
            # Criar a tag principal <usuarios> -------------------------------------------------------------------
            root = ET.Element("usuarios")

            for u in lista:
                # criando tag <usuario> para cada usuario na lista passada---------------------------------------
                elemento_u = ET.SubElement(root, "usuario")

                # criando tags dos dados e seus valores-----------------------------------------------------------
                ET.SubElement(elemento_u, "nome").text = u.nome
                ET.SubElement(elemento_u, "email").text = u.email

        elif lista[0].__class__.__name__ == "Aluno":
            # Criar a tag principal <alunos> -------------------------------------------------------------------
            root = ET.Element("alunos")

            for a in lista:
                # criando tag <aluno> para cada aluno na lista passada---------------------------------------
                elemento_a = ET.SubElement(root, "aluno")

                # criando tags dos dados e seus valores-----------------------------------------------------------
                ET.SubElement(elemento_a, "nome").text = a.nome
                ET.SubElement(elemento_a, "curso").text = a.curso
                ET.SubElement(elemento_a, "serie").text = str(a.serie)

        # Criando arquivo XML
        tree = ET.ElementTree(root)
        ET.indent(tree, space="     ")  # indentação
        tree.write(f"{lista[0].__class__.__name__}s.xml", encoding="utf-8", xml_declaration=True)

        with open(f"{lista[0].__class__.__name__}s.xml", "r", encoding="utf-8") as arquivo:
            print(arquivo.read())

# DUCK TYPING -----------------------------------------------------------------------------------------------
def exportar_dados(lista, tipo):
    tipo.exportar(lista)
