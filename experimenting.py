from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDLabel:
    text :'Hello'
    halign : 'center'
    valign : 'top'
    font_style : 'H3'
            
'''


class Test(MDApp):
    def build(self):

        return Builder.load_string(KV)

Test().run()
