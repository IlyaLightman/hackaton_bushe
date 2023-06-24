from typing import List
from pydantic import BaseModel
import random

from enum import Enum, auto
import networkx as nx
import matplotlib.pyplot as plt


class Metrics(Enum):
    distance = auto()
    time = auto()
    points_count = auto()


class MetricsCoeff(BaseModel):
    distance: int = 1
    time: int = 1
    points_count: int = 1


class Order(BaseModel):
    id: int


class Courier(BaseModel):
    id: int
    balance: int


class WayBill(BaseModel):
    courier: Courier.id
    orders: list[Order.id]


class WayBillGenerator:
    def __init__(self, hub_id, active_couriers: List[Courier], optimize_func, metrics_coeff: MetricsCoeff):
        self.hub_id: int = hub_id
        self.metrics_coeff = metrics_coeff
        self.optimize_func = optimize_func
        self.G = None
        self.active_couriers = active_couriers  # todo del

    def optimize(self) -> List[WayBill]:
        cover_history, cover = self.greedy_max_cover(self.G, self.hub_id)

        for i, cover_i in enumerate(cover_history):
            print(f"Covered vertices at pass {i + 1}:", cover_i)

        print(f"Covered vertices: {cover}\tlen: {len(cover)}")
        self._draw_way(self.G, cover_history)
        return ...

    def create_way_bills(self) -> List[WayBill]:
        G = nx.complete_graph(12)
        self.G = G
        for (u, v) in G.edges():
            G.edges[u, v]['weight'] = random.random()

        print("Количество вершин:", G.number_of_nodes())
        print("Количество ребер:", G.number_of_edges())

        return self.optimize()

    def greedy_max_cover(self, graph, start):
        active_couriers = self._get_active_couriers()

        cover_history = []
        total_cover = set()
        original_start = start
        for courier in active_couriers:
            start = original_start
            visited = [start]
            total_cost = 0
            while True:
                frontiers = [(node, edge_data['weight']) for node, edge_data in graph[start].items() if
                             node not in visited and node not in total_cover]
                affordable_frontiers = [(node, cost) for node, cost in frontiers
                                        if total_cost + cost <= courier.balance]
                if not affordable_frontiers:
                    break
                start, cost = max(affordable_frontiers,
                                  key=lambda x: len(set(graph[x[0]]) - (set(visited) | total_cover)))
                total_cost += cost
                visited.append(start)
            total_cover |= set(visited)
            cover_history.append(visited)
        return cover_history, total_cover

    def _draw_way(self, graph, coverage: list):
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True)
        colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']  # список доступных цветов

        for i, c in enumerate(coverage):
            edges_cover = [(c[i], c[i + 1]) for i in range(len(c) - 1)]
            nx.draw_networkx_edges(graph, pos, edgelist=edges_cover, edge_color=colors[i % len(colors)], width=4)

        plt.show()

    def _get_active_couriers(self) -> List[Courier]:
        ...