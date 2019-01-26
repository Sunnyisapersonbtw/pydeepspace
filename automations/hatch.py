from components.hatch import Hatch
from magicbot import StateMachine, state, timed_state


class HatchController(StateMachine):
    hatch: Hatch

    def start_match(self):
        """Initialise the hatch system at the start of the match."""
        pass

    def start_punch(self, force=False):
        self.engage(initial_state="punching", force=force)

    @state(first=True, must_finish=True)
    def punching(self):
        if self.hatch.hatch_in():
            self.hatch.punch()
        if not self.hatch.hatch_in():
            self.next_state("retracting")

    @timed_state(must_finish=True, duration=2.2)
    def retracting(self, state_tm):
        if state_tm >  2:
            self.hatch.retract()
            self.done()

