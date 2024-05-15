FastAPI integrates with SQLAlchemy through the use of Pydantic models and dependency injection. First, a SQLAlchemy model is defined for the database structure. Then, a Pydantic model is created to handle data validation and serialization. FastAPI uses these models in route functions to interact with the database.

Dependency injection allows for reusable dependencies that manage database sessions. A common pattern involves creating a function that yields a session, then closes it after request handling. This function can be included as a parameter in route functions, providing them with a session instance.

For SQL queries, SQLAlchemy’s ORM is used directly within the route functions. The session provided by the dependency handles transactions, ensuring changes are committed or rolled back appropriately.
