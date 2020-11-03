"""
Create a script that let the user type in a search term and opens and search on the browser for that term on Google
"""
import webbrowser 

search = input("Enter your Google query: ")
url = "https://www.google.com/?#q="
final_url = url + search.replace(" ", "%20")
webbrowser.open(final_url)
