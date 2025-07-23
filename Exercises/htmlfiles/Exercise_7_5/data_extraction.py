import csv

def extraction(mode="default"):
    competitor_path = "C:/Users/ryan_/Downloads/School/Resources/H2 Computing/Materials-Personal/Exercises/resources/Ex_7_4_competitor.csv"
    scores_path = "C:/Users/ryan_/Downloads/School/Resources/H2 Computing/Materials-Personal/Exercises/resources/Ex_7_4_scores.csv"
    altered_namelist = {}
    score_db={}
    round_db={1:[],2:[],3:[]}
    mean_scores={}
    qualifiers = {}
    

    with open(competitor_path) as namelist_data:
        reader = csv.DictReader(namelist_data)
        name_list = list(reader)
    with open(scores_path) as scores_data:
        reader = csv.DictReader(scores_data)
        scores = list(reader)
    # print(scores)
    # print("\n"*10)
    for competitor in name_list:
        altered_namelist[competitor["id"]] = competitor["name"]


    for i in scores:
        current = round_db[int(i["round"])]
        current.append([altered_namelist[i["id"]], i["score"]])
        round_db[int(i["round"])] = current
        if i["id"] in score_db:
            current_data,analysis=score_db[i["id"]]
            total_score,mean_score = analysis
            total_score += int(i["score"])
            # print(total_score)
            mean_score = round(total_score / (len(current_data)+1), 2)
            mean_score = f"{mean_score:.2f}"
            # print(mean_score)
            # print(len(current_data))
            temp = {"round":i["round"],"score":i["score"]}
            current_data.append(temp)
            current = [current_data,[total_score,mean_score]]
            score_db[i["id"]] = current
            mean_scores[altered_namelist[i["id"]]] = mean_score
        else:
            temp = [[{"round":i["round"],"score":i["score"]}],[int(i["score"]),int(i["score"])]]
            score_db[i["id"]] = temp
    altered_meanscores = [list(i) for i in mean_scores.items()]
    altered_meanscores.sort(key=lambda x: x[0])
    qualifiers = [[altered_namelist[i[0]],i[1][1][0],i[1][1][0]>250] for i in score_db.items()]
    qualifiers.sort(key=lambda x: x[0])
    altered_round_db = dict(zip(list(round_db.keys()),[sorted(i,key=lambda x: x[1], reverse=True) for i in round_db.values()]))
    altered_score_db = {i:[altered_namelist[i],[i["score"] for i in score_db[i][0]],score_db[i][1][0],score_db[i][1][0]>250] for i in score_db.keys()}


    if mode == "default":
        return score_db,altered_round_db,altered_meanscores,altered_score_db
    elif mode == "round":
        return altered_round_db
    elif mode == "mean":
        return altered_meanscores
    elif mode == "qualifiers":
        return qualifiers
    elif mode == "query":
        return altered_score_db



if __name__ == "__main__":   
    score_db,round_db,altered_meanscores,altered_score_db = extraction(mode="default")
    # for id,val in score_db.items():
    #     print(f"{id}: {val}")
    # for id,val in round_db.items():
    #     print(f"{id}: {val}")
    # print(altered_namelist)
    # print(altered_meanscores)
    print(altered_score_db)