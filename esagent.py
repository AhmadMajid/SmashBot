import melee
import math
from Strategies.bait import Bait

class ESAgent():
    """
    Expert system agent for SmashBot.
    This is the "manually programmed" TAS-looking agent.
    """
    def __init__(self, dolphin, smashbot_port, opponent_port, controller):
        self.smashbot_port = smashbot_port
        self.opponent_port = opponent_port
        self.controller = controller
        self.framedata = melee.framedata.FrameData()
        self.logger = dolphin.logger
        self.difficulty = 4
        self.strategy = Bait(self.logger,
                            self.controller,
                            self.framedata,
                            self.difficulty)

    def act(self, gamestate):
        # TODO Move this to libmelee
        xdist = gamestate.player[self.smashbot_port].x - gamestate.player[self.opponent_port].x
        ydist = gamestate.player[self.smashbot_port].y - gamestate.player[self.opponent_port].y
        gamestate.distance = math.sqrt( (xdist**2) + (ydist**2) )

        self.strategy.step(gamestate,
                           gamestate.player[self.smashbot_port],
                           gamestate.player[self.opponent_port])
