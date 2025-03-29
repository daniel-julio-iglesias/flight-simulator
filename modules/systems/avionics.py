# avionics.py
import math

def update_gps(state):
    if not state.get("gps_active"):
        return

    waypoints = state.get("gps_waypoints", [])
    if not waypoints:
        return

    wp_index = state.get("current_gps_waypoint", 0)
    if wp_index >= len(waypoints):
        return

    wx, wy = waypoints[wp_index]
    dx = wx - state["x"]
    dy = state["y"] - wy
    distance = math.hypot(dx, dy)
    bearing = (math.degrees(math.atan2(dx, dy)) + 360) % 360

    state["gps_distance"] = distance
    state["gps_bearing"] = bearing

    if distance < 20:
        state["current_gps_waypoint"] = (wp_index + 1) % len(waypoints)
