# practice-constants-env-fastapi-uvcorn
Repository to gain a deep understanding of constants, environment variables, FastAPI, and Uvicorn.

Below are seperate examples:

**Constants:**
    # Dedicated file for constants.
    # This is Optional to Use 'typing.Final' for type safety.
    constants.py
     
    # Organize constants by category.
    group_constants.py

    # For Enum constants
    enum_status.py

    # Test constants using practice_constants_env_main.py file.
    Command: py practice_constants_env_main.py

**Environment Configurations:**
    # Environment variables can be read from operating system variables or .env file.

    Test environment variable using practice_constants_env_main.py file.
    Command: py practice_constants_env_main.py    

**FastAPI:**
    uvicorn practice_fastapi:app --reload

**Router:**
    # Created user (user.py) and product(product.py) router inside routers folder.
    
    # Note: added empty __init__.py file inside routers folder, indicates this is a package.

    # practice_router.py to test router.
    uvicorn practice_router:app --reload    

**Scheduler:**
    # Test Scheduler with FastAPI
    uvicorn practice_scheduler:app --reload

**Depends / Dependency:**
    # Reusable logic that you can attach to your routes (or even entire routers) so you don't have to repeat the same code everywhere.
    uvicorn practice_router_dependencies:app --reload    
