from kivy.factory import Factory
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Fitness App"
        
    MDBoxLayout:

        MDNavigationRail:
            
            MDNavigationRailItem:
                icon: "book-open-variant"

            MDNavigationRailItem:
                icon: "chart-line"

        MDBoxLayout:
            padding: "24dp"

            ScrollView:

                MDList:
                    id: box
                    cols: 3
                    spacing: "12dp"
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        pass


Test().run()
