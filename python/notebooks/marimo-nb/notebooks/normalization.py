import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Database Normalization

        Normalization is an important process in database design that helps improve the database’s efficiency, consistency, and accuracy. It makes it easier to manage and maintain the data and ensures that the database is adaptable to changing business needs.

        - Database normalization is the process of organizing the attributes of the database to reduce or eliminate data redundancy (having the same data but at different places).
        - Data redundancy unnecessarily increases the size of the database as the same data is repeated in many places. Inconsistency problems also arise during insert, delete, and update operations. 
        - In the relational model, there exist standard methods to quantify how efficient a databases is. These methods are called normal forms and there are algorithms to covert a given database into normal forms.
        - Normalization generally involves splitting a table into multiple ones which must be linked each time a query is made requiring data from the split tables.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Why do we need Normalization?

        The primary objective for normalizing the relations is to eliminate the below anomalies. Failure to reduce anomalies results in data redundancy, which may threaten data integrity and cause additional issues as the database increases. Normalization consists of a set of procedures that assist you in developing an effective database structure.

        - **Insertion Anomalies**: Insertion anomalies occur when it is not possible to insert data into a database because the required fields are missing or because the data is incomplete. For example, if a database requires that every record has a primary key, but no value is provided for a particular record, it cannot be inserted into the database.
        - **Deletion anomalies**: Deletion anomalies occur when deleting a record from a database and can result in the unintentional loss of data. For example, if a database contains information about customers and orders, deleting a customer record may also delete all the orders associated with that customer.
        - **Updation anomalies**: Updation anomalies occur when modifying data in a database and can result in inconsistencies or errors. For example, if a database contains information about employees and their salaries, updating an employee’s salary in one record but not in all related records could lead to incorrect calculations and reporting.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Prerequisites for Understanding Database Normalization

        In database normalization, we mainly put only tightly related information together. To find the closeness, we need to find which attributes are dependent on each other. To understand dependencies, we need to learn the below concepts.

        Keys are like unique identifiers in a table. For example, in a table of students, the student ID is a key because it uniquely identifies each student. Without keys, it would be hard to tell one record apart from another, especially if some information (like names) is the same. Keys ensure that data is not duplicated and that every record can be uniquely accessed.

        Functional dependency helps define the relationships between data in a table. For example, if you know a student’s ID, you can find their name, age, and class. This relationship shows how one piece of data (like the student ID) determines other pieces of data in the same table. Functional dependency helps us understand these rules and connections, which are crucial for organizing data properly.

        Once we figure out dependencies, we split tables to make sure that only closely related data is together in a table. When we split tables, we need to ensure that we do not loose information. For this, we need to learn the below concepts.

        Dependency Preserving 

        Lossless Decomposition in DBMS
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Features of Database Normalization""")
    return


@app.cell
def _(mo):
    mo.accordion(
        {
            "Elimination of Data Redundancy": mo.md(
                r"""
    One of the main features of normalization is to eliminate the data redundancy that can occur in a database. Data redundancy refers to the repetition of data in different parts of the database. Normalization helps in reducing or eliminating this redundancy, which can improve the efficiency and consistency of the database.            
                """
            ),
            "Ensuring Data Consistency": mo.md(
                r"""
    Normalization helps in ensuring that the data in the database is consistent and accurate. By eliminating redundancy, normalization helps in preventing inconsistencies and contradictions that can arise due to different versions of the same data.            
                """
            ),
            "Simplification of Data Management": mo.md(
                r"""
    Normalization simplifies the process of managing data in a database. By breaking down a complex data structure into simpler tables, normalization makes it easier to manage the data, update it, and retrieve it.            
                """
            ),
            "Improved Database Design": mo.md(
                r"""
    Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.            
                """
            ),
            "Avoiding Update Anomalies": mo.md(
                r"""
    Normalization helps in avoiding update anomalies, which can occur when updating a single record in a table affects multiple records in other tables. Normalization ensures that each table contains only one type of data and that the relationships between the tables are clearly defined, which helps in avoiding such anomalies.
                """
            ),
            "Standardization": mo.md(
                r"""
    Normalization helps in standardizing the data in the database. By organizing the data into tables and defining relationships between them, normalization helps in ensuring that the data is stored in a consistent and uniform manner.            
                """
            )
        }
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Normal Forms in DBMS

        ## First Normal Form (1NF)

        A relation is in first normal form if every attribute in that relation is a single-valued attribute.

        This form ensures that the table follows basic structural rules to eliminate redundancy and improve data integrity. Each column should contain atomic (indivisible) values. This means no multiple values or lists in a single column.

        ## Second Normal Form (2NF)

        A relation that is in first normal form and every non-primary-key attribute is fully functionally dependent on the primary key, then the relation is in second normal form.


        ## Third Normal Form (3NF)

        A relation is in third normal form, if there is no transitive dependency for non-prime attributes as well as it is in the second normal form. A relation is in 3NF if at least one of the following conditions holds in every non-trivial function dependency X -> Y.

        - X is a super key
        - Y is a prime attribute (each element of Y is part of some candidate key).

        ## Boyce-Codd Normal Form (BCNF)

        For BCNF the relation should satisfy the below conditions

        - The relation should be in 3rd Normal Form.
        - X should be a super-key for every functional dependency (FD) X -> Y in a given relation.

        ## Fourth Normal Form (4NF)

        A relation R is in 4NF if and only if the following conditions are satisfied:

        - It should be in the Boyce-Codd Normal Form (BCNF)
        - The table should not have Multi-valued Dependency.

        ## Fith Normal Form (5NF)

        A relation R is in 5NF if and only if it satisifes the following conditions:

        - R should be already in 4NF.
        - It cannot be further non-loss decomposed (join dependency).
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Advantages of Normalization

        - Normalization eliminates data redundancy and ensures that each piece of data is stored in only one place, reducing the risk of data inconsistency and making it easier to maintain data accuracy.
        - By breaking down data into smaller, more specific tables, normalization helps ensure that each table stores only relevant data, which improves the overall data integrity of the database.
        - Normalization simplifies the process of updating data, as it only needs to be changed in one place rather than in multiple places throughout the database.
        - Normalization enables users to query the database using a variety of different criteria, as the data is organized into smaller, more specific tables that can be joined together as needed.
        - Normalization can help ensure that data is consistent across different applications that use the same database, making it easier to integrate different applications and ensuring that all users have access to accurate and consistent data.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Disadvantages of Normalization

        - Normalization can result in increased performance overhead due to the need for additional join operations and the potential for slower query execution times.
        - Normalization can result in the loss of data context, as data may be split across multiple tables and require additional joins to retrieve.
        - Proper implementation of normalization requires expert knowledge of database design and the normalization process. 
        - Normalization can increase the complexity of a database design, especially if the data model is not well understood or if the normalization process is not carried out correctly.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example of a Table Violating 1NF

        ## Table: Student_Course (Violating 1NF)
        | StudentID | Name  | Courses          |
        |-----------|-------|------------------|
        | 1         | Alice | Math, Science    |
        | 2         | Bob   | English, History |
        | 3         | Charlie | Math           |

        ### **Problems with 1NF Violation:**
        1. **Non-Atomic Values**:  
           - The `Courses` column contains **multiple values in a single cell** (e.g., "Math, Science").
           - 1NF requires each column to have **atomic (indivisible) values**.

        2. **Repeating Groups**:  
           - If a student takes multiple courses, their data is stored in **one row** instead of multiple rows.
           - This makes querying difficult and leads to **data anomalies**.

        ---

        ## **Converting to 1NF (Ensuring Atomicity)**

        To comply with **1NF**, we must **eliminate multiple values per column** by restructuring the table.

        ### **Fixed Table: Student_Course (Now in 1NF)**
        | StudentID | Name    | Course   |
        |-----------|--------|---------|
        | 1         | Alice  | Math    |
        | 1         | Alice  | Science |
        | 2         | Bob    | English |
        | 2         | Bob    | History |
        | 3         | Charlie | Math   |

        ### **Why is this Better?**
        ✅ **Ensures atomic values** (each column contains a single value).  
        ✅ **Eliminates repeating groups** (each row represents a unique fact).  
        ✅ **Easier to query** (e.g., finding all students taking "Math").  


        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example of a Table Violating 2NF

        ## Table: Student_Course (Violating 2NF)
        | StudentID | CourseID | StudentName | CourseName |
        |-----------|---------|-------------|------------|
        | 1         | 101     | Alice       | Math       |
        | 2         | 102     | Bob         | Science    |
        | 1         | 102     | Alice       | Science    |
        | 3         | 103     | Charlie     | History    |

        ### **Problems:**
        - **Primary Key**: `(StudentID, CourseID)` (Composite Key)
        - **Partial Dependency Issues:**
          - `StudentName` depends only on `StudentID`
          - `CourseName` depends only on `CourseID`
          - These violate **2NF** because non-key attributes should depend on the entire primary key.

        ---

        ## **Converting to 2NF (Breaking Partial Dependencies)**

        ### **Table: Students**
        | StudentID | StudentName |
        |-----------|-------------|
        | 1         | Alice       |
        | 2         | Bob         |
        | 3         | Charlie     |

        - **Primary Key**: `StudentID`
        - Now, `StudentName` depends **only on `StudentID`**, making it **2NF-compliant**.

        ---

        ### **Table: Courses**
        | CourseID | CourseName |
        |----------|------------|
        | 101      | Math       |
        | 102      | Science    |
        | 103      | History    |

        - **Primary Key**: `CourseID`
        - Now, `CourseName` depends **only on `CourseID`**, making it **2NF-compliant**.

        ---

        ### **Table: Student_Course (Now in 2NF)**
        | StudentID | CourseID |
        |-----------|---------|
        | 1         | 101     |
        | 2         | 102     |
        | 1         | 102     |
        | 3         | 103     |

        - **Composite Primary Key**: `(StudentID, CourseID)`
        - No non-key attributes exist in this table, ensuring **2NF compliance**.

        ---

        ## **Why is this Better?**
        ✅ **Reduces redundancy** (no repeated student names or course names)  
        ✅ **Prevents update anomalies** (changing a course name in one place updates it everywhere)  
        ✅ **Improves database efficiency and integrity**  


        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example of a Table Violating 3NF

        ## Table: Student_Info (Violating 3NF)
        | StudentID | Name   | Course   | InstructorID | InstructorName |
        |-----------|--------|---------|--------------|---------------|
        | 1         | Alice  | Math    | 101          | Dr. Smith     |
        | 2         | Bob    | Science | 102          | Dr. Johnson   |
        | 3         | Charlie | History | 103         | Dr. Williams  |
        | 4         | Alice  | Science | 102          | Dr. Johnson   |

        ### **Problems with 3NF Violation:**
        1. **Transitive Dependency**:
           - `InstructorName` depends on `InstructorID`, which is **not** a primary key in this table.
           - **3NF Rule**: Every non-key attribute should depend **only** on the primary key (`StudentID`), but here, `InstructorName` depends on `InstructorID`, not `StudentID`.

        2. **Data Redundancy**:
           - If an instructor's name changes, multiple rows must be updated.

        ---

        ## **Converting to 3NF (Eliminating Transitive Dependency)**

        To comply with **3NF**, we must **remove transitive dependencies** by splitting the table.

        ### **Fixed Table: Student_Course (Now in 3NF)**
        | StudentID | Name   | Course   | InstructorID |
        |-----------|--------|---------|--------------|
        | 1         | Alice  | Math    | 101          |
        | 2         | Bob    | Science | 102          |
        | 3         | Charlie | History | 103         |
        | 4         | Alice  | Science | 102          |

        - **Primary Key**: `StudentID`
        - Now, `InstructorName` is removed from this table.

        ---

        ### **New Table: Instructors (Now in 3NF)**
        | InstructorID | InstructorName |
        |--------------|---------------|
        | 101          | Dr. Smith     |
        | 102          | Dr. Johnson   |
        | 103          | Dr. Williams  |

        - **Primary Key**: `InstructorID`
        - `InstructorName` now depends **only on `InstructorID`**, ensuring **3NF compliance**.

        ---

        ### **Why is this Better?**
        ✅ **Eliminates transitive dependencies** (all attributes depend only on their table’s primary key).  
        ✅ **Reduces redundancy** (each instructor’s name is stored only once).  
        ✅ **Improves data integrity** (updating an instructor’s name only requires changing it in one place).  


        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example of a Table Violating BCNF

        ## Table: Course_Instructor (Violating BCNF)
        | CourseID | InstructorID | CourseName | InstructorName |
        |----------|-------------|------------|---------------|
        | 101      | 1           | Math       | Dr. Smith     |
        | 102      | 2           | Science    | Dr. Johnson   |
        | 103      | 3           | History    | Dr. Williams  |
        | 101      | 4           | Math       | Dr. Brown     |

        ### **Problems with BCNF Violation:**
        1. **Functional Dependency Issue**:
           - **Primary Key**: `(CourseID, InstructorID)` (Composite Key)
           - **InstructorName** depends only on `InstructorID`, not on the full composite key.
           - **CourseName** depends only on `CourseID`, not on the full composite key.
           - This creates a **BCNF violation** because there are **determinants** (`CourseID` and `InstructorID`) that are **not candidate keys**.

        2. **Anomalies**:
           - If the name of a course or instructor changes, multiple rows need to be updated.

        ---

        ## **Converting to BCNF (Eliminating Partial Dependencies)**

        To comply with **BCNF**, we must **split the table** to ensure that all determinants are candidate keys.

        ### **Fixed Table: Courses (Now in BCNF)**
        | CourseID | CourseName |
        |----------|------------|
        | 101      | Math       |
        | 102      | Science    |
        | 103      | History    |

        - **Primary Key**: `CourseID`
        - `CourseName` depends only on `CourseID`, ensuring BCNF compliance.

        ---

        ### **Fixed Table: Instructors (Now in BCNF)**
        | InstructorID | InstructorName |
        |-------------|---------------|
        | 1           | Dr. Smith     |
        | 2           | Dr. Johnson   |
        | 3           | Dr. Williams  |
        | 4           | Dr. Brown     |

        - **Primary Key**: `InstructorID`
        - `InstructorName` depends only on `InstructorID`, ensuring BCNF compliance.

        ---

        ### **Fixed Table: Course_Instructor (Now in BCNF)**
        | CourseID | InstructorID |
        |----------|-------------|
        | 101      | 1           |
        | 101      | 4           |
        | 102      | 2           |
        | 103      | 3           |

        - **Composite Primary Key**: `(CourseID, InstructorID)`
        - No functional dependencies exist outside the candidate keys.

        ---

        ### **Why is this Better?**
        ✅ **Eliminates non-trivial functional dependencies on non-candidate keys**  
        ✅ **Reduces redundancy** (course and instructor names are stored only once)  
        ✅ **Prevents anomalies** (updates are simpler and more consistent)  


        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example of a Table Violating 4NF

        ## Table: Student_Enrollment (Violating 4NF)
        | StudentID | Course      | Activity       |
        |-----------|------------|----------------|
        | 1         | Math       | Soccer         |
        | 1         | Math       | Chess          |
        | 1         | Science    | Soccer         |
        | 1         | Science    | Chess          |
        | 2         | History    | Debate         |
        | 2         | History    | Basketball     |

        ### **Problems with 4NF Violation:**
        1. **Multi-Valued Dependencies (MVDs)**:
           - A student can be enrolled in **multiple courses**.
           - A student can also participate in **multiple extracurricular activities**.
           - These two sets of data are **independent** of each other, yet they are stored in the same table.
           - This creates **redundancy** because every combination of a course and activity for a student is unnecessarily repeated.

        2. **Anomalies**:
           - If a student enrolls in a new course, we must duplicate all their extracurricular activities in new rows.
           - If a student joins a new activity, we must duplicate all their enrolled courses.

        ---

        ## **Converting to 4NF (Eliminating Multi-Valued Dependencies)**

        To comply with **4NF**, we must **split the table** into two separate tables, ensuring that each table deals with a **single independent relationship**.

        ### **Fixed Table: Student_Course (Now in 4NF)**
        | StudentID | Course   |
        |-----------|---------|
        | 1         | Math    |
        | 1         | Science |
        | 2         | History |

        - **Primary Key**: `(StudentID, Course)`
        - Now, each student’s enrollment in courses is stored independently of activities.

        ---

        ### **Fixed Table: Student_Activity (Now in 4NF)**
        | StudentID | Activity    |
        |-----------|------------|
        | 1         | Soccer     |
        | 1         | Chess      |
        | 2         | Debate     |
        | 2         | Basketball |

        - **Primary Key**: `(StudentID, Activity)`
        - Now, each student’s participation in activities is stored independently of course enrollment.

        ---

        ### **Why is this Better?**
        ✅ **Removes Multi-Valued Dependencies (MVDs)**  
        ✅ **Eliminates redundancy** (each student’s courses and activities are stored separately)  
        ✅ **Prevents anomalies** (adding a new course or activity no longer requires redundant records)  

        ---

        Would you like an **SQL example** demonstrating this transformation? 🚀
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example of a Table Violating 5NF

        ## Table: Project_Allocation (Violating 5NF)
        | EmployeeID | ProjectID | Role       |
        |------------|-----------|------------|
        | 1          | A         | Developer  |
        | 1          | A         | Tester     |
        | 1          | B         | Developer  |
        | 2          | A         | Developer  |
        | 2          | B         | Tester     |
        | 3          | B         | Tester     |

        ### **Problems with 5NF Violation:**
        1. **Join Dependency Issue**:
           - Employees are assigned to **projects**.
           - Employees are assigned **roles**.
           - Employees have a **role in a project**, but this relationship is not independent.
           - The table is prone to **redundancy and inconsistencies**.

        2. **Anomalies**:
           - If a new project is added, all employee-role combinations must be re-entered.
           - If an employee’s role changes, multiple rows must be updated.

        ---

        ## **Converting to 5NF (Eliminating Join Dependency Issues)**

        To comply with **5NF**, we must **decompose the table** into smaller relations that can be **joined back without redundancy**.

        ### **Fixed Table: Employee_Project (Now in 5NF)**
        | EmployeeID | ProjectID |
        |------------|-----------|
        | 1          | A         |
        | 1          | B         |
        | 2          | A         |
        | 2          | B         |
        | 3          | B         |

        - **Primary Key**: `(EmployeeID, ProjectID)`
        - This table ensures that employees are assigned to projects **without role dependencies**.

        ---

        ### **Fixed Table: Employee_Role (Now in 5NF)**
        | EmployeeID | Role       |
        |------------|-----------|
        | 1          | Developer |
        | 1          | Tester    |
        | 2          | Developer |
        | 2          | Tester    |
        | 3          | Tester    |

        - **Primary Key**: `(EmployeeID, Role)`
        - This table ensures that employee roles are stored **independently of projects**.

        ---

        ### **Fixed Table: Project_Role (Now in 5NF)**
        | ProjectID | Role       |
        |-----------|-----------|
        | A         | Developer |
        | A         | Tester    |
        | B         | Developer |
        | B         | Tester    |

        - **Primary Key**: `(ProjectID, Role)`
        - This table ensures that projects define the roles they need **independently of employees**.

        ---

        ### **Why is this Better?**
        ✅ **Eliminates join dependencies** (no redundant relationships).  
        ✅ **Prevents anomalies** (changing roles, employees, or projects no longer requires unnecessary duplication).  
        ✅ **Maintains data integrity** (independent relationships are correctly stored).  


        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Conclusion

        Database normalization is a key concept in organizing data efficiently within a database. By reducing redundancy, ensuring data consistency, and breaking data into well-structured tables, normalization enhances the accuracy, scalability, and maintainability of a database. It simplifies data updates, improves integrity, and supports flexible querying, making it an essential practice for designing reliable and efficient database systems.
        """
    )
    return


if __name__ == "__main__":
    app.run()
