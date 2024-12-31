results = [
    {"reponse":"A", "id":1},
    {"reponse":"B", "id":2},
    {"reponse":"B", "id":4},
    {"reponse":"C", "id":5},
    {"reponse":"C", "id":5},
]

choices = {}

test = [{"test":"test"}]

# Output can be change if needed
def Quantity_Sort(results):
    final_results = {"winner": [], "looser": []}
    choices = {}

    # Compter le nombre de réponses pour chaque option
    for result in results:
        # Utiliser 'reponse' comme clé pour compter
        choice = result["reponse"]
        if choice not in choices:
            choices[choice] = 1
        else:
            choices[choice] += 1

    # Classer les résultats en gagnant et perdant
    for choice, count in choices.items():
        if not final_results["winner"]:  # Si "winner" est vide, ajouter la première entrée
            final_results["winner"].append({choice: count})
        elif count > list(final_results["winner"][0].values())[0]:
            # Si le choix a plus de votes, remplacer les perdants
            final_results["looser"] += final_results["winner"]
            final_results["winner"] = [{choice: count}]
        elif count == list(final_results["winner"][0].values())[0]:
            # Si le choix a le même nombre de votes que le gagnant, ajouter à "winner"
            final_results["winner"].append({choice: count})
        else:
            # Si le choix a moins de votes, l'ajouter aux perdants
            final_results["looser"].append({choice: count})

    return final_results  # Retourner les résultats

# Tester la fonction
result = Quantity_Sort(results)
print(result)
