"""end= keyword"""

import timeit

# end= lets us print values side by side instead of going to
# a new line. Whatever typed in "..." is shown.
print("5", end="")


"""Overwrite using Print method"""
# Here it's an f-string (formatted string). Here:
# •	{timer} insert our timer value (like “00:09)
# •	\r  carriage return
# \r moves the cursor back to the start of the same line and doesn’t go to a new line
# end="" combine with \r means:
# •	Stay on same line
# •	Overwrite it repeatedly
# By default, python buffers output (waits before showing it). flush=True means show this output immediately. Without it pycharm may delay or show nothing, with it updates every second instantly.
# Pulling it all together. Each loop:
# •	\r → go to start of line
# •	print new timer → overwrite old text
# •	end="" → stay on same line
# •	flush=True → force instant display
timer = timeit.default_timer
print(f"\r{timer}", end="", flush=True)
