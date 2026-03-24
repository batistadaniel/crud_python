-- Codigo simples do banco de dados

-- Este comando cria o banco de dados
CREATE DATABASE db_teste;

-- Este comando usar (inicia) o banco de dados
USE db_teste;

-- Este comando cria a tabela de usuarios do banco de dados
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100)
);

-- Para rodar no MySQL Workbench basta colar isto e clicar no icone de raio da esquerda (Ctrl + Shift + Enter). Ou para ir executando em partes deixe o clique no trecho e clique no icone de raio da direita (Ctrl + Enter)

