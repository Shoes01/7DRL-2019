class State:
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """
    def __init__(self):
        print('Processing current state:', str(self))

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__

class PlayerTurn(State):
    def on_event(self, event):
        if event == 'player_dead':
            return PlayerDead()
        elif event == 'player_acted':
            return EnemyTurn()
        elif event == 'leveled_up':
            return LeveledUp()
        elif event == 'skill_selected':
            return TargetingState()
        elif event == 'open_inventory':
            return OpenInventory()
        elif event == 'exit':
            return Exit()
        return self

class Exit(State):
    def on_event(self, event):
        return self

class OpenInventory(State):
    def on_event(self, event):
        if event == 'close_inventory':
            return PlayerTurn()
        return self

class TargetingState(State):
    def on_event(self, event):
        if event == 'chose_direction':
            return PlayerTurn()
        elif event == 'cancel_targeting':
            return PlayerTurn()
        return self

class LeveledUp(State):
    def on_event(self, event):
        if event == 'chose_stat':
            return PlayerTurn()
        return self

class PlayerDead(State):
    def on_event(self, event):
        # Stuck here forever!
        return self

class EnemyTurn(State):
    def on_event(self, event):
        if event == 'enemies_acted':
            return PlayerTurn()
        return self

class GameStateMachine:
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state = PlayerTurn()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)
        return self.state