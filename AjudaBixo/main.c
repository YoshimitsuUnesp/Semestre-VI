#include <stdio.h>

typedef struct
{
    char string[30];
}Palavra;


/* o primeiro passo tera tamanho N/8 < P <= N/4, com P = 2^k, 
a cada iteracao esse passo sera dividido por 2*/

void shellSort(Palavra palavras[], int n){
    
}

int main(){
    int n, i;

    printf("Digite o número de palavras:\n");
    scanf("%d", &n);
    Palavra palavras[n];

    printf("Digite as palavras:\n");
    for (i = 0; i < n; i++)
    {
        scanf("%s", palavras[i].string);
    }

    shellSort(palavras, n);

    return 0;
}

