# FilmList Web App

FilmList is a simple web application built with Flask and MongoDB that allows you to manage your list of films. You can add, delete, mark as viewed, and edit film entries in your list.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/VitaliySynytskyi/FilmList.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd FilmList
   ```

3. **Create and Activate a Python Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up MongoDB**:

   - Install MongoDB and start the MongoDB server.
   - Update the MongoDB connection URL in `app.py` to match your MongoDB setup:

     ```python
     client = MongoClient("mongodb://localhost:27017/")
     ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Web App**:

   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

3. **Interact with the App**:

   - Add new films by providing a title and director.
   - Delete films by clicking the "Delete" button.
   - Mark films as viewed or not viewed by clicking the "Toggle Viewed" button.
   - Edit film details by clicking the "Edit" button.

## Features

- **Add Films**: Easily add new films to your list.
- **Delete Films**: Remove films from your list when you no longer need them.
- **Toggle Viewed**: Mark films as viewed or not viewed.
- **Edit Films**: Update film titles, directors, and viewing status.

## Technologies Used

- **Flask**: A Python web framework used for building the web application.
- **MongoDB**: A NoSQL database used to store film data.
- **Bootstrap**: A CSS framework for enhancing the user interface.
