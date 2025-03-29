import pygame
from modules.flight.controls import handle_controls
from modules.flight.physics import update_physics
from modules.flight.instruments import draw_instruments
from modules.ui.hud import draw_hud
from modules.atc.atc_logic import update_atc
from modules.atc.crm import copilot_feedback
from modules.systems.avionics import update_gps
from modules.systems.weather import update_weather
from modules.systems.maintenance import update_wear
from modules.systems.passengers import update_passenger_satisfaction

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Traditional Flight Simulator")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    state = {
        'x': 400, 'y': 300,
        'angle': 0,
        'speed': 0,
        'max_speed': 5,
        'stall_speed': 1.5,
        'climb_rate': 0,
        'altitude': 1000,
        'gear_down': True,
        'engine_on': True,
        'fuel': 500,
        'wind_speed': 0.05,
        'wind_direction': 90,
        'fog_density': 0,
        'gps_active': False,
        'gps_waypoints': [(100, 100), (400, 300), (700, 500)],
        'current_gps_waypoint': 0,
        'pilot_logbook': [],
        'passenger_satisfaction': 100,
        'engine_wear': 0,
        'flights_since_maintenance': 0,
        'checklist_active': False,
        'current_checklist': [],
    }

    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()
        keys = {
            "up": keys_pressed[pygame.K_UP],
            "down": keys_pressed[pygame.K_DOWN],
            "left": keys_pressed[pygame.K_LEFT],
            "right": keys_pressed[pygame.K_RIGHT],
            "w": keys_pressed[pygame.K_w],
            "s": keys_pressed[pygame.K_s],
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_controls(state, keys)
        update_weather(state)
        update_gps(state)
        update_physics(state)
        update_atc(state)
        update_wear(state)
        update_passenger_satisfaction(state)
        state["copilot_message"] = copilot_feedback(state)

        screen.fill((135, 206, 235))  # sky blue
        draw_instruments(screen, state, font)
        draw_hud(screen, state, font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
