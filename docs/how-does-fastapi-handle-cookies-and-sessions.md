FastAPI doesn’t directly handle cookies and sessions, but it can be integrated with Starlette’s SessionMiddleware for this purpose. To use cookies, FastAPI has a ‘cookies’ parameter in path operation functions. You declare the cookie name as a string argument to receive its value. For sessions, you add SessionMiddleware to your application, providing a secret key. This middleware uses signed cookies to store session data client-side. The data is cryptographically signed but not encrypted, so user can see contents but cannot modify them without invalidating signature.