#include <stdio.h>
#include <stdlib.h>

#define MAX 5 // Define o tamanho máximo da pilha

// Estrutura da pilha
typedef struct {
    int itens[MAX];
    int topo;
} Pilha;

// Função para inicializar a pilha
void inicializar(Pilha *p) {
    p->topo = -1;
}

// Função para verificar se a pilha está vazia
int estaVazia(Pilha *p) {
    return (p->topo == -1);
}

// Função para verificar se a pilha está cheia
int estaCheia(Pilha *p) {
    return (p->topo == MAX - 1);
}

// Função para inserir um elemento na pilha (PUSH)
void push(Pilha *p, int valor) {
    if (estaCheia(p)) {
        printf("Erro: Pilha cheia!\n");
        return;
    }
    p->topo++;
    p->itens[p->topo] = valor;
    printf("Inserido: %d\n", valor);
}

// Função para remover um elemento da pilha (POP)
int pop(Pilha *p) {
    if (estaVazia(p)) {
        printf("Erro: Pilha vazia!\n");
        return -1;
    }
    int valor = p->itens[p->topo];
    p->topo--;
    return valor;
}


int main() {
    

    return 0;
}
