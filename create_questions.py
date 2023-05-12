import pandas as pd

conjunto_perguntas_respostas = {
    'qual o endereço?': 'O endereço é R Monsenhor Ivo Zanlorenzi, 3770.',
    'quantos dormitórios tem?': 'O apartamento possui 2 dormitórios, sendo 1 suíte.',
    'qual o preço de venda?': 'O preço de venda é R$ 378.449,00.',
    'quais são as medidas do apartamento?': 'O apartamento tem 69,49m² de área útil.',
    'tem sacada?': 'Sim, o apartamento tem sacada de frente para uma vista incrível.',
    'quais são os detalhes do empreendimento?': 'O empreendimento está localizado em frente ao terminal do Campo Comprido. Possui apartamentos com 2 e 3 dormitórios.',
    'tem estacionamento?': 'Sim, o empreendimento possui estacionamento disponível para os moradores.',
    'qual é a área total do apartamento?': 'A área total do apartamento não foi informada.',
    'quais são as opções de lazer do empreendimento?': 'O empreendimento oferece diversas opções de lazer, incluindo piscina, academia e salão de festas.',
    'quais são as formas de pagamento aceitas?': 'As formas de pagamento aceitas são dinheiro, cheque e financiamento bancário.',
    'qual é a data de entrega do empreendimento?': 'A data de entrega prevista é em dezembro de 2023.',
    'o empreendimento é pet-friendly?': 'Sim, o empreendimento é pet-friendly, permitindo animais de estimação.',
    'qual é a política de manutenção do empreendimento?': 'O empreendimento conta com uma equipe de manutenção dedicada que realiza a manutenção regular das áreas comuns e das unidades.',
    'há opções de comércio próximas ao empreendimento?': 'Sim, o empreendimento está localizado próximo a várias opções de comércio, incluindo supermercados, restaurantes e lojas.',
    'o empreendimento possui sistema de segurança?': 'Sim, o empreendimento possui um sistema de segurança com câmeras de vigilância e controle de acesso.',
    # Adicione mais perguntas e respostas conforme necessário
}

# Criar DataFrame a partir do dicionário de perguntas e respostas
df = pd.DataFrame.from_dict(conjunto_perguntas_respostas, orient='index', columns=['Resposta'])

# Salvar em um arquivo CSV
df.to_csv('conjunto_perguntas_respostas.csv', index_label='Pergunta')
