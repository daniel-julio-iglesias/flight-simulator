# atc_logic.py
def update_atc(state):
    altitude = state.get("altitude", 0)
    speed = state.get("speed", 0)
    ils_active = state.get("ils_active", False)

    if altitude < 10 and speed < 0.5:
        state["atc_phase"] = "GROUND"
        state["atc_message"] = "Ground: Taxi to runway, cleared for takeoff."
    elif altitude < 500:
        state["atc_phase"] = "TAKEOFF"
        state["atc_message"] = "Tower: Climb to 1000 ft."
    elif altitude < 1000:
        state["atc_phase"] = "ENROUTE"
        state["atc_message"] = f"Departure: Maintain heading {int(state.get('angle', 0)%360)}°."
    elif altitude >= 1000:
        state["atc_phase"] = "CENTER"
        state["atc_message"] = f"Center: Cruise at {int(altitude)} ft."
    if ils_active and altitude < 500:
        state["atc_phase"] = "APPROACH"
        state["atc_message"] = f"Approach: Cleared for ILS landing."
