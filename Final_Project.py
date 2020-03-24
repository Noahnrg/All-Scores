import Date_Functions as date
a = """
Noah Gomez & Connor Grace
Nov. 22, 2015
Cs - 1411 - 003
This program starts off with a search function and prints scores and game start times

INPUT -
            print("Examples A User May Search For...")
            print("- MLS games in 2 days")
            print("- BPL soccer games in 6 days")
            print("- nba scores from yesterday")
            print("- Show me German League scores 5 days ago")
            print("- Portland Timbers")
            print("- nba games 4 days from now")
            print("- All Soccer Games today")

OUTPUT
-   print(" ----------------------------------------------------------")
    print("|"        +         LeagueNAme       +           "|")
    print("|----------------------------------------------------------|")
    print("|"+F2.format("Last Match")+ "||"+F2.format("Next Match")+ "|")
    print("|----------------------------||----------------------------|")
    print("|                            ||                            |")
    print("|"  +F2.format(Team1) +      "||" + F2.format(Team1)  + "|")
    print("|"  +F2.format("vs")     +  "||" + F2.format(vs)       + "|")
    print("|"  +F2.format(Team2) +     "||" + F2.format(Team2)  + "|")
    print("|                            ||                            |")
    print("|                            ||                            |")
    print("|"  +F2.format(Ldate)    +  "||" +F2.format(Ndate)      + "|")
    print("|"  +F2.format(Linfo)    +  "||" +F2.format(Ninfo)      + "|")
    print("|                            ||                            |")
    print(" ----------------------------------------------------------")
Info- 
Both of us built this program together, i worked on mostly the function implementation
Connor mostly worked on building sets, dictionaries and HTML gathering
We both had a major part in this program together
This program requires all 4 files within the folder.





"""
#Our search Function
def search():
#Loops The Ability To Search Until User Enters "Exit"
    print("Type 'Help' for info and instructions.")
    print("Type 'Exit' To exit Program.")
    print()
    while True:
    #Checks if user wants to exit by typing "exit"
        searchRequest = input("Search: ").strip().lower()
        if "exit" in searchRequest: 
            return
        elif "@leagues" in searchRequest:
            print("Leagues you can search from:")
            print()
            print()
            print("Nation:  | League Name:")
            print("         |      " )
            print("France   | Ligue 1")
            print("USA      | Major League Soccer")
            print('England  | Barclays Premier League')
            print('Spain    | Spanish Primera (La Liga)')
            print('Germany  | Bundesliga')
            print('Italy    | Italian Serie A')
            print("\nSimply type in a country to get scores from their top league!")
            print("***** Want every game for a specific date? *****")
            print("Type in 'All games' as your search Request")
            print("\n\n")
        elif "@examples" in searchRequest:
            print()
            print("Examples A User May Search For...")
            print("- MLS games in 2 days")
            print("- BPL soccer games in 6 days")
            print("- nba scores from yesterday")
            print("- Show me German League scores 5 days ago")
            print("- Portland Timbers")
            print("- nba games 4 days from now")
            print("- All Soccer Games today")
            print()
            print("*Please feel free to mix and match search terms :)")
            print()
        elif "help" in searchRequest:
            printHelp()
            
        elif "@test" in searchRequest:
            testConnection()
        elif "help" in searchRequest:
            print("Welcome To All_Scores!\nYou can")
        elif "nba" in searchRequest:
            nbaScores(date.searchForDate(searchRequest))
        else:
            searchWith(searchRequest)
            a =  """
            try:
                searchWith(searchRequest)
            except:
                print("Could not find Request")"""
#Tests our connection to google for a test case           
def testConnection():
    try:
        a = getSoup("http://www.google.com").title
        print("Test Successful, Your Connection is good.\n")
    except:
        print("Test Unsuccessful, Error connecting to server\n")
        
def printHelp():
    print("------------------------------")
    print(("|{:^28s}|").format("Welcome to All_Scores!"))
    print("------------------------------")
    print()
    print("This program provides Scores from the world's 6 Top Soccer Leagues and scores from the NBA.")
    print("This program only needs What league you want into the search Box.")
    print("If you want a specific date type it in as well!\n(If you don't type in a date it'll assume the date you want is today)")
    print()
    print("***** Need more info? *****")
    print("Type     '@test'    to test your connection.")
    print("Type   '@leagues'   for the top 6 Leagues you Can Search From.")
    print("Type   '@examples'  if you would like Examples for Input")
    print()
            
