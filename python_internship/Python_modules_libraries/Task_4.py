print("\n--- Use datetime module to display current date and time. ---")


import datetime as dt

current_time = dt.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"The current time is {formatted_time}")
