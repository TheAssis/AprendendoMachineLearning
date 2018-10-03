#include <iostream>
#include <cstdlib>     /* rand, exit, EXIT_FAILURE */
#include <ctime>       /* time */

#include "perceptron.h"

using namespace std;

int main()
{

    float saida[2] = {-1,1};
    float entrada[6] = {0,0,1,1,1,0};
    int qtd = 3;
    int padroes = 2;
    float taxa = 0.4;
    Perceptron p(qtd,entrada,saida,taxa,padroes);
    p.treinarNeuronio(); // c�lculos necess�rios para treinar o perceptron
    p.exibirAprendizado(); // exibi��o do vi�s e do vetor de pesos resultantes

}
