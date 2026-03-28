 from openenv.server import create_app
from server.my_env_environment import MyEnvironment
from models import MyAction, MyObservation

# In server/app.py - use factory mode for concurrent sessions
app = create_app(
    MyEnvironment,  # Pass class, not instance
    MyAction,
    MyObservation,
    max_concurrent_envs=4,  # Allow 4 concurrent sessions
)
