# Conversor de Moeda USD para BRL

Este é um simples conversor de moeda que converte dólares americanos (USD) para reais brasileiros (BRL) utilizando a API [Exchangerate API](https://www.exchangerate-api.com/). O projeto foi construído com **Flask**, **HTMX**, **TailwindCSS** e **DaisyUI**.

## Funcionalidades

- Converte de **USD para BRL** em tempo real.
- Exibe o valor convertido ao carregar a página (padrão: 1 USD).
- O usuário pode inserir um valor em USD e ver sua conversão instantânea para BRL.
- Interface simples e responsiva com **TailwindCSS** e **DaisyUI**.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python utilizado para criar a aplicação backend.
- **HTMX**: Usado para realizar requisições assíncronas e atualizar o conteúdo da página sem a necessidade de recarregar.
- **TailwindCSS**: Framework CSS para estilização.
- **DaisyUI**: Biblioteca de componentes de UI para o TailwindCSS.
- **Exchangerate API**: API utilizada para obter a taxa de conversão entre USD e BRL.

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado. Você pode verificar se o Python está instalado executando:

```bash
python --version
```

Se não estiver instalado, baixe e instale a versão mais recente do Python em [python.org](https://www.python.org/).

### Passos para execução:

1. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/Conversor-de-Moeda.git
cd Conversor-de-Moeda
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

- **Windows**:

```bash
venv\Scripts\activate
```

- **Linux/macOS**:

```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute a aplicação:

```bash
python app.py
```

6. Acesse a aplicação no seu navegador, indo para [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação, onde as rotas Flask estão definidas.
- `templates/index.html`: Arquivo HTML que contém a interface do usuário.
- `requirements.txt`: Lista de dependências do projeto (Flask, requests, etc.).

## Contribuições

Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork e abrir pull requests com melhorias ou correções de bugs. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que deseja alterar.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Desenvolvido por [Zorzenon Dev](https://github.com/LuizZorzenon).
