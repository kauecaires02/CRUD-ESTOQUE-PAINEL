# CRUD-ESTOQUE-PAINEL
Debbug
class Estoque: Itens = {} def incluir(self,codigo,desc,preco): if codigo not in self.itens: self.itens[codigo]={"descricao":desc,"preco":preco}

else: print("Codigo cadastrado")

def alterar(self,codigo,preco): if codigo in self.itens: self.itens[codigo]["preco"]=preco

else: print("codigo nao ta na base")

def excluir(self,codigo): if codigo in self.itens: self.itens.pop.(codigo) else: print ("cod inexistente")

def listar(self): print("") for codigo in self.itens: print(codigo,self,itens[codigo]["descricao"],self.itens[codigo]["preco"]) print("***")

e = estoque()

sair = False

while not sair:
  os.system("clear")
  print("""
  +--------------------+
  | SISTEMA DE ESTOQUE |
  +--------------------+
  |       <MENU>       |
  +--------------------+
  |     (I)ncluir      |
  |     (A)lterar      |
  |     (E)xcluir      |
  |     (L)istar       |
  |     (S)air         |         +--------------------+   
        """)
  op = include("selecione uma opcao: ").upper()

if op == "S":
  sair = True

elif op == "I":
codigo = input("codigo: ")descricao = input("Descricao: ")
preco = input("preco: ")
e.incluir(codigo,descricao,float(preco))

elif op == "A":
codigo = input("codigo: ")
preco = input("preco: ")
e.alterar(codigo,preco)
input("<ENTER> para continuar")


elif op == "E":
codigo = input("codigo: ")
e.alterar(codigo,preco)
inpput("<ENTER> para continuar")

elif op == "L":
os.system('clear')
e.listar()
input("<ENTER> para continuar")
