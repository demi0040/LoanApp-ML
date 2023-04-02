# LoanApp-ML

Loan and Insurance Prediction App
=================================

This is a Flask application that allows users to register and login, create customers, and make two predictions for each customer: loan approval and insurance premium predictions. The application uses SQLite for database management and the pickle library to use the machine learning predictions in the application.

Dependencies
------------

The following Python packages are required to run the application:

*   Flask
*   Flask-WTF
*   SQLAlchemy
*   scikit-learn
*   numpy
*   pickle

You can install these packages using pip:

`pip install Flask Flask-WTF SQLAlchemy scikit-learn numpy pickle`

Usage
-----

To run the application, clone the repository and navigate to the root directory. Then run the following command:

`python app.py`

This will start the Flask server, and you can access the application by opening your web browser and going to `http://localhost:5000/`.

Features
--------

### User Authentication

Users can register for a new account by providing a username, email, and password. Once registered, users can login with their credentials to access the main application.

### Customer Creation

Users can create new customers by providing their name, age, income, and other details.

### Loan Approval Prediction

For each customer, users can make a prediction on whether the customer's loan application will be approved or denied. The prediction is based on a machine learning model trained on historical loan application data.

### Insurance Premium Prediction

For each customer, users can make a prediction on the customer's insurance premium. The prediction is based on a machine learning model trained on historical insurance premium data.

Contributing
------------

Contributions to this project are welcome! If you notice a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
