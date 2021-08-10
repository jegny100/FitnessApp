from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.screen import Screen

KV = '''
<ContentNavigationDrawer22>:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "Aktivitäten"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "activities"
                    
            OneLineListItem:
                text: "Statistiken"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "statistics"
                    
MDScreen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top":1}
        elevation: 5
        title: "FitnessApp"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        
    MDNavigationLayout:
        x: toolbar.height
        
        ScreenManager:
            id: screen_manager
            
            MDScreen:
                name: "activities"
                MDLabel:
                    text: "Aktivitäten"
                    halign: "center"
            
            MDScreen:
                name: "statistics"
                MDLabel:
                    text: "Statistiken"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer22:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ContentNavigationDrawer22(MDBoxLayout):
    screen_manager = ObjectProperty()  # TODO check documentary
    nav_drawer = ObjectProperty()


class FitnessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        activities = Screen()

        label = MDLabel(text='Hello', halign='center', valign='top',
                        theme_text_color='Custom',
                        text_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1),
                        font_style='H1')
        activities.add_widget(label)

        btn_flat = MDFillRoundFlatButton(text='Aktivität hinzufügen',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.25})
        activities.add_widget(btn_flat)

        plus_btn = MDIconButton(icon='plus',
                                pos_hint={'center_x': 0.5, 'center_y': 0.125},
                                md_bg_color=(154 / 255.0, 212 / 255.0, 194 / 255.0, 1))
        activities.add_widget(plus_btn)

        return Builder.load_string(KV)


FitnessApp().run()
