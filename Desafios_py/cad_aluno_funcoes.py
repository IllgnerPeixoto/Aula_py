class Aluno:
    def __init__(self, nome, matricula, curso = "", dataNascimento = ""):
        self._nome = nome
        self._matricula = matricula
        self._curso = curso
        self._dataNascimento = dataNascimento

@property
def nome(self):
    print(self._nome)

@property 
def matricula(self):
   return self._matricula
