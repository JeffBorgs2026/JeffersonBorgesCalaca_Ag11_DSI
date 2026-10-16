# Sistema de Monitoramento de Níveis de Água (Agenda 11)

Projeto desenvolvido como parte das atividades práticas da disciplina de Desenvolvimento de Sistemas (ETEC), aplicando lógica de programação estruturada, listas, funções e estilização visual no terminal em Python.

## Sobre a Atividade

O objetivo deste projeto é simular o monitoramento em tempo real de um reservatório de água através do terminal. O programa exibe os níveis de criticidade de forma visual e intuitiva, utilizando cores customizadas para cada faixa de risco.

## Funcionalidades do Sistema

- **Estruturas de Dados**: Armazenamento dos níveis, descrições e alertas utilizando listas estruturadas.
- **Modularização**: Utilização de funções dedicadas para o tratamento dinâmico das cores de exibição.
- **Estilização Visual**: Integração com a biblioteca `colorama` para destacar diferentes níveis de risco (desde estados críticos até situações normais de alerta).
- **Gerenciamento de Terminal**: Restauração automática dos padrões visuais do terminal após cada execução.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Biblioteca Externa**: Colorama
- **Controle de Versão**: Git e GitHub

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca de cores necessária executando o seguinte comando no seu terminal:
   ```bash
   pip install colorama
