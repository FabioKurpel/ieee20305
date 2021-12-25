# Projeto de Iniciação Científica - IEEE 2030.5
## Iniciado em Outubro de 2021

Implementação de uma API Rest para comunicação e controle de dispositivos de geração distribuida de energia fotovoltaica no padrão proposto pela norma IEEE 2030.5.
Essa versão foi desenvolvida utilizando a biblioteca Flask disponível para linguagem de programação Python. 

O arquivo principal é teste.py, nele foi implementado o processo de registro de novos dispositos. Esse arquivo contém as seguintes funções:
  + raiz: essa função é chamada quando invocado o caminho /edev. Ao fazer uma requisição GET nesse caminho a resposta é a lista de dispositivos registrados na rede. Ao fazer um POST
  com os dados de *sFID* e *changedTime* é registrado no banco de dados o novo dispositivo e gerada a nova rota;
  + serializer: responsável por transformar as informações contidas no banco de dados de dispositivos para o formato XML contido na norma;

O processo de registro de novos dispositivos, com seu fluxograma e padronização de formatos de requisição GET e POST pode ser encontrado na página 272 da norma.

