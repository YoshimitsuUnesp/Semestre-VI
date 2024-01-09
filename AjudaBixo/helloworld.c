#include <stdio.h>

int main(){
    float nota1, nota2, media;

    printf("Digite uma primeira nota:\n");
    scanf("%f", &nota1);
    printf("Digite uma segunda nota:\n");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

    printf("A média é de: %.2f\n", media);

    return 0;
}