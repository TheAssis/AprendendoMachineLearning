#ifndef KMEANS_H
#define KMEANS_H

class Kmeans
{
    public:
        Kmeans(); // construtor
        Kmeans(int _dim, int* _clusters); // entra com as dimens�es e aos clusters
        int getCluster(int * features, int _dim); // entrou com um dado, esse m�todo diz qual o cluster a qual pertence

    protected:

    private:
        int num_clusters = 0; // numero de clusters
        int dim = 0; // dimens�o de cada elemento do cluster
        int * clusters = new int [num_clusters*dim]; // ponteiro para os clusters
};

#endif // KMEANS_H
