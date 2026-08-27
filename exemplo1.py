# -*- coding: utf-8 -*-
from java.io import FileWriter, BufferedReader, FileReader, File

def escrever_arquivo(caminho):
    writer = FileWriter(caminho)
    frases = [
        "Ola, este arquivo foi criado com Jython.",
        "java.io.FileWriter foi usado para escrever este texto.",
        "Agora vamos ler o arquivo de volta com BufferedReader.",
    ]
    for frase in frases:
        writer.write(frase + "\n")
    writer.close()
    print("Arquivo escrito em: %s" % caminho)

def ler_arquivo(caminho):
    reader = BufferedReader(FileReader(caminho))
    print("\n--- Conteudo lido do arquivo ---")
    total_linhas = 0
    linha = reader.readLine()
    while linha is not None:
        total_linhas += 1
        print("%d: %s" % (total_linhas,linha))
        linha = reader.readLine()
    reader.close()
    return total_linhas



if __name__ == "__main__":
    caminho_arquivo = File("saida.text").getAbsolutePath()
    escrever_arquivo(caminho_arquivo)
    total = ler_arquivo(caminho_arquivo)
    print("\nTotal de linhas lidas: %d" % total)