#Function that gathers and prints nba scores using a date for input
def nbaScores(inputDate):
    url_date = date.URLDateFrom(int(inputDate))
    year,month,day = str(url_date)[0:4],str(url_date)[4:6],str(url_date)[6:]
    allSoup = getSoup("http://www.usatoday.com/sports/nba/scores/"+year+"/"+month+"/"+day+"/")
    allScoresSoup = searchSoup(allSoup,"article","id","scorespage")
    timeSoup = findAll(allScoresSoup,"li","class","outcome first",100)
    scoresSoup = findAll(allScoresSoup,"li","class","outcomes total",100)
    actualTime = []
    for thing in timeSoup:
        b = str(thing).replace('<li class="outcome first">',"").replace('</li>','').split(':')
        try:
            actualTime.append(str(str(int(b[0])-1)+":"+str(b[1])).replace("ET","CT"))
        except:
            actualTime.append("")
        
    count,z = 1,0
    vsList = []
    if not scoresSoup:
        if inputDate == 0:
            when = "today"
        elif inputDate < 0:
            when = str((int(inputDate) * -1)).strip() + " days ago"
        else:
            when =  "in "+str(inputDate).strip()+" days"
            print("There are no games " + when)
    for (record,score) in zip(findAll(allScoresSoup,"ul",'class',"basketball",100),scoresSoup):
        if count == 1:
            vsList.append([str(record.text).replace(" ","").strip(),score])
            count += 1
        else:
            vsList.append([str(record.text).replace(" ","").strip(),score])
            print2Teams(vsList,str(actualTime[z]))
            print("____________________________________________________________")
            z += 1
            count = 1
            vsList = []
    
#Easy function that takes in a start time and team info and prints it
def print2Teams(vList,startTime):
    dictionary = BBallDictionary()
    team1 = vList[0]
    team2 = vList[1]
    team1Name = BBallDictionary()[team1[0].split("\n")[0]]
    team2Name = BBallDictionary()[team2[0].split("\n")[0]]
    t1 = str(team1[1])[27:].replace('</li>',"").strip()
    t2 = str(team2[1])[27:].replace('</li>',"").strip()
    info = ''
    if t1 =="" and t2 == "":
        info= "Game Starts at "+startTime
    else:
        info = "("+str(t1)+"-"+str(t2)+")"
    printGame(team1Name,team2Name,info)
#Gathers and prints information gatehred from espn about soccer scores           
def print_Team_Info(teamName):
    Soup = getSoup(getURLForTeam(teamName,"fixtures"))
    teamContent = searchSoup(Soup,"div","id","club-fixtures")
    team_Recent_Soup = searchSoup(teamContent,"div","class","recent-matches")
    lastMatch = searchSoup(team_Recent_Soup,"div","class","last-match").text.replace("\n"," ")
    nextMatch = searchSoup(team_Recent_Soup,"div","class","next-match").text.replace("\n"," ")
    l = lastMatch.split("   ")
    n = nextMatch.split("   ")
    Ndate,Ninfo,mid = "","",""
    Nteam = ["No Upcoming","Matches"]
    if nextMatch.strip() != "":
        Ndate = ""+n[0].split("Match - ")[1].strip()
        mid = "vs"
        Nteam = [n[2].strip(),n[3].strip()]
        if n[5].strip() == "":
            Ninfo = " "+str(date.UTC2CT(n[7].strip().split(" ")[0]))
            gT = ""
        else:
            Ninfo = n[4].strip() +" - "+ n[5].strip()
            ngT = n[6]
            
    Ldate = ""+l[0].split("Match - ")[1].strip()
    lgT = l[6]
    Linfo = l[4].strip() +" - "+ l[5].strip()
    Lteam = [l[2].strip(),l[3].strip()]
    F5 = "{:^58s}"
    F2 = "{:^28s}"
    print(" ----------------------------------------------------------")
    print("|"        +         F5.format(teamName)       +           "|")
    print("|----------------------------------------------------------|")
    print("|"+F2.format("Last Match")+ "||"+F2.format("Next Match")+ "|")
    print("|----------------------------||----------------------------|")
    print("|                            ||                            |")
    print("|"  +F2.format(Lteam[0]) +  "||" + F2.format(Nteam[0])  + "|")
    print("|"  +F2.format("vs")     +  "||" + F2.format(mid)       + "|")
    print("|"  +F2.format(Lteam[1]) +  "||" + F2.format(Nteam[1])  + "|")
    print("|                            ||                            |")
    print("|                            ||                            |")
    print("|"  +F2.format(Ldate)    +  "||" +F2.format(Ndate)      + "|")
    print("|"  +F2.format(Linfo)    +  "||" +F2.format(Ninfo)      + "|")
    print("|                            ||                            |")
    print(" ----------------------------------------------------------")
