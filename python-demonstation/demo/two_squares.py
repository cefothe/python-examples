import random

def football_quiz():
    footballers = [
        {"name": "Lionel Messi", "clubs": ["Barcelona", "Paris Saint-Germain"]},
        {"name": "Cristiano Ronaldo", "clubs": ["Manchester United", "Real Madrid", "Juventus"]},
        {"name": "Robert Lewandowski", "clubs": ["Bayern Munich", "Botev Plovdiv"]},
        {"name": "Erling Haaland", "clubs": ["Borussia Dortmund","Mancester City"]},
        {"name": "Kylian Mbappe", "clubs": ["Paris Saint-Germain", "Real Madrid"]},
        {"name": "Bruno Fernandes", "clubs": ["Sporting CP", "Manchester United"]},
        {"name": "Kevin De Bruyne", "clubs": ["Manchester City", "Borussia Dortmund"]},
        {"name": "N'Golo Kanté", "clubs": ["Chelsea", "Man city"]},
         {"name": "Andrés Iniesta", "clubs": ["Barcelona", "Vissel Kobe"], "active": False},
        {"name": "Franck Ribéry", "clubs": ["Bayern Munich", "Fiorentina"], "active": False},
        {"name": "Daniel Alves", "clubs": ["Barcelona", "Paris Saint-Germain"], "active": False},
        {"name": "Wesley Sneijder", "clubs": ["Real Madrid", "Inter Milan"], "active": False},
        {"name": "Arjen Robben", "clubs": ["Chelsea", "Bayern Munich"], "active": False},
        {"name": "Fernando Torres", "clubs": ["Atletico Madrid", "Liverpool"], "active": False},
        {"name": "Xavi Hernandez", "clubs": ["Barcelona", "Al-Sadd"], "active": False},
        {"name": "Iker Casillas", "clubs": ["Real Madrid", "Porto"], "active": False},
        {"name": "Samir Nasri", "clubs": ["Arsenal", "Manchester City"], "active": False},
        {"name": "Bastian Schweinsteiger", "clubs": ["Bayern Munich", "Chicago Fire"], "active": False}
    ]

    score = 0
    random.shuffle(footballers)

    for player in footballers:
        print(f"Guess the club where {player['name']} is a football star:")
        print("Options:", ", ".join(player['clubs']))
        
        user_guess = input("Your guess: ")
        
        if user_guess.lower() in [club.lower() for club in player['clubs']]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {', '.join(player['clubs'])}\n")

    print(f"Quiz completed! Your score: {score}/{len(footballers)}")

if __name__ == "__main__":
    football_quiz()
