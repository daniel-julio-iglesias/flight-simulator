# weather.py
import random
import math

def update_weather(state):
    if random.randint(0, 500) == 1:
        state["wind_speed"] = random.uniform(0.02, 0.1)
        state["wind_direction"] = random.randint(0, 360)

    state["turbulence"] = random.uniform(-0.01, 0.01)

    # Apply wind
    wind_speed = state.get("wind_speed", 0.05)
    wind_dir = math.radians(state.get("wind_direction", 90))
    state["x"] += wind_speed * math.cos(wind_dir) + state["turbulence"]
    state["y"] -= wind_speed * math.sin(wind_dir) + state["turbulence"]

    # Fog update
    if random.randint(0, 800) == 1:
        state["fog_density"] = random.randint(0, 150)
