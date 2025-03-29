# maintenance.py
import random

def update_wear(state):
    if state.get("landed", False):
        state["flights_since_maintenance"] = state.get("flights_since_maintenance", 0) + 1
        state["engine_wear"] = state.get("engine_wear", 0) + random.uniform(1, 3)

    if state.get("engine_wear", 0) > 80:
        state["max_speed"] -= 0.01

def perform_maintenance(state):
    state["engine_wear"] = 0
    state["flights_since_maintenance"] = 0
