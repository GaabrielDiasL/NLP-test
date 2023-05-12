import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from fuzzywuzzy import fuzz

def preprocessar_pergunta(pergunta):
    # Tokenização
    tokens = word_tokenize(pergunta)

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

    return tokens_lemmatized

# Carregar os tokens lematizados do arquivo CSV
df_tokens = pd.read_csv('tokens_lemmatized.csv')

# Converter os tokens lematizados em uma lista
tokens_lemmatized = df_tokens.iloc[0].tolist()

# Carregar o conjunto de perguntas e respostas do arquivo CSV
df_perguntas_respostas = pd.read_csv('conjunto_perguntas_respostas.csv')

# Criar um dicionário a partir do DataFrame
conjunto_perguntas_respostas = df_perguntas_respostas.set_index('Pergunta').to_dict()['Resposta']

from fuzzywuzzy import fuzz

def calcular_pontuacao(pergunta_entrada, pergunta_conjunto):
    pontuacao = fuzz.ratio(pergunta_entrada, pergunta_conjunto) / 100.0
    return pontuacao


def chatbot_responder(pergunta):
    pergunta_lemmatized = preprocessar_pergunta(pergunta)  # Pré-processar a pergunta de entrada (lemmatização, remoção de stopwords, etc.)
    print(f'Pergunta lemmantizada: {pergunta_lemmatized}')
    # Procurar pela melhor correspondência entre as perguntas do conjunto e a pergunta de entrada
    melhor_correspondencia = None
    max_pontuacao = 0
    
    for pergunta_conjunto in conjunto_perguntas_respostas.keys():
        pontuacao = calcular_pontuacao(pergunta_lemmatized, pergunta_conjunto)  # Calcular a pontuação de correspondência
        
        if pontuacao > max_pontuacao:
            max_pontuacao = pontuacao
            melhor_correspondencia = pergunta_conjunto
    
    if melhor_correspondencia is not None:
        resposta = conjunto_perguntas_respostas[melhor_correspondencia]
    else:
        resposta = "Desculpe, não tenho a resposta para essa pergunta."
    
    return resposta

while True:
    pergunta = input("Digite sua pergunta (ou pressione Enter para encerrar): ")
    if pergunta == "":
        break
    resposta = chatbot_responder(pergunta)
    print(resposta)