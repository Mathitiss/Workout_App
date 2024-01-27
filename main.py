import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

kivy.require('1.9.0')


Builder.load_string("""
<Choosing>: ############################################################################################## CHOOSING BODY PART SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size
            
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            color: 0, 0, 0
            font_size: 30  
            text: 'CHOOSE A BODY PART'
            bold: True
        
        Button:
            text: "UPPER BODY"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'UpperMuscles'

        Button:
            text: "LOWER BODY"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'LowerMuscles'

        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\WorkoutLogo-300x90.png'
            

<UpperMuscles>: ############################################################################################## UPPER MUSCLE SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size
            
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            color: 0, 0, 0
            font_size: 30  
            text: 'CHOOSE A MUSCLE'
            bold: True
        
        Button:
            text: "Arms" 
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Arms'
    
        Button:
            text: "Chest"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Chest'

        Button:
            text: "Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Back'
    
        Button:
            text: "Abs"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Abs'

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Choosing'


<Arms>: ############################################################################################## ARM MUSCLES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size
        
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 27
            color: 0, 0, 0
            text: 'CHOOSE AN ARM MUSCLE'
            bold: True

        Button:
            text: "Shoulders"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Shoulders'

        Button:
            text: "Biceps" 
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Biceps'
    
        Button:
            text: "Triceps"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Triceps'

        Button:
            text: "Forearms"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Forearms'

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'UpperMuscles'
                
                
<Shoulders>: ############################################################################################## SHOULDERS EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Shoulders\\Barbell Press.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Shoulders\\Barbell Raises.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Shoulders\\Dumbbell Front Raises.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Shoulders\\Dumbbell Press.jpg'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Shoulders\\Dumbbell Raises.png'
                size: self.size
                pos: self.pos        

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Arms'


<Biceps>: ############################################################################################## BISEPS EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Biceps\\Barbell Curls.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Biceps\\Barbell Curls 2.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Biceps\\Dumbbell Curl.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Biceps\\Hammer Curls.jpg'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Biceps\\Incline Dumbbell Curl.png'
                size: self.size
                pos: self.pos        
            
        
        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Arms'


<Triceps>: ############################################################################################## TRICEPS EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Triceps\\Cable Press.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Triceps\\Dips.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Triceps\\Dumbell Press.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Triceps\\Push Ups.png'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Triceps\\Skull Crusher.png'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Arms'


<Forearms>: ############################################################################################## FOREARMS EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Forearms\\Forearms Barbell.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Forearms\\Forearms Dumbbell.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Forearms\\Plate Rises.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Arms\\Forearms\\Wrist Roller.jpg'
                size: self.size
                pos: self.pos         
            
        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Arms'


<Chest>: ############################################################################################## CHEST EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Arnold Press.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\BenchPress.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Butterfly.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Cables Press.png'
                size: self.size
                pos: self.pos         
            
            Image: 
            
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Cables Press 2.png'
                size: self.size
                pos: self.pos
                
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Dips.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Dumbbell Press.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Dumbbell Press 45.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Flyes.jpg'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Plates Press.jpg'
                size: self.size
                pos: self.pos

            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Pullover.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Push Ups.png'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Chest\\Sitting Press.jpg'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'UpperMuscles'


<Back>: ############################################################################################## BACK EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Barbell Pull.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Barbell Row.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Barbell Row 2.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Cable Pull.png'
                size: self.size
                pos: self.pos         
            
            Image: 
            
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Dumbells Row.png'
                size: self.size
                pos: self.pos
                
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Hiperextention.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Plates Pull.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Pull Down Block.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Pull Up Block.png'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Pull Ups.png'
                size: self.size
                pos: self.pos

            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Back\\Single Dumbell Row.png'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'UpperMuscles'


<Abs>: ############################################################################################## ABS EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Abs Classic.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Abs Dumbell.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Abs Hang.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Abs Rolling.png'
                size: self.size
                pos: self.pos         
            
            Image: 
            
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Bicecle.png'
                size: self.size
                pos: self.pos
                
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Book.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Cisors.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Full Abs.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Abs 45.jpg'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Plank Side.png'
                size: self.size
                pos: self.pos

            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Upper Body\\Abs\\Russian Twist.jpg'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'UpperMuscles'


<LowerMuscles>: ############################################################################################## LOWER MUSCLE SCREEN

    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size
            
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            color: 0, 0, 0
            font_size: 30  
            text: 'CHOOSE A MUSCLE'
            bold: True
        
        Button:
            text: "Legs"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Legs'
        
        Button:
            text: "Calves"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Calves'
                
        Button:
            text: "Glutes"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 20
            bold: True
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 2
                root.manager.current = 'Glutes'

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Choosing'

<Legs>: ############################################################################################## LEGS EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Bulgar Squats.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\CuttleBell Squats.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Dumbells Squads.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Dumbells Squads.png'
                size: self.size
                pos: self.pos         
            
            Image: 
            
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Dumbells Stand Ups.png'
                size: self.size
                pos: self.pos
                
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Machine Press.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Machine Rises.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Machine Stands.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Squads.png'
                size: self.size
                pos: self.pos         
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Wide Dumbell Squad.png'
                size: self.size
                pos: self.pos

            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Legs\\Machine Press 2.jpg'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'LowerMuscles'


<Calves>: ############################################################################################## CALVES EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Calves\\Calves Dumbells Raises.png'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Calves\\Calves Standing.jpg'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Calves\\Machine Calves.png'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'LowerMuscles'


<Glutes>: ############################################################################################## BUTT EXERCISES SCREEN
    canvas:
        Color:
            rgba: 255, 255, 255 
        Rectangle:
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        
        Carousel:
            direction: 'bottom'
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Glutes\\Beattle.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Glutes\\Deadlift.png'
                size: self.size
                pos: self.pos    
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Glutes\\Lieng Press.jpg'
                size: self.size
                pos: self.pos
            
            Image:
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Glutes\\Machine Press.png'
                size: self.size
                pos: self.pos         
            
            Image: 
            
                source: r'C:\\Users\\egorm\\PycharmProjects\\WorkOutApp\\Images\\Exercises\\Lower Body\\Glutes\\Standing Press.png'
                size: self.size
                pos: self.pos

        Button:
            text: "<< Go Back"
            background_color : 255, 255, 255
            color: 0, 0, 0
            font_size: 15
            bold: True
            size: 100, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'LowerMuscles'

""")


