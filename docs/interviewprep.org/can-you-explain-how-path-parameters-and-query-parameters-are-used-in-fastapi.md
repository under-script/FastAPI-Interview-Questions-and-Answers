FastAPI uses path parameters and query parameters to extract data from a URL. Path parameters are defined in the route’s URL, enclosed in curly braces {}. They’re used to capture specific values from the path itself. For example, @app.get(“/items/{item_id}”) would capture the item_id from the URL.

Query parameters, on the other hand, are appended after the URL following a question mark ?. They allow optional information to be passed into the function. For instance, @app.get(“/items/”) might accept ‘skip’ and ‘limit’ as query parameters to control pagination.

In both cases, FastAPI automatically validates these parameters, generates error messages when data is invalid, and provides interactive documentation for them.
