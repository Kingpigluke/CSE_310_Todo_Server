Cloud Firestore To‑Do List Application

A simple Python-based to‑do list application that stores, retrieves, updates, and deletes task data using Google Cloud Firestore. This project demonstrates how to connect a local Python program to a cloud NoSQL database and perform full CRUD operations.

Instructions for Build and Use
Steps to build and/or run the software
Create and activate a virtual environment

Code
python -m venv venv
Activate it:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install required libraries

Code
pip install google-cloud-firestore
Download your Firebase service account key

Go to Firebase → Project Settings → Service Accounts

Click Generate new private key

Save it as serviceAccountKey.json in your project folder

Ensure Firestore is created

Go to Firebase Console → Firestore

Click Create database

Choose Start in test mode

Run the program

Code
python todo.py
Instructions for using the software
When the program runs, it automatically:

Adds a task

Reads all tasks

Updates a task

Deletes a task

You can modify the function calls at the bottom of todo.py to:

Add new tasks

Update existing tasks

Delete tasks

Print all tasks

View your stored data in:
Firebase Console → Firestore → Data

Development Environment
To recreate the development environment, install the following:

Python 3.12

VS Code with the Python extension

google-cloud-firestore (Python library)

Firebase project with:

Firestore enabled

Service account key downloaded

Useful Websites to Learn More
These resources were helpful during development:

Firebase Firestore Documentation

Google Cloud Firestore Python Client (cloud.google.com in Bing)

Firebase Console (console.firebase.google.com in Bing)

Python Virtual Environments (docs.python.org in Bing)

Future Work
The following items could be added or improved in future versions:

[ ] Add a menu system (Add/View/Update/Delete tasks interactively)

[ ] Add timestamps for task creation and completion

[ ] Add a GUI using Tkinter or PyQt

[ ] Add user authentication with Firebase Auth

[ ] Deploy as a web app using Flask or FastAPI

[ ] Add error handling and input validation
