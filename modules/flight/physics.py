# physics.py
import math

def update_physics(state):
    # Apply basic aerodynamics
    stall_speed = state['stall_speed']
    speed = state['speed']
    climb_rate = state['climb_rate']

    # Aerodynamics: lift and stall
    if speed < stall_speed:
        climb_rate -= 0.05
    else:
        lift_factor = 0.02
        climb_rate += (speed - stall_speed) * lift_factor - climb_rate * 0.01

    # Update altitude
    state['altitude'] += climb_rate
    state['altitude'] = max(0, state['altitude'])

    # Speed adjustments
    if not state.get('engine_on', True):
        state['speed'] = max(state['speed'] - 0.02, 0)
    else:
        weight_penalty = state.get('weight_penalty', 1)
        state['speed'] -= climb_rate * 0.005 * weight_penalty

    # Update position based on heading
    angle_rad = math.radians(state['angle'])
    state['x'] += state['speed'] * math.cos(angle_rad)
    state['y'] -= state['speed'] * math.sin(angle_rad)

    # Loop around screen
    state['x'] %= 800
    state['y'] %= 600

    # Update climb_rate in state
    state['climb_rate'] = climb_rate
