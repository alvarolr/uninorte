class TabelaHashLinear:
    def __init__(self, tamanho_fixo=31):
        """
        Define um tamanho fixo para a tabela (como o 'TAM = 31' do vídeo)
        e inicializa todas as posições com 0 (indicando que estão vazias).
        """
        self.tamanho = tamanho_fixo
        self.tabela = [0] * self.tamanho

    def _funcao_hash(self, chave):
        """
        A famosa Função Hash: calcula o resto da divisão 
        da chave pelo tamanho fixo da tabela.
        """
        return chave % self.tamanho

    def inserir(self, valor):
        """Insere um valor utilizando sondagem linear em caso de colisão."""
        indice = self._funcao_hash(valor)

        # Se a posição já estiver ocupada (diferente de 0), avança para a próxima
        while self.tabela[indice] != 0:
            indice = (indice + 1) % self.tamanho

        # Insere na primeira posição livre encontrada
        self.tabela[indice] = valor

    def buscar(self, valor):
        """Busca um valor na tabela."""
        indice = self._funcao_hash(valor)
        inicio = indice # Guarda onde começou para evitar loop infinito

        while self.tabela[indice] != 0:
            if self.tabela[indice] == valor:
                return indice # Retorna a posição onde o valor está
            
            indice = (indice + 1) % self.tamanho
            
            # Se deu a volta inteira na tabela e não achou
            if indice == inicio:
                break

        return None # Não encontrado

    def imprimir(self):
        """Exibe o vetor da tabela hash na tela."""
        print(f"\n--- Tabela Hash (Tamanho Fixo: {self.tamanho}) ---")
        for i, valor in enumerate(self.tabela):
            print(f"[{i:02d}] = {valor}")
        print("-" * 35)


# ==========================================
# Exemplo de Uso
# ==========================================
if __name__ == "__main__":
    # Criamos a tabela já com o tamanho fixo definido (ex: 31)
    tabela = TabelaHashLinearSimples(tamanho_fixo=31)

    # Inserindo alguns valores
    valores = [45, 12, 89, 33, 99, 100, 175]
    for v in valores:
        tabela.inserir(v)

    # Mostra a tabela preenchida
    tabela.imprimir()

    # Testando busca
    alvo = 89
    pos = tabela.buscar(alvo)
    if pos is not None:
        print(f"Valor {alvo} encontrado no índice [{pos}]!")
    else:
        print(f"Valor {alvo} não encontrado.")
