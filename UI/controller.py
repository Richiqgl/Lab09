import flet as ft
from modello.model import Model
from UI.view import View


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the modello, which implements the logic of the program and holds the data
        self._model = model
        self._distanza = None

    def handleAnalizza(self, e):
        self._view._txt_result.controls.clear()
        if self._view._txtIn.value == "":
            self._view._txt_result.controls.append(ft.Text("ERRORE MANCA LA DISTANZA", color="red"))
            self._view.update_page()
            return
        grafo = self._model.calcolografo(self._distanza)
        self._view._txt_result.controls.append(ft.Text("I VERTICI SONO", color="red"))
        self._view._txt_result.controls.append(ft.Text(self._model.getnumNodes()))
        self._view._txt_result.controls.append(ft.Text("GLI ARCHI  SONO", color="red"))
        self._view._txt_result.controls.append(ft.Text(self._model.getnumEdges()))
        self._view.controls.append(ft.Text("Lista voli",color="red"))
        for u,v,p in grafo.edges(data=True):
                self._view._txt_result.controls.append(ft.Text("Aereoporto di partenza",color="red"))
                self._view._txt_result.controls.append(ft.Text(u.__str__()))
                self._view._txt_result.controls.append(ft.Text("Aereoporto di arrivo",color="red"))
                self._view._txt_result.controls.append(ft.Text(v.__str__()))
                self._view._txt_result.controls.append(ft.Text("Distanza",color="red"))
                self._view._txt_result.controls.append(ft.Text(p["weight"]))
        self._view.update_page()


    def leggi_distanza(self, e):
        self._distanza = self._view._txtIn.value
