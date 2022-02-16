"""
Save this file to ESP32
Function returns a string (html code for web page)
"""

def web_page(temp, duration):
  html = """<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>ESP32 Web Server</title>
    </head>

    <body>
        <p>ESP32 temperature: <strong>""" + f"{temp:.1f} C" + """</strong></p>
        <p>ESP32 up time: <strong>""" + f"{duration} sec" + """</strong></p>
    </body>

    </html>"""
  
  return html
