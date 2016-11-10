# Closeness-centrality

In this challenge, suppose we are looking to do social network analysis for prospective customers. We want to extract from their social network a metric called "closeness centrality".
Centrality metrics try to approximate a measure of influence of an individual within a social network. The distance between any two vertices is their shortest path. The farness of a given vertex v is the sum of all distances from each vertex to v. Finally, the closeness of a vertex v is the inverse of the farness.
The first part of the challenge is to rank the vertices in a given graph by their closeness. The graph is provided in the attached file; each line of the file consists of two vertex names separated by a single space, representing an edge between those two nodes.
The second part of the challenge is to create a RESTful web server with endpoints to register edges and display the centrality of the graph.

References:
* Closeness Centrality: http://en.wikipedia.org/wiki/Centrality#Closeness_centrality
* Shortest path: http://en.wikipedia.org/wiki/Shortest_path_problem

# Descrição do projeto

O projeto foi executado na linguagem Python 2.7 (pacote Anaconda), fazendo uso de algumas bibliotecas. Para executar o projeto é necessário ter o python instaldo, recomendamos a instalação do pacote Anaconda para a versão 2.7, pois conterá todas as bibliotecas utilizadas neste trabalho, no link: https://www.continuum.io/downloads.

Foram utilizadas as seguintes bibliotecas:

collections - https://docs.python.org/2/library/collections.html
networkx - https://networkx.github.io/
operator - https://docs.python.org/2/library/operator.html
flask - http://flask.pocoo.org/

Para executar o código é necessário ter os dois arquivos sematixcase.py e edges.dat no mesmo diretorio e executar o seguinte comando:

> python sematixcase.py

OBS: Caso o python não for adicionado na variável PATH do sistema no momento da instalação, o comando deve ser executado da seguinte forma:

> diretorio/do/python/python sematixcase.py

# Outros

O projeto contém um arquivo do Jupyter e um PDF gerado a partir do mesmo, com passo a passo da implementação e outras informações, como o grafo inicial plotado e etc.
