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
        # Test Database Schema Definition

        ```sql
        -- Table to store test suites
        CREATE TABLE test_suites (
            suite_id INT PRIMARY KEY AUTO_INCREMENT,
            suite_name VARCHAR(255) NOT NULL,
            errors INT NOT NULL CHECK (errors >= 0),
            failures INT NOT NULL CHECK (failures >= 0),
            skipped INT NOT NULL CHECK (skipped >= 0),
            total_tests INT NOT NULL CHECK (total_tests >= 0),
            execution_time DECIMAL(10,3) NOT NULL CHECK (execution_time >= 0),
            timestamp TIMESTAMP NOT NULL,
            hostname VARCHAR(255) NOT NULL
        );

        -- Table to store test classes (avoiding redundancy in class names)
        CREATE TABLE test_classes (
            class_id INT PRIMARY KEY AUTO_INCREMENT,
            class_name VARCHAR(255) UNIQUE NOT NULL
        );

        -- Table to store test cases independently (removes dependency on test suites)
        CREATE TABLE test_cases (
            test_id INT PRIMARY KEY AUTO_INCREMENT,
            test_name VARCHAR(255) NOT NULL
        );

        -- Associative table to handle multi-valued dependencies
        CREATE TABLE test_case_execution (
            execution_id INT PRIMARY KEY AUTO_INCREMENT,
            suite_id INT NOT NULL,
            class_id INT NOT NULL,
            test_id INT NOT NULL,
            execution_time DECIMAL(10,3) NOT NULL CHECK (execution_time >= 0),

            -- Foreign Keys for Referential Integrity
            CONSTRAINT fk_execution_suite FOREIGN KEY (suite_id) REFERENCES test_suites(suite_id) 
                ON DELETE CASCADE,
            CONSTRAINT fk_execution_class FOREIGN KEY (class_id) REFERENCES test_classes(class_id) 
                ON DELETE CASCADE,
            CONSTRAINT fk_execution_test FOREIGN KEY (test_id) REFERENCES test_cases(test_id) 
                ON DELETE CASCADE
        );

        -- Indexes for Performance Optimization
        CREATE INDEX idx_test_suite ON test_case_execution(suite_id);
        CREATE INDEX idx_test_class ON test_case_execution(class_id);
        CREATE INDEX idx_test_case ON test_case_execution(test_id);
        CREATE INDEX idx_execution_time ON test_case_execution(execution_time);
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Create a .env file

        ```plaintext
        # .env file
        POSTGRES_USER=your_username
        POSTGRES_PASSWORD=your_password
        POSTGRES_DB=test_results
        POSTGRES_HOST=localhost
        POSTGRES_PORT=5432
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Modify your SQLModel databasew setup to use python-dotenv

        ```python
        import os
        from dotenv import load_dotenv
        from sqlmodel import SQLModel, Field, Relationship, create_engine, Session
        from typing import Optional, List
        from datetime import datetime

        # Load environment variables from .env
        load_dotenv()

        # Read PostgreSQL connection details from environment variables
        POSTGRES_USER = os.getenv("POSTGRES_USER")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        POSTGRES_DB = os.getenv("POSTGRES_DB")
        POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

        # Construct PostgreSQL Database URL
        DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

        # Create the database engine
        engine = create_engine(DATABASE_URL)

        # -------------------- Test Suites Table --------------------
        class TestSuite(SQLModel, table=True):
            suite_id: Optional[int] = Field(default=None, primary_key=True)
            suite_name: str = Field(index=True)
            errors: int = Field(default=0)
            failures: int = Field(default=0)
            skipped: int = Field(default=0)
            total_tests: int
            execution_time: float
            timestamp: datetime
            hostname: str

            test_cases: List["TestCaseExecution"] = Relationship(back_populates="test_suite")

        # -------------------- Test Classes Table --------------------
        class TestClass(SQLModel, table=True):
            class_id: Optional[int] = Field(default=None, primary_key=True)
            class_name: str = Field(unique=True, index=True)

            test_cases: List["TestCaseExecution"] = Relationship(back_populates="test_class")

        # -------------------- Test Cases Table --------------------
        class TestCase(SQLModel, table=True):
            test_id: Optional[int] = Field(default=None, primary_key=True)
            test_name: str = Field(index=True)

            executions: List["TestCaseExecution"] = Relationship(back_populates="test_case")

        # -------------------- Test Case Execution (Join Table) --------------------
        class TestCaseExecution(SQLModel, table=True):
            execution_id: Optional[int] = Field(default=None, primary_key=True)

            suite_id: int = Field(foreign_key="testsuite.suite_id")
            class_id: int = Field(foreign_key="testclass.class_id")
            test_id: int = Field(foreign_key="testcase.test_id")

            execution_time: float

            test_suite: TestSuite = Relationship(back_populates="test_cases")
            test_class: TestClass = Relationship(back_populates="test_cases")
            test_case: TestCase = Relationship(back_populates="executions")

        # -------------------- Database Setup --------------------
        def create_db_and_tables():
            SQLModel.metadata.create_all(engine)
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Example DAO (Data Access Object) Implementation

        ```python
        class TestResultsDAO:
            def __init__(self, session: Session):
                self.session = session

            def add_test_suite(self, suite: TestSuite):
                self.session.add(suite)
                self.session.commit()
                self.session.refresh(suite)
                return suite

            def get_test_suite(self, suite_id: int):
                return self.session.get(TestSuite, suite_id)

            def add_test_class(self, test_class: TestClass):
                self.session.add(test_class)
                self.session.commit()
                self.session.refresh(test_class)
                return test_class

            def add_test_case(self, test_case: TestCase):
                self.session.add(test_case)
                self.session.commit()
                self.session.refresh(test_case)
                return test_case

            def add_test_case_execution(self, execution: TestCaseExecution):
                self.session.add(execution)
                self.session.commit()
                self.session.refresh(execution)
                return execution
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Insert Sample Data

        ```python
        def insert_sample_data():
            with Session(engine) as session:
                dao = TestResultsDAO(session)

                suite = dao.add_test_suite(
                    TestSuite(
                        suite_name="pytest",
                        errors=0,
                        failures=0,
                        skipped=0,
                        total_tests=8,
                        execution_time=0.116,
                        timestamp=datetime.utcnow(),
                        hostname="Omars-Mac-Studio.local"
                    )
                )

                test_class = dao.add_test_class(TestClass(class_name="tests.test_deploy"))
                test_case = dao.add_test_case(TestCase(test_name="test_example"))

                execution = dao.add_test_case_execution(
                    TestCaseExecution(
                        suite_id=suite.suite_id,
                        class_id=test_class.class_id,
                        test_id=test_case.test_id,
                        execution_time=0.001
                    )
                )

        if __name__ == "__main__":
            create_db_and_tables()
            insert_sample_data()
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Querying Data

        ```python
        def get_test_cases_by_suite(suite_id: int):
            with Session(engine) as session:
                test_cases = session.query(TestCase).join(TestCaseExecution).filter(
                    TestCaseExecution.suite_id == suite_id
                ).all()
                return test_cases

        test_cases = get_test_cases_by_suite(1)
        for test in test_cases:
            print(test.test_name)
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # FastAPI Integration

        ```python
        import os
        from datetime import datetime
        from dotenv import load_dotenv
        from fastapi import FastAPI, Depends, HTTPException
        from sqlmodel import SQLModel, Field, Session, Relationship, create_engine, select
        from typing import List, Optional

        # Load environment variables from .env
        load_dotenv()

        # PostgreSQL Database Configuration
        POSTGRES_USER = os.getenv("POSTGRES_USER")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        POSTGRES_DB = os.getenv("POSTGRES_DB")
        POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

        # Construct the PostgreSQL connection URL
        DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

        # Create database engine
        engine = create_engine(DATABASE_URL)

        # -------------------- Test Suites Table --------------------
        class TestSuite(SQLModel, table=True):
            suite_id: Optional[int] = Field(default=None, primary_key=True)
            suite_name: str = Field(index=True)
            errors: int = Field(default=0)
            failures: int = Field(default=0)
            skipped: int = Field(default=0)
            total_tests: int
            execution_time: float
            timestamp: datetime
            hostname: str

            test_cases: List["TestCaseExecution"] = Relationship(back_populates="test_suite")

        # -------------------- Test Classes Table --------------------
        class TestClass(SQLModel, table=True):
            class_id: Optional[int] = Field(default=None, primary_key=True)
            class_name: str = Field(unique=True, index=True)

            test_cases: List["TestCaseExecution"] = Relationship(back_populates="test_class")

        # -------------------- Test Cases Table --------------------
        class TestCase(SQLModel, table=True):
            test_id: Optional[int] = Field(default=None, primary_key=True)
            test_name: str = Field(index=True)

            executions: List["TestCaseExecution"] = Relationship(back_populates="test_case")

        # -------------------- Test Case Execution (Join Table) --------------------
        class TestCaseExecution(SQLModel, table=True):
            execution_id: Optional[int] = Field(default=None, primary_key=True)

            suite_id: int = Field(foreign_key="testsuite.suite_id")
            class_id: int = Field(foreign_key="testclass.class_id")
            test_id: int = Field(foreign_key="testcase.test_id")

            execution_time: float

            test_suite: TestSuite = Relationship(back_populates="test_cases")
            test_class: TestClass = Relationship(back_populates="test_cases")
            test_case: TestCase = Relationship(back_populates="executions")

        # -------------------- Database Setup --------------------
        def create_db_and_tables():
            SQLModel.metadata.create_all(engine)

        def get_session():
            with Session(engine) as session:
                yield session

        # -------------------- FastAPI Initialization --------------------
        app = FastAPI(title="Test Results API")

        # -------------------- API Endpoints --------------------

        # ✅ **1. Create a Test Suite**
        @app.post("/test-suites/", response_model=TestSuite)
        def create_test_suite(suite: TestSuite, session: Session = Depends(get_session)):
            session.add(suite)
            session.commit()
            session.refresh(suite)
            return suite

        # ✅ **2. Get All Test Suites**
        @app.get("/test-suites/", response_model=List[TestSuite])
        def get_test_suites(session: Session = Depends(get_session)):
            return session.exec(select(TestSuite)).all()

        # ✅ **3. Create a Test Class**
        @app.post("/test-classes/", response_model=TestClass)
        def create_test_class(test_class: TestClass, session: Session = Depends(get_session)):
            session.add(test_class)
            session.commit()
            session.refresh(test_class)
            return test_class

        # ✅ **4. Get All Test Classes**
        @app.get("/test-classes/", response_model=List[TestClass])
        def get_test_classes(session: Session = Depends(get_session)):
            return session.exec(select(TestClass)).all()

        # ✅ **5. Create a Test Case**
        @app.post("/test-cases/", response_model=TestCase)
        def create_test_case(test_case: TestCase, session: Session = Depends(get_session)):
            session.add(test_case)
            session.commit()
            session.refresh(test_case)
            return test_case

        # ✅ **6. Get All Test Cases**
        @app.get("/test-cases/", response_model=List[TestCase])
        def get_test_cases(session: Session = Depends(get_session)):
            return session.exec(select(TestCase)).all()

        # ✅ **7. Associate Test Case with Suite and Class**
        @app.post("/test-executions/", response_model=TestCaseExecution)
        def create_test_case_execution(execution: TestCaseExecution, session: Session = Depends(get_session)):
            session.add(execution)
            session.commit()
            session.refresh(execution)
            return execution

        # ✅ **8. Get Test Cases by Suite ID**
        @app.get("/test-suites/{suite_id}/test-cases/", response_model=List[TestCase])
        def get_test_cases_by_suite(suite_id: int, session: Session = Depends(get_session)):
            query = (
                select(TestCase)
                .join(TestCaseExecution)
                .where(TestCaseExecution.suite_id == suite_id)
            )
            return session.exec(query).all()

        # ✅ **9. Get Test Suites by Hostname**
        @app.get("/test-suites/hostname/{hostname}", response_model=List[TestSuite])
        def get_test_suites_by_hostname(hostname: str, session: Session = Depends(get_session)):
            return session.exec(select(TestSuite).where(TestSuite.hostname == hostname)).all()
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Directory Structure

        ```plaintext
        test_results_api/
        │── .env                 # Environment variables for PostgreSQL
        │── .gitignore           # Git ignore file
        │── requirements.txt     # Python dependencies
        │── README.md            # Documentation
        │── main.py              # Entry point for FastAPI application
        │
        ├── app/                 # Application source code
        │   ├── __init__.py      # Makes 'app' a Python package
        │   │
        │   ├── core/            # Core configurations and settings
        │   │   ├── __init__.py
        │   │   ├── config.py    # Load environment variables
        │   │   ├── database.py  # SQLModel DB engine and session
        │   │
        │   ├── models/          # Database models using SQLModel
        │   │   ├── __init__.py
        │   │   ├── test_suite.py      # TestSuite model
        │   │   ├── test_class.py      # TestClass model
        │   │   ├── test_case.py       # TestCase model
        │   │   ├── test_execution.py  # TestCaseExecution (Join Table)
        │   │
        │   ├── repositories/    # Data Access Layer (DAO)
        │   │   ├── __init__.py
        │   │   ├── test_suite_repo.py      # CRUD operations for TestSuite
        │   │   ├── test_class_repo.py      # CRUD operations for TestClass
        │   │   ├── test_case_repo.py       # CRUD operations for TestCase
        │   │   ├── test_execution_repo.py  # CRUD operations for Test Execution
        │   │
        │   ├── schemas/         # Pydantic models for request validation
        │   │   ├── __init__.py
        │   │   ├── test_suite.py      # TestSuite request/response schema
        │   │   ├── test_class.py      # TestClass request/response schema
        │   │   ├── test_case.py       # TestCase request/response schema
        │   │   ├── test_execution.py  # TestCaseExecution schema
        │   │
        │   ├── services/        # Business logic layer
        │   │   ├── __init__.py
        │   │   ├── test_suite_service.py      # Logic for TestSuite operations
        │   │   ├── test_class_service.py      # Logic for TestClass operations
        │   │   ├── test_case_service.py       # Logic for TestCase operations
        │   │   ├── test_execution_service.py  # Logic for Test Execution operations
        │   │
        │   ├── api/             # API routes (FastAPI routers)
        │   │   ├── __init__.py
        │   │   ├── test_suites.py      # Routes for TestSuite endpoints
        │   │   ├── test_classes.py      # Routes for TestClass endpoints
        │   │   ├── test_cases.py       # Routes for TestCase endpoints
        │   │   ├── test_executions.py  # Routes for Test Execution endpoints
        │   │
        │   ├── utils/           # Utility functions (helpers)
        │   │   ├── __init__.py
        │   │   ├── logger.py    # Logging configuration
        │   │   ├── time_utils.py  # Time-related helper functions
        │   │
        │   ├── tests/           # Unit & integration tests
        │   │   ├── __init__.py
        │   │   ├── test_api.py  # API tests using pytest
        │   │   ├── test_db.py   # Database-related tests
        │   │   ├── test_services.py  # Business logic tests
        │   │
        └── docker/              # Docker-related files
            ├── Dockerfile       # Docker build file
            ├── docker-compose.yml  # Docker Compose for local dev
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Usage

        ## Running the FastAPI Server

        ```shell
        uvicorn main:app --reload
        ```

        ## Local URL's

        - [Swagger](http://127.0.0.1:8000/docs)
        - [Redoc](http://127.0.0.1:8000/redoc)

        ## Example API Call's Using cURL

        ### Create a Test Suite

        ```shell
        curl -X 'POST' 'http://127.0.0.1:8000/test-suites/' \
             -H 'Content-Type: application/json' \
             -d '{
                   "suite_name": "pytest",
                   "errors": 0,
                   "failures": 0,
                   "skipped": 0,
                   "total_tests": 8,
                   "execution_time": 0.116,
                   "timestamp": "2025-03-08T03:15:45.644023-05:00",
                   "hostname": "Omars-Mac-Studio.local"
                 }'
        ```

        ### Get All Test Suites

        ```shell
        curl -X 'GET' 'http://127.0.0.1:8000/test-suites/'
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Adding JWT Authentication to FastAPI with PostgreSQL

        ## Install requried dependencies

        ```shell
        pip install passlib[bcrypt] pyjwt python-multipart
        ```

        - passlib[bcrypt] for securely hashing passwords
        - pyjwt for JWT token generation & validation
        - python-multipart required for OAuth2 password flow

        ## Update Directory structure

        ```plaintext
        test_results_api/
        │── app/
        │   ├── auth/                 # Authentication & security logic
        │   │   ├── __init__.py
        │   │   ├── auth_handler.py    # JWT token generation & validation
        │   │   ├── auth_service.py    # User authentication service
        │   │   ├── auth_routes.py     # API routes for login & registration
        │   │
        │   ├── models/
        │   │   ├── user.py            # User model (database schema)
        │   │
        │   ├── schemas/
        │   │   ├── user.py            # Pydantic schemas for User API
        │   │
        │   ├── repositories/
        │   │   ├── user_repo.py       # CRUD operations for User
        │   │
        │   ├── api/
        │   │   ├── users.py           # API routes for user management
        │   │
        │   ├── core/
        │   │   ├── security.py        # Password hashing & verification
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Folder Breakdown

        ---


        ### 🔹 **`app/core/` (Configuration & Security)**
        | File | Description |
        |------|------------|
        | `config.py` | Loads **environment variables** using `dotenv` |
        | `database.py` | Sets up **PostgreSQL connection** using `SQLModel` |
        | `security.py` | Handles **password hashing & verification** |

        ---

        ### 🔹 **`app/auth/` (Authentication & JWT)**
        | File | Description |
        |------|------------|
        | `auth_handler.py` | Handles **JWT token generation & validation** |
        | `auth_service.py` | Manages **user authentication & login logic** |
        | `auth_routes.py` | API routes for **user login & registration** |

        ---

        ### 🔹 **`app/models/` (Database Models)**
        | File | Description |
        |------|------------|
        | `test_suite.py` | Defines the `TestSuite` model (test metadata) |
        | `test_class.py` | Defines the `TestClass` model (test categories) |
        | `test_case.py` | Defines the `TestCase` model (individual test cases) |
        | `test_execution.py` | Defines the `TestCaseExecution` model (join table) |
        | `user.py` | Defines the `User` model (authentication) |

        ---

        ### 🔹 **`app/repositories/` (Data Access Layer - DAO)**
        | File | Description |
        |------|------------|
        | `test_suite_repo.py` | CRUD operations for `TestSuite` |
        | `test_class_repo.py` | CRUD operations for `TestClass` |
        | `test_case_repo.py` | CRUD operations for `TestCase` |
        | `test_execution_repo.py` | CRUD operations for `TestCaseExecution` |
        | `user_repo.py` | CRUD operations for `User` authentication |

        ---

        ### 🔹 **`app/schemas/` (Pydantic Models for Request Validation)**
        | File | Description |
        |------|------------|
        | `test_suite.py` | Pydantic model for `TestSuite` request/response |
        | `test_class.py` | Pydantic model for `TestClass` request/response |
        | `test_case.py` | Pydantic model for `TestCase` request/response |
        | `test_execution.py` | Pydantic model for `TestCaseExecution` request/response |
        | `user.py` | Pydantic model for **User authentication** |

        ---

        ### 🔹 **`app/api/` (API Routes - FastAPI)**
        | File | Description |
        |------|------------|
        | `test_suites.py` | **API routes** for managing test suites |
        | `test_classes.py` | **API routes** for managing test classes |
        | `test_cases.py` | **API routes** for managing test cases |
        | `test_executions.py` | **API routes** for executing test cases |
        | `users.py` | **Protected API routes** for users |

        ---

        ## **📌 Summary**
        ✅ **Follows MVC architecture**  
        ✅ **Modular & scalable**  
        ✅ **Secure authentication with JWT**  
        ✅ **Docker support** for deployment  

        Would you like to **add Role-Based Access Control (RBAC)** next? 🚀
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # User Model (models/user.py)

        ```python
        from sqlmodel import SQLModel, Field
        from typing import Optional

        class User(SQLModel, table=True):
            id: Optional[int] = Field(default=None, primary_key=True)
            username: str = Field(unique=True, index=True)
            email: str = Field(unique=True, index=True)
            password_hash: str  # Hashed password
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Password Hashing (core/security.py)

        ```python
        from passlib.context import CryptContext

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        # Hash a password
        def hash_password(password: str) -> str:
            return pwd_context.hash(password)

        # Verify a password
        def verify_password(plain_password: str, hashed_password: str) -> bool:
            return pwd_context.verify(plain_password, hashed_password)
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # JWT Token Handler (auth/auth_handler.py)

        ```python
        import os
        import jwt
        from datetime import datetime, timedelta
        from fastapi import HTTPException, Security
        from fastapi.security import OAuth2PasswordBearer
        from dotenv import load_dotenv

        load_dotenv()

        # Secret key & settings
        SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 30

        # OAuth2 scheme
        oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

        # Generate JWT token
        def create_access_token(data: dict, expires_delta: timedelta = None):
            to_encode = data.copy()
            expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
            to_encode.update({"exp": expire})
            return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        # Decode & validate JWT token
        def decode_access_token(token: str):
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                return payload
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Token expired")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="Invalid token")

        # Get current user from token
        def get_current_user(token: str = Security(oauth2_scheme)):
            payload = decode_access_token(token)
            return payload.get("sub")
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # User Repository (repositories/user_repo.py)

        ```python
        from sqlmodel import Session, select
        from app.models.user import User

        class UserRepository:
            def __init__(self, session: Session):
                self.session = session

            def create_user(self, user: User):
                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return user

            def get_user_by_username(self, username: str):
                return self.session.exec(select(User).where(User.username == username)).first()

            def get_user_by_email(self, email: str):
                return self.session.exec(select(User).where(User.email == email)).first()
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Authentication Service

        ```python
        from sqlmodel import Session
        from app.repositories.user_repo import UserRepository
        from app.core.security import hash_password, verify_password
        from app.auth.auth_handler import create_access_token
        from app.models.user import User
        from datetime import timedelta

        class AuthService:
            def __init__(self, session: Session):
                self.user_repo = UserRepository(session)

            def register_user(self, username: str, email: str, password: str):
                if self.user_repo.get_user_by_username(username):
                    raise ValueError("Username already exists")
                if self.user_repo.get_user_by_email(email):
                    raise ValueError("Email already in use")

                user = User(username=username, email=email, password_hash=hash_password(password))
                return self.user_repo.create_user(user)

            def login_user(self, username: str, password: str):
                user = self.user_repo.get_user_by_username(username)
                if not user or not verify_password(password, user.password_hash):
                    raise ValueError("Invalid credentials")

                return create_access_token({"sub": user.username}, expires_delta=timedelta(minutes=30))
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Authentication Routes (auth/auth_routes.py)

        ```python
        from fastapi import APIRouter, Depends, HTTPException
        from sqlmodel import Session
        from app.core.database import get_session
        from app.auth.auth_service import AuthService

        router = APIRouter(prefix="/auth", tags=["Authentication"])

        @router.post("/register/")
        def register(username: str, email: str, password: str, session: Session = Depends(get_session)):
            try:
                auth_service = AuthService(session)
                user = auth_service.register_user(username, email, password)
                return {"message": "User registered successfully", "user_id": user.id}
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

        @router.post("/login/")
        def login(username: str, password: str, session: Session = Depends(get_session)):
            try:
                auth_service = AuthService(session)
                token = auth_service.login_user(username, password)
                return {"access_token": token, "token_type": "bearer"}
            except ValueError as e:
                raise HTTPException(status_code=401, detail=str(e))
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Protect API Routes with JWT

        ```python
        from fastapi import APIRouter, Depends
        from app.auth.auth_handler import get_current_user

        router = APIRouter(prefix="/test-suites", tags=["Test Suites"])

        @router.get("/", dependencies=[Depends(get_current_user)])
        def get_test_suites():
            return {"message": "This is a protected test results endpoint"}
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Testing Authentication

        ## Register a User

        ```shell
        curl -X POST "http://127.0.0.1:8000/auth/register/" \
             -d "username=testuser&email=test@email.com&password=securepassword"
        ```

        ## Login to Get GWT Token

        ```shell
        curl -X POST "http://127.0.0.1:8000/auth/login/" \
             -d "username=testuser&password=securepassword"
        ```

        Response:

        ```json
        {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI...", "token_type": "bearer"}
        ```

        ## Access a Protected Route

        ```shell
        curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
             -X GET "http://127.0.0.1:8000/test-suites/"
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Running with Docker

        ## Create a Dockerfile

        ```dockerfile
        # Use the official Python base image
        FROM python:3.11-slim

        # Set environment variables
        ENV PYTHONUNBUFFERED=1 \
            PYTHONDONTWRITEBYTECODE=1

        # Set working directory
        WORKDIR /app

        # Install system dependencies
        RUN apt-get update && apt-get install -y \
            curl \
            gcc \
            libpq-dev \
            && rm -rf /var/lib/apt/lists/*

        # Copy dependency files first
        COPY requirements.txt .

        # Install dependencies
        RUN pip install --no-cache-dir -r requirements.txt

        # Copy the entire application
        COPY . .

        # Expose FastAPI port
        EXPOSE 8000

        # Command to run the app
        CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
        ```

        ## Create a docker-compose file

        ```yaml
        version: '3.8'
        services:
          db:
            image: postgres:14
            container_name: test_results_db
            restart: always
            environment:
              POSTGRES_USER: your_user
              POSTGRES_PASSWORD: your_password
              POSTGRES_DB: test_results
            ports:
              - "5432:5432"
            volumes:
              - postgres_data:/var/lib/postgresql/data

          api:
            build: .
            container_name: test_results_api
            restart: always
            depends_on:
              - db
            ports:
              - "8000:8000"
            environment:
              DATABASE_URL: postgresql://your_user:your_password@db:5432/test_results

        volumes:
          postgres_data:
        ```

        ## Build the Docker Image

        ```shell
        docker build -t test-results-api .
        ```

        ## Run Everything

        ```shell
        docker-compose up -d
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Kubernetes Probes

        - Liveness Probe (/healthz/live) -> Checks if the application is still running
        - Readiness Probe (/heathz/ready) -> Checks if the application is ready to accept traffic

        ## Add Kubernetes Probe Routes (app/api/probes.py)

        Create a new FastAPI router to handle the probes.

        ```python
        from fastapi import APIRouter, Depends
        from sqlmodel import Session
        from app.core.database import get_session

        router = APIRouter(prefix="/healthz", tags=["Kubernetes Probes"])

        @router.get("/live", status_code=200)
        def liveness_probe():
            \"""
            ✅ Liveness probe: Returns 200 if the service is running.
            \"""
            return {"status": "alive"}

        @router.get("/ready", status_code=200)
        def readiness_probe(session: Session = Depends(get_session)):
            \"""
            ✅ Readiness probe: Returns 200 if the database connection is alive.
            \"""
            try:
                # Execute a simple query to check DB connectivity
                session.exec("SELECT 1")
                return {"status": "ready"}
            except Exception:
                return {"status": "not ready"}, 500

        # 🚀 NEW: Startup Probe (checks if app has fully started)
        @router.get("/startup", status_code=200)
        def startup_probe():
            return {"status": "started"}        
        ```

        ## Register the Routes in main.py

        Modify main.py to include Kubernetes probe routes.

        ```python
        from fastapi import FastAPI
        from app.api import test_suites, test_classes, test_cases, test_executions, probes
        from app.core.database import create_db_and_tables

        # Initialize FastAPI app
        app = FastAPI(title="Test Results API")

        # Database Initialization
        @app.on_event("startup")
        def on_startup():
            create_db_and_tables()

        # Include API routers
        app.include_router(test_suites.router, prefix="/test-suites", tags=["Test Suites"])
        app.include_router(test_classes.router, prefix="/test-classes", tags=["Test Classes"])
        app.include_router(test_cases.router, prefix="/test-cases", tags=["Test Cases"])
        app.include_router(test_executions.router, prefix="/test-executions", tags=["Test Executions"])
        app.include_router(probes.router, prefix="/healthz", tags=["Kubernetes Probes"])
        ```

        ## Define Kubernetes Probes in deployment.yaml

        Modify Kubernetes deployment file to include the liveness and readiness probes.

        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: test-results-api
        spec:
          replicas: 2
          selector:
            matchLabels:
              app: test-results-api
          template:
            metadata:
              labels:
                app: test-results-api
            spec:
              containers:
                - name: test-results-api
                  image: your-docker-image:latest
                  ports:
                    - containerPort: 8000
                  envFrom:
                    - configMapRef:
                        name: test-results-config

                  # 🚀 NEW: Startup Probe
                  startupProbe:
                    httpGet:
                      path: /healthz/startup
                      port: 8000
                    failureThreshold: 30  # Fail after 30 unsuccessful attempts
                    periodSeconds: 5       # Check every 5 seconds

                  # ✅ Liveness Probe
                  livenessProbe:
                    httpGet:
                      path: /healthz/live
                      port: 8000
                    initialDelaySeconds: 5
                    periodSeconds: 10

                  # ✅ Readiness Probe
                  readinessProbe:
                    httpGet:
                      path: /healthz/ready
                      port: 8000
                    initialDelaySeconds: 5
                    periodSeconds: 5
        ```

        ## How It Works

        Liveness Probe (/healthz/live):
        - If this probe fails, Kubernetes kills the container and starts a new one.
        - Ensures the app is not stuck in an unresponsive state.

        Readiness Probe (/healthz/ready):
        - If this probe fails, Kubernetes removes the pod from the load balancer until it recovers.
        - Ensures the app does not receive traffic before it is ready.
        """
    )
    return


if __name__ == "__main__":
    app.run()
