import sys
import csv
import pandas as pd
import pprint

#Create List and populate with several values
neededCol_List = ["Player", "Pos", "Tm", "MP", "FGpct","3P","FTpct","TRB","AST","STL","BLK","TOV", "PTS"]
#Read data from an external file
playerStats = pd.read_csv("2019_20_NBAStats.csv", usecols=neededCol_List)
#Used pandas to add and subtract different columns to create a new column added into the list.
sumofStats = playerStats["3P"] + playerStats["TRB"] + playerStats["AST"] + playerStats["STL"] + playerStats["BLK"] - playerStats["TOV"] + playerStats["PTS"]
playerStats["Score"] = sumofStats

#Sets Panda DataFrame Column Options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.latex.longtable', True)
pd.options.display.width = 0


#loop designed to allow user to go back to main menu or leave the application.
def loop_Menu():
    print('------------------------------------------------------')
    loopmenu = input("Where would you like to go now? 1 for Main Menu, or 2 to exit:  ")
    if loopmenu == '1':
        main_Menu()
    elif loopmenu == '2':
        print('------------------------------------------------------')
        sys.exit("Thank you for choosing the NBA Manager!")
        print('------------------------------------------------------')
    else:
       print("invalid entry try again")
       loop_Menu()

#Sorts players for the "All Player Sort" Command. Additional limit based on a minimum of 15 minutes played on average per game.
def Player_sort():
    Playerall = pd.DataFrame(playerStats.sort_values('Player',ascending=True))
    PlayerFilter = Playerall[Playerall['MP'] > 15].reset_index(drop=True)
    print(PlayerFilter)
    loop_Menu()

#Allows Sorting by Category and limits player Selection to top 100 players. Additional limit based on a minimum of 15 minutes played on average per game.
def name_sort(sort_column):
    nameall = pd.DataFrame(playerStats.sort_values(sort_column,ascending=False,ignore_index=True))
    namefilter = nameall[nameall['MP'] > 15].reset_index(drop=True)
    namesort = namefilter.head(100)
    print(namesort)
    loop_Menu()

#Main Menu to Direct
def main_Menu():
        print('------------------------------------------------------')
        print("Welcome to The NBA Draft Manager!") 
        print("Please select an option from below to access our data:")
        print("------------------------------------------------------")
        print("1: View All Players")
        print("2: View All Players Sorted by Category")
        print("3: Exit")
        print('------------------------------------------------------')
        main_Menu.Selection = input("Choose a number from above: ")
        print('------------------------------------------------------')
        if main_Menu.Selection == '1':
            Player_sort()
        elif main_Menu.Selection == '2':
            searchCategory_Menu()
        elif main_Menu.Selection == '3':
            print('------------------------------------------------------')
            sys.exit("Thank you for choosing the NBA Manager!")
            print('------------------------------------------------------')
        else:
           print("")
           print("Please Try Again")
           print("")
           print("")
           main_Menu()


#Menu used to Sort Categories
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
    print('------------------------------------------------------')
    searchCategory_Menu.Selection = input("Choose a number from above: ")
    print('------------------------------------------------------')
    if searchCategory_Menu.Selection == '1':
            name_sort(neededCol_List[4])
    elif searchCategory_Menu.Selection == '2':
            name_sort(neededCol_List[5])
    elif searchCategory_Menu.Selection == '3':
            name_sort(neededCol_List[6])
    elif searchCategory_Menu.Selection == '4':
            name_sort(neededCol_List[7])
    elif searchCategory_Menu.Selection == '5':
            name_sort(neededCol_List[8])
    elif searchCategory_Menu.Selection == '6':
            name_sort(neededCol_List[9])
    elif searchCategory_Menu.Selection == '7':
            name_sort(neededCol_List[10])
    elif searchCategory_Menu.Selection == '8':
            name_sort(neededCol_List[11])
    elif searchCategory_Menu.Selection == '9':
            name_sort(neededCol_List[12])
    elif searchCategory_Menu.Selection == '10':
            main_Menu()  

#Calls Main_Menu function to run application.
main_Menu()




#Extra Features for TeamSearch to come later:
#def NBAteamplayer_sort(team_sorted):
    #nameall = pd.DataFrame(playerStats.sort_values('Player',ascending=False,ignore_index=True))
    #namefilter = nameall[nameall['Tm'] == team_sorted].reset_index(drop=True)
    #namesort = namefilter.head(100)
    #print(namesort)
    #loop_Menu()
#def searchTeam_Menu():
   # print("Please Choose the team abbreviations from the list below:")
   # team_sort()
    #input()
#def team_players(team):
 #   teamPlayers = pd.DataFrame(playerStats.sort_values('Player', ascending=False))
  #  teamPlayerFilter = teamPlayers[teamPlayers['Tm'] == team]
   # print(teamPlayerFilter)
#def team_sort():
 #   nba_Team = pd.DataFrame(playerStats, columns = ['Tm'])
  #  player_Team = pd.DataFrame.drop_duplicates(nba_Team,keep="first")
   # print(player_Team.sort_values('Tm',ascending=True,).reset_index(drop=True))
    #nbaplayer_Team()

#def team_sort():
    #nba_Team = pd.DataFrame(playerStats, columns = ['Tm'])
    #player_Team = pd.DataFrame.drop_duplicates(nba_Team,keep="first")
    #print(player_Team.sort_values('Tm',ascending=True,).reset_index(drop=True))
    #nbaplayer_Team()

#def nbaplayer_Team():
#    nba_Team = pd.DataFrame(playerStats, columns = ['Tm'])
#    player_Team = pd.DataFrame.drop_duplicates(nba_Team,keep="first")
#    team = input("Please select a team abbreviation from above. Select 10 for Main Menu or 11 to Exit the Program: ")
#    if team == '11':
#        print("Thank you for Choosing NBA Player Selector, Have a nice day")
#        main_Menu.loop = False
#    elif team == '10':
#        main_Menu()
#    elif team not in player_Team:
#        print("Invalid selection please try again")
#        NBAteamplayer_sort()
#    else:
#        NBAteamplayer_sort(team)
#Methods below for Sort mechanics
#def team_sort():
 #   nba_Team = pd.DataFrame(playerStats, columns = ['Tm'])
  #  player_Team = pd.DataFrame.drop_duplicates(nba_Team,keep="first")
   # print(player_Team.sort_values('Tm',ascending=True,).reset_index(drop=True))
    #team = input("Which Team would you like to view players for? Please choose an abbreviation above. Select 10 if you would like to return to the main menu or 11 to exit the program.")
    #return team
    #if team == '11':
    #   sys.exit("Thank you for Choosing NBA Player Selector, Have a nice day")
    #elif team == '10':
    #    main_Menu()
    #team_players(team)
#print(playerStats.drop_duplicates["Tm"])
        #print("2: View A Specific Teams Players")
                #elif main_Menu.Selection == '2':
        #    team_sort()