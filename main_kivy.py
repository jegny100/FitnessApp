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
                    
            OneLineListItem:
                text: "Buddys"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "buddys"
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
                name: "activity_collection"
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "32dp"
                    spacing: '10dp'
                       
                    MDLabel:
                        size_hint_y : 0.1
                        text: "Activity Collection"
                        font_style : 'Subtitle1'
                        halign: "center"
                        theme_text_color : 'Secondary'
                    
                    ScrollView:
                        MDList:
                            id: container
                     
                    MDIconButton:
                        id : add_activity_plus
                        icon: 'plus'
                        spacing: '20dp'
                        pos_hint: {"center_x": .5, "center_y": .5}
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
                            theme_text_color : 'Secondary'
                            
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
                name: "buddys"
                
                MDBoxLayout:
                    id:buddy_box_id
                    orientation: "vertical"
                    spacing : '15dp'
                    padding : '12dp'
                    
                    MDLabel:
                        size_hint_y : 0.1
                        text: "Your Workout Buddys"
                        halign: "center"                        
                        valign: "bottom"
                        font_style : 'H5' 
                        theme_text_color : 'Secondary'
                        
                    MDSwiper:
                        
                        MDSwiperItem:
                            orientation: 'vertical'
                            FitImage:
                                source: "images/RedPanda.jpg"
                                radius: [20,]
                                
                            MDRectangleFlatButton:
                                text: "Red Panda"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                size_hint_y : 0.1
                                
                        MDSwiperItem:
                            orientation: 'vertical'
                            FitImage:
                                source: "images/Penguin.jpg"
                                radius: [20,]
                                
                            MDRectangleFlatButton:
                                text: "Penguin"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                size_hint_y : 0.1
                        
                        MDSwiperItem:
                            orientation: 'vertical'
                            FitImage:
                                source: "images/Robin.jpg"
                                radius: [20,]
                        
                            MDRectangleFlatButton:
                                id: robin_button
                                text: "Robin"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                size_hint_y : 0.1
                                on_press: 
                                    app.set_convo_infos(robin_button.text)
                                    
            MDScreen:
                name: "buddy_page"
                
                MDBoxLayout:
                    orientation: 'vertical' 
                
                    MDBoxLayout:
                        orientation: 'horizontal'
                        spacing : '15dp'
                        padding : '12dp'
                    
                        FitImage:
                            id: buddy_page_image_id
                            radius: [20,]
                            source:
                            
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y : 0.5
                            
                            MDLabel:
                                id: buddy_name
                                text: 
                                halign: "center"                        
                                valign: "top"
                                
                            MDLabel:
                                id: buddy_description
                                text: 
                                halign: "center"                        
                                valign: "bottom"
                            MDLabel:    
                            MDLabel:
                            
                    MDBoxLayout: 
                        orientation: 'vertical'
                        spacing : '15dp'
                        padding : '12dp'
                        
                        MDLabel:
                        
                        MDBoxLayout:
                            orientation: 'horizontal'
                            MDLabel:
                            MDRectangleFlatButton:
                                text: "How is my workout working out?"
                                on_press:
                                    screen_manager.current = "buddy_convo_page"                                    
                            MDLabel:
                            
                        MDBoxLayout:  
                            orientation: 'horizontal'  
                            MDLabel: 
                            MDRectangleFlatButton:
                                text: "Let's chat a little"
                            MDLabel:
                              
            MDScreen:
                name: "buddy_convo_page"
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing : '15dp'
                    padding : '12dp'
                
                    MDBoxLayout:
                        orientation: 'horizontal'
                        
                        MDLabel:
                        FitImage:
                            id: convo_page_image_id
                            radius: [20,]
                            source: 
                        MDLabel:
                            
                    MDBoxLayout: 
                        orientation: "vertical"
                        MDLabel:
                            id: convo_window
                            text: "Hier steht ein lustiger Text"

                        MDBoxLayout:
                            MDRectangleFlatButton:
                                text: "Back"
                                pos_hint: {"center_x": .5, "center_y": .5}
                            MDRectangleFlatButton:
                                text: "Continue"
                                pos_hint: {"center_x": .5, "center_y": .5}
                
            
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
