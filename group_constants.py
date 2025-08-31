from typing import Final

# Organize constants by category.

class Database:
    URL: Final = "postgresql://user:pass@localhost/db"
    USER_NAME: Final = "user"
    PASSWORD: Final = "pass"

class Server:
    DNS: Final = "db.example.com"
    PORT: Final = "8888"
