from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import date

def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    return HttpResponse(content=template)


def index(request):
    # Prepare some data before creating the template.
    welcome_message = "Welcome to my website!"
    page_title = "My First View"
    
    # You can process the data as needed, e.g., retrieving data from a database, calculating something, etc.
    # In this case, we just use the prepared strings directly in the template.

    # Create a simple html page as a string using triple quotes for better readability.
    template = f"""<html>
                    <head>
                        <title>{page_title}</title>
                    </head>
                    <body>
                        <h1>{welcome_message}</h1>
                        <p>Home Page</p>
                    </body>
                  </html>"""

    # Return the template as content argument in an HttpResponse object.
    return HttpResponse(content=template)

def index2(request):
    # Prepare some data before creating the template.
    welcome_message = "Welcome to my 2nd page!"
    page_title = "My Second View"
    
    # You can process the data as needed, e.g., retrieving data from a database, calculating something, etc.
    # In this case, we just use the prepared strings directly in the template.

    # Create a simple html page as a string using triple quotes for better readability.
    template = f"""<html>
                    <head>
                        <title>{page_title}</title>
                    </head>
                    <body>
                        <h1>{welcome_message}</h1>
                    </body>
                  </html>"""

    # Return the template as content argument in an HttpResponse object.
    return HttpResponse(content=template)