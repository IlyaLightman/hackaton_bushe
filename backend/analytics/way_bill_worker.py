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
    max_items: int


class WayBill(BaseModel):
    courier_id: int
    orders_id: list[int]


class WayBillGenerator:
    def __init__(self, hub_id, optimize_func, metrics_coeff: MetricsCoeff):
        self.hub_id: int = hub_id
        self.metrics_coeff = metrics_coeff
        self.optimize_func = optimize_func
        self.G = None

    def _generate_weight(self, u, v):
        self.G.edges[u, v]['travel_time'] = random.random()  # пример значения времени путешествия
        self.G.edges[u, v]['valid_until'] = random.random()  # пример значения времени актуальности посещения
        self.G.edges[u, v]['cargo'] = random.random()  # пример значения количества товара

    def optimize(self) -> List[WayBill]:
        self.generate_graph()
        active_couriers = WayBillGenerator._get_active_couriers(self.hub_id)

        cover_history, cover = self.greedy_max_cover(graph=self.G, active_couriers=active_couriers, start=self.hub_id)

        for i, cover_i in enumerate(cover_history):
            print(f"Covered vertices at pass {i + 1}:", cover_i)

        print(f"Covered vertices: {cover}\tlen: {len(cover)}")
        self._draw_way(self.G, cover_history)
        return ...

    def create_way_bills(self) -> List[WayBill]:
        return self.optimize()

    def greedy_max_cover(self, graph, active_couriers, start):

        cover_history = []
        total_cover = set()
        original_start = start  # Сохраняем исходную точку start

        for courier in active_couriers:
            start = original_start  # Обновляем start перед каждым проходом
            visited = [start]
            total_items = 0
            current_time = 0  # Добавляем отслеживание текущего времени
            while True:
                frontiers = [(node, edge_data) for node, edge_data in graph[start].items() if
                             node not in visited and node not in total_cover]
                affordable_frontiers = [(node, edge_data) for node, edge_data in frontiers if
                                        total_items + edge_data['cargo'] <= courier.max_items
                                        and current_time + edge_data['travel_time'] <= edge_data['valid_until']]
                if not affordable_frontiers:
                    break
                start, edge_data = max(affordable_frontiers,
                                       key=lambda x: len(set(graph[x[0]]) - (set(visited) | total_cover)))
                total_items += edge_data['cargo']

                current_time += edge_data['travel_time']
                visited.append(start)
            total_cover |= set(visited)
            cover_history.append(visited)
        return cover_history, total_cover

    @staticmethod
    def _draw_way(graph, coverage: list):
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True)
        colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']  # список доступных цветов

        for i, c in enumerate(coverage):
            edges_cover = [(c[i], c[i + 1]) for i in range(len(c) - 1)]
            nx.draw_networkx_edges(graph, pos, edgelist=edges_cover, edge_color=colors[i % len(colors)], width=4)

        plt.show()

    @staticmethod
    def _get_active_couriers(hub_id) -> List[Courier]:
        active_couriers = [Courier(id=i, max_items=random.random()*20) for i in range(5)]
        print(f"Active couriers: {len(active_couriers)}")
        return active_couriers

    @staticmethod
    def _get_active_orders(hub_id) -> List[Order]:
        active_orders = [Order(id=i*10) for i in range(1, 12)]
        print(f"Active orders: {len(active_orders)}")
        return active_orders

    def generate_graph(self):
        active_orders = WayBillGenerator._get_active_orders(self.hub_id)
        order_ids = [order.id for order in active_orders]

        self.G = nx.complete_graph(len(active_orders) + 1)  # +1 this is hub
        self.G = nx.relabel_nodes(self.G, {i: order_id for i, order_id in enumerate(order_ids, start=1)})
        self.G = nx.relabel_nodes(self.G, {0: self.hub_id})
        for (u, v) in self.G.edges():
            # find weight
            self._generate_weight(u, v)


if __name__ == '__main__':
    way_bill_worker = WayBillGenerator(hub_id=1111111, optimize_func=None, metrics_coeff=MetricsCoeff())
    way_bill_worker.create_way_bills()
