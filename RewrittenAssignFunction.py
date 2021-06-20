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
    print("1 Extremely Unfavorable, 2 Unfavorable, 3 Neutral, 4 Favorable, 5 Extremely Favorable / Enter 0 If The Position Isn't Available To You.")
    time.sleep(.5)
    
    best_score = 6
    worst_score = 0
    sumtotal = 0
    
    pos_ver = True

    
    
    while pos_ver:
        cashier_input = input("Cashier: ")
        if cashier_input.isdigit():
            cash_pos_int = int(cashier_input)
            if cash_pos_int in range(worst_score, best_score):
                pos_ver = False
                cashier_pos.append(cash_pos_int)
                sumtotal += cash_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")
    
    pos_ver = True
    while pos_ver:
        expo_input = input("Expo: ")
        if expo_input.isdigit():
            expo_pos_int = int(expo_input)
            if expo_pos_int in range(worst_score, best_score):
                pos_ver = False
                expo_pos.append(expo_pos_int)
                sumtotal += expo_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")
    
    pos_ver = True
    while pos_ver:
        dining_input = input("Dining Room: ")
        if dining_input.isdigit():
            dining_pos_int = int(dining_input)
            if dining_pos_int in range(worst_score, best_score):
                pos_ver = False
                dining_pos.append(dining_pos_int)
                sumtotal += dining_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")
    
    pos_ver = True
    while pos_ver:
        board_input = input("Board: ")
        if board_input.isdigit():
            board_pos_int = int(board_input)
            if board_pos_int in range(worst_score, best_score):
                pos_ver = False
                board_pos.append(board_pos_int)
                sumtotal += board_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")

    pos_ver = True
    while pos_ver:
        baskets_input = input("Baskets: ")
        if baskets_input.isdigit():
            baskets_pos_int = int(baskets_input)
            if baskets_pos_int in range(worst_score, best_score):
                pos_ver = False
                baskets_pos.append(baskets_pos_int)
                sumtotal += baskets_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")

    pos_ver = True
    while pos_ver:
        bird_input = input("Bird: ")
        if bird_input.isdigit():
            bird_pos_int = int(bird_input)
            if bird_pos_int in range(worst_score, best_score):
                pos_ver = False
                bird_pos.append(bird_pos_int)
                sumtotal += bird_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")

    pos_ver = True
    while pos_ver:
        toast_input = input("Toast: ")
        if toast_input.isdigit():
            toast_pos_int = int(toast_input)
            if toast_pos_int in range(worst_score, best_score):
                pos_ver = False
                toast_pos.append(toast_pos_int)
                sumtotal += toast_pos_int
            else:
                print("Try Selecting A Number Between 1 and 5!")
        else:
            print(f"That isn't 0, 1, 2, 3, 4, or 5. I'm disappointed in you already {new_crew}.")
    if sumtotal == 0:
        print("Good For Nothing Crew Members Dont Deserve To Get A Spot On The Schedule!")
        return     
    # input confirmation
    print(f"Thank you {new_crew}, your position preferences have been stored successfully!")
    crew = {

        "name":new_crew,
        "cash":cash_pos_int,
        "expo":expo_pos_int,
        "dining":dining_pos_int,
        "board":board_pos_int,
        "baskets":baskets_pos_int,
        "bird":bird_pos_int,
        "toast":toast_pos_int
    }

    masterlist.append(crew)

    return


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
                return
            elif crew_remover == "back":
                valid_input = False
                return
            if valid_input:
                print("Invalid Input: Crew Member Not In Data Base!")
            
