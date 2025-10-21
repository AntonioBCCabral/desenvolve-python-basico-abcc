import csv

# ===================== ESTRUTURAS DE DADOS =====================
usuarios = {}
produtos = []
servicos = []

with open("usuarios.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["username","senha","permissao"])
        writer.writerows(usuarios)

with open("usuarios.csv","a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Antonio","oinotna","gerente"])
        writer.writerow(["Maria","airam","gerente"])
        writer.writerow(["Diva","avid","funcionario"])
        writer.writerow(["Fernando","odnanref","funcionario"])
        writer.writerow(["Oscar","racso","cliente"])
        writer.writerow(["Ronaldo","odlanor","funcionario"])
        writer.writerow(["Helenice","ecineleh","cliente"])
        writer.writerow(["Benicio","oicineb","cliente"])
        writer.writerow(["Goreti","iterog","cliente"])
        writer.writerow(["Guilherme","emrehliug","cliente"])
        writer.writerow(["Marcelo","olecram","cliente"])
        writer.writerow(["Sergio","oigres","cliente"])
        writer.writerow(["Soraya","ayaros","funcionario"])
        writer.writerow(["Edelweiss","ssiewlede","cliente"])

with open("produtos.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["codigo","nome","preco","quantidade"])
    writer.writerow(produtos)

with open("produtos.csv","a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ABC001","Notebook","3500.00","30"])
        writer.writerow(["ABC002","Smartphone","2500.00","50"])
        writer.writerow(["ABC003","Tablet","1500.00","20"])
        writer.writerow(["ABC004","Monitor","800.00","15"])
        writer.writerow(["ABC005","Teclado","150.00","100"])
        writer.writerow(["ABC006","Mouse","100.00","120"])
        writer.writerow(["ABC007","Impressora","600.00","10"])
        writer.writerow(["ABC008","Roteador","200.00","40"])
        writer.writerow(["ABC009","Webcam","300.00","25"])
        writer.writerow(["ABC010","Headset","250.00","35"])
        writer.writerow(["ABC011","Pen-Drive","45.00","45"])

        
# ===================== FUNÇÕES DE ARQUIVO =====================
def carregar_usuarios():
    try:
        with open("usuarios.csv", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuarios[row["username"]] = (row["senha"], row["permissao"])
    except FileNotFoundError:
        print("O arquivo 'usuarios.csv' não foi encontrado.")
    except KeyError as e:
        print(f"Erro: A coluna {e} não existe no arquivo CSV.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def salvar_usuarios():
    with open("usuarios.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["username", "senha", "permissao"])
        for user, (senha, permissao) in usuarios.items():
            writer.writerow([user, senha, permissao])

def carregar_produtos():
    try:
        with open("produtos.csv", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                produtos.append({
                    "codigo": row["codigo"],
                    "nome": row["nome"],
                    "preco": float(row["preco"]),
                    "quantidade": int(row["quantidade"])
                })
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")

def salvar_produtos():
    with open("produtos.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["codigo", "nome", "preco", "quantidade"])
        for p in produtos:
            writer.writerow([p["codigo"], p["nome"], p["preco"], p["quantidade"]])


# ===================== AUTENTICAÇÃO =====================
def login():
    username = input("Usuário: ")
    senha = input("Senha: ")
    if username in usuarios and usuarios[username][0] == senha:
        print(f"Bem-vindo, {username} ({usuarios[username][1]})!")
        return usuarios[username][1]
    else:
        print("Login inválido.")
        return None

# ===================== CRUD USUÁRIOS =====================
def criar_usuario():
    user = input("Novo usuário: ")
    senha = input("Senha: ")
    permissao = input("Permissão (gerente, funcionario, estagiario, cliente): ")
    usuarios[user] = (senha, permissao)
    salvar_usuarios()
    print("Usuário criado com sucesso.")

def listar_usuarios():
    for user, (senha, perm) in usuarios.items():
        print(f"{user} - {perm}")

def atualizar_usuario():
    user = input("Usuário a atualizar: ")
    if user in usuarios:
        nova_senha = input("Nova senha: ")
        nova_perm = input("Nova permissão: ")
        usuarios[user] = (nova_senha, nova_perm)
        salvar_usuarios()
        print("Usuário atualizado.")
    else:
        print("Usuário não encontrado.")

def deletar_usuario():
    user = input("Usuário a remover: ")
    if user in usuarios:
        del usuarios[user]
        salvar_usuarios()
        print("Usuário removido.")
    else:
        print("Usuário não encontrado.")

# ===================== CRUD PRODUTOS =====================
def criar_produto():
    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos()
    print("Produto adicionado.")

def listar_produtos():
    for p in produtos:
        print(f'{p["codigo"]} - {p["nome"]} - R${p["preco"]:.2f} - Qtd: {p["quantidade"]}')

def atualizar_produto():
    codigo = input("Código do produto: ")
    for p in produtos:
        if p["codigo"] == codigo:
            p["nome"] = input("Novo nome: ")
            p["preco"] = float(input("Novo preço: "))
            p["quantidade"] = int(input("Nova quantidade: "))
            salvar_produtos()
            print("Produto atualizado.")
            return
    print("Produto não encontrado.")
def deletar_produto():
    codigo = input("Código do produto a remover: ")
    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            salvar_produtos()
            print("Produto removido.")
            return
    print("Produto não encontrado.")
# ===================== MENU PRINCIPAL =====================
def menu():
    carregar_usuarios()
    carregar_produtos()
    permissao = login()
    if not permissao:
        return

    while True:
        print("\nMenu Principal")
        if permissao == "gerente":
            print("1. Gerenciar Usuários")
            print("2. Gerenciar Produtos")
        elif permissao == "funcionario":
            print("1. Gerenciar Produtos")
        elif permissao == "estagiario":
            print("1. Listar Produtos")
        elif permissao == "cliente":
            print("1. Listar Produtos")
        
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break
        elif escolha == "1":
            if permissao == "gerente":
                gerenciar_usuarios()
            elif permissao in ["funcionario", "estagiario", "cliente"]:
                listar_produtos()
        elif escolha == "2" and permissao == "gerente":
            gerenciar_produtos()
        else:
            print("Opção inválida.")
def gerenciar_usuarios():
    while True:
        print("\nGerenciar Usuários")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("0. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break
        elif escolha == "1":
            criar_usuario()
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            atualizar_usuario()
        elif escolha == "4":
            deletar_usuario()
        else:
            print("Opção inválida.")
def gerenciar_produtos():
    while True:
        print("\nGerenciar Produtos")
        print("1. Criar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("0. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break
        elif escolha == "1":
            criar_produto()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            deletar_produto()
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    menu()
    
    def _corrigir_estruturas_e_recarregar():
        global produtos, usuarios
        # garantir tipos corretos
        if not isinstance(produtos, list):
            produtos = []
        if not isinstance(usuarios, dict):
            usuarios = {}
        # recarregar arquivos (caso não tenham sido carregados corretamente antes)
        carregar_usuarios()
        carregar_produtos()

    # Pergunta ao usuário se deseja reiniciar o menu com as estruturas corrigidas
    try:
        escolha = input("Corrigir estruturas e reiniciar menu se necessário? (s/n): ").strip().lower()
    except EOFError:
        escolha = "n"

    if escolha == "s":
        _corrigir_estruturas_e_recarregar()
        menu()