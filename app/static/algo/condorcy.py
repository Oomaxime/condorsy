convertion_choices = {}
convertion_result = {}
points = {}
i = 0


def add_point(where, remove = False):
    if convertion_choices[where] not in points :
        points[convertion_choices[where]] = 1
        
    else :
        if remove == False : 
            points[convertion_choices[where]] += 1
        else : 
            points[convertion_choices[where]] -= 1   


def verif_add_choice(choice) :
    global i
    if choice not in convertion_choices :
        if choice[::-1] in convertion_choices :
            add_point(choice[::-1], True)
        
        else :
            convertion_choices[choice] = str(i)
            convertion_result[str(i)] = choice
            add_point(choice)
            i += 1

    else :
        add_point(choice)

def Condorcy(results) :
    final_results = {"winner":[], "looser":[]}

    for result in results :
        cursor_start = 0
        end = len(result['reponse'])
        while cursor_start < end - 1 :
            for cursor_end in range(cursor_start + 1,len(result['reponse'])) :
                    result_start = result['reponse'][cursor_start]
                    result_end = result['reponse'][cursor_end]

                    if isinstance(result_start, list) and isinstance(result_end, list) : 
                        for ele_start in result_start :
                            for ele_end in result_end :
                                verif_add_choice(ele_start + ele_end)
                    
                    elif isinstance(result_start, list) :
                        for ele_start in result_start :
                            verif_add_choice(ele_start + result_end)

                    elif isinstance(result_end, list) :
                        for ele_end in result_end :
                            verif_add_choice(result_start + ele_end)

                    else :
                        verif_add_choice(result_start + result_end)
            
            cursor_start += 1

    for choice in points :

        if final_results["winner"] == [] :
            final_results["winner"].append({convertion_result[choice] : points[choice]})

        elif points[choice] >= list(final_results["winner"][0].values())[0]:
            if points[choice] > list(final_results["winner"][0].values())[0] :
                final_results["looser"] += final_results["winner"]
                final_results["winner"] = [{convertion_result[choice] : points[choice]}]
            
            else :
                final_results["winner"].append({convertion_result[choice] : points[choice]})
            
        else :
            final_results["looser"].append({convertion_result[choice] : points[choice]})

    return final_results #the results to send back
    
Condorcy(results)
