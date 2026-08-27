# Atividade Jython — Integração Python e Java

Atividade da disciplina de Programação, sobre interoperabilidade entre linguagens que rodam na mesma plataforma de execução (JVM). O objetivo foi explorar o Jython, que permite usar classes Java diretamente em código Python.

## 📌 O que é o Jython?

Jython é uma implementação da linguagem Python que, ao invés de rodar sobre o interpretador padrão (CPython), roda em cima da JVM — a mesma máquina virtual usada por programas Java.

Como o código Python é compilado para bytecode e executado dentro da JVM, é possível importar e usar classes Java diretamente dentro de um script Python, sem precisar de nenhuma biblioteca de ponte ou conversão manual entre as linguagens. Na prática, dá pra escrever `from java.util import ArrayList` e usar a `ArrayList` como se fosse um objeto Python normal.

## 📁 Estrutura do repositório

```
atividade-jython/
├── README.md
├── Dockerfile
├── exemplo1.py
└── exemplo2.py
```
## 🐍☕ Programas desenvolvidos

### exemplo1.py — Manipulação de arquivos (java.io)

Escreve algumas linhas em um arquivo de texto e depois lê esse mesmo arquivo de volta, linha por linha, contando quantas linhas existem.

**Classes Java usadas:**
| Classe | Para que serve |
|---|---|
| `java.io.FileWriter` | Escreve o conteúdo no arquivo |
| `java.io.BufferedReader` | Lê o arquivo de forma eficiente, linha por linha |
| `java.io.FileReader` | Abre o arquivo para leitura |
| `java.io.File` | Resolve o caminho absoluto do arquivo |

### exemplo2.py — Estruturas de dados (java.util)

Cria uma lista de tarefas, ordena em ordem alfabética e marca quais já estão concluídas.

**Classes Java usadas:**
| Classe | Para que serve |
|---|---|
| `java.util.ArrayList` | Armazena a lista de tarefas |
| `java.util.Collections` | Ordena a lista com `Collections.sort()` |
| `java.util.HashMap` | Guarda o status (concluída ou não) de cada tarefa |

## 🔗 Como a integração Python/Java acontece

Nos dois exemplos, as classes Java são importadas normalmente, do mesmo jeito que se importa qualquer módulo Python:

```python
from java.io import FileWriter, BufferedReader, FileReader
from java.util import ArrayList, Collections, HashMap
```

A partir daí, elas são usadas com os métodos originais da própria API Java (`.write()`, `.readLine()`, `.add()`, `.put()`, `Collections.sort()`), enquanto o controle de fluxo (laços, funções, formatação de string) é escrito em Python puro.

Isso só é possível porque o Jython executa o código Python dentro da própria JVM — então objetos Python e objetos Java convivem no mesmo ambiente de execução, sem necessidade de serialização, chamadas remotas ou qualquer camada intermediária.

## ▶️ Como executar

### Opção 1 — Com Jython instalado na máquina

1. Baixe o Jython em [jython.org/download](https://www.jython.org/download)
2. Rode os scripts:

```bash
jython exemplo1.py
jython exemplo2.py
```

### Opção 2 — Com Docker (recomendado, não precisa instalar nada)

O `Dockerfile` já provisiona o Java e o Jython automaticamente dentro da imagem.

```bash
docker build -t atividade-jython .
docker run --rm atividade-jython
```

Esse comando builda a imagem e roda os dois exemplos em sequência, imprimindo a saída de ambos no terminal.

## 🎥 Vídeo explicativo

Vídeo mostrando o funcionamento do projeto e a integração entre Python e Java:

- **YouTube:** [Assista aqui](https://youtu.be/CFJlo0bWla4)
- **Google Drive:** [Assista aqui](https://drive.google.com/file/d/1mDzDUx_27VweaOlXooxq-xHa6QLGfxIP/view?usp=drive_link)

## 👤 Autor
Ricardo Costa Filho

Discente da Matéria de Paradigma de Linguagens de Programação
