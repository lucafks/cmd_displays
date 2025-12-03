from os import system
from time import sleep

scroll = """
     _                                _
    |/|==============================|/|
    |/|                              |\|
    |\|                              |\|
    |\|                              |/|         
    |/|                              |/|
    |/|                              |\|
    |\|                              |\|
    |\|                              |/|
    |/|                              |/|
    |/|                              |\|
    |\|                              |\|
    |\|==============================|/|
    `¨´                              `¨´"""

take1 = """
                        _  _
                       |/||/|
                       |/||\|
                       |\||\|
                       |\||/|         
                       |/||/|
                       |/||\|
                       |\||\|
                       |\||/|
                       |/||/|
                       |/||\|
                       |\||\|
                       |\||/|
                       `¨´`¨´"""

take2 = """
                       _    _
                      |/|==|/|
                      |/|  |\|
                      |\|  |\|
                      |\|  |/|         
                      |/|  |/|
                      |/|AD|\|   
                      |\|  |\|
                      |\|  |/|
                      |/|  |/|
                      |/|  |\|
                      |\|  |\|
                      |\|==|/|
                      `¨´  `¨´"""
take3 = """
                     _         _
                    |/|=======|/|
                    |/|       |\|
                    |\|       |\|
                    |\|       |/|         
                    |/|       |/|
                    |/|LOADING|\|
                    |\|       |\|
                    |\|       |/|
                    |/|       |/|
                    |/|       |\|
                    |\|       |\|
                    |\|=======|/|
                    `¨´       `¨´"""
take4 = """
                  _                _
                 |/|==============|/|
                 |/|              |\|
                 |\|              |\|
                 |\|              |/|         
                 |/|              |/|
                 |/|   LOADING    |\|
                 |\|              |\|
                 |\|              |/|
                 |/|              |/|
                 |/|              |\|
                 |\|              |\|
                 |\|==============|/|
                 `¨´              `¨´"""
take5 = """
             _                       _
            |/|=====================|/|
            |/|                     |\|
            |\|                     |\|
            |\|                     |/|         
            |/|                     |/|
            |/|        LOADING.     |\|
            |\|                     |\|
            |\|                     |/|
            |/|                     |/|
            |/|                     |\|
            |\|                     |\|
            |\|=====================|/|
            `¨´                     `¨´"""
take6 = """
          _                              _
         |/|============================|/|
         |/|                            |\|
         |\|                            |\|
         |\|                            |/|         
         |/|                            |/|
         |/|           LOADING..        |\|
         |\|                            |\|
         |\|                            |/|
         |/|                            |/|
         |/|                            |\|
         |\|                            |\|
         |\|============================|/|
         `¨´                            `¨´"""
take7 = """
      _                                      _
     |/|====================================|/|
     |/|                                    |\|
     |\|                                    |\|
     |\|                                    |/|         
     |/|                                    |/|
     |/|               LOADING...           |\|
     |\|                                    |\|
     |\|                                    |/|
     |/|                                    |/|
     |/|                                    |\|
     |\|                                    |\|
     |\|====================================|/|
     `¨´                                    `¨´"""
take8 = """
 _                                                  _
|/|================================================|/|
|/|                                                |\|
|\|                                                |\|
|\|                                                |/|         
|/|                                                |/|
|/|                    LOADING                     |\|
|\|                                                |\|
|\|                                                |/|
|/|                                                |/|
|/|                                                |\|
|\|                                                |\|
|\|================================================|/|
`¨´                                                `¨´"""
arcade = """
         ____________________________________
        |   ________________________________ |   
        |  |                                ||   
        |  |                                ||   
        |  |                                ||   
        |  |                                ||   
        |  |                                ||   
        |  |                                ||   
        |  |________________________________||   
        |   \   @   ooo oo                    \  
        |    \  !   ooo                        \ 
        |     ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨|
        |     |                                 |
        |     |                                 |
        |     |                                 |
        |     |                                 |
        |     |                                 |
        |     |                                 |
        |     |                                 |
        |     |                                 |
              |_________________________________|"""

def clean(): system('cls||clear')
class index:
    pass
def selector_arcade(quest:str,*alternatives:str,mark:str = '+')-> index:
    index = 0
    linesset = 33
    lines = 33
    while True:
        clean()
        print(quest)

        print(r"""       
         ____________________________________
        |   ________________________________ |   
        |  |                                ||""")
        for alternative in alternatives:
            if index == alternatives.index(alternative):
                if len({f'     {alternative} {mark}'}) < lines:
                    lines = lines - len({f'     {alternative} {mark}'})
                print(f"        |  |{f'     {alternative} {mark}':<{lines}}{''}||")
            else:
                if len({f'     {alternative} {mark}'}) < lines:
                    lines = lines - len({f'     {alternative} {mark}'})
                print(f"        |  |{f'     {alternative}':<{lines}}||")
            lines = linesset
        print(r"""        |  |                                ||   
        |  |                                ||   
        |  |________________________________||   
        |   \   @  ooo oo          \\type any \     
        |    \  !   ooo             \ character\ 
        |     ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨|¨¨¨¨¨¨¨¨¨¨|
        |     |                      |to confirm|
        |     |                      |          |
        |     |                      |          |
        |___  |                      |          |
        |    \|______________________|__________|
        |     |                      | MADE BY  |
        |     |                      |  lucafks |
        |     |                      |          |
              |______________________ꓕ__________|""")
        if not(r:=input()) and index != alternatives.index(alternatives[-1]):
            index+=1
        elif index == alternatives.index(alternatives[-1])and not(r):
            index=0
        else:
            return index

def scrolload(time = 5)->None:
        while time:
            for i in range(1,9):
                clean()
                print(eval(f'take{i}'))
                sleep(0.1)
            time-=1

def loadingFish(time=5,time_swim=0.15):
    frame = 0
    swim = 0
    while True:
        
        system('cls || clear')
        match frame:
            case 0:
                print('\n     _   \n ___/_|__\n/_ @  ))  \\_/|\n\\_____))_ / \\|   Loading.   Don’t worry, we’re fishing for data fast!\n    \\_|')
            case 1:
                print('\n     _   \n ___/_|__\n/_ @  ))  \\|\n\\_____))_ /|     Loading..  Don’t worry, we’re fishing for data fast!\n    \\_|')
            case 2:
                print('\n     _   \n ___/_|__    _\n/_ @  ))  \\_/ |\n\\_____))_ / \\_|  Loading... Don’t worry, we’re fishing for data fast!\n    \\_|')
        swim+=1
        if frame != 3:
            sleep(time_swim)
        frame +=1
        if frame ==3:frame = 0
        if swim == time*3:
            system('cls || clear')
            print('\n   |\n   |__\n  /¿ @ \\ \n |      \\ \n  \\ UU   \\ \n   \\__ __/ \n       \\__ \n     /____\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('  \n  |\n  |__\n /¿ @\\ \n|     |\n| UU  |\n|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('\n  |__\n /¿ @\\ \n|     |\n| UU  |\n|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('  |__\n /¿ @\\ \n|     |\n| UU  |\n|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print(' /¿ @\\ \n|     |\n| UU  |\n|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('|     |\n| UU  |\n|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('| UU  |\n|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('|     |\n \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print(' \\   /\n  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('  /__\\ ')
            sleep(time_swim/3.5)

            system('cls || clear')
            print('\n\n\n\n                 completed\n\n\n')
            sleep(time_swim/3.5)
            break

if __name__ == '__main__':
    match selector_arcade('switch anyone for view a screen loading','scroll','fish'):
        case 0:
            scrolload(True)
        case 1:
            loadingFish()
