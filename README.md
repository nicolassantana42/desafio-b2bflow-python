# Desafio de Estágio - Notificador de Contatos

Este projeto em Python lê uma lista de contatos de um banco de dados Supabase e envia uma mensagem personalizada de "Olá" para cada um via WhatsApp, utilizando a Z-API.

## Funcionalidades

-   Conexão segura com o banco de dados Supabase.
-   Leitura de contatos de uma tabela específica.
-   Envio de mensagens personalizadas via Z-API.
-   Uso de variáveis de ambiente para proteger credenciais.
-   Logs detalhados para acompanhar a execução.

## Setup do Projeto

### 1. Pré-requisitos

-   Python 3.8+
-   Uma conta no [Supabase](https://supabase.com/)
-   Uma conta na [Z-API](https://z-api.io/)

### 2. Instalação

1.  Clone o repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuração do Supabase

-   Crie um novo projeto no Supabase.
-   Vá para o **Table Editor** e crie uma nova tabela chamada `contatos`.
-   Adicione as seguintes colunas:
    -   `id` (int8, chave primária - criado por padrão)
    -   `created_at` (timestamptz - criado por padrão)
    -   `nome` (tipo `text`)
    -   `telefone` (tipo `text`, inclua o código do país e DDD, ex: 5511999998888)
-   Insira alguns contatos de teste na tabela.

### 4. Variáveis de Ambiente

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Copie o conteúdo do exemplo abaixo e preencha com suas credenciais:

    ```
    # Supabase
    SUPABASE_URL="SUA_URL_DO_PROJETO_SUPABASE"
    SUPABASE_KEY="SUA_CHAVE_ANON_PUBLICA_DO_SUPABASE"

    # Z-API
    ZAPI_INSTANCE_ID="SEU_ID_DE_INSTANCIA_NA_ZAPI"
    ZAPI_TOKEN="SEU_TOKEN_DA_INSTANCIA_NA_ZAPI"
    ```

### 5. Como Rodar

Com o ambiente virtual ativado e o `.env` configurado, execute o seguinte comando no terminal:

```bash
python main.py
```

O terminal exibirá os logs do processo de envio.
