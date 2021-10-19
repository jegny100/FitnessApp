from kivy.lang import Builder
from kivymd.app import MDApp

# your layouts
KV = '''
Screen
    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        text: 'select items'
        items: app.items
        on_release: self.set_item("vipin coding")    
'''

class Test(MDApp):

    def build(self):
        self.items = ["a","b"]
        return Builder.load_string(KV)


Test().run()
