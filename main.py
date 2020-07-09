from boat import Boat
from q import Q
from display import Display

from random import choice,random
from time import sleep

class Agent:
    def __init__(self,new=False):
        self.boat = Boat()
        self.world = self.boat.world
        self.display = Display()

        self.discount = 1
        self.epsilon = 0.1
        self.step_size = 0.15

        self.actions = [(i,j) for i in range(-1,2) for j in range(-1,2)]

        self.Qs = {(state,action):Q(state,action) for state in self.world.states.values() for action in self.actions}
        
        if not new:
            self.download_policy()

    def e_greedy(self,state=None,eps=True):
        if state == None:
            state = self.world.states[self.boat.coord]

        actions = self.actions[:]
        action_values = [self.Qs[(state,action)].value for action in actions]

        max_value = max(action_values)
        ind = action_values.index(max_value)

        max_action = actions.pop(ind)

        if eps == True:
            if random() > self.epsilon:
                return max_action
            else:
                return choice(actions)
        else:
            return max_action

    def get_max_Qp(self,state):
        action = self.e_greedy(state,eps=False)
        return self.Qs[(state,action)]

    def upload_policy(self):
        with open('memory','w') as policy_file:
            for state_tup in self.world.states.keys():
                for action in self.actions:
                    policy_file.write(f'{state_tup}:{action}:{self.Qs[self.world.states[state_tup],action].value}\n')

    def download_policy(self):
        with open('memory','r') as policy:
            for state_action in policy:
                state_tup,action_tup,value = state_action.rstrip().split(':')
                state_tup = self.string2tup(state_tup)
                action_tup = self.string2tup(action_tup)
                value = float(value) 

                self.Qs[self.world.states[state_tup],action_tup].value = value              

    @staticmethod
    def string2tup(string):
        str1, str2 = string.split(', ')
        return (int(str1[1:]),int(str2[:-1])) 

    def learn(self,wait=False):
        i = 0
        while True:
            S = self.world.states[self.boat.coord]
            A = self.e_greedy()
            self.boat.move(*A)
            Sp = self.world.states[self.boat.coord]
            R = Sp.reward
            Q = self.Qs[(S,A)]
    
            Q.value = Q.value + self.step_size*( R + self.discount*self.get_max_Qp(Sp).value - Q.value)

            self.display.update_screen(self.boat)
            if self.display.check_if_exit():
                self.upload_policy()
                break
            i += 1
            if S.is_terminal:
                print(i)
                self.upload_policy()
                break
            if wait:
                sleep(0.1)


if __name__ == "__main__":
    agent = Agent()
    agent.learn(wait=True)
