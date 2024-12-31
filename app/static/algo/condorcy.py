class Condorcy:
    def __init__(self):
        self.conversion_choices = {}
        self.conversion_result = {}
        self.points = {}
        self.i = 0

    def add_point(self, where, remove=False):
        choice = self.conversion_choices.get(where)
        if choice not in self.points:
            self.points[choice] = 1
        else:
            if remove:
                self.points[choice] -= 1
            else:
                self.points[choice] += 1

    def verif_add_choice(self, choice):
        if choice not in self.conversion_choices:
            if choice[::-1] in self.conversion_choices:
                self.add_point(choice[::-1], True)
            else:
                self.conversion_choices[choice] = str(self.i)
                self.conversion_result[str(self.i)] = choice
                self.add_point(choice)
                self.i += 1
        else:
            self.add_point(choice)

    def process_results(self, results):
        final_results = {"winner": [], "looser": []}

        for result in results:
            cursor_start = 0
            end = len(result['reponse'])

            while cursor_start < end - 1:
                for cursor_end in range(cursor_start + 1, end):
                    result_start = result['reponse'][cursor_start]
                    result_end = result['reponse'][cursor_end]

                    if isinstance(result_start, list) and isinstance(result_end, list):
                        for ele_start in result_start:
                            for ele_end in result_end:
                                self.verif_add_choice(ele_start + ele_end)

                    elif isinstance(result_start, list):
                        for ele_start in result_start:
                            self.verif_add_choice(ele_start + result_end)

                    elif isinstance(result_end, list):
                        for ele_end in result_end:
                            self.verif_add_choice(result_start + ele_end)

                    else:
                        self.verif_add_choice(result_start + result_end)

                cursor_start += 1

        for choice, score in self.points.items():
            if not final_results["winner"]:
                final_results["winner"].append({self.conversion_result[choice]: score})
            elif score >= list(final_results["winner"][0].values())[0]:
                if score > list(final_results["winner"][0].values())[0]:
                    final_results["looser"] += final_results["winner"]
                    final_results["winner"] = [{self.conversion_result[choice]: score}]
                else:
                    final_results["winner"].append({self.conversion_result[choice]: score})
            else:
                final_results["looser"].append({self.conversion_result[choice]: score})

        return final_results


# Exemple d'utilisation
results = [
    {'reponse': [['A', 'B'], 'C']},
    {'reponse': [['C', 'D'], 'A']}
]

Condorcy = Condorcy()
final_results = Condorcy.process_results(results)
print(final_results)
