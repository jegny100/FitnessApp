from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"
        left_action_items: [["menu", lambda x: app.callback()]]
        right_action_items: [["dots-vertical", lambda x: app.callback()]]

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