#returns a string that the program uses to gather info   
def getURLForTeam(teamName,section):
    #Key = Team Name   /    Value = URL Access Numer
    MLS_URL = {"Chicago Fire":"182","Columbus Crew SC":"183",
"DC United":"193","Montreal Impact":"9720","New England Revolution":"189",
"New York City FC":"17606", "New York Red Bulls":"190","LA Galaxy":"187",
"Orlando City SC":"12011","Toronto FC":"7318","Philadelphia Union":"10739",
"Colorado Rapids":"184","FC Dallas":"185","Houston Dynamo" :"6077",
"Portland Timbers":"9723","Real Salt Lake":"4771",
"San Jose Earthquakes":"191","Seattle Sounders FC":"9726",
"Sporting Kansas City":"186","Vancouver Whitecaps FC":"9727"}
    return ("http://www.espnfc.us/club/"+lowerAndStrip(teamName).replace(" ","-")+"/"+MLS_URL[teamName]+"/"+section)
#uses a external module to help gather html code from espm
def getSoup(URL): #returns Soup
    from importlib import machinery as m
    bsFolder = m.SourceFileLoader('bs4',str(getPaths()[0])).load_module()
    request = m.SourceFileLoader('get',str(getPaths()[1])).load_module()
    return (bsFolder.BeautifulSoup(request.get(URL).content,"html.parser"))
#Prints information
def showScores(dateChange = 0,team = "", league = ""):
    a = date.URLDateFrom(dateChange)
#This Exception Checks The Connection With The Website
    soup = getSoup(("http://www.espnfc.us/scores?date="+str(a)))
    allContent = searchSoup(soup,"div","id","score-leagues") #Finds the HTML box with the All of the Scores
    allLeagues = findAll(allContent,"div","class","score-league",8) #Finds all Leagues and saves in a List
    if league == "All":
        leagues = allLeagues
    else:
        leagues = getLeagues(allLeagues,league)
    try:
        printLeagues(leagues,printedDate(a))
    except:
         print("\nThere are no "+league+" Games on " + printedDate(a+"\n") )
#Searches for a specific type of html code           
def searchSoup(soup,str1,str2,str3): #Finds the first instance of The Parameters
    return soup.find(str1,{str2:str3})
#Finds all the html code containting specific code that we are looking for
def findAll(content,str1,str2,str3,searchLimit): #Finds all instance of the Parameters with a limit
    return content.find_all(str1,{str2:str3},limit = searchLimit)
#Prints 1 of the 12 months
def printedDate(URLdate):
    monthList = ["","January","Febuary","March",
              "April","May","June","July","August",
              "September","October","November","December"]
    return (monthList[(int(URLdate[4:6]))] +" "+URLdate[6:])
#our "search tool" and returns a specific league
def getLeague():
    while True:           
        request = input("\nWhat league scores do you wish to view?\n-> ").lower().replace(" ","")
        if request in "majorleaguesoccermls":                  #MLS
            return "Major League Soccer"
        elif request in "bplbarclayspremierleague":     #Primier League
            return 'Barclays Premier League'
        elif request in "spanishprimeralaligaspanishleague":   #La Liga
            return 'Spanish Primera'
        elif request in "germanbundesligagermanleague":        #Bundesliga
            return "German Bundesliga"
        elif request in "italianserieaitalyleagueitalianleague": #Italian Serie A
            return 'Italian Serie A'
        elif request in "frenchligue1frenchleague1french1":    #Ligue 1
            return 'French Ligue 1'
        elif "all" in searchString:
            return "All"
        else:
            print("That search didn't return any leagues...\nPlease Try Again.")
