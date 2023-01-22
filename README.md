# Run-Colab
This is a simple Flask application that allows you to download and run a Google Colab notebook from a URL.

Requirements
Flask
gdown
Usage

To run the application, you need to have Flask and gdown installed. You can install them using pip:
pip install flask gdown
python app.py

The application will be running on http://localhost:5000/
To download and run a Colab notebook, you need to make a GET request to the endpoint /run-colab and include the Google Drive ID of the Colab notebook in the URL.
For example :
http://localhost:5000/run-colab?colab_notebook_id=<your_ID_here>

The application will then download the notebook from the URL and save it as colab.ipynb in the current directory.

The endpoint returns a JSON object with a message key and value indicating that the notebook ran successfully.

Note
You need to have the access to the Google Colab notebook in order to download it via the link.

Limitations
This is a simple application intended for demonstration purposes only, it is not suitable for use in a production environment.

License
This project is licensed under the MIT License.

Author
This code was written by ChatGPT and is open to contributions.

Please feel free to use, modify, and distribute this code as you see fit. And don't hesitate to contact me if you have any questions or suggestions.


