import os
import csv

def read_file():
    directory = "/Users/Luke/Desktop/Python_work/T20_files/"
    file_name = "693009.csv"
    f = open("{}ntb_male_csv/".format(directory) + "{}".format(file_name), "r")
    csv_f = list(csv.reader(f))
    f.close()
    return csv_f

def info_grabber(csv_f):
    info = []
    #Adding useful information from spreadsheet to info list
    for row in csv_f:
        useless_rows = ["gender", "season", "event", "city"]
        if row[0] == "info":
            if row[1] == 'team' and row[1] not in info:
                info.append(['Team 1', row[2]])
            elif row[1] == 'team' and row[1] not in info:
                info.append(['Team 2', row[2]])
            elif row[1] not in useless_rows:
                info.append([row[1],row[2]])
        else:
            break
    return info

def match_stats_grabber(csv_f, info):
    """column_headings = ["0 ball", "1 Innings", "2 Over", "3 Batting Team",
    "4 On-Strike Batter", "5 Off-Strike Batter", "6 Bowler", "7 Runs",
    "8 Extras", "9 Wides", "10 No-Ball", "11 Byes", "12 Leg-Byes",
    "13 Penalty", "14 How out", "15 Player Out"]"""
    runs = {}
    scorecard = {}
    runs_breakdown = {"Name": "" , 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    balls = {}
    how_out = {}
    batting_stats = runs, balls, how_out
    name = batting_stats
    for row in csv_f:
        if row[0] != "ball":
            continue
        if row[0] == "ball":
            batter = row[4]
            if batter not in runs:
                runs[batter] = int(row[7])
                scorecard[batter] = "{}".format(row[7])
            elif batter in runs:
                runs[batter] += int(row[7])
                scorecard[batter] += "{}".format(row[7])
    #        for name, scores in scorecard.items():
    #            for score in scores:
    #                runs_breakdown[batter] = runs_breakdown.get(score, 0)+1
#
#                    break
#                break
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

###BREAK FOR LOOP###
    deliveries = sum(balls.values())
    print(runs_breakdown)
    return scorecard

def score_breakdown(scorecard)
    for batter_name,scores in scorecard.items():
        runs_breakdown["Name"] = batter_name
        #for score in scores:

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

"""def info_grabber(rows):
    #irrelevant_rows = [3,4,8]
    useless_rows = ["gender", "season", "event", "city"]
    info = {}
    for row in rows:
        print(info)
        if row[0] == "version":
            continue
        elif row[0] == "info":
            if row[1] in useless_rows:
                continue
            else:
                #current issue is team 2 is overwriting team 1 in dict
                info[row[1]] = row[2]
        else:
            break
    return info"""


def build_file():
    print("hello world")

if __name__ == "__main__":
    x = read_file()
    y = info_grabber(x)
    (match_stats_grabber(x, y))
