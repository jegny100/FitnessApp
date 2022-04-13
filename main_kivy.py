KV = '''
<ListItem>:
    IconRightWidget:
        icon: root.icon

<ItemConfirm>
    on_release: root.set_icon(check)
    
    CheckboxLeftWidget:
        id: check
        group: "check"
        
<BuddyConfirm>
    on_release: root.set_buddy(check)
    
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
                text: "Activity Collection"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "activity_collection"
                    root.screen_manager.transition.direction = 'left'
                    app.load_activity_collection_list()
                    
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
                name: "activity_collection"
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "32dp"
                       
                    MDLabel:
                        text: "Activity Collection"
                        halign: "center"
                    
                    ScrollView:
                        MDList:
                            id: container
                                
                    MDBoxLayout:    
                        MDIconButton:
                            id : add_activity_plus
                            icon: 'plus'
                            spacing: '10dp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            md_bg_color : (154 / 255.0, 212 / 255.0, 194 / 255.0, 1)
                            on_release: 
                                screen_manager.current = "add_activity"
                                screen_manager.transition.direction = 'left'
            
                                
            MDScreen:
                name: "add_activity"
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing : '15dp'
                    padding : '12dp'
                    
                    MDLabel:
                        text: "Add an Activity to your collection"
                        halign: "center"                        
                        valign: "top"
                        font_style : 'Subtitle1' 
                        theme_text_color : 'Secondary'
                    
                    MDLabel:
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        MDLabel:
                        
                        MDIconButton:
                            id: buddy
                            icon: app.chosen_buddy
                            #icon: 'images/RedPanda.jpg'
                            user_font_size: "100sp"
                            size: self.parent.size
                            on_release:
                                app.show_buddy_dialog()
                            
                        MDLabel:

                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'                        
                                  
                        MDLabel:
                            text: "Activity Name"
                            halign: "left"
                            valign: "center"
                            
                        MDTextField:  
                            id : activity_name
                            mode: "rectangle"
                            size_hint_x: 0.5
                            pos_hint: {"center_x": .5, "center_y": .5}
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'                        
                                  
                        MDLabel:
                            text: "Duration Required"
                            halign: "left"
                            valign: "center"
                            
                        MDSwitch:  
                            id : duration_switch
                            pos_hint: {"center_x": .9, "center_y": .5}
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'                        
                                  
                        MDLabel:
                            text: "Repetitions Required"
                            halign: "left"
                            valign: "center"
                            
                        MDSwitch:  
                            id : repetition_switch
                            pos_hint: {"center_x": .9, "center_y": .5}

                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'                        
                                  
                        MDLabel:
                            text: "Weight Required"
                            halign: "left"
                            valign: "center"
                            
                        MDSwitch:  
                            id : weight_switch
                            pos_hint: {"center_x": .9, "center_y": .5}
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                    
                        MDIconButton:
                            id: activity_cancel
                            icon: 'close'
                            md_bg_color: app.theme_cls.primary_color      
                            on_release:
                                screen_manager.transition.direction = 'right'
                                screen_manager.current = "activity_collection"
                            
                        MDLabel:              
                        
                        MDIconButton:
                            id: activity_confirm
                            icon: 'check'
                            text: 'CONFIRM'
                            md_bg_color: app.theme_cls.primary_color
                            on_release: 
                                app.add_activity_to_collection(activity_name.text, duration_switch.active, repetition_switch.active, weight_switch.active)
                                app.load_activity_collection_list()          
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
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                    
                        MDIconButton:
                            id: logger_cancel
                            icon: 'close'
                            md_bg_color: app.theme_cls.primary_color      
                            on_release:
                                screen_manager.transition.direction = 'right'
                                screen_manager.current = "homescreen"
                                app.empty_logger()
                            
                        MDLabel:              
                        
                        MDIconButton:
                            id: logger_confirm
                            icon: 'check'
                            text: 'CONFIRM'
                            md_bg_color: app.theme_cls.primary_color
                            on_release: 
                                screen_manager.transition.direction = 'right'
                                app.get_logger([logger_duration_hour.text,logger_duration_min.text,logger_duration_sec.text],logger_repetition.text, logger_weight.text)
                                if not app.chosen_activity_check(): app.error_activity_dialog()
                                if app.chosen_activity_check() and not app.check_collection_required() : app.error_required_dialog()
                                if app.chosen_activity_check() and app.check_collection_required() : app.save_logger()
                            
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
