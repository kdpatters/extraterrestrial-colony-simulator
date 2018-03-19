# -----------------------------------------------------------------------------------------
#                                Extraterrestrial colony simulator
# -----------------------------------------------------------------------------------------
#                           Created by Kyle D. Patterson and Julia Holgado
#                                            Spring 2018
#

from ecs.game import Game
from ecs.step import step
import sys, getopt # Processing command line arguments

def process_args(args):
    '''
    Processes command line arguments associated with running script.
    :args: List of string arguments received upon start of script
    |return| None
    '''

    help_msg = 'main.py [-l <loadfile>]'

    try:
        opts, args = getopt.getopt(argv, "h?l:", ["loadfile=", "help"])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)
    for opt, arg in opts:
        if (opt == '-h') or (opt == '?') or (opt == 'help'):
            print(help_msg)
            sys.exit()
        elif opt in ("-l", "--loadfile"):
            global save_file = arg

if __name__ == "__main__":
    save_file = ''
   
    # Process game settings 
    process_args(args)

    # Start up game
    if '' == save_file: game = Game()
    else:
        try: game = Game(save_file=save_file)
        except:
            pass # Need to add some kind of error handling here

    # Game loop
    while True:
        # Listen for end turn event

        # Take step
        step(game)
