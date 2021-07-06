from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.screen import Screen


class FitnessApp(MDApp):
    def build(self):
        homescreen = Screen()
        btn_flat = MDFillRoundFlatButton(text='Aktivität hinzufügen',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                         md_bg_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1))
        homescreen.add_widget(btn_flat)

        plus_btn = MDIconButton(icon='plus',
                                pos_hint={'center_x': 0.5, 'center_y': 0.125},
                                md_bg_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1))
        homescreen.add_widget(plus_btn)

        label = MDLabel(text='Hello', halign='center',
                        theme_text_color='Custom',
                        text_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1),
                        font_style='H1')
        homescreen.add_widget(label)
        icon_label = MDIcon(icon='car-seat', halign='center',
                            theme_text_color='Custom',
                            text_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1))
        return homescreen


FitnessApp().run()
