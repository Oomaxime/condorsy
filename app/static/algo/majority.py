choices = {}


def Majority(results):
    final_results = {"winner":[],"looser":[]}

    for result in results :
        if result["reponse"] not in choices :
            choices[result["reponse"]] = 1
        else :
            choices[result["reponse"]] += 1
    
    for choice in choices :
        
        result = choices[choice] / len(results)

        if choices[choice] >= (len(results) // 2 + 1) :
            final_results['winner'].append({choice : result})
            print("The winner is " + choice + " with : " + str(result * 100)  + "%")
        else :
            final_results['looser'].append({choice : result})
            print(choice + ":" + str(result * 100) + "%")

    return final_results #the results to send back


Majority(results)
    

    