#Uses a string and returns info on a league
def getLeagues(leagueList,requests):
    leagueReturn = []
    for league in leagueList:
        leagueName = league.contents[2].text.replace("\n"," ").strip()
        if requests in leagueName:
            leagueReturn.append(league)
            return leagueReturn
#Allow us to use our external module
def getPaths():
    from os import getcwd as whereAmI
    return [(str(whereAmI()) + "/customModule/__init__.py"),(str(whereAmI()) + "/requests/__init__.py")]
#Prints information
def printLeagues(leagueList,actualDate):
    F = "{:^60s}"
    for league in leagueList:
        gameList = league.find_all("div",{"class":"score-content"})
        leagueName = league.contents[2].text.replace("\n"," ")
        print("\n")
        print("------------------------------------------------------------")
        print(F.format((leagueName.split(" (")[0]) + " On "+ actualDate))
        print("------------------------------------------------------------")
        for game in gameList:
            teamList = game.contents[1].text.strip().split("\n\n\n")            
            print("\n"+F.format(teamList[0]+" vs. " + teamList[1]))
            try:
                scoreList = game.contents[3].text.strip().split("\n\n\n")
                print(F.format(scoreList[0]+" - " + scoreList[1]))
            except:
                print()
            try:
                gameInfo = str(formatGameInfo(xStrip(game.contents[5].text)))
                print(F.format(gameInfo))
            except:
                print("",end="")               
            print("____________________________________________________________")
#Easy function that simply prints information
def printGame(team1,team2,info):
    print("____________________________________________________________")
    print()
    F = "{:^60s}"
    try:
        print(F.format(team1+" vs. " + team2))
    except:
        print()
    print()
    try:
        print(F.format(info))
    except:
        print()
#Prints organized information    
def formatGameInfo(info):
    infoList = info.split(" ")
    timeString,channel = "",""
    if infoList[0].upper().strip() == "LIVE":
            return infoList[1].strip()
    for thing in infoList:
        if ":" in thing:
            timeString = thing
        elif thing == "AM" or thing == "PM":
            timeString += thing
        elif "ESPN" in thing.upper():
            channel = " on " +thing
    centralTime = date.UTC2CT(timeString) #UTC time conversion to Central Time
    return centralTime +channel
#Strips all whitespace
def xStrip(string):
    return str(string.strip().replace("\n"," ").strip())
#Another search Function for us to gather input form the user
def searchForLeague(searchString):
        if "mls" in searchString or "major" in searchString:       #MLS
            return "Major League Soccer"
        
        elif "barclay" in searchString or "bpl"in searchString or "premier" in searchString:     #Primier League
            return 'Barclays Premier League'

        elif "spanish" in searchString or "laliga" in searchString.replace(" ","") or "primera" in searchString:   #La Liga
            return 'Spanish Primera'
        
        elif "german" in searchString or "bundesliga" in searchString:        #Bundesliga
            return "German Bundesliga"
        
        elif "italian" in searchString or "serie" in searchString or "italy" in searchString: #Italian Serie A
            return 'Italian Serie A'
        
        elif "ligue1"  in searchString or "french"  in searchString.replace(" ",""):    #Ligue 1
            return 'French Ligue 1'

        elif "all" in searchString and "dallas" not in searchString:
            return "All"
        else:
            return ""
#Returns an int that we use for  dates
def searchWith(searchString):
    league = searchForLeague(searchString)
    date2 = date.searchForDate(searchString)
    if date2 == 0:
        when = "today"
    elif date2 == 1:
        when = "tomorrow"
    elif date2 == -1:
        when = "yesterday"
    elif date2 < 0:
        when = str((int(date2) * -1)).strip() + " days ago"
    else:
        when =  "in "+str(date2).strip()+" days"
    if league != "":
        print("\nSearching for "+league + " Games " + when+"....")
        showScores(date2,"",league)
    
    elif league == "":
        team = getTeam(searchString)
        if team == "":
            print("Could not find Request")
        else:
            print_Team_Info(getTeam(searchString))
