# CRUD com Flask, SQLite e HTML

## Executando projeto sem Docker

Para executar o projeto, será necessário realizar o clone do mesmo para algum diretório no computador, após isso criar, e ativar o ambiente virtual, e assim executar a instalação das dependências necessárias:
```sh
pip install -r requirements.txt
```
Após isso, o projeto estará pronto para ser executado.


### Testes

Para executar os testes unitários, deve ser utilizado o arquivo **tests.py**:
```sh
python tests.py
```

### Aplicação

Para executar a aplicação, deve ser utilizado o arquivo **app.py**:
```sh
python app.py
```

## Executando o projeto com Docker

Para executar o projeto e os testes utilizando o Docker, será necessário realizar o clone do mesmo para algum diretório no computador, após isso executar o seguindo comando na raiz do projeto:
```sh
docker-compose up
```
