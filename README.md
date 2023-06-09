# Gerador-de-dados_backup
**Gerador de dados ficticios**<br />
Criar uma base de dados ficticios para simulação:
- Utilização da bibliotca Faker com a localização definida como 'pt_BR' para gerar dados aleatórios como nome, endereço completo, CPF e data de admissão;
- Um loop, que será executado de acordo com a quantidadde de vezes que desejar, os dados são gerados aleatoriamente para cada iteração;
- A data aleatória é gerada utilizando o método fake.date_between() do Faker, que recebe uma data de início e fim. Nesse caso, a data de início é definida como 1º de janeiro do ano atual e a data de fim é definida como a data atual;
- A data aleatória é formatada para o padrão 'dd/mm/aaaa' utilizando o método strftime();
- Os dados gerados para cada iteração são armazenados em uma lista dentro da lista "dados";
- Por fim, é criado um DataFrame chamado utilizando o pandas, com as colunas definidas como ['Nome', 'Endereço', 'CPF', 'Data de Admissão'] e os dados gerados anteriormente.
- O DataFrame é salvo em um arquivo Excel utilizando o método to_excel() do pandas e o parâmetro index=False é usado para não incluir o índice do DataFrame no arquivo Excel.

**Tabela filtrada**<br />
Objetivo de criar uma planilha com os dados filtrados criando um backuo para deixar a planilha original menos pesada de informações:
- Carrega uma planilha original no formato Excel.
- Filtra os dados com base em uma data limite.
- Gera uma nova planilha com os dados filtrados.
- Preserva a formatação original dos dados.
- Salva a nova planilha com um nome correspondente à data atual.
