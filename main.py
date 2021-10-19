from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.screen import Screen

from kivy.core.window import Window
Window.size = (350, 600)

KV = '''
<ContentNavigationDrawer>:
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
                
                MDBoxLayout:
                    orientation: "vertical"
                        
                    MDLabel:
                        text :'Hello'
                        halign : 'center'
                        valign : 'top'
                        font_style : 'H3'  
                        
                    MDIconButton:
                        icon: 'plus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        md_bg_color : (154 / 255.0, 212 / 255.0, 194 / 255.0, 1)
                        
            
            MDScreen:
                name: "statistics"
                MDLabel:
                    text: "Statistiken"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()  # TODO check documentary
    nav_drawer = ObjectProperty()


class FitnessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"

        return Builder.load_string(KV)


FitnessApp().run()
