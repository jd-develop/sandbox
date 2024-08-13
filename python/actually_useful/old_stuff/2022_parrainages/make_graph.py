#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import os


def display_graph(list_of_all_candidates_dicts: list[dict]):
    x_list = []
    for file in os.listdir("json_history"):
        if file.endswith(".json") and file.startswith("2022-"):
            x_list.append(file[:10])  # we just delete the '.json'

    candidates = {}
    loop_ = 0
    for candidate_dict in list_of_all_candidates_dicts:
        loop_ += 1
        for candidate in candidate_dict:
            if loop_ == 1:
                candidates[candidate] = [candidate_dict[candidate]]
            else:
                try:
                    candidates[candidate].append(candidate_dict[candidate])
                except KeyError:
                    candidates[candidate] = [0] * (loop_ - 1)  # we create a list with missing elements.
                    candidates[candidate].append(candidate_dict[candidate])

    candidates_to_show = 0
    for pos, candidate in enumerate(candidates):
        plt.plot(x_list, candidates[candidate], label=candidate)
        candidates_to_show += 1
        if (pos + 1) % 10 == 0:
            candidates_to_show = 0
            plt.legend()
            plt.grid()
            plt.show()

    if candidates_to_show != 0:
        plt.legend()
        plt.grid()
        plt.show()
