from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color , Rectangle  # Add this import for Color
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video


# Initialize Firebase
cred = credentials.Certificate(r"C:\Users\riyak\OneDrive\Desktop\CitizenThreatApp\firebase-key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Reference to the Firestore collection for storing reports
reports_ref = db.collection("threat_reports")

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical",**kwargs,)
        self.add_widget(Image(source=r"C:\Users\riyak\OneDrive\Desktop\bg1.png", size_hint=(1, 2)))
        
        
        report_button = Button(text="Report Threat", size_hint=(1, 0.25), background_color=(255, 0, 0, 0.55))
        report_button.bind(on_press=self.open_report_screen)
        self.add_widget(report_button)

        view_button = Button(text="View Reports", size_hint=(1, 0.25), background_color=(0, 232, 255, 0.8))
        view_button.bind(on_press=self.open_view_screen)
        self.add_widget(view_button)

    def open_report_screen(self, instance):
        self.clear_widgets()
        self.add_widget(ReportThreatScreen())

    def open_view_screen(self, instance):
        self.clear_widgets()
        self.add_widget(ViewReportsScreen())


class ReportThreatScreen(BoxLayout):
  
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        
        # Name input
        self.add_widget(Label(text="Name:", font_size=28,bold= True,
                              size_hint_y=None,
                              height=30,
                              size_hint_x=None,
                              width=110))
        self.name_input = TextInput(hint_text="Enter your Name", multiline=True,
                                    size_hint_y=None,
                                    height=200,
                                    size_hint_x=None,
                                    width=100000,
                                    background_color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.name_input)
        
        # Contact number input
        self.add_widget(Label(text="Contact No.:", font_size=28,bold= True,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=170))
        self.contact_input = TextInput(hint_text="Enter your contact number", multiline=True,
                                       size_hint_y=None,
                                       height=200,
                                       size_hint_x=None,
                                       width=100000,
                                       background_color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.contact_input)
        
        # Threat description input
        self.add_widget(Label(text="Describe the Threat:", font_size=28,bold= True,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=270))
        self.threat_input = TextInput(hint_text="Enter threat details", multiline=True,
                                      size_hint_y=None,
                                      height=200,
                                      size_hint_x=None,
                                      width=100000,
                                      background_color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.threat_input)

        # Location input
        self.add_widget(Label(text="Enter Location:", font_size=28,bold= True,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=210))
        self.location_input = TextInput(hint_text="Enter location details", multiline=True,
                                        size_hint_y=None,
                                        height=200,
                                        size_hint_x=None,
                                        width=100000,
                                        background_color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.location_input)
        
        self.add_widget(Label(text="", font_size=28,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=210))

        # Create a horizontal BoxLayout for buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, padding=[650, 20], spacing=20)

        # Back button
        back_button = Button(text="Back", 
                             size_hint_x=None, 
                             width=300,
                             size_hint_y= None,
                             height=60,
                             background_color=(1, 0.2, 0.2, 1))
        
        back_button.bind(on_press=self.go_back)
        button_layout.add_widget(back_button)

        # Submit button
        submit_button = Button(text="Submit", 
                               size_hint_x=None, 
                               width=300,
                               size_hint_y= None,
                               height=60, 
                               background_color=(0.3, 0.8, 0.2, 1))
        submit_button.bind(on_press=self.submit_report)
        submit_button.bind(on_press=self.open_sumbit_screen)
        button_layout.add_widget(submit_button)

        # Add button layout to the screen
        self.add_widget(button_layout)

    def submit_report(self, instance):
        name= self.name_input.text
        contact= self.contact_input.text
        description = self.threat_input.text
        location = self.location_input.text
        
        if name and contact and description and location:
            # Get current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Add report to Firestore with time, description, and location
            reports_ref.add({
                "name": name,
                "contact": contact,
                "description": description,
                "location": location,
                "time": current_time  
            })
            self.name_input.text = "Name Submitted!"
            self.contact_input.text = "Contact details Submitted!"
            self.threat_input.text = "Report Submitted!"# Feedback to the user
            self.location_input.text = ""
            
    def open_sumbit_screen(self, instance):
        self.clear_widgets()
        self.add_widget(SumbitScreen())

    def go_back(self, instance):
        self.clear_widgets()
        self.add_widget(HomeScreen()) 

class SumbitScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.size_hint = (1, 1)  # Make sure the layout fills the screen

        # Use FloatLayout for precise positioning
        self.layout = FloatLayout(size_hint=(1, 1))
        self.add_widget(self.layout)

        # "Report Submitted!!" label centered at the top of the layout
        self.report_submitted_label = Label(
            text="Report Submitted!!", 
            font_size=58, 
            bold=True, 
            color=(0, 0.8, 0, 1),
            size_hint=(None, None),  
            size=(self.width, 80),  # Make it wide enough to center
            pos_hint={"center_x": 0.5, "center_y": 0.6}  # Centered at the top part
        )
        self.layout.add_widget(self.report_submitted_label)

        # Thank you message below the "Report Submitted!!"
        self.thank_you_label = Label(
            text="Thank you for your report. Our team will review the details and take appropriate action. "
                 "We appreciate your effort in helping us ensure safety and security in the community.", 
            font_size=20, 
            color=(1, 1, 1, 1),  
            size_hint=(None, None), 
            size=(self.width, 120),  
            pos_hint={"center_x": 0.5, "center_y": 0.5},  # Centered below the first label
            halign="center", 
            valign="middle"
        )
        self.layout.add_widget(self.thank_you_label)

        # Button layout for navigation (Back and View Reports)
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, padding=[650, -20], spacing=20)
        button_layout.pos_hint = {"center_x": 0.5, "y": 0.1}  # Position the button layout at the bottom

        back_button = Button(text="Back", 
                             size_hint_x=None, 
                             width=300,
                             size_hint_y=None, 
                             height=60,
                             background_color=(1, 0.2, 0.2, 1))
        
        back_button.bind(on_press=self.go_back)
        button_layout.add_widget(back_button)
        
        view_button = Button(text="View Reports", 
                             size_hint_x=None, 
                             width=300,
                             size_hint_y=None, 
                             height=60,
                             background_color=(0, 202, 187, 0.6))
        view_button.bind(on_press=self.open_view_screen)
        button_layout.add_widget(view_button)

        self.layout.add_widget(button_layout)

    def go_back(self, instance):
        self.clear_widgets()
        self.add_widget(ReportThreatScreen()) 

    def open_view_screen(self, instance):
        self.clear_widgets()
        self.add_widget(ViewReportsScreen1()) 

 
     
    