def fill_positions():

    this_shift = []
    
    # input: for managers assigning ops schedules
    print("Lets Assign A Shift!")
    print("Please Specify How Many Crew You Need In Each Position. ")
    
    cash_ver = True
    pos_list = []
    while cash_ver:
        cash = input("Cashiers Needed: ")
        if cash.isdigit():
            cash_ver = False
            cashint = int(cash)
            while cashint > len(pos_list):
                pos_list.append("cash")
        if cash.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")
    expo_ver = True
    while expo_ver:
        expo = input("Expo Needed: ")
        if expo.isdigit():
            expoint = int(expo)
            expo_ver = False
            while cashint + expoint > len(pos_list):
                pos_list.append("expo")
        if expo.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")
    dining_ver = True
    while dining_ver:
        dining = input("Dining Needed: ")
        if dining.isdigit():
            dining_ver = False
            diningint = int(dining)
            while cashint + expoint + diningint > len(pos_list):
                pos_list.append("dining")
        if dining.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")
    board_ver = True
    while board_ver:
        board = input("Board Needed: ")
        if board.isdigit():
            board_ver = False
            boardint = int(board)
            while cashint + expoint + diningint + boardint > len(pos_list):
                pos_list.append("board")
        if board.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")
    baskets_ver = True
    while baskets_ver:
        baskets = input("Baskets Needed: ")
        if baskets.isdigit():
            baskets_ver = False
            basketsint = int(baskets)
            while cashint + expoint + diningint + boardint + basketsint > len(pos_list):
                pos_list.append("baskets")
        if baskets.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")
    bird_ver = True
    while bird_ver:
        bird = input("Bird Needed: ")
        if bird.isdigit():
            bird_ver = False
            birdint = int(bird)
            while cashint + expoint + diningint + boardint + basketsint + birdint > len(pos_list):
                pos_list.append("bird")
        if bird.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")
    toast_ver = True
    while toast_ver:
        toast = input("Toast Needed: ")
        if toast.isdigit():
            toast_ver = False
            toastint = int(toast)
            while cashint + expoint + diningint + boardint + basketsint + birdint + toastint > len(pos_list):
                pos_list.append("toast")
        if toast.isdigit() == False:
            print("Lets Try That One More Time!")
            print("Please Specify How Many Crew You Need In Each Position. ")

    total_positions = (cashint + expoint + diningint + boardint + basketsint + birdint + toastint)
    occupied_positions = 1
    # temp / for testing
    print(f"{total_positions} position(s). for testing purposes only.")
    print(pos_list)
    print("Type 'back' at any point to abandon task.")
    print("Which Crew Members Are Working This Shift: ")
    

    while total_positions >= occupied_positions:
        crew_verifier = True
        while crew_verifier:
            crew_input = input(f"Crew Member {occupied_positions}: ")
            for crew in masterlist:
                if crew.get("name") == crew_input:
                    this_shift.append(crew)
                    crew_verifier = False
                    occupied_positions += 1  
                # else:
                #     print("Invalid Input: Crew Member Unrecognized.")
                

            if crew_input == "back":
                print("Task Abandoned.")
                return

    print("This Shift Includes The Following Crew: ")
    
    for crew in this_shift:
        print(crew.get("name"))
    
    confirmation_verifier = True
    while confirmation_verifier:
        confirmation = input("Please Confirm This List Is Correct (type 'confirm' / 'back' to cancel): ")
        if confirmation == "confirm":
            print("Lovely!")
            confirmation_verifier = False
            pos_assignment(this_shift, pos_list, cashint, expoint, diningint, boardint, basketsint, birdint, toastint)
        elif confirmation == "back":
            print("Task Abandoned.")
            confirmation_verifier = False
            return
        if confirmation_verifier:
            print("Either Type 'confirm' or 'back'!")

