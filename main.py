from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.screen import Screen

from kivy.lang import Builder

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Fitness App"
        
    MDBoxLayout:

        MDNavigationRail:
            md_bg_color: app.theme_cls.primary_color
            
            MDNavigationRailItem:
                icon: "book-open-variant"

            MDNavigationRailItem:
                icon: "chart-line"

'''


class FitnessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        homescreen = Screen()

        label = MDLabel(text='Hello', halign='center', valign='top',
                        theme_text_color='Custom',
                        text_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1),
                        font_style='H1')
        homescreen.add_widget(label)

        btn_flat = MDFillRoundFlatButton(text='Aktivität hinzufügen',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.25})
        homescreen.add_widget(btn_flat)

        plus_btn = MDIconButton(icon='plus',
                                pos_hint={'center_x': 0.5, 'center_y': 0.125},
                                md_bg_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1))
        homescreen.add_widget(plus_btn)

        return Builder.load_string(KV)


FitnessApp().run()
