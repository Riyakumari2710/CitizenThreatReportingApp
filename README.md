[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5EYOwlQ1)
# Citizen Threat Reporting APP

This is a Kivy-based mobile application for reporting and viewing potential threats in the community. It allows users to submit reports detailing threats they encounter and view other submitted reports. The app integrates with Firebase to store and retrieve reports.

## Features

Report Threats: Users can submit reports detailing threats, including their name, contact number, threat description, and location.

View Reports: Users can view a list of submitted reports, which are displayed in chronological order.

Firebase Integration: All reports are stored and retrieved from Firebase Firestore.

User Feedback: After submitting a report, users will receive feedback confirming the submission.

## Requirements
To run this app, you'll need the following:

Python: Version 3.x

Kivy: Version 2.x or later

Firebase Admin SDK: To interact with Firebase Firestore

Other dependencies:

firebase-admin

kivy

To install dependencies, use the following command:
bash
pip install kivy firebase-admin

### Setting Up Firebase
Go to Firebase Console.

Create a new Firebase project or select an existing one.

Under Project Settings, create a new Service Account and download the JSON credentials.

Save the firebase-key.json file and replace the path in the following line of code with the path to your credentials:

### python

cred = credentials.Certificate(r"C:\path\to\your\firebase-key.json")

### File Structure
bash
CitizenThreatApp/


├── main.py                 # Main Kivy application code

├── firebase-key.json       # Firebase credentials (should not be uploaded to GitHub)

├── README.md               # Documentation for setting up and using the app

### How to Run the Application

Install the required dependencies by running the command mentioned above.

Make sure you have the Firebase credentials (downloaded firebase-key.json).

Modify the path to the Firebase credentials in the script as needed.

Run the app with:
bash
python main.py
This will start the app, and you will see the Home Screen with options to report a threat or view existing reports.

### App Screens

Home Screen: The starting screen where you can choose to either report a threat or view existing reports.

![Screenshot (164)](https://github.com/user-attachments/assets/da17ea4f-d6e3-4389-8990-a03be1eac9de)

Report Threat Screen: A form where users can input details about the threat (name, contact, description, location).

![Screenshot (165)](https://github.com/user-attachments/assets/5b5b8af7-2958-49b9-924b-d76ced78cf39)

Submit Screen: A confirmation screen shown after submitting a report with a thank you message.

![Screenshot (166)](https://github.com/user-attachments/assets/a766f923-7019-4c03-bdd6-3c1a082609ce)

View Reports Screen: Displays all submitted reports in a scrollable list, showing name, contact, description, location, and submission time.

![Screenshot (167)](https://github.com/user-attachments/assets/d0d2980c-43f9-4f49-b797-bd21e88eb9e9)

### Firebase Data Structure

The data from each report is stored in the Firebase Firestore database as follows:

Collection: threat_reports

#### Document Fields:
name: Name of the person submitting the report.

contact: Contact number of the person.

description: Description of the threat.

location: Location of the threat.

time: Timestamp of when the report was submitted.
