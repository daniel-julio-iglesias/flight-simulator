# hud.py
import pygame

def draw_hud(screen, state, font):
    y = 200
    for entry in state.get("pilot_logbook", [])[-3:]:
        log_text = font.render(
            f"{entry['Date']}: {entry['Departure']} → {entry['Destination']} ({entry['Duration (min)']} min)", True, (0,0,0))
        screen.blit(log_text, (10, y))
        y += 20

    atc_msg = state.get("atc_message", "")
    if atc_msg:
        screen.blit(font.render(f"ATC: {atc_msg}", True, (0,0,128)), (10, 140))

    copilot_msg = state.get("copilot_message", "")
    if copilot_msg:
        screen.blit(font.render(copilot_msg, True, (0,0,128)), (10, 160))

    if state.get("checklist_active"):
        screen.blit(font.render("Checklist:", True, (0,0,0)), (10, 490))
        y = 510
        for item in state.get("current_checklist", []):
            screen.blit(font.render(f"☐ {item}", True, (0,0,0)), (10, y))
            y += 20
        if not state["current_checklist"]:
            screen.blit(font.render("Checklist Complete!", True, (0,128,0)), (10, y))
