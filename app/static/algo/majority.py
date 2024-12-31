choices = {}


def Majority(results):
    final_results = {"winner": [], "looser": []}

    for result in results:
        choice = str(result["reponse"])
        if choice not in choices:
            choices[choice] = 1
        else:
            choices[choice] += 1

    for choice in choices:
        vote_count = choices[choice]
        total_votes = len(results)

        percentage = (vote_count / total_votes) * 100

        if vote_count > total_votes // 2:
            final_results['winner'].append({choice: percentage})
            print(f"The winner is {choice} with: {percentage:.2f}%")
        else:
            final_results['looser'].append({choice: percentage})
            print(f"{choice}: {percentage:.2f}%")

    return final_results


# Exemple d'appel
results = [
    {"reponse": "Option A"},
    {"reponse": "Option B"},
    {"reponse": "Option A"},
    {"reponse": "Option A"},
    {"reponse": "Option B"},
]

Majority(results)
