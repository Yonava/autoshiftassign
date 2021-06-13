import random
import time

masterlist = []
crew_list = []
cashier_pos = []
baskets_pos = []
board_pos = []
dining_pos = []
expo_pos = []
bird_pos = []
toast_pos = []

def add_crew():

    new_crew = input("Crew Member Name: ")
    crew_list.append(new_crew)
    print("This Is A Progam Designed To Put You In Your Favorite Position Here At Raising Canes. Please Respond With A Number Between 1 and 5 To The Following Questions.")
    time.sleep(.75)
    print("1 Extremely Unfavorable, 2 Unfavorable, 3 Neutral, 4 Favorable, 5 Extremely Favorable")
    time.sleep(1)
    cashier_input = int(input("Cashier: "))
    cashier_pos.append(cashier_input)
    expo_input = int(input("Expo: "))
    expo_pos.append(expo_input)
    dining_input = int(input("Dining Room: "))
    dining_pos.append(dining_input)
    board_input = int(input("Board: "))
    board_pos.append(board_input)
    baskets_input = int(input("Baskets: "))
    baskets_pos.append(baskets_input)
    bird_input = int(input("Bird: "))
    bird_pos.append(bird_input)
    toast_input = int(input("Toast: "))
    toast_pos.append(toast_input)
    # input confirmation
    print(f"Thank you {new_crew}, your position preferences have been stored successfully!")
    crew = {

        "name":new_crew,
        "cash":cashier_input,
        "expo":expo_input,
        "dining":dining_input,
        "board":board_input,
        "baskets":baskets_input,
        "bird":bird_input,
        "toast":toast_input
    }

    masterlist.append(crew)


def remove_crew():
    
    print("Select a crew member from this list or type 'back' to go return:")
    print(" ")

    for crew in masterlist:
            
            print(crew.get("name"))

    valid_input = True
    while valid_input:
        crew_remover = input("Name of Crew Member: ")
        for crew in masterlist:
        
            if crew.get("name") == crew_remover:
                masterlist.remove(crew)
                print(crew_remover + " Has Been Successfully Removed.")
                valid_input = False
            elif crew_remover == "back":
                valid_input = False
            if valid_input:
                print("Invalid Input: Crew Member Not In Data Base!")
            
def fill_positions():

    this_shift = []
    
    # input: for managers assigning ops schedules
    print("Lets Assign A Shift!")
    print("Please Specify How Many Crew You Need In Each Position: ")
    cash = int(input("Cashiers Needed: "))
    expo = int(input("Expo Needed: "))
    dining = int(input("Dining Needed: "))
    board = int(input("Board Needed: "))
    baskets = int(input("Baskets Needed: "))
    bird = int(input("Bird Needed: "))
    toast = int(input("Toast Needed: "))

    total_positions = (cash + expo + dining + board + baskets + bird + toast)
    occupied_positions = 0
    # temp / for testing
    print(total_positions)
    
    print("Which Crew Members Are Working This Shift: ")
    
    while total_positions > occupied_positions:
    
        crew_verifier = True
        while crew_verifier:
            fir_crew = input("Crew Member 1: ")
            for crew in masterlist:
                if crew.get("name") == fir_crew:
                    this_shift.append(fir_crew)
                    crew_verifier = False
                    occupied_positions += 1
                else: print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
                sec_crew = input("Crew Member 2: ")
                for crew in masterlist:
                    if crew.get("name") == sec_crew:
                        this_shift.append(sec_crew)
                        crew_verifier = False
                        occupied_positions += 1
                    if crew_verifier:
                        print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
            third_crew = input("Crew Member 3: ")
            for crew in masterlist:
                if crew.get("name") == third_crew:
                    this_shift.append(third_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")
                
    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
            for_crew = input("Crew Member 4: ")
            for crew in masterlist:
                if crew.get("name") == for_crew:
                    this_shift.append(for_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
            fif_crew = input("Crew Member 5: ")
            for crew in masterlist:
                if crew.get("name") == fif_crew:
                    this_shift.append(fif_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
            six_crew = input("Crew Member 6: ")
            for crew in masterlist:
                if crew.get("name") == six_crew:
                    this_shift.append(six_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
            sev_crew = input("Crew Member 7: ")
            for crew in masterlist:
                if crew.get("name") == sev_crew:
                    this_shift.append(sev_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:
         
        crew_verifier = True
        while crew_verifier:
            eth_crew = input("Crew Member 8: ")
            for crew in masterlist:
                if crew.get("name") == eth_crew:
                    this_shift.append(eth_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:
        
        crew_verifier = True
        while crew_verifier:
            nin_crew = input("Crew Member 9: ")
            for crew in masterlist:
                if crew.get("name") == nin_crew:
                    this_shift.append(nin_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")

    while total_positions > occupied_positions:

        crew_verifier = True
        while crew_verifier:
            ten_crew = input("Crew Member 10: ")
            for crew in masterlist:
                if crew.get("name") == ten_crew:
                    this_shift.append(ten_crew)
                    crew_verifier = False
                    occupied_positions += 1
                if crew_verifier:
                    print("Invalid Input: Crew Member Unrecognized.")
        
            total_positions += 1000

    print("This Shift Includes The Following Crew: ")
    print(this_shift)
    confirmation = input("Please Confirm This List Is Correct (type 'confirm'): ")
    if confirmation == "confirm":
        print("Lovely!")

# input: Task Routing

def main():

    running_input = input("Run A Task (New Crew, Remove Crew, Fill Positions, Fill Secondary Positions, Print Dictionaries, Print Lists): ")
    
    if running_input == "New Crew":
        add_crew()
    elif running_input == "Fill Positions":
        fill_positions()
    elif running_input == "Print Dictionaries":
        print(masterlist)
    elif running_input == "Print Lists":
        print(f"Crew Member Name: {crew_list}, Cashier: {cashier_pos}, Baskets: {baskets_pos}, Board: {board_pos}, Dining Room: {dining_pos}, Expo: {expo_pos}, Bird: {bird_pos}, Toast: {toast_pos}")
    elif running_input == "Remove Crew":
        remove_crew()
    else:
        print("Invalid Input: Task Unrecognized.")
        print("One More Time Please (Case Sensative)...")


while True:
    
    main()
