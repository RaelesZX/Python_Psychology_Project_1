from grid import GridScreen
from pythonProject.colour_blind_test import ColorblindTest
from pythonProject.main_menu import MainMenu
from pythonProject.menu_manager import menu_manager
from pythonProject.options_menu import OptionsMenu
import tkinter as tk

root = tk.Tk()
screen_manager = menu_manager(root)
menu1 = MainMenu(root, screen_manager)
screen_manager.add_screen("MainMenu", menu1)

colour_blind_menu = ColorblindTest(root, screen_manager)
screen_manager.add_screen("ColorblindTest", colour_blind_menu)

experiment_screen = GridScreen(root, screen_manager)
screen_manager.add_screen("Experiment", experiment_screen)

options_screen = OptionsMenu(root, screen_manager)
screen_manager.add_screen("Options", options_screen)

screen_manager.show_screen("MainMenu")

root.mainloop()



