### Variables and Names
 
1. Place a comment above each variable assignment explaining what is being calculated and what is being stored in the variable.
# Assign the team name to the variable 'team'
team = "Toronto Blue Jays"

# Assign the current date to the variable 'current_date'
current_date = "July 18, 2021"

# Assign the player's name to the variable 'player'
player = "Vladimir Guerrero Jr."

# Assign the number of home runs the player has hit in the season to the variable 'home_runs_to_date'
home_runs_to_date = 31

# Assign the number of games the player has played in the season to the variable 'games_played'
games_played = 88

# Assign the number of total games per MLB season to the variable 'total_season_games'
total_season_games = 162

# Assign the MLB record for most home runs in a season to the variale 'home_run_record'
home_run_record = 73


# Subtract the total games per season by the amount of games the player has played so far to get the number of remaining games
games_remaining = total_season_games - games_played

# Divide the player's home runs in the season by the amount of games they played to get the average home runs per game
home_runs_per_game = home_runs_to_date / games_played

# Multiply the player's average home runs per game by the total games per season to project the player's total home runs in the season
projected_home_runs = home_runs_per_game * total_season_games

# Determine if the player can break the home run record if the projected total home runs in the season is greater than the home run record 
can_break_record = projected_home_runs > home_run_record


print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {home_runs_per_game} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {projected_home_runs} home runs this season.")

2. My code has two empty lines in it. Explain why I might have done this and explain how I chose to group specific lines of code.
# The code has empty lines to make the code easier to read, because different parts of the code are separated 
# The first group assigns simple numerical values to the variables
# The second group uses the variables from the first group to calculate new variables
# The third group prints the conclusion based on the calculations from the previous groups

3. Use the round() function to tidy up the printing of the values (not the values being stored in the variables).

print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"{player} is projected to hit {round (projected_home_runs, 2)} home runs this season.")

4. Without knowing any of the values stored in the variables, how do you know the line games_remaining = total_season_games - games_played must be correct?
# The total amount of games in the season is stored as 'total_season_games' and the amount of games the player has played so far is stored as 'games_played'
# If the total number of games per season is subtracted by the amount of games the player has played so far, the result will be the amount of remaining games in the season
