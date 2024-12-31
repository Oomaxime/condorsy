results = [
    {"choices":"A", "id":1},
    {"choices":"B", "id":2},
    {"choices":"B", "id":4},
    {"choices":"C", "id":5},
    {"choices":"C", "id":5},
]

choices = {}

test = [{"test":"test"}]

# Output can be change if needed

def Quantity_Sort(results):
    final_results = {"winner":[],"looser":[]}

    for result in results :
        if result["choices"] not in choices :
            choices[result["choices"]] = 1
        else :
            choices[result["choices"]] += 1
    
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
    