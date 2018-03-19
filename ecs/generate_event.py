class Generate_Event():
    '''
    Class for generating next event from available trees
    Assuming each entry in the table has only one outcome, could
    maybe add more for randomly generating next event?
    '''
    def gen_event(self, tree_list, action, node_table):
        '''
        Check all trees and generate next node for each
        Check if player has made an action we can transition on AND
        if we are in a state we can transition from
        For each node, check if action is valid(does this action require a state)
        Also check if incoming nodes are valid
        :param tree_list: List of event trees
        :param action: String, possibly, needs to match whatever we're using for actions
        :param node_table: table contructed from spreadsheet, used as a transition table
        :return: none yet, possibly an event node
        '''
        for event_node in tree_list:
            self.get_next_event(event_node,tree_list,action,node_table)

    def get_next_event(self, tree_node, tree_list, action, node_table):
        if action in tree_node.get_valid_actions():
            if self.check_conditions(tree_node, tree_list, node_table):
                '''
                This part requires more definition on the representation of the table
                '''
                tree_node.set_current(node_table[tree_node]['outgoing_node'])


    def check_conditions(self, tree_node, tree_list, node_table):
        '''
        Are the present conditions valid for a transition?
        Also assumes each entry has a set of valid incoming nodes
        :param tree_node:
        :param tree_list:
        :param node_table:
        :return:
        '''
        for node in node_table[tree_node.name()]['incoming_nodes']:
            if node in tree_list:
                satisfy = True
            else:
                satisfy = False
                break
        return satisfy
