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
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "homescreen"
                    
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
        size_hint_y: 1.0 - toolbar.height/root.height
        
        ScreenManager:
            id: screen_manager
            
            MDScreen:
                name: "homescreen"
            
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "32dp"
                        
                    MDLabel:
                        text :'Hello'
                        halign : 'center'
                        valign : 'top'
                        font_style : 'H3'  
                        
                    MDIconButton:
                        icon: 'plus'
                        spacing: '10dp'
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
                    id: logging_box
                    orientation: "vertical"
                    spacing : '15dp'
                    padding: "12dp"
                    
                    MDLabel:
                        text: "Logging Activity"
                        halign: "center"                        
                        valign: "bottom"
                        font_style : 'H5' 
                        theme_text_color : 'Secondary'
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        
                                  
                        MDLabel:
                            text: "Choose Activity"
                            halign: "center"
                            valign: "center"
                            
                        MDFlatButton:
                            id: chosen_activity
                            text: app.chosen_activity
                            on_release: app.show_activities_dialog()
                            pos_hint: {"center_x": .5, "center_y": .5}
                            
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
                        padding: '10dp'
                        
                        MDLabel:
                            text: "Weight"
                            halign: "center"
                            
                        MDTextField:
                            icon_right: "weight-kilogram"
                            mode: "rectangle"
                            size_hint_x: 0.5
                            pos_hint: {"center_x": .5, "center_y": .5}
                            
                    MDIconButton:
                        id: confirm_logging
                        icon: 'check'
                        text: 'CONFIRM'
                        md_bg_color: app.theme_cls.primary_color
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: #test
                            
                        

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
