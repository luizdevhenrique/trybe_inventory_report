# Inventory Report

Neste projeto, foi desenvolvido um gerador de relatórios. O objetivo é receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque poderão ser obtidos de duas fontes:

Através da importação de um arquivo CSV;

Através da importação de um arquivo JSON;

## Testes

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.
O arquivo pyproject.toml já configura corretamente o pytest.

```bash
python3 -m pytest
```


1. Crie o ambiente virtual para o projeto

-   `python3 -m venv .venv && source .venv/bin/activate`

2. Instale as dependências

-   `python3 -m pip install -r dev-requirements.txt`

### 1. Teste do construtor/inicializador do objeto Produto

> **Teste em:** `tests/product/test_product.py`

<details>

**<summary>Teste se o construtor do objeto <code>Product</code> contém os atributos corretos.**

</summary>

O nome deste teste deve é `test_create_product` e ele verifica o correto preenchimento dos seguintes atributos:

-   `id`
-   `company_name`
-   `product_name`
-   `manufacturing_date`
-   `expiration_date`
-   `serial_number`
-   `storage_instructions`

**O que é testado:**

-   **1.1** - Se o teste valida que o atributo `id` existe na classe e é igual ao passado pelo construtor.
-   **1.2** - Se o teste valida que o atributo `company_name` existe na classe e é igual ao passado pelo construtor.
-   **1.3** - Se o teste valida que o atributo `product_name` existe na classe e é igual ao passado pelo construtor.
-   **1.4** - Se o teste valida que o atributo `manufacturing_date` existe na classe e é igual ao passado pelo construtor.
-   **1.5** - Se o teste valida que o atributo `expiration_date` existe na classe e é igual ao passado pelo construtor.
-   **1.6** - Se o teste valida que o atributo `serial_number` existe na classe e é igual ao passado pelo construtor.
-   **1.7** - Se o teste valida que o atributo `storage_instructions` existe na classe e é igual ao passado pelo construtor.

</details>

### 2. Teste do relatório individual gerado por Produto

> **Teste em:** `tests/product_report/test_product_report.py`

<details>

**<summary>Testa se o "método mágico" <code>**str**</code> do objeto <code>Product</code> retorna a frase correta.**

</summary>

Já foi implementado o primeiro relatório no arquivo `inventory_report/product.py`, e também foi criada uma frase com as informações do produto, que será útil para etiquetar o estoque. Para desenvolver esse relatório, utilizamos o método `__str__` do Python, que é chamado quando utilizamos a função `str(objeto)`.

Exemplo da frase:

**Trecho 1:** _The product `farinha`,_
**Trecho 2:** _with serial number `TY68 409C JJ43 ASD1 PL2F`,_
**Trecho 3:** _manufactured in `01-05-2021`_
**Trecho 4:** _by the company `Farinini`,_
**Trecho 5:** _valid until `02-06-2023`,_
**Trecho 6:** _must be stored according to the following instructions: `precisa ser armazenado em local protegido da luz`._

O nome do teste é `test_product_report`. Ele instancia um objeto `Product` e verifica se a frase retornada está correta.

**O que será testado:**

-   **2.1** - Se o teste verifica se o Trecho 1 do relatório está correto no texto base e no dado inserido nele.
-   **2.2** - Se o teste verifica se o Trecho 2 do relatório está correto no texto base e no dado inserido nele.
-   **2.3** - Se o teste verifica se o Trecho 3 do relatório está correto no texto base e no dado inserido nele.
-   **2.4** - Se o teste verifica se o Trecho 4 do relatório está correto no texto base e no dado inserido nele.
-   **2.5** - Se o teste verifica se o Trecho 5 do relatório está correto no texto base e no dado inserido nele.
-   **2.6** - Se o teste verifica se o Trecho 6 do relatório está correto no texto base e no dado inserido nele.

</details>

### 3. Cria a Interface `Importer`

> **Criado em:** `inventory_report/importers.py`

<details>

**<summary>Cria a classe abstrata <code>Importer</code> com o inicializador implementado e com o método abstrato <code>import_data</code>.**

</summary>
  <br />

Como já temos o arquivo com os produtos, precisamos importar os dados. Em razão dos diversos formatos e para não repetir lógica, criei uma classe abstrata que será responsável por definir como as classes importadoras dos dados dos arquivos serão.

Para isso, criei uma classe abstrata chamada `Importer`, contém um método chamado `import_data`, que recebe o caminho do arquivo e retorna uma lista de produtos:

**O que é testado:**

-   **3.1** - Se a classe `Importer` é abstrata;
-   **3.2** - Se o método `__init__` não é abstrato;
-   **3.3** - Se o método `__init__` recebe `self` e `path`;
-   **3.4** - Se o tipo do `path` é `str`;
-   **3.5** - Se o método `import_data` é abstrato;
-   **3.6** - Se o método `import_data` recebe `self`;
-   **3.7** - Se o método `import_data` retorna uma lista de produtos;

</details>

### 4. Cria a classe `JsonImporter`

> **Criado em:** `inventory_report/importers.py`

<details>

**<summary>Cria a classe <code>JsonImporter</code> que herda de <code>Importer</code> e implemente o método <code>import_data</code> para ler um arquivo JSON.**

</summary>
  <br />

