from generate_event import gen_event
from step import step
from handle_event import handle_event
from game_file_ops import load_from_file()

class Game():
    '''
    Class containing all operations for game instance.
    '''

    def __init__(game_settings={diff=0, seed=''}, \
                load_game=False, save_file=''):
        '''
        Function to process the creation of new games or loading
        from existing saves.
        :param load_game: boolean for whether to load from save
        :param save_file: name of file to load from in save directory
        :return:
        '''
        if load_game: self.load(save_file)
        else:

    def new_game(self):
        '''
        Create a new game.
        :return:
        ''' 
            ## Initialize counters
            self.time_passed = 0 # Amount of time passed since last event
            self.time_next_event = 0 # Amount of time between events
            self.difficulty = game_settings('diff')

            # Generate starting conditions
            self.gen_environment(game_settings('seed')) 


    def save(self, save_file):
        '''
        Save game to given file.
        :return:
        '''

    def load(self, save_file):
        '''
        Initialize game from save file.
        :return:
        '''
        
        load_from_file()

    def gen_event(self):
        '''
        Generates next event from available trees and based
        on player's current position in those trees.
        :return:
        '''
        gen_event()

    def handle_event(self):
        '''
        Effects consequences from player's choice in last event
        onto game variables.
        :return:
        '''

        handle_event()

    def step(self):
        '''
        Function called every unit of time to generate events,
        process changes in resource quantities, and simulate
        everything else that happens.
        :return:
        '''

        step()

