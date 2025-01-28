import random
# Main function to control game flow
def play_game():
    # Print Intital Welcome Line
    print("""
    Welcome to the Prisoner's Dilemma Simulation

    Game Rules:
    1. You will play against the computer for a chosen number of rounds.
    2. In each round, you must choose to either 'cooperate' or 'betray'.
    3. The computer will follow a specific strategy throughout the game.

    Scoring System:
    - If both you and the computer cooperate, you each earn 3 points.
    - If you betray and the computer cooperates, you earn 5 points while the computer gets 0.
    - If the computer betrays and you cooperate, the computer earns 5 points while you get 0.
    - If both of you betray, you each earn 1 point.

    Objective:
    - Try to achieve the highest score possible while considering the consequences of trust and betrayal.
    - Experiment with different strategies to see how the game plays out.

    Let's begin!
    """)    


    # Setting Intital Variables 
    rounds = None
    users_choice = None
    computer_strategy = None

    # User Inputs Desired Rounds and setting rounds to selected_rounds
    selected_rounds = int(input("How many Rounds Would You Like to Play?:"))
    rounds = selected_rounds
    
    # User Decides Which Strategy They Want
    def get_strat():
        print(""" 
        Here are the different strategies you can play against. Input is on Left and Option is on right. 
        1: always cooperate
        2: always defect
        3: tit_for_tat
        4: random 
        """)

        selected_strat = int(input("What Strategy Did You Select?: "))


        """
        Figure out how to return the strategy. If it should be a string with the function name or the actual function call.
        This return should be placed inside computer_strategy.
        """
        if selected_strat == int(4):
            
            return

        










    # Computer Algorithm that always cooperates
    def always_cooperate():
        return "cooperate"

    # Computer Algorithm that always defects
    def always_defect():
        return "betray"

    def tit_for_tat(previous_user_choice):
        return "cooperate" if previous_user_choice == None else previous_user_choice

    # Scoring Logic
    def scoring_logic():
        scoring = {
        ("cooperate", "cooperate"): (3, 3),
        ("betray", "cooperate"): (5, 0),
        ("cooperate", "betray"): (0, 5),
        ("betray", "betray"): (1, 1)
        }
        return

    # Random_Stat Function that will decide for the user which Stategy To Play Against.
    def random_strat():
        random_number = random.randint(1,3)
        return random_number
    


   
   




    return

