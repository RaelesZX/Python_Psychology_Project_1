from pythonProject.screen_definitions import Screen


class menu_manager:
    def __init__(self):
        self.current_menu = None

    def switch_menu(self, screen):
        if screen == Screen.MAIN_MENU:
            self.current_menu =