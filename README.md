# PDF_Leser
Este Front End é parte da entrega necessária para completar o primeiro 
sprint da Pós-Graduação em Engenharia de Software. A API é capaz de 
cadastrar dados de projetos de extração de texto em PDFs, agrupados por tema,
assim como cadastrar tarefas relacionadas a esses projetos, com parâmetros de
leitura individualizadas.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo 
`requirements.txt`. Caso o sistema apresente problemas, recomenda-se a remoção das versões no 
arquivo.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
