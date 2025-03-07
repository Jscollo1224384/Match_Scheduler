# Match_Scheduler
In the Barclay's Premier League for English football, there are 20 teams scattered across the country:

team                        location
----------------------------------------
Arsenal                     North London
Aston Villa                 Birmingham
Bournemouth                 Bournemouth
Brentford                   West London
Brighton and Hove Albion    Falmer
Chelsea                     West London
Crystal Palace              London
Everton                     Liverpool
Fulham                      West London
Ipswich Town                Ipswich
Leicester City              Leicester
Liverpool                   Liverpool
Manchester City             Manchester
Manchester United           Manchester
Newcastle United            Newcastle
Nottingham Forest           Nottingham
Southampton                 Southampton
Tottenham Hotspur           West London
West Ham United             North London
Wolverhampton Wanderers     Birmingham

Some teams share the same location. For example, Everton and Liverpool.

This is an interactive map showing the teams and their locations:
https://www.google.com/maps/d/viewer?mid=1WxTzRcZFS9WMLgBF8-_cg8NVX-c

In a full season, each team must play every other team twice -- once at home, once away -- totaling 38 matchweeks.

Your task is to create a schedule of matches for all 38 matchweeks.

In the schedule of matches for each matchweek, the first team in the pair is the home team.
-   Example:
    -   Liverpool v Everton
        -   Liverpool is the home team
        -   Everton is the visiting team


Requirements:
-   Each team pairing cannot play in successive matchweeks.
    -   Example:
        -   Liverpool plays Everton in matchweek N
        -   Everton cannot play Liverpool in either matchweek N-1 or matchweek N+1

-   No location can host more than one home match in any matchweek.
    -   Example:
        -   Liverpool and Everton both cannot play at home in the same matchweek


Bonus Features:
-   Display the home/away schedule for each team for their entire season.
    -   Example:
        -   Liverpool: H A A A H A H H A...
