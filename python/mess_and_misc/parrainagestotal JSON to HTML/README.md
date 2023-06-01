# parrainagestotal JSON to HTML

This code has for goal to generate an HTML beautiful page from [this file](parrainagestotal.json) found on the [Conseil Constitutionnel's website](https://presidentielle2022.conseil-constitutionnel.fr/les-parrainages/tous-les-parrainages-valides.html).

## JSON shape

The JSON is a list of parrainages. The parrainages are under this shape:

    {
    "Civilite" ("M." or "Mme"),
    "Nom" (last name),
    "Prenom" (first name),
    "Mandat" ("Maire", "Sénateur", "Président de Consulat", etc.),
    "Circonscription",
    "Departement",
    "Candidat" (candidate),
    "DatePublication" (publication date under the shape "YYYY-MM-DDThh:mm:ss")
    }
