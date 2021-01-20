print("The way to win is to have the most points! Theif gives you -2 points,theif2 gives you -1 points and gold gives you 1.5 points. Assasin gives each player 1.5 points except for the person who got the assasin! Gold2 gives you 2 points and others -0.5 points.Robber gives you -1 points if you the robber it and others 1 point. Piggy gives 0 points and doesn't let you try again!")
print("It's a number from 1-30.")
print("Police has came out!")
print("If you get police you get 2 points and the other players lose 0.5 points. Gold only gives you 2 points. No harm for the other players.")
print("Can't think of a new update.")
while True:
  import random
  gold = random.randint(1,30)
  theif = random.randint(1,30)
  theif2 = random.randint(1,30)
  assasin = random.randint(1,30)
  gold2 = random.randint(1,30)
  robber = random.randint(1,30)
  piggy = random.randint(1,30)
  police = random.randint(1,30)
  number2 = int(input("Find the correct number.:"))
  if number2 < 1:
    print("Please type a different number.")
  if number2 > 30:
    print("Please type a different number.")
  if number2 == gold:
    print("You won!")
    print("You found the gold and you get 1.5 points!")
    break
  if number2 == theif:
    print("You lose!")
    print("You're money was stolen by theif and you lose 2 points!")
    break
  if number2 == theif2:
    print("You lose!")
    print("You're money was stolen by theif2 and you lose 1 point!")
    break
  if number2 == assasin:
    print("You lose!")
    print("Assasin killed you.")
    print("You get 0 points!")
    print("Each player gets 1.5 points except you!")
    break
  if number2 == gold2:
    print("You found the gold2!")
    print("You get 2 points!")
    break
  if number2 == robber:
    print("You lose!")
    print("You're money was stolen by robber!")
    break
  if number2 == piggy:
    print("You get piggy so you get 0 points and other players get 0 points.")
    break
  if number2 == police:
    print("You get police so you get 2 points and the others lose 0.5 points.")
    break
  else:
    print("Try again.")