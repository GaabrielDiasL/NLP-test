import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import csv

# Exemplo de dados fictícios
dados = "Apartamento - R Monsenhor Ivo Zanlorenzi, 3770\nVenda - R$ 378.449,00\n\nDetalhes\n\n2 dormitórios sendo 1 suíte\n2 banheiros\n\nMedidas\n\n69.49 m² útil\n\nDescrição\n\nNão perca essa oportunidade! Empreendimento localizado em frente ao terminal do Campo Comprido.\nApartamentos com 2 e 3 dormitórios.\nO apartamento de 2 dormitórios possui 69,49m² de área útil.\n\nMais detalhes\n\nSacada de frente para uma vista incrível."

# Tokenização
tokens = word_tokenize(dados)

# Remoção de pontuação
tokens_sem_pontuacao = [token for token in tokens if token not in string.punctuation]

# Conversão para letras minúsculas
tokens_minusc = [token.lower() for token in tokens_sem_pontuacao]

# Remoção de stop words
stop_words = set(stopwords.words("portuguese"))
tokens_sem_stop_words = [token for token in tokens_minusc if token not in stop_words]

# Lematização
lemmatizer = WordNetLemmatizer()
tokens_lemmatized = [lemmatizer.lemmatize(token) for token in tokens_sem_stop_words]

# Exibição dos tokens pré-processados
print(tokens_lemmatized)

# Caminho para o arquivo CSV de saída
caminho_arquivo = 'tokens_lemmatized.csv'

# Salvar os tokens lematizados em um arquivo CSV
with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tokens Lematizados'])  # Adiciona o cabeçalho da coluna
    writer.writerow(tokens_lemmatized)  # Salva os tokens em uma coluna
