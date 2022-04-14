from kivy.lang.builder import Builder
from kivymd.app import MDApp
kv = '''
<MagicButton@MagicBehavior+MDIconButton>

<MySwiper@MDSwiperItem>
    RelativeLayout:
        FitImage:
            source: "images/RedPanda.jpg"
            radius: [10,]

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            MagicButton:
                id: icon
                icon: "weather-sunny"
                user_font_size: "56sp"
                opposite_colors: True

            MDLabel:
                text: "MDLabel"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}
                opposite_colors: True
                
MDScreen:
    MDToolbar:
        id: toolbar
        title: "MDSwiper"
        elevation: 10
        pos_hint: {"top": 1}

    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(40)
        y: root.height - self.height - toolbar.height - dp(20)
        on_swipe: self.get_current_item().ids.icon.shake()

        MySwiper:
        MySwiper:
'''
class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)
Main().run()
