class State:
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """
    def __init__(self):
        # print('Processing current state:', str(self)) # This is printed every time a State is changed.
        pass

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
        elif event == 'skill_selected':
            return TargetingState()
        elif event == 'exit':
            return Exit()
        elif event == 'compare_items':
            return CompareItems()
        elif event == 'consume_soul':
            return ConsumeSoul()
        elif event == 'open_character_sheet':
            return CharacterSheet()
        elif event == 'victory':
            return VictoryScreen()
        return self

class Exit(State):
    def on_event(self, event):
        return self

class TargetingState(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        elif event == 'chose_direction':
            return PlayerTurn()
        elif event == 'cancel_targeting':
            return PlayerTurn()
        return self

class PlayerDead(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        return self

class EnemyTurn(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        elif event == 'enemies_acted':
            return PlayerTurn()
        return self

class CompareItems(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        elif event == 'done_comparing':
            return PlayerTurn()
        return self

class ConsumeSoul(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        elif event == 'done_consuming':
            return PlayerTurn()
        return self

class CharacterSheet(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        elif event == 'close_character_sheet':
            return PlayerTurn()
        return self

class VictoryScreen(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        return self

class OpeningScreen(State):
    def on_event(self, event):
        if event == 'exit':
            return Exit()
        elif event == 'begin':
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
        self.state = OpeningScreen()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)
        # print('Current event:', str(event)) # This is printed every time a State is changed.
        # print('Current state:', str(self.state)) # This is printed every time a State is changed.
        return self.state