#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json  # we'll use the json module
# from pprint import pprint
import webbrowser


def file_to_list(file_name: str) -> list[dict]:
    """Returns a list of dicts from a file name. Does not check for any error."""
    return json.load(open(file_name, encoding='UTF-8'))


def raw_list_to_candidate_by_candidate_dict(raw_list: list[dict]) -> dict:
    """Returns a dict which every key is a candidate and every value is the parrainages count for this candidate."""
    candidate_by_candidate_dict = {}
    for parrainage in raw_list:
        candidate = parrainage["Candidat"]  # we get the candidate from the parrainage dict
        try:  # NB: we remove the things like \u0027 with `u'{}'.format(candidate)`
            candidate_by_candidate_dict[u'{}'.format(candidate)] += 1  # +1 parrainage to our candidate
        except KeyError:  # the candidate is not in our list yet : let's create it !
            candidate_by_candidate_dict[u'{}'.format(candidate)] = 1

    return candidate_by_candidate_dict


def raw_list_to_mandat_by_mandat_dict(raw_list: list[dict]) -> dict:
    """Returns a dict in which every key is a mandat and every value is the parrainages given by people exercising this
    mandat."""
    mandat_by_mandat_dict = {}
    for parrainage in raw_list:
        mandat = parrainage["Mandat"]
        mandat = mandat.replace("Conseiller", "Conseiller.e").replace("Conseillère", "Conseiller.e")
        mandat = mandat.replace("Sénateur", "Sénateur.trice").replace("Sénatrice", "Sénateur.trice")

        if "métropolitaine" in mandat:
            mandat = mandat.replace("métropolitaine", "métropolitain.e")
        elif "métropolitain" in mandat and "métropolitain.e" not in mandat:
            mandat = mandat.replace("métropolitain", "métropolitain.e")

        if "Députée" in mandat:
            mandat = mandat.replace("Députée", "Député.e")
        elif "Député" in mandat and "Député.e" not in mandat:
            mandat = mandat.replace("Député", "Député.e")

        if "Maire déléguée" in mandat:
            mandat = mandat.replace("Maire déléguée", "Maire délégué.e")
        elif "Maire délégué" in mandat and "Maire délégué.e" not in mandat:
            mandat = mandat.replace("Maire délégué", "Maire délégué.e")

        if "Présidente" in mandat:
            mandat = mandat.replace("Présidente", "Président.e")
        elif "Président" in mandat and "Président.e" not in mandat:
            mandat = mandat.replace("Président", "Président.e")

        if "Représentante française" in mandat:
            mandat = mandat.replace("Représentante française", "Représentant.e français.e")
        elif "Représentant français" in mandat and "Représentant.e français.e" not in mandat:
            mandat = mandat.replace("Représentant français", "Représentant.e français.e")
        
        try:
            mandat_by_mandat_dict[u'{}'.format(mandat)] += 1
        except KeyError:
            mandat_by_mandat_dict[u'{}'.format(mandat)] = 1

    return mandat_by_mandat_dict


def generate_html(candidate_by_candidate_dict: dict, mandat_by_mandat_dict: dict) -> str:
    """Generates HTML str from the different dicts."""
    html = "<!DOCTYPE html>\n" \
           "<html lang=\"en\">\n" \
           "<head>\n" \
           "    <meta charset=\"UTF-8\">\n" \
           "    <title>parrainagestotal HTML</title>\n" \
           "</head>\n" \
           "<style>\n" \
           "    table, tr, td {\n" \
           "        border: 1px solid black;\n" \
           "        border-collapse: collapse;\n" \
           "    }\n" \
           "</style>\n" \
           "<body>\n" \
           "<h1>Tables generated from the parrainagestotal.json file.</h1>\n" \
           "<h2>Summary</h2>\n" \
           "<ul>\n" \
           "   <li><a href=\"#candidatebycandidate\">Amount of parrainages by candidate</a></li>\n" \
           "   <li><a href=\"#mandatbymandat\">Amount of parrainages by mandate type</a></li>\n" \
           "</ul>\n" \
           "<h2 id=\"candidatebycandidate\">Amount of parrainages by candidate</h2>\n" \
           "<table>\n"

    for candidate in sorted(candidate_by_candidate_dict.keys()):  # sorted in alphanumeric order.
        html += f"\t<tr>\n\t\t<td>{candidate}</td>\n\t\t<td>{candidate_by_candidate_dict[candidate]}</td>\n\t</tr>\n"
    html += f"\t<tr>\n\t\t<td>TOTAL</td>\n\t\t<td>{sum(candidate_by_candidate_dict.values())}"

    html += "</table>\n" \
            "<h2 id=\"mandatbymandat\">Amount of parrainages by mandate type</h2>\n" \
            "<table>\n"

    for mandat in sorted(mandat_by_mandat_dict.keys()):
        html += f"\t<tr>\n\t\t<td>{mandat}</td>\n\t\t<td>{mandat_by_mandat_dict[mandat]}</td>\n\t</tr>\n"
    html += f"\t<tr>\n\t\t<td>TOTAL</td>\n\t\t<td>{sum(mandat_by_mandat_dict.values())}"

    html += "</table>\n</body>\n</html>\n"
    return html


def main():
    raw_list = file_to_list(FILE_NAME)
    # pprint(raw_dict)
    candidate_by_candidate_dict = raw_list_to_candidate_by_candidate_dict(raw_list)
    mandat_by_mandat_dict = raw_list_to_mandat_by_mandat_dict(raw_list)
    # pprint(candidate_by_candidate_dict)
    # pprint(mandat_by_mandat_dict)
    html = generate_html(candidate_by_candidate_dict, mandat_by_mandat_dict)
    with open("output.html", 'w', encoding='UTF-8') as html_file:
        html_file.write(html)
        html_file.close()
    webbrowser.open("output.html")


if __name__ == '__main__':
    FILE_NAME = "parrainagestotal.json"
    main()
