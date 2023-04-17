
SOVIET_UNION = [[-800,400],[100,100]]
USA = [[-800,-400],[100,100]]

print("\nThe Game represented in a Normal Game Form below\n")
print(f"_________________________\n\n{SOVIET_UNION[0][0]},{USA[0][0]}  ||  {SOVIET_UNION[0][1]},{USA[0][1]}")
print(f"_________________________\n\n{SOVIET_UNION[1][0]},{USA[1][0]}    ||  {SOVIET_UNION[1][1]},{USA[1][1]}\n_________________________\n")

print(f"\nThe Nash Equibliriums are: ({SOVIET_UNION[0][1]},{USA[0][1]}) and ({SOVIET_UNION[1][1]},{USA[1][1]})\n")


action_space_usa = ['Retaliate','Not Retaliate']
action_space_soviet_union = ['Attack','Not Attack']

move_USA =''
move_SOVIET_UNION = ''

SOVIET_UNION_turn = True
USA_turn = False
is_game_over = False

if(SOVIET_UNION_turn and  USA_turn==False and is_game_over==False):
    print(f'\nSoviet Union please pick your move\n\nType A or B to pick from the options below\nA - {action_space_soviet_union[0]}\nB - {action_space_soviet_union[1]}\n')
    option=input()
    if option == 'A' or option == 'a':
        move_SOVIET_UNION = action_space_soviet_union[0]
    elif option == 'B' or option == 'b':
        move_SOVIET_UNION = action_space_soviet_union[1]
    else:
        print("Invalid Input")
            
    SOVIET_UNION_turn = False
    USA_turn = True
    print ("SOVIET UNION YOU CHOSE TO",move_SOVIET_UNION)

if(move_SOVIET_UNION==action_space_soviet_union[1]):
    is_game_over=True

if(SOVIET_UNION_turn == False and USA_turn and is_game_over == False):
    print(f'\nUSA please pick your move   SOVIET UNION CHOSE TO {move_SOVIET_UNION} you\n\nType A or B to pick from the options below\nA - {action_space_usa[0]}\nB - {action_space_usa[1]}\n')
    option=input()
    if option == 'A' or option == 'a':
        move_USA = action_space_usa[0]
    elif option == 'B' or option == 'b':
        move_USA = action_space_usa[1]
    else:
        print("Invalid Input")
    USA_turn = False
    is_game_over = True
    print ("USA YOU CHOSE TO",move_USA)

if(is_game_over):
    if (move_SOVIET_UNION==action_space_soviet_union[1]):
        print("\nSOVIET UNION CHOSE NOT TO ATTACK USA HENCE THE GAME IS OVER\nPAYOFFS OF EACH NATION IS LISTED BELOW\n")
        print("SOVIET UNION",SOVIET_UNION[1][1])
        print("USA",USA[1][1])
        print("THE GAME IS OVER! BOTH USA AND SOVIET UNION WON AS THEY DIDNOT ATTACK EACH OTHER\nIT IS A NASH EQUIBLIRIA\n")
        
    if (move_SOVIET_UNION==action_space_soviet_union[0] and move_USA==action_space_usa[0]):
        print("\nCONGRATULATIONS, YOU TWO JUST STARTED A NUCLEAR WAR DESTROYING EVERYTHING\n\nPAYOFFS OF EACH NATION IS LISTED BELOW\n")
        print("SOVIET UNION",SOVIET_UNION[0][0])
        print("USA",USA[0][0])
        print("\nTHE GAME IS OVER! BOTH USA AND SOVIET UNION LOST AS BOTH NATIONS DESTROYED EVERYTHING\n")    
    
    if (move_SOVIET_UNION==action_space_soviet_union[0] and move_USA==action_space_usa[1]):
        print("\nSOVIET UNION ATTACKED USA BUT USA CONCEDED\n\nPAYOFFS OF EACH NATION IS LISTED BELOW\n")
        print("SOVIET UNION",SOVIET_UNION[0][1])
        print("USA",USA[0][1])
        print("\nTHE GAME IS OVER! SOVIET UNION WON BUT USA LOST\nIT IS A NASH EQAUILIBRIA\n")  
    

    