# controls.py
def handle_controls(state, keys):
    if keys.get("up"):
        state['speed'] = min(state['speed'] + 0.05, state['max_speed'])
    if keys.get("down"):
        state['speed'] = max(state['speed'] - 0.05, 0)
    if keys.get("left"):
        state['angle'] += 1.5
    if keys.get("right"):
        state['angle'] -= 1.5
    if keys.get("w"):
        state['climb_rate'] = min(state['climb_rate'] + 0.02, 2)
    elif keys.get("s"):
        state['climb_rate'] = max(state['climb_rate'] - 0.02, -2)
    else:
        state['climb_rate'] *= 0.98