def pos_assignment(crew_on_shift, positions, cashint, expoint, diningint, boardint, basketsint, birdint, toastint):

    crew_on_shift_backup = crew_on_shift
    positions_backup = positions
    cashwinner = []
    cashwon = []
    expowinner = []
    expowon = []
    diningwinner = []
    diningwon = []
    boardwinner = []
    boardwon = []
    basketswinner = []
    basketswon = []
    birdwinner = []
    birdwon = []
    toastwinner = []
    toastwon = []

    random.shuffle(positions)
    auction = True
    while auction:
        if len(positions) > 0:
            if positions[0] == "cash":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("cash") == 5:
                        cashwinner.append(crew.get("name"))
                if len(cashwinner) > 0 and cashint >= len(cashwon):    
                    random.shuffle(cashwinner)
                    cashwon.append(cashwinner[0])
                    for crew in crew_on_shift:
                        if len(cashwon) > 1:
                            list_reorder = [1, 0]
                            cashwon = [cashwon[i] for i in list_reorder]
                        if crew_on_shift == cashwon[0]:
                            crew_on_shift.remove(crew)
                            break
                cashwinner = []

                for crew in crew_on_shift:
                    if crew.get("cash") == 4:
                        cashwinner.append(crew.get("name"))
                if len(cashwinner) > 0 and cashint >= len(cashwon):    
                    random.shuffle(cashwinner)
                    cashwon.append(cashwinner[0])
                    for crew in crew_on_shift:
                        if len(cashwon) > 1:
                            list_reorder = [1, 0]
                            cashwon = [cashwon[i] for i in list_reorder]
                        if crew_on_shift == cashwon[0]:
                            crew_on_shift.remove(crew)
                            break
                cashwinner = []

                for crew in crew_on_shift:
                    if crew.get("cash") == 3:
                        cashwinner.append(crew.get("name"))
                if len(cashwinner) > 0 and cashint >= len(cashwon):    
                    random.shuffle(cashwinner)
                    cashwon.append(cashwinner[0])
                    for crew in crew_on_shift:
                        if len(cashwon) > 1:
                            list_reorder = [1, 0]
                            cashwon = [cashwon[i] for i in list_reorder]
                        if crew_on_shift == cashwon[0]:
                            crew_on_shift.remove(crew)
                            break
                cashwinner = []

                for crew in crew_on_shift:
                    if crew.get("cash") == 2:
                        cashwinner.append(crew.get("name"))
                if len(cashwinner) > 0 and cashint >= len(cashwon):    
                    random.shuffle(cashwinner)
                    cashwon.append(cashwinner[0])
                    for crew in crew_on_shift:
                        if len(cashwon) > 1:
                            list_reorder = [1, 0]
                            cashwon = [cashwon[i] for i in list_reorder]
                        if crew_on_shift == cashwon[0]:
                            crew_on_shift.remove(crew)
                            break
                cashwinner = []

                for crew in crew_on_shift:
                    if crew.get("cash") == 1:
                        cashwinner.append(crew.get("name"))
                if len(cashwinner) > 0 and cashint >= len(cashwon):    
                    random.shuffle(cashwinner)
                    cashwon.append(cashwinner[0])
                    for crew in crew_on_shift:
                        if len(cashwon) > 1:
                            list_reorder = [1, 0]
                            cashwon = [cashwon[i] for i in list_reorder]
                        if crew_on_shift == cashwon[0]:
                            crew_on_shift.remove(crew)
                            break
                cashwinner = []

        if len(positions) > 0:
            if positions[0] == "expo":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("expo") == 5:
                        expowinner.append(crew.get("name"))
                if len(expowinner) > 0 and expoint >= len(expowon):    
                    random.shuffle(expowinner)
                    expowon.append(expowinner[0])
                    for crew in crew_on_shift:
                        if len(expowon) > 1:
                            list_reorder = [1, 0]
                            expowon = [expowon[i] for i in list_reorder]
                        if crew_on_shift == expowon[0]:
                            crew_on_shift.remove(crew)
                            break
                expowinner = []

                for crew in crew_on_shift:
                    if crew.get("expo") == 4:
                        expowinner.append(crew.get("name"))
                if len(expowinner) > 0 and expoint >= len(expowon):    
                    random.shuffle(expowinner)
                    expowon.append(expowinner[0])
                    for crew in crew_on_shift:
                        if len(expowon) > 1:
                            list_reorder = [1, 0]
                            expowon = [expowon[i] for i in list_reorder]
                        if crew_on_shift == expowon[0]:
                            crew_on_shift.remove(crew)
                            break
                expowinner = []

                for crew in crew_on_shift:
                    if crew.get("expo") == 3:
                        expowinner.append(crew.get("name"))
                if len(expowinner) > 0 and expoint >= len(expowon):    
                    random.shuffle(expowinner)
                    expowon.append(expowinner[0])
                    for crew in crew_on_shift:
                        if len(expowon) > 1:
                            list_reorder = [1, 0]
                            expowon = [expowon[i] for i in list_reorder]
                        if crew_on_shift == expowon[0]:
                            crew_on_shift.remove(crew)
                            break
                expowinner = []

                for crew in crew_on_shift:
                    if crew.get("expo") == 2:
                        expowinner.append(crew.get("name"))
                if len(expowinner) > 0 and expoint >= len(expowon):    
                    random.shuffle(expowinner)
                    expowon.append(expowinner[0])
                    for crew in crew_on_shift:
                        if len(expowon) > 1:
                            list_reorder = [1, 0]
                            expowon = [expowon[i] for i in list_reorder]
                        if crew_on_shift == expowon[0]:
                            crew_on_shift.remove(crew)
                            break
                expowinner = []

                for crew in crew_on_shift:
                    if crew.get("expo") == 1:
                        expowinner.append(crew.get("name"))
                if len(expowinner) > 0 and expoint >= len(expowon):    
                    random.shuffle(expowinner)
                    expowon.append(expowinner[0])
                    for crew in crew_on_shift:
                        if len(expowon) > 1:
                            list_reorder = [1, 0]
                            expowon = [expowon[i] for i in list_reorder]
                        if crew_on_shift == expowon[0]:
                            crew_on_shift.remove(crew)
                            break
                expowinner = []
        
        if len(positions) > 0:
            if positions[0] == "dining":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("dining") == 5:
                        diningwinner.append(crew.get("name"))
                if len(diningwinner) > 0 and diningint >= len(diningwon):    
                    random.shuffle(diningwinner)
                    diningwon.append(diningwinner[0])
                    for crew in crew_on_shift:
                        if len(diningwon) > 1:
                            list_reorder = [1, 0]
                            diningwon = [diningwon[i] for i in list_reorder]
                        if crew_on_shift == diningwon[0]:
                            crew_on_shift.remove(crew)
                            break
                diningwinner = []

                for crew in crew_on_shift:
                    if crew.get("dining") == 4:
                        diningwinner.append(crew.get("name"))
                if len(diningwinner) > 0 and diningint >= len(diningwon):    
                    random.shuffle(diningwinner)
                    diningwon.append(diningwinner[0])
                    for crew in crew_on_shift:
                        if len(diningwon) > 1:
                            list_reorder = [1, 0]
                            diningwon = [diningwon[i] for i in list_reorder]
                        if crew_on_shift == diningwon[0]:
                            crew_on_shift.remove(crew)
                            break
                diningwinner = []

                for crew in crew_on_shift:
                    if crew.get("dining") == 3:
                        diningwinner.append(crew.get("name"))
                if len(diningwinner) > 0 and diningint >= len(diningwon):    
                    random.shuffle(diningwinner)
                    diningwon.append(diningwinner[0])
                    for crew in crew_on_shift:
                        if len(diningwon) > 1:
                            list_reorder = [1, 0]
                            diningwon = [diningwon[i] for i in list_reorder]
                        if crew_on_shift == diningwon[0]:
                            crew_on_shift.remove(crew)
                            break
                diningwinner = []

                for crew in crew_on_shift:
                    if crew.get("dining") == 2:
                        diningwinner.append(crew.get("name"))
                if len(diningwinner) > 0 and diningint >= len(diningwon):    
                    random.shuffle(diningwinner)
                    diningwon.append(diningwinner[0])
                    for crew in crew_on_shift:
                        if len(diningwon) > 1:
                            list_reorder = [1, 0]
                            diningwon = [diningwon[i] for i in list_reorder]
                        if crew_on_shift == diningwon[0]:
                            crew_on_shift.remove(crew)
                            break
                diningwinner = []

                for crew in crew_on_shift:
                    if crew.get("dining") == 1:
                        diningwinner.append(crew.get("name"))
                if len(diningwinner) > 0 and diningint >= len(diningwon):    
                    random.shuffle(diningwinner)
                    diningwon.append(diningwinner[0])
                    for crew in crew_on_shift:
                        if len(diningwon) > 1:
                            list_reorder = [1, 0]
                            diningwon = [diningwon[i] for i in list_reorder]
                        if crew_on_shift == diningwon[0]:
                            crew_on_shift.remove(crew)
                            break
                diningwinner = []

        
            if positions[0] == "board":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("board") == 5:
                        boardwinner.append(crew.get("name"))
                if len(boardwinner) > 0 and boardint >= len(boardwon):    
                    random.shuffle(boardwinner)
                    boardwon.append(boardwinner[0])
                    for crew in crew_on_shift:
                        if len(boardwon) > 1:
                            list_reorder = [1, 0]
                            boardwon = [boardwon[i] for i in list_reorder]
                        if crew_on_shift == boardwon[0]:
                            crew_on_shift.remove(crew)
                            break
                boardwinner = []

                for crew in crew_on_shift:
                    if crew.get("board") == 4:
                        boardwinner.append(crew.get("name"))
                if len(boardwinner) > 0 and boardint >= len(boardwon):    
                    random.shuffle(boardwinner)
                    boardwon.append(boardwinner[0])
                    for crew in crew_on_shift:
                        if len(boardwon) > 1:
                            list_reorder = [1, 0]
                            boardwon = [boardwon[i] for i in list_reorder]
                        if crew_on_shift == boardwon[0]:
                            crew_on_shift.remove(crew)
                            break
                boardwinner = []

                for crew in crew_on_shift:
                    if crew.get("board") == 3:
                        boardwinner.append(crew.get("name"))
                if len(boardwinner) > 0 and boardint >= len(boardwon):    
                    random.shuffle(boardwinner)
                    boardwon.append(boardwinner[0])
                    for crew in crew_on_shift:
                        if len(boardwon) > 1:
                            list_reorder = [1, 0]
                            boardwon = [boardwon[i] for i in list_reorder]
                        if crew_on_shift == boardwon[0]:
                            crew_on_shift.remove(crew)
                            break
                boardwinner = []

                for crew in crew_on_shift:
                    if crew.get("board") == 2:
                        boardwinner.append(crew.get("name"))
                if len(boardwinner) > 0 and boardint >= len(boardwon):    
                    random.shuffle(boardwinner)
                    boardwon.append(boardwinner[0])
                    for crew in crew_on_shift:
                        if len(boardwon) > 1:
                            list_reorder = [1, 0]
                            boardwon = [boardwon[i] for i in list_reorder]
                        if crew_on_shift == boardwon[0]:
                            crew_on_shift.remove(crew)
                            break
                boardwinner = []

                for crew in crew_on_shift:
                    if crew.get("board") == 1:
                        boardwinner.append(crew.get("name"))
                if len(boardwinner) > 0 and boardint >= len(boardwon):    
                    random.shuffle(boardwinner)
                    boardwon.append(boardwinner[0])
                    for crew in crew_on_shift:
                        if len(boardwon) > 1:
                            list_reorder = [1, 0]
                            boardwon = [boardwon[i] for i in list_reorder]
                        if crew_on_shift == boardwon[0]:
                            crew_on_shift.remove(crew)
                            break
                boardwinner = []
        
        if len(positions) > 0:
            if positions[0] == "baskets":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("baskets") == 5:
                        basketswinner.append(crew.get("name"))
                if len(basketswinner) > 0 and basketsint >= len(basketswon):    
                    random.shuffle(basketswinner)
                    basketswon.append(basketswinner[0])
                    for crew in crew_on_shift:
                        if len(basketswon) > 1:
                            list_reorder = [1, 0]
                            basketswon = [basketswon[i] for i in list_reorder]
                        if crew_on_shift == basketswon[0]:
                            crew_on_shift.remove(crew)
                            break
                basketswinner = []

                for crew in crew_on_shift:
                    if crew.get("baskets") == 4:
                        basketswinner.append(crew.get("name"))
                if len(basketswinner) > 0 and basketsint >= len(basketswon):    
                    random.shuffle(basketswinner)
                    basketswon.append(basketswinner[0])
                    for crew in crew_on_shift:
                        if len(basketswon) > 1:
                            list_reorder = [1, 0]
                            basketswon = [basketswon[i] for i in list_reorder]
                        if crew_on_shift == basketswon[0]:
                            crew_on_shift.remove(crew)
                            break
                basketswinner = []

                for crew in crew_on_shift:
                    if crew.get("baskets") == 3:
                        basketswinner.append(crew.get("name"))
                if len(basketswinner) > 0 and basketsint >= len(basketswon):    
                    random.shuffle(basketswinner)
                    basketswon.append(basketswinner[0])
                    for crew in crew_on_shift:
                        if len(basketswon) > 1:
                            list_reorder = [1, 0]
                            basketswon = [basketswon[i] for i in list_reorder]
                        if crew_on_shift == basketswon[0]:
                            crew_on_shift.remove(crew)
                            break
                basketswinner = []

                for crew in crew_on_shift:
                    if crew.get("baskets") == 2:
                        basketswinner.append(crew.get("name"))
                if len(basketswinner) > 0 and basketsint >= len(basketswon):    
                    random.shuffle(basketswinner)
                    basketswon.append(basketswinner[0])
                    for crew in crew_on_shift:
                        if len(basketswon) > 1:
                            list_reorder = [1, 0]
                            basketswon = [basketswon[i] for i in list_reorder]
                        if crew_on_shift == basketswon[0]:
                            crew_on_shift.remove(crew)
                            break
                basketswinner = []

                for crew in crew_on_shift:
                    if crew.get("baskets") == 1:
                        basketswinner.append(crew.get("name"))
                if len(basketswinner) > 0 and basketsint >= len(basketswon):    
                    random.shuffle(basketswinner)
                    basketswon.append(basketswinner[0])
                    for crew in crew_on_shift:
                        if len(basketswon) > 1:
                            list_reorder = [1, 0]
                            basketswon = [basketswon[i] for i in list_reorder]
                        if crew_on_shift == basketswon[0]:
                            crew_on_shift.remove(crew)
                            break
                basketswinner = []

        
        if len(positions) > 0:
            if positions[0] == "bird":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("bird") == 5:
                        birdwinner.append(crew.get("name"))
                if len(birdwinner) > 0 and birdint >= len(birdwon):    
                    random.shuffle(birdwinner)
                    birdwon.append(birdwinner[0])
                    for crew in crew_on_shift:
                        if len(birdwon) > 1:
                            list_reorder = [1, 0]
                            birdwon = [birdwon[i] for i in list_reorder]
                        if crew_on_shift == birdwon[0]:
                            crew_on_shift.remove(crew)
                            break
                birdwinner = []

                for crew in crew_on_shift:
                    if crew.get("bird") == 4:
                        birdwinner.append(crew.get("name"))
                if len(birdwinner) > 0 and birdint >= len(birdwon):    
                    random.shuffle(birdwinner)
                    birdwon.append(birdwinner[0])
                    for crew in crew_on_shift:
                        if len(birdwon) > 1:
                            list_reorder = [1, 0]
                            birdwon = [birdwon[i] for i in list_reorder]
                        if crew_on_shift == birdwon[0]:
                            crew_on_shift.remove(crew)
                            break
                birdwinner = []

                for crew in crew_on_shift:
                    if crew.get("bird") == 3:
                        birdwinner.append(crew.get("name"))
                if len(birdwinner) > 0 and birdint >= len(birdwon):    
                    random.shuffle(birdwinner)
                    birdwon.append(birdwinner[0])
                    for crew in crew_on_shift:
                        if len(birdwon) > 1:
                            list_reorder = [1, 0]
                            birdwon = [birdwon[i] for i in list_reorder]
                        if crew_on_shift == birdwon[0]:
                            crew_on_shift.remove(crew)
                            break
                birdwinner = []

                for crew in crew_on_shift:
                    if crew.get("bird") == 2:
                        birdwinner.append(crew.get("name"))
                if len(birdwinner) > 0 and birdint >= len(birdwon):    
                    random.shuffle(birdwinner)
                    birdwon.append(birdwinner[0])
                    for crew in crew_on_shift:
                        if len(birdwon) > 1:
                            list_reorder = [1, 0]
                            birdwon = [birdwon[i] for i in list_reorder]
                        if crew_on_shift == birdwon[0]:
                            crew_on_shift.remove(crew)
                            break
                birdwinner = []

                for crew in crew_on_shift:
                    if crew.get("bird") == 1:
                        birdwinner.append(crew.get("name"))
                if len(birdwinner) > 0 and birdint >= len(birdwon):    
                    random.shuffle(birdwinner)
                    birdwon.append(birdwinner[0])
                    for crew in crew_on_shift:
                        if len(birdwon) > 1:
                            list_reorder = [1, 0]
                            birdwon = [birdwon[i] for i in list_reorder]
                        if crew_on_shift == birdwon[0]:
                            crew_on_shift.remove(crew)
                            break
                birdwinner = []

        if len(positions) > 0:
            if positions[0] == "toast":
                positions.pop(0)
                for crew in crew_on_shift:
                    if crew.get("toast") == 5:
                        toastwinner.append(crew.get("name"))
                if len(toastwinner) > 0 and toastint >= len(toastwon):    
                    random.shuffle(toastwinner)
                    toastwon.append(toastwinner[0])
                    for crew in crew_on_shift:
                        if len(toastwon) > 1:
                            list_reorder = [1, 0]
                            toastwon = [toastwon[i] for i in list_reorder]
                        if crew_on_shift == toastwon[0]:
                            crew_on_shift.remove(crew)
                            break
                toastwinner = []

                for crew in crew_on_shift:
                    if crew.get("toast") == 4:
                        toastwinner.append(crew.get("name"))
                if len(toastwinner) > 0 and toastint >= len(toastwon):    
                    random.shuffle(toastwinner)
                    toastwon.append(toastwinner[0])
                    for crew in crew_on_shift:
                        if len(toastwon) > 1:
                            list_reorder = [1, 0]
                            toastwon = [toastwon[i] for i in list_reorder]
                        if crew_on_shift == toastwon[0]:
                            crew_on_shift.remove(crew)
                            break
                toastwinner = []

                for crew in crew_on_shift:
                    if crew.get("toast") == 3:
                        toastwinner.append(crew.get("name"))
                if len(toastwinner) > 0 and toastint >= len(toastwon):    
                    random.shuffle(toastwinner)
                    toastwon.append(toastwinner[0])
                    for crew in crew_on_shift:
                        if len(toastwon) > 1:
                            list_reorder = [1, 0]
                            toastwon = [toastwon[i] for i in list_reorder]
                        if crew_on_shift == toastwon[0]:
                            crew_on_shift.remove(crew)
                            break
                toastwinner = []

                for crew in crew_on_shift:
                    if crew.get("toast") == 2:
                        toastwinner.append(crew.get("name"))
                if len(toastwinner) > 0 and toastint >= len(toastwon):    
                    random.shuffle(toastwinner)
                    toastwon.append(toastwinner[0])
                    for crew in crew_on_shift:
                        if len(toastwon) > 1:
                            list_reorder = [1, 0]
                            toastwon = [toastwon[i] for i in list_reorder]
                        if crew_on_shift == toastwon[0]:
                            crew_on_shift.remove(crew)
                            break
                toastwinner = []

                for crew in crew_on_shift:
                    if crew.get("toast") == 1:
                        toastwinner.append(crew.get("name"))
                if len(toastwinner) > 0 and toastint >= len(toastwon):    
                    random.shuffle(toastwinner)
                    toastwon.append(toastwinner[0])
                    for crew in crew_on_shift:
                        if len(toastwon) > 1:
                            list_reorder = [1, 0]
                            toastwon = [toastwon[i] for i in list_reorder]
                        if crew_on_shift == toastwon[0]:
                            crew_on_shift.remove(crew)
                            break
                toastwinner = []
            
        if len(positions) == 0:
            auction = False
            print("Here Are Your Assignments As Following.")
            time.sleep(1)
            if cashint > 0:
                print("On Cash:")
                print(cashwon[0])
                print(cashwon[1])
            time.sleep(1)
            if expoint > 0:
                print("On Expo:")
                print(expowon[expoint])
            time.sleep(1)
            if diningint > 0:
                print("On Dining Room")
                print(diningwon[diningint])
            time.sleep(1)
            if boardint > 0:
                print("On Board:")
                print(boardwon[boardint])
            time.sleep(1)
            if basketsint > 0:
                print("On Baskets:")
                print(basketswon[basketsint])
            time.sleep(1)
            if birdint > 0:
                print("On Bird:")
                print(birdwon[birdint])
            time.sleep(1)
            if toastint > 0:
                print("On Toast:")
                print(toastwon[toastint])

            main()
        # if len(positions) > 0:
        #     print("auction failed: rerunning.")
        #     fill_positions()


        

                    
                
                


                
            





# input: Task Routing   

def main():

    running_input = input("Run A Task (New Crew, Remove Crew, Fill Positions, Fill Secondary Positions, Print Dictionaries, Print Lists): ")
    
    if running_input == "nc":
        add_crew()
    elif running_input == "fp":
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