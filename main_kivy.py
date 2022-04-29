KV = '''
# ListItem Object for the display of the activity collection including 
# the correspondent buddy as an icon
<ListItem>:
    IconRightWidget:
        icon: root.icon

# ItemConfirm Object for Single Choice Dialog Windows
<ItemConfirm>
    on_release: root.set_icon(check)
    
    CheckboxLeftWidget:
        id: check
        group: "check"
        
# BuddyConfirm Object for adding a buddy to a new activity
<BuddyConfirm>
    on_release: root.set_buddy(check)
    
    CheckboxLeftWidget:
        id: check
        group: "check"

# Menu for Navigation through subpages
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
                    Window.size = (Window.size[0] + 1, Window.size[1])
            
            OneLineListItem:
                text: "Settings"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "settings"
                    root.screen_manager.transition.direction = 'left'
   
### THE APP ###                 
                    
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
            
            # Home Screen
            MDScreen:
                name: "homescreen"
            
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "32dp"
                    
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            size_hint_y : 0.5
                            text :'Welcome to your science-based fitness tracker!'
                            halign : 'center'
                            valign : 'top'
                            font_style : 'H5'  
                            parent_background: app.theme_cls.primary_color
                        MDLabel:
                    
                    MDBoxLayout:
                        size_hint_y : 0.8
                        orientation: "horizontal"
                        
                        FitImage:
                            source: app.get_random_buddy_image()
                            radius: [20,]
                        
                        MDLabel:
                            size_hint_x : 0.1
                            
                        MDLabel:
                            id: random_image_name
                            text: "Hi! Come and work out with me!"
                    
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Log your new activity here:"
                            halign : 'center'
                            valign : 'bottom'

                        MDIconButton:
                            icon: 'plus'
                            spacing: '10dp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            md_bg_color: app.theme_cls.primary_color
                            on_release: 
                                screen_manager.current = "logging"
                                screen_manager.transition.direction = 'left'
            
            # Settings Screen        
            MDScreen:
                name: "settings"
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing : '15dp'
                    padding : '12dp'
                    
                    MDLabel:
                        text: "Settings"
                        halign: "center"                        
                        valign: "top"
                        font_style : 'H5' 
                        theme_text_color : 'Secondary'
                        size_hint_y : 0.1
                                
                    # Reminder & Encouragement Box
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: '10dp'   
                        
                        # headline
                        MDBoxLayout:
                            orientation: "horizontal"
                            MDLabel:
                                text: "Reminder & Encouragement"
                                font_style : 'H6'
                                theme_text_color : 'Secondary'
                            
                            TooltipMDIconButton:
                                icon: "information-outline"  
                                tooltip_text: "test"
                                tooltip_bg_color: app.theme_cls.primary_color
                                valign: "top"
                         
                        # Slider        
                        MDBoxLayout:
                            orientation: "horizontal"
                        
                            MDLabel:
                                text: "Encouragement after logging a workout"
                                size_hint_x : 0.8

                            MDBoxLayout:
                                orientation: "vertical"  
                                
                                MDSlider:
                                    id: setting_logg_encouragement
                                    min: 0
                                    max: 2
                                    step: 1
                                    hint: False
                                    color: app.theme_cls.primary_color
                                    
                                    
                                MDBoxLayout:
                                    orientation: "horizontal"
                                    
                                    MDLabel:
                                        text: "Never"
                                        halign: "left"
                                        valign: "center"
                                        font_style: "Caption"
                                        
                                    MDLabel:
                                        text: "Sometimes"
                                        halign: "left"
                                        valign: "center"
                                        font_style: "Caption"
                                        size_hint_x: 1.2
                                        
                                    MDLabel:
                                        text: "Always"
                                        halign: "right"
                                        valign: "center"
                                        font_style: "Caption"            
                        # switch
                        MDBoxLayout:
                            orientation: "horizontal"                     
                                      
                            MDLabel:
                                text: "Reminder on startscreen"
                            
                            MDSwitch:  
                                id : setting_start_reminder
                                pos_hint: {"center_x": .9, "center_y": .5}
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                    
                        MDIconButton:
                            id: settings_close
                            icon: 'close'
                            md_bg_color: app.theme_cls.primary_color      
                            on_release:
                                screen_manager.transition.direction = 'right'
                                screen_manager.current = "homescreen"
                            
                        MDLabel:              
                        
                        MDIconButton:
                            id: activity_confirm
                            icon: 'check'
                            text: 'CONFIRM'
                            md_bg_color: app.theme_cls.primary_color
                            on_release: 
                                #app.change_settings()
                                screen_manager.current = "homescreen" 
                    
            
            # Activity Collection Screen
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
                        md_bg_color: app.theme_cls.primary_color
                        on_release: 
                            screen_manager.current = "add_activity"
                            screen_manager.transition.direction = 'left'

            # Activity Collection Subscreen : Add New Activity to Collection
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
            
            # Buddy Screen
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
                                source: "images/Bo.jpg"
                                radius: [20,]
                        
                            MDLabel:
                                size_hint_y : 0.01
                                
                            MDRectangleFlatButton:
                                id: bo_button
                                text: "Bo"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                size_hint_y : 0.1
                                on_press: 
                                    app.set_convo_info(bo_button.text)
                                
                        MDSwiperItem:
                            orientation: 'vertical'
                            FitImage:
                                source: "images/Penguin.jpg"
                                radius: [20,]
                            
                            MDLabel:
                                size_hint_y : 0.01
                                
                            MDRectangleFlatButton:
                                id: penguin_button
                                text: "Penguin"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                size_hint_y : 0.1
                                on_press: 
                                    app.set_convo_info(penguin_button.text)
                        
                        MDSwiperItem:
                            orientation: 'vertical'
                            FitImage:
                                source: "images/Robin.jpg"
                                radius: [20,]
                            
                            MDLabel:
                                size_hint_y : 0.01
                        
                            MDRectangleFlatButton:
                                id: robin_button
                                text: "Robin"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                size_hint_y : 0.1
                                on_press: 
                                    app.set_convo_info(robin_button.text)
            
            # Buddy Screen Subscreen : Buddy Detail & Choose a chat                        
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
                            
                            MDLabel:
                                id: buddy_name
                                text: 
                                halign: "center"                        
                                valign: "center"
                                size_hint_y : 0.5
                                
                            MDLabel:
                                id: buddy_description
                                text: 
                                halign: "center"                        
                                valign: "center"
                            MDLabel:    
                            MDLabel:
                            
                    MDBoxLayout: 
                        orientation: 'vertical'
                        spacing : '15dp'
                        padding : '12dp'
                        
                        MDLabel:
                            size_hint_y : 0.2
                        
                        MDBoxLayout:
                            orientation: 'horizontal'
                            MDLabel:
                            MDRectangleFlatButton:
                                id: workout_convo_btn
                                text: "How is my workout working out?"
                                on_press:
                                    app.callback_activity_menu()
                            MDLabel:
                            
                        MDBoxLayout:  
                            orientation: 'horizontal'  
                            MDLabel: 
                            MDRectangleFlatButton:
                                id: chat
                                text: "                  Let's chat a little                 "
                                on_press: 
                                    app.start_convo("chat")
                            MDLabel:
                            
                        MDLabel:
                            size_hint_y : 0.2
                              
            # Buddy Screen Subscreen : Conversation Screen
            MDScreen:
                name: "convo_page"
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing : '15dp'
                    padding : '12dp'
                
                    MDBoxLayout:
                        orientation: 'horizontal'
                        
                        MDLabel:
                            size_hint_x : 0.25
                        FitImage:
                            id: convo_image_id
                            radius: [20,]
                            source: 
                        MDLabel:
                            size_hint_x : 0.25
                            
                    MDBoxLayout: 
                        orientation: "vertical"
                        
                        MDLabel:
                            id: convo_buddy_name
                            text: 
                            font_style: 'H6'
                            halign: "center"
                            size_hint_y : 0.1
                        
                        MDBoxLayout: 
                            orientation: "horizontal"
                            MDLabel:
                                size_hint_x : 0.1
                            MDLabel:
                                id: convo_chat
                                text:
                                halign: "center"
                            MDLabel:
                                size_hint_x : 0.1
                            
                        MDBoxLayout:
                            size_hint_y : 0.3
                            orientation: "horizontal"
                            MDLabel:
                                size_hint_x : 0.1
                            MDRectangleFlatButton:
                                text: "Back"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press: 
                                    app.last_message()

                                    
                            MDRectangleFlatButton:
                                text: "Continue"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press:
                                    app.next_message()
                            MDLabel:
                                size_hint_x : 0.1
                
            # Activity Logger Screen
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
                        
                    # Chosen Activity for logging
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'                        
                                  
                        MDLabel:
                            text: "Choose Activity"
                            halign: "center"
                            valign: "center"
                            
                        MDRectangleFlatButton:
                            id: logger_chosen_activity
                            text: app.chosen_activity
                            on_release: app.show_activities_dialog()
                            pos_hint: {"center_x": .5, "center_y": .5}
                    
                    # Date
                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: '10dp'
                        
                        MDLabel:
                            text: "Date"
                            halign: "center"
                            
                        MDRectangleFlatButton:
                            id: logger_date
                            text: app.date
                            on_release: app.show_date_picker()
                            pos_hint: {"center_x": .5, "center_y": .5}
                    
                    # Duration        
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
                    
                    # Repetitions       
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
                    
                    # Weight 
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
                            
                    # Buttons for close / save
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
                                if app.chosen_activity_check() and app.check_collection_required() : app.handle_logger()
        
        # handle Object Properties                    
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
