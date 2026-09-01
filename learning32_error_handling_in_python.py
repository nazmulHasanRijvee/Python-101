"""Error Handling"""

# # Syntax. try: is for errors that checks if an error
# is happening or not. except ...: handles the error and the
# code does not crash. finally: runs the code error or no error.
try:
    # Some risky code that may cause error
    pass
except NameError:
    # Handles the error
    pass
finally:
    print("finally")


"""ValueError"""
# Here, if we enter a string instead of integer. except: will
# handle it using ValueError printing invalid input. finally:
# will run the code no matter what
var_int = 0
try:
    var_int = int(input("Enter: "))
except ValueError:
    print("Invalid input")
finally:
    print(var_int)  # hi - Invalid Input 0


"""Error handling in loop"""
# # We can use this to handle error in loop if except has
# ValueError, it will continue the code which skips iteration
# and run the loop again.
while True:
    try:
        # risky code
        var_int = int(input("Enter: "))
    except ValueError:
        # handles error
        print("Invalid input")
    finally:
        print(var_int)
    break

# NOTE: There’s also FileExistError and KeyError like ValueError
# (except FileExistError)


"""More error handling for REST APIs"""
# We can use try/except to catch network issues or server errors.
# There are multiple errors like:
# •	HTTPError – The server responded but returned an error (e.g., 404, 500).
# •	ConnectionError – There was a problem connecting to the server (no network or server down).
# •	Timeout – The request took too long to get a response from the server.
# •	RequestException – A general error that covers all other kinds of issues during a request.
import requests

try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()  # Raises an HTTPError for bad codes
    print(response.json())
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Error:", err)
