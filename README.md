# criminalip_dns_monitor
OSINT representative search service Criminal IP's Python API is used to monitor threat information, which is a registered domain.  It was developed based on the Python Flask web framework.

Running a Python Flask Application with SQLAlchemy and External API Integration

This guide outlines the steps to run a Python Flask web application that integrates SQLAlchemy for database management and utilizes an external API to retrieve information about bookmarked domains. The application allows users to save domain bookmarks, fetch information about those domains using a third-party API, and display the gathered data.

Prerequisites:

Python installed on your machine.
Basic understanding of Flask and web development concepts.
An API key from criminalip.io to access domain reports.
Steps:

Clone the Repository:

Start by cloning the GitHub repository containing the Flask application code.

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Install Dependencies:

Navigate to the repository folder and install the required Python packages using pip.

bash
Copy code
pip install Flask Flask-SQLAlchemy requests
API Key Setup:

Replace "YOUR KEY" in the headers dictionary with your actual API key from criminalip.io.

Database Configuration:

Configure the SQLite database URI and disable SQLAlchemy track modifications in the app.config section:

python
Copy code
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookmark.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Run Database Migration:

Inside the if __name__ == "__main__": block, create the necessary database tables by running:

bash
Copy code
python app.py
Run the Application:

Start the Flask application by running:

bash
Copy code
python app.py
The application will start locally on http://127.0.0.1:5000/.

Access the Application:

Open your web browser and navigate to http://127.0.0.1:5000/ to access the running Flask application. You will be able to input and save domain bookmarks. The application will fetch domain information using the provided API key and display the gathered data on the homepage.

Note:

This guide assumes you have the necessary API key and that the external API is available and functioning.
Ensure that your API key is kept secure and not shared in your public repository.
By following these steps, you can run the provided Flask application on your local machine and interact with it via your web browser. Remember to replace <repository_url> and <repository_folder> with the actual GitHub repository information.
