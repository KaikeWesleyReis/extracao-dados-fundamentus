import re
import numpy as np
import fundamentus

def linearizar_info_bruta_acao(papel, tipo='acao'):
    '''
    Puxar informações diversas do site fundamentus para determinado papel convertendo em um formato legível.
    Parâmetros
        papel: Código da ação. Por exemplo: BBAS3
        tipo: (Str) Natureza da ação. Atualmente os tipos são: 'fii' e 'acao'
    Retorno
        Dicionário com o máximo de informações extraídas para serem tratadas.
    '''
    # Puxar informação de ações
    df_acao = fundamentus.get_detalhes_raw(papel)
    
    # Validar tamanho esparado 
    if tipo == 'acao':
        assert len(df_acao) == 5, 'ERRO - Extração não possui quantidade esperada de informações.'
    else:
        assert len(df_acao) == 6, 'ERRO - Extração não possui quantidade esperada de informações.'
    
    # Montar linha de ação
    linha_acao = dict()
    
    # Loop nas informações
    for df in df_acao:
        # Remover qualquer nulo
        df.fillna('', inplace=True)
        # Validar existência de coluna - valor (número par)
        assert len(df.columns) % 2 == 0, 'ERRO - Padrão desconhecido de dados extraídos.'
        # Loop nas colunas que contém o nome
        for col_idx in range(0, len(df.columns), 2):
            # Definir index de valor
            val_idx = col_idx + 1
            # Extração chave - valor
            res = dict(zip(df[col_idx].tolist(), df[val_idx].tolist()))
            # Corrigir resultados 12 e 3 meses AQUI
            if 'Últimos 12 meses' in [k.strip() for k in res.keys()]:
                for col in ['?Receita','?Venda de ativos','?FFO','?Rend. Distribuído']:
                    res[col +' 12 Meses'] = res.pop(col)
            elif 'Últimos 3 meses' in [k.strip() for k in res.keys()]:
                for col in ['?Receita','?Venda de ativos','?FFO','?Rend. Distribuído']:
                    res[col +' 3 Meses'] = res.pop(col)                
            # Salvar
            linha_acao = {**linha_acao, **res}
    # Retornar
    return linha_acao


def converter_string_numero(x):
    '''
    Tratar strings para converter em números a partir dos padrões identificados.
    Parâmetros
        x: (Str) string numérica
    Retorno
        Valor numérico tratado
    '''
    if type(x) == str:
        xo = x
        # Aplicar substituições padrões
        x = x.replace(',','.').replace('%', '')
        # Garantir que tenhamos um número e nenhuma letra
        if bool(re.search(r'\d', x)) is True and bool(re.search(r'[a-zA-Z]', x)) is False:
            # Remover problema de excesso de pontos
            if len(x.split('.')) > 1:
                x = ''.join(x.split('.')[:-1]) + '.' + x.split('.')[-1]
            # Report
            #print(f'> De {xo} para {x} que é numérico.')
            # Retorno
            return float(x)
        else:
            return np.nan
    else:
        return x