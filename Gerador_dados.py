import pandas as pd
from faker import Faker
from datetime import date

#criar dados aleatorios 
fake = Faker('pt_BR')
dados = []

for _ in range(300):
    nome_completo = fake.name()
    endereco_completo = fake.address()
    cpf = fake.cpf()
    ano_atual = date.today().year
    start_date = date(ano_atual, 1, 1)
    end_date = date.today()
    data_aleatoria = fake.date_between(start_date=start_date, end_date=end_date)
    data_formatada = data_aleatoria.strftime('%d/%m/%Y')
    
    dados.append([nome_completo, endereco_completo, cpf, data_formatada])

# Cria um DataFrame com os dados
df = pd.DataFrame(dados, columns=['Nome', 'Endereço', 'CPF', 'Data de Admissão'])

# Salva o DataFrame em um arquivo Excel
df.to_excel(r'C:\Users\Usuário\Documentos\Cadastro_funcionarios\Informacoes.xlsx', index=False)