Agora que temos a interface, criei a classe que irá implementar o método `import_data` para ler um arquivo JSON. Para isso, criei uma classe chamada `JsonImporter`, herda da classe `Importer` e implementa o método `import_data`. Esse método, por sua vez, recebe o caminho do arquivo e retorna uma lista de produtos. A lista é retornada como no formato abaixo:

```
[
  Product(
    id='1',
    product_name='Nicotine Polacrilex',
    company_name='Target Corporation',
    manufacturing_date='2021-02-18',
    expiration_date='2024-09-17',
    serial_number='CR25 1551 4467 2549 4402 1',
    storage_instructions='instrucao 1'
  ),

  Product(
    id='2',
    product_name='fentanyl citrate',
    company_name='Target Corporation',
    manufacturing_date='2020-12-06',
    expiration_date='2024-12-25',
    serial_number='FR29 5951 7573 74OY XKGX 6CSG D20',
    storage_instructions='instrucao 2'
  ),
  // ...
]
```

**O que é testado:**

-   **4.1** - Se a classe `JsonImporter` herda de `Importer`.
-   **4.2** - Se o método `import_data` importa corretamente um arquivo JSON válido.
-   **4.3** - Se o método `import_data` exporta os dados do JSON importado no formato apropriado.

</details>

### 5. Cria a classe `Inventory`

> **Criado em:** `inventory_report/inventory.py`

<details>

**<summary>Criada a classe <code>Inventory</code> que armazenará o estoque e poderá adicionar itens a ele.**

</summary>
  <br />

Com o nosso importador de dados feito, foi criada a classe que representa um estoque para, a partir dele, gerar o nosso relatório! Atenção para as especificações:

-   A classe `Inventory` deve poder ser instanciada, de forma opcional, com uma lista de produtos.
-   Caso a lista não seja fornecida, a lista da instância deve ser inicializada como vazia.
-   A classe deve conter um método chamado `add_data`, que recebe uma lista de produtos e adiciona todos os produtos à lista de produtos da instância.
-   Além disso, a classe deve ter uma propriedade chamada `data`, que deve ser somente leitura e retornar uma cópia da lista de produtos da instância.

**O que é testado:**

-   **5.1** - Se o inicializador recebe dois parâmetros: `self` e `data`.
-   **5.2** - Se `data` tem a anotação de tipo `List[Products]` e é opcional.
-   **5.3** - Se `data` tem o valor padrão `None`.
-   **5.4** - Se `data` é inicializado com uma lista vazia quando o valor padrão é usado.
-   **5.5** - Se `data` recebe uma lista de produtos.
-   **5.6** - Se `data` é uma propriedade somente de leitura.
-   **5.7** - Se `add_data` recebe uma lista de produtos.
-   **5.8** - Se `add_data` adiciona todos os produtos da lista de produtos recebida por parâmetro à lista de produtos da instância.

</details>

### 6. Cria o protocolo `Report`

> **Criado em:** `inventory_report/reports/report.py`

<details>

**<summary>Criado o protocolo <code>Report</code>, que deverá ser usado como contrato dos relatórios <code>simple</code> e <code>complete</code>.**

</summary>
  <br />

Feita nossa classe de inventário, vamos usá-la para criar nossos relatórios! Visto que teremos dois formatos dele, primeiro criamos um contrato para todos os formatos respeitarem. Usaremos um protocolo para isso. Atenção à especificação:

-   No protocolo `Report` existe um método chamado `add_inventory` recebendo um parâmetro `inventory`, do tipo `Inventory`, classe criada no quinto requisito.

-   Há um método chamado `generate` que retorna uma string.

**O que é testado:**


-   **6.1** - Se `add_inventory` recebe dois parâmetros: `self` e `inventory`.
-   **6.2** - Se `inventory` tem a anotação de tipo `Inventory`.
-   **6.3** - Se `generate` recebe `self`.
-   **6.4** - Se `generate` tem um retorno do tipo `str`.

</details>

### 7. Cria o relatório `SimpleReport`

> **Cria a classe em:** `inventory_report/reports/simple_report.py`

<details>

**<summary>Cria a classe <code>SimpleReport</code> que implementa os métodos <code>add_inventory</code> e <code>generate</code> do protocolo <code>Report</code>.**

</summary>
  <br />

A classe `SimpleReport` inicializa sem parâmetros, contudo, tem um atributo para armazenar cada um dos estoques que podem ser adicionados.

O método `add_inventory` segue o contrato do protocolo `Report` e é capaz de adicionar um estoque ao atributo que armazena cada um dos estoques.

O método `generate` é capaz de gerar o relatório a partir dos produtos que estão presentes em cada um dos estoques armazenados. Atenção às especificações:

-   Ao rodar os testes localmente, você terá um teste para cada validação de cada informação presente no relatório;
-   O método `add_inventory` recebe um parâmetro que representa um `Inventory`, classe implementada no quinto requisito.
-   O método `generate` retorna uma `string` de saída com o seguinte formato:

```txt
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
```

-   A data de validade mais próxima considera somente itens que ainda não venceram.

**O que é testado:**

-   **7.1** - Se o relatório traz corretamente a data de fabricação mais antiga dos estoques,
-   **7.2** - Se o relatório traz corretamente a data de validade mais próxima, descartando itens já vencidos, do estoque
-   **7.3** - Se o relatório traz corretamente a empresa com o maior estoque
-   **7.4** - Se o relatório é gerado no formato especificado.

</details>
