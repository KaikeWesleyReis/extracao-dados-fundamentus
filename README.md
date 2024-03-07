# Extração de Informações do Fundamentus
![fundamentus](https://github.com/KaikeWesleyReis/extracao-dados-fundamentus/assets/32513366/061cf423-e873-4ddd-991b-dbef125d3971)

**Objetivo do repositório**

Permitir a raspagem máxima de informações do site fundamentus com uma visão por ação / FII. O diferencial deste projeto, é que ele consegue extrair o máximo de informações da página do papel, ao contrário do que se encontra na páginas `resultados` que falta indicadores fundamentalistas importantes.

**Palavras-Chave**

python; scraping; fundamentus; investimentos; analises

**Implementações**

☑️ Extrair papeis de ações

☑️ Extrair papeis de fundos imobiliários

⏭️ Implementar extração de ações para executar de forma períodica através da AWS

⏭️ Desenvolver dashboard com avaliações fundamentalistas para revisão de carteira (...)

## Passo a Passo
Ao clonar este repositório, será necessário que (dentro dele) você realize o seguinte comando para puxar um dos requisitos para correta execução: 

`git clone https://github.com/KaikeWesleyReis/fundamentus_api.git`

Após isso, você pode:

- Extrair dados de FII - Executando os códigos de forma sequencial: `fii_0` -> `fii_1` -> `fii_2`
- Extrair dados de Ações - Executando os códigos de forma sequencial: `acao_0` -> `acao_1` -> `acao_2`

OBS: É possível que alguns papéis mais avulsos não sejam extraídos. Isso acontece devido a lógica implementada nessas extrações: **Só são buscados papéis que estejam alocados em um setor específico. Papeis sem setores mapeados, não serão salvos**. Para saber os setores mapeados, foi necessário a construção manual da tabela `dados/FUNDAMENTUS_SETORES.xlsx` e `dados/FUNDAMENTUS_SETORES_FII.xlsx`.