#Dictionary that contains a specific team info        
def getTeam(stringInput):
    searchList = stripAndSplit(stringInput," ")
#Eastern Conference
    MLS_EC = [["Chicago Fire","chicago","fire"],
["Columbus Crew SC","columbus","crew"],
["DC United","dc","united"],
["Montreal Impact","montreal","impact"],
["New England Revolution","england","revolution"],
["New York City FC","city"],
["New York Red Bulls","red","bulls"],
["Orlando City SC","orlando"],
["Philadelphia Union","philadelhia","union"],
["Toronto FC","toronto"]]
#Western Conference
    MLS_WC = [["Colorado Rapids","colorado","rapids"],
["Houston Dynamo","houston","dynamo"],
["LA Galaxy","la","galaxy"],
["FC Dallas","dallas"],
["Portland Timbers","portland","timbers"],
["Real Salt Lake","salt","lake"],
["San Jose Earthquakes","san","jose","earthquakes"],
["Seattle Sounders FC","seattle","sounders"],
["Sporting Kansas City","sporting","kansas"],
["Vancouver Whitecaps FC","vancouver","whitecaps"]]
    for searchRequest in searchList:
        for x in range(0,len(MLS_WC)):
            if searchRequest in MLS_WC[x]:
                return MLS_WC[x][0]
        for x in range(0,len(MLS_EC)):
            if searchRequest in MLS_EC[x]:
                return MLS_EC[x][0]
    else:
        return ""
#Dictionary that contains a specific team info
def BBallDictionary():
    return {'ATL' : 'Atlanta Hawks',
'BRK':"Brooklyn Nets",'BOS' : 'Boston Celtics' ,'BUF': 'Buffalo Braves'  ,
'CHA':"Charlotte Hornets",'CHI' :'Chicago Bulls'  ,'CIN': 'Cincinnati Royals' ,
'CLE': 'Cleveland Cavaliers', 'DAL': 'Dallas Mavericks' ,'DEN': 'Denver Nuggets' ,
'DET': 'Detroit Pistons' ,'FTW': 'Fort Wayne Pistons', 'GSW': 'Golden State Warriors' ,
'HOU': 'Houston Rockets' ,'IND': 'Indiana Pacers' ,'KCK': 'Kansas City Kings' ,
'KCO': 'Kansas City-Omaha Kings' ,'LAC': 'Los Angeles Clippers' ,'LAL': 'Los Angeles Lakers' ,
'MEM': 'Memphis Grizzlies' ,'MIA': 'Miami Heat' ,'MIL': 'Milwaukee Bucks' ,
'MIN': 'Minnesota Timberwolves' ,'MLH': 'Milwaukee Hawks' ,'MPL': 'Minneapolis Lakers', 
'NJN': 'New Jersey Nets' ,'NOP': 'New Orleans Pelicans', 'NOJ': 'New Orleans Jazz' ,
'NOK':'New Orleans-Oklahoma City Hornets' ,'NY': 'New York Knicks' ,'NYN': 'New York Nets' ,
'OKC': 'Oklahoma City Thunder' ,'ORL': 'Orlando Magic' ,'PHI': 'Philadelphia 76ers' ,
'PHO': 'Phoenix Suns' ,'PHW': 'Philadelphia Warriors', 'POR': 'Portland Trail Blazers', 
'ROC': 'Rochester Royals' ,'SAC': 'Sacramento Kings' ,'SAN': 'San Antonio Spurs' ,
'SDC': 'San Diego Clippers' ,'SDR': 'San Diego Rockets' ,'SEA': 'Seattle SuperSonics', 
'SFW': 'San Francisco Warriors', 'STL': 'St. Louis Hawks' ,'SYR': 'Syracuse Nationals', 
'TOR': 'Toronto Raptors' ,'TRI': 'Tri-Cities Blackhawks', 'UTA': 'Utah Jazz' ,
'VAN': 'Vancouver Grizzlies', 'WAB': 'Washington Bullets', 'WAS': 'Washington Wizards'}

def stripAndSplit(string,splitByThis):
    return string.strip().split(splitByThis)
def lowerAndStrip(string):
    return string.lower().strip()
    
search()

