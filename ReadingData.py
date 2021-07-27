import sys
import csv
import pandas as pd

neededCol_List = ["Player", "Pos", "Tm", "MP", "FGpct","3P","FTpct","TRB","AST","STL","BLK","TOV", "PTS"]
playerStats = pd.read_csv("2019_20_NBAStats.csv", usecols=neededCol_List)
#for col in playerStats.columns:
    #print(col)

#nba_Team = pd.DataFrame(playerStats, columns = ['Tm'])
#old_player_Team = pd.DataFrame.drop_duplicates(nba_Team,keep="first")

def nba_TeamSearch():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    nba_Team = pd.DataFrame(playerStats, columns = ['Tm'])
    player_Team = pd.DataFrame.drop_duplicates(nba_Team,keep="first")
    print(player_Team.sort_values('Tm',ascending=True,))

def NBAPlayer_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    Playerall = pd.DataFrame(playerStats.sort_values('Player',ascending=False,ignore_index=True))
    PlayerFilter = Playerall[Playerall['MP'] > 15]
    PlayerSort = pd.DataFrame.head(PlayerFilter, 100)
    print(PlayerSort)


def FGpct_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    FGAall = pd.DataFrame(playerStats.sort_values('FGpct',ascending=False,ignore_index=True))
    FGFilter = FGAall[FGAall['MP'] > 15]
    FGSort = pd.DataFrame.head(FGFilter, 100)
    print(FGSort)

def ThreePointer_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    ThreePAll = pd.DataFrame(playerStats.sort_values('3P',ascending=False,ignore_index=True))
    ThreePFilter = ThreePAll[ThreePAll['MP'] > 15]
    ThreePSort = pd.DataFrame.head(ThreePFilter, 100)
    print(ThreePSort)

def FTpct_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    FTAall = pd.DataFrame(playerStats.sort_values('FTpct',ascending=False,ignore_index=True))
    FTFilter = FTAall[FTAall['MP'] > 15]
    FTSort = pd.DataFrame.head(FTFilter, 100)
    print(FTSort)

def TRB_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    TRBall = pd.DataFrame(playerStats.sort_values('TRB',ascending=False,ignore_index=True))
    TRBFilter = TRBall[TRBall['MP'] > 15]
    TRBSort = pd.DataFrame.head(TRBFilter, 100)
    print(TRBSort)

def AST_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    Astall = pd.DataFrame(playerStats.sort_values('Ast',ascending=False,ignore_index=True))
    AstFilter = Astall[Astall['MP'] > 15]
    AstSort = pd.DataFrame.head(AstFilter, 100)
    print(AstSort)
    
def STL_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    STLall = pd.DataFrame(playerStats.sort_values('STL',ascending=False,ignore_index=True))
    STLFilter = STLall[STLall['MP'] > 15]
    STLSort = pd.DataFrame.head(STLFilter, 100)
    print(STLSort)

def BLK_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    BLKall = pd.DataFrame(playerStats.sort_values('BLK',ascending=False,ignore_index=True))
    BLKFilter = BLKall[BLKall['MP'] > 15]
    BLKSort = pd.DataFrame.head(BLKFilter, 100)
    print(BLKSort)

def TOV_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    TOVall = pd.DataFrame(playerStats.sort_values('TOV',ascending=False,ignore_index=True))
    TOVFilter = TOVall[TOVall['MP'] > 15]
    TOVSort = pd.DataFrame.head(TOVFilter, 100)
    print(TOVSort)

def PTS_sort():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.latex.longtable', True)
    PTSall = pd.DataFrame(playerStats.sort_values('PTS',ascending=False,ignore_index=True))
    PTSFilter = PTSall[PTSall['MP'] > 15]
    PTSSort = pd.DataFrame.head(PTSFilter, 100)
    print(PTSSort)

    
def main_Menu():
    print("Welcome to The NBA Draft Manager!") 
    print("Please select an option from below to access our data:")
    print("----------------------------------")
    print("1: View All Players")
    print("2: View A Specific Teams Players")
    print("3: View All Players Sorted by Category")
    print("4: Search for Player by Last Name")
    print("5: Search for Player Position")
    print("6: Exit")
    main_Menu.Selection = input("Choose a number from above: ")
    if main_Menu.Selection == '1':
        NBAPlayer_sort()
    elif main_Menu.Selection == '2':
        Team_sort()
    elif main_Menu.Selection == '3':
        searchCategory_Menu()
    elif main_Menu.Selection == '4':
        NBAPlayer_sort()
    elif main_Menu.Selection == '5':
        NBAPlayer_sort()
    elif main_Menu.Selection == '6':
        NBAPlayer_sort()



def allPlayer_Menu():
    print("Please select an option below to continue:")
    print("1: Search for Specific Teams Players")
    print("2: Sort by Category")
    print("3: Search Player by Last Name")
    print("4: Return to Main Menu")
    input()

def searchCategory_Menu():
    print("What Category would you like to Sort By?")
    print("1. FieldGoal pct")
    print("2. Three Pointers")
    print("3. FreeThrow pct")
    print("4. Total Rebounds")
    print("5. Assists")
    print("6. Steals")
    print("7. Blocks")
    print("8. Turnovers")
    print("9. Points")
    print("10. Main Menu")
    searchCategory_Menu.Selection = input("Choose a number from above: ")
    if searchCategory_Menu.Selection == '1':
            FGpct_sort()
    elif searchCategory_Menu.Selection == '2':
            ThreePointer_sort()
    elif searchCategory_Menu.Selection == '3':
            FTpct_sortt()
    elif searchCategory_Menu.Selection == '4':
            TRB_sort()
    elif searchCategory_Menu.Selection == '5':
            AST_sort()
    elif searchCategory_Menu.Selection == '6':
            STL_sort()
    elif searchCategory_Menu.Selection == '7':
            BLK_sort()
    elif searchCategory_Menu.Selection == '8':
            TOV_sort()
    elif SsearchCategory_Menu.Selection == '9':
            PTS_sort()
    elif searchCategory_Menu.Selection == '10':
            main_Menu()

def searchTeam_Menu():
    print("Please Choose the team abbreviations from the list below:")
    nba_TeamSearch()
    input()




#print(playerStats.drop_duplicates["Tm"])


#ThreePointer()
#FTpct()
#TRB()

main_Menu()
#allPlayer_Menu()
#searchCategory_Menu()
#searchTeam_Menu()
#FGpct()

#print(playerStats)
