# Desafio de Estágio: Notificador WhatsApp com Python 🚀

Este projeto é uma solução para o desafio de estágio da b2bflow. O script em Python lê contatos de um banco de dados na plataforma Supabase e envia uma mensagem de saudação personalizada para cada um via WhatsApp, utilizando a Z-API.

## ✨ Funcionalidades

-   Conexão segura com o banco de dados Supabase para buscar a lista de contatos.
-   Envio de mensagens de texto personalizadas através da Z-API.
-   Gerenciamento de credenciais e chaves de API de forma segura usando variáveis de ambiente (`.env`).
-   Logging detalhado para acompanhar cada passo da execução do script.
-   Código organizado e robusto com tratamento de erros de conexão e de API.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3
-   **Banco de Dados:** Supabase
-   **API de Mensageria:** Z-API
-   **Bibliotecas Principais:** `requests`, `supabase-py`, `python-dotenv`

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

### 1. Pré-requisitos

-   Python 3.8 ou superior instalado.
-   Conta gratuita no [Supabase](https://supabase.com/).
-   Conta gratuita na [Z-API](https://z-api.io/) com uma instância ativa e conectada.

### 2. Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_AQUI]
    cd [NOME_DO_SEU_REPOSITORIO_AQUI]
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Unix/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows (PowerShell)
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuração do Banco de Dados (Supabase)

-   No seu projeto Supabase, vá para **Table Editor** e crie uma nova tabela chamada `contatos`.
-   Adicione as seguintes colunas:
    -   `nome` (tipo `text`)
    -   `numero` (tipo `text`)  <-- **Atenção:** O nome da coluna deve ser `numero`.
-   Insira os contatos de teste. O telefone deve estar no formato internacional: `55` (código do país) + `11` (DDD) + `999998888` (número).

### 4. Variáveis de Ambiente

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Copie o conteúdo abaixo para o arquivo e **substitua os valores pelas suas credenciais**:
    ```env
    # Credenciais do Supabase (encontre em Project Settings > API)
    SUPABASE_URL="SUA_URL_DO_PROJETO_SUPABASE"
    SUPABASE_KEY="SUA_CHAVE_ANON_PUBLICA_DO_SUPABASE"

    # Credenciais da Z-API (encontre no painel da sua instância)
    ZAPI_INSTANCE_ID="SEU_ID_DE_INSTANCIA_NA_ZAPI"
    ZAPI_TOKEN="SEU_TOKEN_DA_INSTANCIA_NA_ZAPI"
    ```

### 5. Execução

Com o ambiente virtual ativado e o `.env` preenchido, execute o seguinte comando no seu terminal:
```bash
python main.py
```
Acompanhe os logs no terminal para ver o progresso do envio das mensagens.
