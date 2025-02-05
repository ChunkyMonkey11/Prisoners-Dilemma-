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
        return random.choice(["always_cooperate", "always_betray", "tit_for_tat"])

    # Strategy randomly selected 
    computer_strategy = random_strat()

    
    # Computer Algorithm that always cooperates
    def always_cooperate():
        return "cooperate"

    # Computer Algorithm that always defects
    def always_betray():
        return 'betray'

    # Computer Algorithm that follows tit for tat logic
    def tit_for_tat(previous_user_choice):
        return "cooperate" if previous_user_choice == None else previous_user_choice

    # Scoring Logic
    def scoring_logic():
        scoring = {
        ('cooperate', 'cooperate'): (3, 3),
        ('betray', 'cooperate'): (5, 0),
        ('cooperate', 'betray'): (0, 5),
        ('betray', 'betray'): (1, 1)
        }
        return scoring
    
    # Function to get users_choice
    def get_user_choice():
        while True:
            user_choice = input("Do you want to Cooperate or Betray? ").strip().lower()
            if user_choice in ["cooperate", "betray"]:
                return user_choice
            else:
                print("Invalid choice. Please enter 'Cooperate' or 'betray'.")


        

    # Setting Intital Points. 
    user_points = 0
    computer_points = 0

    # We set previous user_choice to None to set tit for tat to cooperate for if computer goes first. 
    previous_user_choice = None
    for round_num in range(total_rounds + 1):
        # Prompt User for their choice
        user_choice = get_user_choice()


        # What to do if computer_strat is "tit_for_tat"
        if computer_strategy == "tit_for_tat":
            # Storing computers choice for round
            computer_choice = tit_for_tat(previous_user_choice)
           
            # Having a dictonary that stores my scoring logic in a dictonary.
            scoring_dict = scoring_logic()  # () -> dict[tuple[str, str], tuple[int, int]]


            # Points earned for user and computer scoring_logic -> (int,int) --> (user_points,computer_points)
            points_earned = scoring_dict[user_choice,computer_choice]

            # Adding points earned per round for user and computer
            user_points += points_earned[0]
            computer_points += points_earned[1]
        
        elif computer_strategy == "cooperate":
            # Storing computers choice for round
            computer_choice = always_cooperate()

            # Having a dictonary that stores my scoring logic in a dictonary.
            scoring_dict = scoring_logic()  # () -> dict[tuple[str, str], tuple[int, int]]

            # Points earned for user and computer scoring_logic -> (int,int) --> (user_points,computer_points)
            points_earned = scoring_dict[user_choice,computer_choice]

            # Adding points earned per round for user and computer
            user_points += points_earned[0]
            computer_points += points_earned[1]
        
        elif computer_strategy == "betray":
                # Storing computers choice for round
                computer_choice = always_cooperate()

                # Having a dictonary that stores my scoring logic in a dictonary.
                scoring_dict = scoring_logic()  # () -> dict[tuple[str, str], tuple[int, int]]

                # Points earned for user and computer scoring_logic -> (int,int) --> (user_points,computer_points)
                points_earned = scoring_dict[user_choice,computer_choice]

                # Adding points earned per round for user and computer
                user_points += points_earned[0]
                computer_points += points_earned[1]
        
        print(f"The game is on round {round_num} out of {total_rounds}.")
        if round_num < total_rounds:
            print(f"The user has {user_points}, and the computer has {computer_points}")
        
        previous_user_choice = user_choice

    print(f"Thank you for playing you ended up with {user_points}, and the computer ended up with {computer_points}. ")

    
    
    

play_game()
