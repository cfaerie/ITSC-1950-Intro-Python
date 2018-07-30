#Program Name: Game Score Average
#Date: 1/18/2013
#Developer: Rachel Sanford

#Program will take input of 2 game scores from user
#and give the user the average

score1 = raw_input("What's your score in round one?")
score2 = raw_input("What's your score in round two?")
score1 = float(score1)
score2 = float(score2)
sum_score = score1 + score2
average_score = sum_score/2
print "Your average score over two rounds was", average_score
