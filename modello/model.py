from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._idMap={}
        self._aereoporti=DAO.getAeroporti()
        for v in self._aereoporti:
            self._idMap[v.ID]=v


    def calcolografo(self,distanza):
        self._grafo.add_nodes_from(self._aereoporti)
        self.voli=set(DAO.getallflights(distanza))
        for u in self.voli:
            u_partenza=self._idMap[u.ORIGIN_AIRPORT_ID]
            u_destinazione=self._idMap[u.DESTINATION_AIRPORT_ID]
            self._grafo.add_edge(u_partenza,u_destinazione,weight=u.DISTANCE)
        return self._grafo

    def getnumNodes(self):
        return self._grafo.number_of_nodes()

    def getnumEdges(self):
        return self._grafo.number_of_edges()


