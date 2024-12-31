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
    final_results = {"winner":[],"looser":[]}

    for result in results :
        if result["v"] not in choices :
            choices[result["reponse"]] = 1
        else :
            choices[result["reponse"]] += 1
    
    for choice in choices :
        
        result = choices[choice]

        if final_results["winner"] == [] :
            final_results["winner"].append({choice : result})


        elif choices[choice] >= list(final_results["winner"][0].values())[0]:
            if choices[choice] > list(final_results["winner"][0].values())[0] :
                final_results["looser"] += final_results["winner"]
                final_results["winner"] = [{choice : result}]
            
            else :
                final_results["winner"].append({choice : result})
            
        else :
            final_results["looser"].append({choice : result})

    return final_results #the results to send back


majority(results)
    