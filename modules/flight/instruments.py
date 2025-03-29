# instruments.py
import pygame

def draw_instruments(screen, state, font):
    speed = state.get('speed', 0)
    altitude = state.get('altitude', 0)
    climb_rate = state.get('climb_rate', 0)
    heading = state.get('angle', 0) % 360
    fuel = state.get('fuel', 0)

    text_color = (0, 0, 0)

    screen.blit(font.render(f"Speed: {round(speed*100)} knots", True, text_color), (10, 10))
    screen.blit(font.render(f"Altitude: {int(altitude)} ft", True, text_color), (10, 35))
    screen.blit(font.render(f"Climb Rate: {round(climb_rate*100)} ft/min", True, text_color), (10, 60))
    screen.blit(font.render(f"Heading: {int(heading)}°", True, text_color), (10, 85))
    screen.blit(font.render(f"Fuel: {int(fuel)}", True, text_color), (10, 110))
