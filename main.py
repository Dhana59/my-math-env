import random
from openenv import OpenEnv

class MathEnv(OpenEnv):
    def __init__(self):
        super().__init__()
        self.problem = ""
        self.answer = 0

    def reset(self):
        self.problem = f"{random.randint(1, 10)} + {random.randint(1, 10)}"
        self.answer = eval(self.problem)
        return {"problem": self.problem}

    def step(self, action):
        # Action nunchi answer teesukuntundi
        try:
            user_ans = int(action.get("answer", 0))
        except:
            user_ans = 0
            
        reward = 1.0 if user_ans == self.answer else 0.0
        return {"reward": reward, "done": True, "state": {"problem": self.problem}}

if __name__ == "__main__":
    import uvicorn
    from openenv.server import create_app
    app = create_app(MathEnv())
    uvicorn.run(app, host="0.0.0.0", port=8000)