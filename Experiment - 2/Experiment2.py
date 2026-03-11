pl = int(input("Enter Number of players: "))
for i in range (pl):
    print("Player",i+1)
    Runs = int(input("Enter runs scored: "))
    balls = int(input("Enter the no of balls faced: "))
    fours = int(input("Enter the no of fours scored: "))
    sixes = int(input("Enter the nos of sixes scored: "))
    wickets = int(input("Enter the no of wickets taken: "))
    runs_conc = int(input("Enter runs conceded: "))
    overs = int(input("Enter the no of overs bowled: "))
    catches = int(input("Enter the no of catches taken: "))
    
    sr = (Runs / balls) * 100
    print(sr)
    er = runs_conc / overs
    print(er)
    
    if (Runs >= 50 and sr >= 120):
        batter = "Excellent Batter"
    elif (Runs >= 30 and sr >= 100):
        batter = "Good Batter"
    elif (Runs >= 20):
        batter = "Average Batter"
    else:
        batter = "Poor Batter"
        
    if (wickets >= 3 and er <= 6):
        bowler = "Excellent Bowler"
    elif (wickets >= 2 and er <= 8):
        bowler = "Good Bowler"
    elif (wickets >= 1):
        bowler = "Average Bowler"
    else:
        bowler = "Poor Bowler"
        
    if (catches >= 2):
        fielder="Outstanding Fielder"
    elif (catches == 1):
        fielder=" Active fielder"
    else:
        fielder="Needs Improvement"
        
    if (batter == "Excellent Batter" and bowler == "Excellent Bowler"):
        overall="Star All-Rounder"
    elif (batter == "Good Batter" and bowler == "Good Bowler"):
        overall="Strong All-Rounder"
    elif (batter == "Good Batter" or bowler == "Good Bowler"):
        overall="Supporting All-Rounder"
    else:
        overall="Needs Improvement"
    
    print("Strike Rate:",sr)
    print("Economy Rate:",er)
    print("Batting Performance:",batter)
    print("Bowling Performance:",bowler)
    print("Feilding Performance:",fielder)
    print("Over All Rounder performance",overall)