SQLAlchemy Educational Projects

A collection of educational Python projects demonstrating how to use SQLAlchemy ORM with SQLite databases. These examples cover database models, CRUD operations, queries, relationships, and cascading deletion.

📚 Projects

1. Student Database

A simple student management example using SQLAlchemy and SQLite.

Features:

- Create a SQLite database named "Student.db".
- Define a "Student" model with "id", "name", and "score" columns.
- Insert multiple student records.
- Retrieve and display all students.
- Search for a student by name.
- Update a student's score.
- Delete a student from the database.

2. University Database

An example of managing students and courses using a one-to-many relationship.

Features:

- Create a SQLite database named "University.db".
- Define "Student" and "Course" models.
- Associate courses with students using a foreign key.
- Use SQLAlchemy relationships to connect models.
- Retrieve and display course information.
- Delete a student and demonstrate cascading ORM deletion.

🛠️ Technologies

- Python
- SQLAlchemy
- SQLite

⚙️ Installation

Make sure Python is installed on your system.

Install SQLAlchemy:

pip install sqlalchemy

No separate SQLite installation is normally required because SQLite is included with standard Python distributions.

▶️ Usage

Run either Python script:

python student_database.py

Or:

python university_database.py

Replace these filenames with the actual names of your Python files.

The scripts create their respective SQLite databases and execute the example operations.

Note: Running the scripts multiple times may insert duplicate records because the examples do not clear or check existing data before inserting new records.

🧠 Concepts Demonstrated

- SQLAlchemy engine creation
- Declarative model definitions
- Database table creation
- Session creation and management
- Adding and querying records
- Filtering query results
- Updating and deleting objects
- Foreign keys
- ORM relationships
- Cascading deletion
- SQLite database integration

📌 Learning Purpose

These projects are intended for educational purposes and provide a starting point for learning how Python applications interact with relational databases through SQLAlchemy ORM.

They can be extended with input validation, reusable database functions, exception handling, and more advanced relationship management.

📄 License

This project is available for educational and personal use.