class ViewReportsScreen1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="Submitted Reports", font_size=34, bold=True, size_hint=(1, 0.1)))

        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.report_list = GridLayout(cols=1, size_hint_y=None, height=150,spacing=40, padding=10)
        self.report_list.bind(minimum_height=self.report_list.setter("height"))
        self.scroll_view.add_widget(self.report_list)
        self.add_widget(self.scroll_view)

        back_button = Button(text="Back", size_hint=(1, 0.1), background_color=(1, 0.2, 0.2, 1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        self.load_reports()

    def load_reports(self):
        # Fetch reports from Firestore and display them, sorted by time
        reports = [doc.to_dict() for doc in reports_ref.stream()]
        
        print(reports)  # Debugging: Print fetched reports to check if data is coming correctly
        
        sorted_reports = sorted(reports, key=lambda x: x.get("time", "1900-01-01 00:00:00"), reverse=True)  # Default value for missing 'time'

        for report in sorted_reports:
            report_card = BoxLayout(orientation="vertical", size_hint_y=None, height=150, padding=10, spacing=5)

            # Use .get() to avoid KeyError if 'description' or 'location' is missing
            name = report.get("name", "No Name provided")
            contact = report.get("contact", "No Contact provided")
            description = report.get("description", "No description provided")
            location = report.get("location", "No location provided")
            time = report.get("time", "Not Provided")
            
            # Ensure proper alignment
            report_card.add_widget(Label(text=f"Name: {name}", font_size=16, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Contact: {contact}", font_size=16, size_hint_y=None, height= 10, halign="left"))
            report_card.add_widget(Label(text=f"Description: {description}", font_size=16, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Location: {location}", font_size=14, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Time: {time}", font_size=14, size_hint_y=None, halign="left"))

            separator = Widget(size_hint_y=None, height=2)
            separator.canvas.add(Color(0.8, 0.8, 0.8, 1))  # Color is now imported
            separator.canvas.add(Rectangle(size=(self.width, 2)))
            report_card.add_widget(separator)

            self.report_list.add_widget(report_card)

    def go_back(self, instance):
        self.clear_widgets()
        self.add_widget(SumbitScreen())
        

class ViewReportsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="Submitted Reports", font_size=34, bold=True, size_hint=(1, 0.1)))

        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.report_list = GridLayout(cols=1, size_hint_y=None, height=150,spacing=40, padding=10)
        self.report_list.bind(minimum_height=self.report_list.setter("height"))
        self.scroll_view.add_widget(self.report_list)
        self.add_widget(self.scroll_view)

        back_button = Button(text="Back", size_hint=(1, 0.1), background_color=(1, 0.2, 0.2, 1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        self.load_reports()

    def load_reports(self):
        # Fetch reports from Firestore and display them, sorted by time
        reports = [doc.to_dict() for doc in reports_ref.stream()]
        
        print(reports)  # Debugging: Print fetched reports to check if data is coming correctly
        
        sorted_reports = sorted(reports, key=lambda x: x.get("time", "1900-01-01 00:00:00"), reverse=True)  # Default value for missing 'time'

        for report in sorted_reports:
            report_card = BoxLayout(orientation="vertical", size_hint_y=None, height=150, padding=10, spacing=5)

            # Use .get() to avoid KeyError if 'description' or 'location' is missing
            name = report.get("name", "No Name provided")
            contact = report.get("contact", "No Contact provided")
            description = report.get("description", "No description provided")
            location = report.get("location", "No location provided")
            time = report.get("time", "Not Provided")
            
            # Ensure proper alignment
            report_card.add_widget(Label(text=f"Name: {name}", font_size=16, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Contact: {contact}", font_size=16, size_hint_y=None, height= 10, halign="left"))
            report_card.add_widget(Label(text=f"Description: {description}", font_size=16, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Location: {location}", font_size=14, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Time: {time}", font_size=14, size_hint_y=None, halign="left"))

            separator = Widget(size_hint_y=None, height=2)
            separator.canvas.add(Color(0.8, 0.8, 0.8, 1))  # Color is now imported
            separator.canvas.add(Rectangle(size=(self.width, 2)))
            report_card.add_widget(separator)

            self.report_list.add_widget(report_card)

    def go_back(self, instance):
        self.clear_widgets()
        self.add_widget(HomeScreen())



class CitizenThreatApp(App):
    def build(self):
        return HomeScreen()


if __name__ == "__main__":
    CitizenThreatApp().run()
