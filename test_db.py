from database import engine

try:
    # Connection test karne ke liye engine ko connect karein
    connection = engine.connect()
    print("Database connection successfully establish ho gaya hai! 🎉")
    connection.close()
except Exception as e:
    print(f"Connection fail ho gaya hai. Error yeh hai: {e}")