#!/usr/bin/python3
import sys

# You need the following enabled for this script to work properly:
# LADDERLOG_WRITE_NUM_HUMANS 1
# LADDERLOG_WRITE_TEAM_PLAYER_ADDED 1
# LADDERLOG_WRITE_TEAM_PLAYER_REMOVED 1
# LADDERLOG_WRITE_ROUND_COMMENCING 1

# LADDERLOG_WRITE_NEXT_ROUND 1
# LADDERLOG_WRITE_ROUND_SCORE 1
# LADDERLOG_WRITE_MATCH_SCORE 1
# LADDERLOG_WRITE_NEW_MATCH 1
# LADDERLOG_WRITE_PLAYER_RENAMED 1
# LADDERLOG_WRITE_PLAYER_LEFT 1

print("WAIT_FOR_EXTERNAL_SCRIPT 1\nWAIT_FOR_EXTERNAL_SCRIPT_TIMEOUT 1");

scores = {}

print_round_scores = 0
num_players = -1
while True:
    line = input()
    try:
        if line.startswith("TEAM_PLAYER_ADDED"):
            num_players += 1
        elif line.startswith("TEAM_PLAYER_REMOVED"):
            num_players -= 1
            parsed_line = line.split()
            if parsed_line[2]:
                username = parsed_line[2]
        elif line.startswith('NUM_HUMANS'):
            parsed_line = line.split()
            if num_players == -1:
                line = "ROUND_COMMENCING"
            # make sure num_players has a second argument passed to it
            if len(parsed_line) >= 1:
                num_players = int(parsed_line[1])

        if line.startswith("ROUND_COMMENCING"):
            if num_players != -1:
                if num_players > 10:
                    num_players = 10
                elif num_players < 2:
                    num_players = 2
                print("MAP_FILE Titanoboa/sumobar/dynamic-0."+str(num_players)+".aamap.xml")
                print("SIZE_FACTOR 1")
 
        #if line.startswith("PLAYER_LEFT "):
            #parsed_line = line.split()
            #username = parsed_line[1]
            #if username in scores:
                #if scores[username] != 0:
                    #print("CONSOLE_MESSAGE Player " + username + " left with a score of: " + str(scores.pop(username)))
                #else:
                    #scores.pop(username)

        #if line.startswith("PLAYER_RENAMED "):
            #parsed_line = line.split()
            #old_username = parsed_line[1]
            #new_username = parsed_line[2]
            #if old_username in scores:
                #scores[new_username] = scores.pop(old_username)

        #if line.startswith("ROUND_SCORE "):
            #parsed_line = line.split()
            #username = parsed_line[2]
            #score = int(parsed_line[1])
            #if not username in scores:
                #scores[username] = score
            #else:
                #scores[username] += score

        #if line.startswith("MATCH_SCORE "):
            #if not match_scores:
                #print("CONSOLE_MESSAGE Match scores:")
            #parsed_line = line.split()
            #username = parsed_line[2]
            #score = int(parsed_line[1])
            #if score != 0: 
                #print("CONSOLE_MESSAGE .. " + username + ": " + str(score))
            #match_scores = True
        #else:
            #match_scores = False

        #if line.startswith("NEW_MATCH "):
            #scores = {}

    except:
        print("CONSOLE_MESSAGE Error: " + str(sys.exc_info()[0]) + ":" + str(sys.exc_info()[1]))

