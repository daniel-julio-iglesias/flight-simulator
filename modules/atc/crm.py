# crm.py
def copilot_feedback(state):
    if state.get("fuel", 0) < 100:
        return "Co-pilot: Fuel low, consider landing soon."
    elif state.get("speed", 0) < state.get("stall_speed", 1.5) + 0.2:
        return "Co-pilot: Approaching stall speed!"
    elif state.get("altitude", 1000) < 200 and not state.get("gear_down", True):
        return "Co-pilot: Gear is up, please lower for landing."
    return "Co-pilot: Flight conditions normal."
