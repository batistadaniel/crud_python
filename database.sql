-- Codigo simples do banco de dados

-- Este comando cria o banco de dados
CREATE DATABASE db_teste;

-- Este comando USE (inicia) o banco de dados
USE db_teste;

-- Este comando cria a tabela de usuarios do banco de dados
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100)
);

ALTER TABLE usuarios
ADD idade INT,
ADD sexo ENUM('masculino', 'feminino', 'indiferente');

INSERT INTO usuarios (nome, email, senha, idade, sexo) VALUES
('Ana Silva', 'ana1@email.com', '123', 18, 'feminino'),
('Bruno Souza', 'bruno1@email.com', '123', 21, 'masculino'),
('Carla Lima', 'carla1@email.com', '123', 25, 'feminino'),
('Daniel Rocha', 'daniel1@email.com', '123', 30, 'masculino'),
('Eduarda Alves', 'eduarda1@email.com', '123', 19, 'feminino'),
('Felipe Costa', 'felipe1@email.com', '123', 22, 'masculino'),
('Gabriela Mendes', 'gabriela1@email.com', '123', 27, 'feminino'),
('Henrique Dias', 'henrique1@email.com', '123', 35, 'masculino'),
('Isabela Santos', 'isabela1@email.com', '123', 20, 'feminino'),
('João Pedro', 'joao1@email.com', '123', 24, 'masculino'),

('Larissa Gomes', 'larissa1@email.com', '123', 23, 'feminino'),
('Matheus Ribeiro', 'matheus1@email.com', '123', 28, 'masculino'),
('Nathalia Pereira', 'nathalia1@email.com', '123', 26, 'feminino'),
('Otavio Martins', 'otavio1@email.com', '123', 31, 'masculino'),
('Patricia Freitas', 'patricia1@email.com', '123', 29, 'feminino'),
('Rafael Oliveira', 'rafael1@email.com', '123', 33, 'masculino'),
('Sofia Carvalho', 'sofia1@email.com', '123', 18, 'feminino'),
('Thiago Barbosa', 'thiago1@email.com', '123', 22, 'masculino'),
('Vanessa Moraes', 'vanessa1@email.com', '123', 24, 'feminino'),
('William Araujo', 'william1@email.com', '123', 37, 'masculino'),

('Amanda Rocha', 'amanda2@email.com', '123', 19, 'feminino'),
('Bruno Lima', 'bruno2@email.com', '123', 23, 'masculino'),
('Camila Souza', 'camila2@email.com', '123', 21, 'feminino'),
('Diego Santos', 'diego2@email.com', '123', 30, 'masculino'),
('Elaine Alves', 'elaine2@email.com', '123', 27, 'feminino'),
('Fernando Costa', 'fernando2@email.com', '123', 34, 'masculino'),
('Giovana Mendes', 'giovana2@email.com', '123', 20, 'feminino'),
('Hugo Dias', 'hugo2@email.com', '123', 25, 'masculino'),
('Ivana Santos', 'ivana2@email.com', '123', 28, 'feminino'),
('Julio Cesar', 'julio2@email.com', '123', 32, 'masculino'),

('Kelly Rocha', 'kelly2@email.com', '123', 26, 'feminino'),
('Lucas Pereira', 'lucas2@email.com', '123', 24, 'masculino'),
('Mariana Gomes', 'mariana2@email.com', '123', 22, 'feminino'),
('Nicolas Ribeiro', 'nicolas2@email.com', '123', 29, 'masculino'),
('Olivia Martins', 'olivia2@email.com', '123', 18, 'feminino'),
('Pedro Henrique', 'pedro2@email.com', '123', 31, 'masculino'),
('Renata Freitas', 'renata2@email.com', '123', 27, 'feminino'),
('Samuel Oliveira', 'samuel2@email.com', '123', 36, 'masculino'),
('Tatiana Carvalho', 'tatiana2@email.com', '123', 25, 'feminino'),
('Vinicius Barbosa', 'vinicius2@email.com', '123', 23, 'masculino'),

('Yasmin Araujo', 'yasmin2@email.com', '123', 21, 'feminino'),
('Zeca Silva', 'zeca2@email.com', '123', 38, 'masculino'),
('Alice Souza', 'alice3@email.com', '123', 19, 'feminino'),
('Brenda Lima', 'brenda3@email.com', '123', 22, 'feminino'),
('Carlos Mendes', 'carlos3@email.com', '123', 30, 'masculino'),
('Daniela Alves', 'daniela3@email.com', '123', 27, 'feminino'),
('Eduardo Costa', 'eduardo3@email.com', '123', 33, 'masculino'),
('Fernanda Dias', 'fernanda3@email.com', '123', 26, 'feminino'),
('Gustavo Santos', 'gustavo3@email.com', '123', 24, 'masculino'),
('Helena Lima', 'helena3@email.com', '123', 20, 'feminino');

-- Para rodar no MySQL Workbench basta colar isto e clicar no icone de raio da esquerda (Ctrl + Shift + Enter). Ou para ir executando em partes deixe o clique no trecho e clique no icone de raio da direita (Ctrl + Enter)