class Choosing(Screen):       ########################################### CHOOSING BODY PART SCREEN
    pass

class UpperMuscles(Screen):   ########################################### CHOOSING UPPER BODY MUSCLE   \/ \/ \/
    pass

class Chest(Screen):
    pass

class Back(Screen):
    pass

class Abs(Screen):
    pass

class Arms(Screen):       ########################################### CHOOSING ARM MUSCLE   \/ \/ \/
    pass

class Shoulders(Screen):
    pass

class Biceps(Screen):
    pass

class Triceps(Screen):
    pass

class Forearms(Screen):
    pass

class LowerMuscles(Screen):   ########################################### CHOOSING LOWER BODY MUSCLE   \/ \/ \/
    pass

class Legs(Screen):
    pass

class Calves(Screen):
    pass

class Glutes(Screen):
    pass


screen_manager = ScreenManager()

screen_manager.add_widget(Choosing(name="Choosing"))

screen_manager.add_widget(UpperMuscles(name="UpperMuscles"))

screen_manager.add_widget(Arms(name="Arms"))
screen_manager.add_widget(Shoulders(name="Shoulders"))
screen_manager.add_widget(Biceps(name="Biceps"))
screen_manager.add_widget(Triceps(name="Triceps"))
screen_manager.add_widget(Forearms(name="Forearms"))

screen_manager.add_widget(Back(name="Back"))
screen_manager.add_widget(Chest(name="Chest"))
screen_manager.add_widget(Abs(name="Abs"))

screen_manager.add_widget(LowerMuscles(name="LowerMuscles"))
screen_manager.add_widget(Legs(name="Legs"))
screen_manager.add_widget(Calves(name="Calves"))
screen_manager.add_widget(Glutes(name="Glutes"))



class ScreenApp(App):
    def build(self):
        Window.size = (375, 645)
        return screen_manager

sample_app = ScreenApp()
sample_app.run()




