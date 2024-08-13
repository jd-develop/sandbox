#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pprint
import urllib.request
import make_graph
from datetime import datetime


def list_candidates_from_request(response_: dict):
    candidates_ = {}
    for parrain_ in response_:
        candidate_ = parrain_['Candidat']
        try:
            candidates_[candidate_] += 1
        except KeyError:
            candidates_[candidate_] = 1
    return candidates_


def list_departments_from_request(response_: dict):
    departments_ = {}
    for parrain in response_:
        department = parrain['Departement']
        candidate = parrain['Candidat']
        try:
            departments_[department][candidate] += 1
        except KeyError:
            try:
                departments_[department][candidate] = 1
            except KeyError:
                departments_[department] = {candidate: 1}
    return departments_


url_of_parrainages = "https://presidentielle2022.conseil-constitutionnel.fr/telechargement/parrainagestotal.json"
actual_file_name = f"json_history/{datetime.today().strftime('%Y-%m-%d')}.json"

with urllib.request.urlopen(url_of_parrainages) as response:  # response is HTTPResponse
    file_content = response.read().decode('utf-8')  # writable in a file.
    file = open(actual_file_name, "w", encoding="utf-8")
    file.write(file_content)
    file.close()
    with open(actual_file_name, "r", encoding="utf-8-sig") as file:
        response_dict = json.load(file)
        file.close()

candidates = list_candidates_from_request(response_dict)

departments = list_departments_from_request(response_dict)

most_by_department = {}
for department_ in departments:
    most_by_department[department_] = max(departments[department_], key=departments[department_].get)

print("ACTUAL PARRAINAGES:")
pprint.pprint(candidates)

print("\nBY DEPARTMENT:")
pprint.pprint(departments)

print("\nMOST POPULAR CANDIDATES BY DEPARTMENT:")
pprint.pprint(most_by_department)

# graph
list_of_all_candidates_dicts = []
for file in make_graph.os.listdir("json_history"):  # os is imported in make_graph
    if file.endswith(".json") and file.startswith("2022-"):
        with open(f"json_history/{file}", "r", encoding="utf-8-sig") as file_:
            response_dict = json.load(file_)
            file_.close()
        list_of_all_candidates_dicts.append(list_candidates_from_request(response_dict))


make_graph.display_graph(list_of_all_candidates_dicts)
