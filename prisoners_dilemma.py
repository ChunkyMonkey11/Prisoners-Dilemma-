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


    
    # User Inputs Desired Rounds and setting rounds to selected_rounds
    total_rounds = int(input("How many Rounds Would You Like to Play?:"))
    
    
    # Function that randomly selects computer strategy to run. Return name of function to be called. 
    def random_strat():
        """
        The purpose of this function is to randomly select computer strategy for game.
        """
        return random.choice(["always_cooperate", "always_defect", "tit_for_tat"])

    # Strategy Selected
    computer_strategy = random_strat()

    # Computer Algorithm that always cooperates
    def always_cooperate():
        return "cooperate"

    # Computer Algorithm that always defects
    def always_defect():
        return "betray"

    # Computer Algorithm that follows tit for tat logic
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
     
    def get_user_choice():
        while True:
            user_choice = input("Do you want to Cooperate or Defect? ").strip().lower()
            if user_choice in ["cooperate", "defect"]:
                return user_choice
            else:
                print("Invalid choice. Please enter 'Cooperate' or 'Defect'.")


        


    """
    Figure out what goes down below???

    """
    for round_num in range(total_rounds + 1):  
        """
        Within the loop prompt user for chouce
        Use an if-elif-else statement to call the correct computer strategy based on the chosen strategy.

        """
        print(round_num)
    

    
    
    
    

play_game()
