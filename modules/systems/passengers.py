# passengers.py
def update_passenger_satisfaction(state):
    satisfaction = state.get("passenger_satisfaction", 100)

    if abs(state.get("climb_rate", 0)) > 1.8:
        satisfaction -= 0.05
    if state.get("turbulence", 0) > 0.02:
        satisfaction -= 0.05
    if state.get("engine_failure_active") or state.get("fuel_leak_active"):
        satisfaction -= 0.1

    state["passenger_satisfaction"] = max(0, satisfaction)
