import os
import csv
from collections import Counter

def read_file():
    directory = "/Users/Luke/Desktop/Python_work/T20_files/"
    file_name = "693009.csv"
    f = open("{}ntb_male_csv/".format(directory) + "{}".format(file_name), "r")
    csv_f = list(csv.reader(f))
    f.close()
    return csv_f

def info_grabber(csv_f):
    info_list = []
    info = {}
    #Adding useful information from spreadsheet to info list
    for row in csv_f:
        useless_rows = ["gender", "season", "event", "city"]
        if row[0] == "info":
            if row[1] not in useless_rows:
                info_list.append([row[1],row[2]])
        elif row[0] == "ball":
            break
    info_listed = [val for sublist in info_list for val in sublist]
    info["home team"] = info_listed[1]
    info["away team"] = info_listed[3]
    for i in range(3,len(info_listed)-1):
        if i % 2 == 0:
            info[info_listed[i]] = info_listed[i+1]
    print(info)

    #print(info)
    return info

def match_stats_grabber(csv_f, info):
    """column_headings = ["0 ball", "1 Innings", "2 Over", "3 Batting Team",
    "4 On-Strike Batter", "5 Off-Strike Batter", "6 Bowler", "7 Runs",
    "8 Extras", "9 Wides", "10 No-Ball", "11 Byes", "12 Leg-Byes",
    "13 Penalty", "14 How out", "15 Player Out"]"""
    #runs_breakdown = []
    runs = {}
    scorecard = {}
    balls = {}
    how_out = {}
    team_total = {}
    #extras =
    #bowlers_figures =
    runs_dict = {}
    for row in csv_f:
        if row[0] != "ball":
            continue
        if row[0] == "ball":
            batter = row[4]
            team = row[3]
            if team not in team_total:
                team_total[team] = int(row[7]) + int(row[8])
            elif team in team_total:
                team_total[team] += int(row[7]) + int(row[8])
            if batter not in runs:
                runs[batter] = int(row[7])
                scorecard[batter] = "{}".format(row[7])
            elif batter in runs:
                runs[batter] += int(row[7])
                scorecard[batter] += "{}".format(row[7])
            else:
                print("Error in adding {}'s total".format(batter))
                break
            #If not a wide, start counting deliveries
            if row[9] == "":
                if batter not in balls:
                    balls[batter] = 1
                elif batter in balls:
                    balls[batter] += 1
            elif batter not in balls:
                balls[batter] = 0
            if row[15] != "":
                how_out[batter] = row[14]

###BREAK FOR LOOP###
    # This loop adds creates a breakdown of how they scored their runs and returns
    # an array with the batters name and the breakdown
    team_scores = [score for team,score in team_total.items()]

#Neeed to add code for who batted first / won the toss and therefore if they
#win do they win by wickets or runs
#"""    for team,score in team_total.items():
#        if team_scores[0] > team_scores[1]:
#            winning_margin = "{} won by {} runs".format(info["Home team"])
#    #print(winning_margin)"""
    for batter_name,scores in scorecard.items():
        listed_scores = sorted(list(scores))
        breakdown = [[x,listed_scores.count(x)] for x in set(listed_scores)]
        #runs_breakdown.append([batter_name, sorted(breakdown)])
        runs_dict[batter_name] = sorted(breakdown)
    return



"""def file_checker():
    """"""Function checks whether file to add data to exists already or not,
    if not, it creates a new file ready""""""
    file_number = 1
    file_check= os.path.isfile("{}Match_Files/match{}.csv".format(directory, file_number))
    if file_check:
        return info_grabber()
    else:
        h = open("{}/Match_Files/match{}.csv".format(directory, file_number), "x")
        print("else")
        return info_grabber()"""


def build_file():
    print("hello world")

if __name__ == "__main__":
    x = read_file()
    y = info_grabber(x)
    (match_stats_grabber(x, y))
