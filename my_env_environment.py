import random
from openenv_core import Environment

class MyEnv(Environment):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.answer = 0

    def reset(self):
        # AI ki kotha question ivvadam
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 20)
        self.answer = self.a + self.b
        return f"Solve this: What is {self.a} + {self.b}?"

    def step(self, action):
        # AI ichina answer check cheyadam
        try:
            agent_ans = int(str(action).strip())
            if agent_ans == self.answer:
                return f"Correct! {self.answer}", 1.0, True
            else:
                return f"Wrong. Answer is {self.answer}", 0.0, True
        except:
            return "Please enter a number", 0.0, False

    def state(self):
        return {"q": f"{self.a}+{self.b}"}