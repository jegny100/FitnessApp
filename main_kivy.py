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
                    root.screen_manager.transition.direction = 'left'
                    
            OneLineListItem:
                text: "statistics"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "statistics"
                    root.screen_manager.transition.direction = 'left'
                    
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
                        on_release: 
                            screen_manager.current = "logging"
                            screen_manager.transition.direction = 'left'
                        
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
                    padding : '12dp'
                    
                    MDLabel:
                        text: "Logging Activity"
                        halign: "center"                        
                        valign: "bottom"
                        font_style : 'H5' 
                        theme_text_color : 'Secondary'
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'                        
                                  
                        MDLabel:
                            text: "Choose Activity"
                            halign: "center"
                            valign: "center"
                            
                        MDFlatButton:
                            id: logger_chosen_activity
                            text: app.chosen_activity
                            on_release: app.show_activities_dialog()
                            pos_hint: {"center_x": .5, "center_y": .5}
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                        
                        MDLabel:
                            text: "Date"
                            halign: "center"
                            
                        MDFlatButton:
                            id: logger_date
                            text: app.date
                            on_release: app.show_date_picker()
                            pos_hint: {"center_x": .5, "center_y": .5}
                    
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding : '10dp'
                        
                        MDLabel:
                            text: "Duration"
                            halign: "center"
                            
                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing : '25dp'
                            size_hint_x: None
                            height: self.minimum_width
                            
                            MDTextField:
                                id : logger_duration_hour
                                hint_text: "h"
                                mode: "rectangle"
                            
                            MDTextField:
                                id : logger_duration_min
                                hint_text: "m"
                                mode: "rectangle"
                        
                            MDTextField:
                                id : logger_duration_sec
                                hint_text: "s"
                                mode : "rectangle"
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                        
                        MDLabel:
                            text: "Repetitions"
                            halign: "center"
                            
                        MDTextField:
                            id : logger_repetition
                            mode: "rectangle"
                            size_hint_x: 0.5
                            pos_hint: {"center_x": .5, "center_y": .5}
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                        
                        MDLabel:
                            text: "Weight"
                            halign: "center"
                            
                        MDTextField:
                            id : logger_weight
                            icon_right: "weight-kilogram"
                            mode: "rectangle"
                            size_hint_x: 0.5
                            pos_hint: {"center_x": .5, "center_y": .5}
                            
                    MDIconButton:
                        id: logger_confirm
                        icon: 'check'
                        text: 'CONFIRM'
                        md_bg_color: app.theme_cls.primary_color
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: 
                            screen_manager.transition.direction = 'right'
                            screen_manager.current = "homescreen"
                            app.get_logger([logger_duration_hour.text,logger_duration_min.text,logger_duration_sec.text],logger_repetition.text, logger_weight.text)
                            
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
