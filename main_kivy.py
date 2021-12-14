KV = '''
<ItemConfirm>
    on_release: root.set_icon(check)
    

    CheckboxLeftWidget:
        id: check
        group: "check"

<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "activities"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "activities"
                    
            OneLineListItem:
                text: "statistics"
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
                        on_press: screen_manager.current = "logging"
                        
            
            MDScreen:
                name: "statistics"
                MDLabel:
                    text: "Statistics"
                    halign: "center"
                    
            MDScreen:
                name: "logging"
                MDBoxLayout:
                    orientation: "vertical"
                    
                    MDLabel:
                        text: "Logging Activity"
                        halign: "center"                        
                        valign: "bottom"
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        
                        MDLabel:
                            text: "Choose Activity"
                            halign: "center"
                            
                        MDFlatButton:
                            id: chosen_activity
                            text: app.chosen_activity
                            halign: "center"
                            on_release: app.show_activities_dialog()
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        
                        MDLabel:
                            text: "Time"
                            halign: "center"
                            
                        MDLabel:
                            text: "placeholder"
                            halign: "center"
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        
                        MDLabel:
                            text: "Repetitions"
                            halign: "center"
                            
                        MDLabel:
                            text: "placeholder"
                            halign: "center"
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        
                        MDLabel:
                            text: "Weight"
                            halign: "center"
                            
                        MDLabel:
                            text: "placeholder"
                            halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
