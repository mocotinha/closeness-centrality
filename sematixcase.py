import collections
import networkx as nx
import operator
from flask import Flask
from flask import request

closeness = {}
grafo = nx.Graph()
closeness_vet = None
closeness_max_value = None
app = Flask(__name__)


def adiciona_relacionamento(v1=None,v2=None,inicio=False):
    global closeness_max_value
    global closeness_vet
    global grafo
    global closeness
    c = {}
    if v1 == None and v2 == None and inicio == False:
        return
    elif inicio == True:
        dados = open('edges.dat')
        for linha in dados:
            v1,v2 = linha.replace("\n","").split(" ")
            grafo.add_node(v1)
            grafo.add_node(v2)
            grafo.add_edge(v1,v2)
    
    else:
        grafo.add_node(v1)
        grafo.add_node(v2)
        grafo.add_edge(v1,v2)
        
    for no in grafo.nodes():
        c[no] = 1/float(sum(nx.single_source_shortest_path_length(grafo, no).itervalues()))

    closeness = c
    print closeness
    closeness_max_value = max(closeness.itervalues())
    closeness_vet = max(closeness.iteritems(), key=operator.itemgetter(1))[0]

  
@app.route('/add_edge',methods=['GET', 'POST'])
def add_edges():
    if request.method == 'POST':
        print request
        v1 = request.form['v1']
        v2 = request.form['v2']
        adiciona_relacionamento(v1,v2)
        return "Relacionamento adicionado: %s, %s"%(v1,v2), 201
    
    elif request.method == 'GET':
        print request
        v1 = request.args.get('v1')
        v2 = request.args.get('v2')
        adiciona_relacionamento(v1,v2)
        return "Relacionamento adicionado: %s, %s"%(v1,v2), 201
    else:
        return "",501
    
@app.route('/centralidade',methods=['GET'])
def centralidade():
    global closeness_vet
    global closeness_max_value
    if request.method == 'GET':
        return "Vertice %s com valor de %f de closeness."%(closeness_vet,closeness_max_value) , 201
    else:
        return "",501

if __name__ == '__main__':
    adiciona_relacionamento(inicio=True)
    app.run(debug=False)



