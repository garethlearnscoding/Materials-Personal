import csv

def extraction():
    with open("../../resources/Ex_7_4_competitor.csv") as namelist_data:
        reader = csv.DictReader(namelist_data)
        name_list = list(reader)
    with open("../../resources/Ex_7_4_scores.csv") as scores_data:
        reader = csv.DictReader(scores_data)
        scores = list(reader)
    # print(scores)
    # print("\n"*10)
    score_db={}
    for i in scores:
        if i["id"] in score_db:
            current=score_db[i["id"]]
            temp = {"round":i["round"],"score":i["score"]}
            current.append(temp)
            score_db[i["id"]] = current
        else:
            temp = [{"round":i["round"],"score":i["score"]}]
            score_db[i["id"]] = temp
    for id,val in score_db.items():
        print(f"{id}: {val}")
extraction()