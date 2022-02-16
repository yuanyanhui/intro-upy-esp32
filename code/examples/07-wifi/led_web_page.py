"""
Save this file to ESP32
Function returns a string (html code for web page)
"""

def web_page(led_state):
  html = """<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>ESP32 Web Server</title>
        <style>
            html {
                font-family: Helvetica;
                display: inline-block;
                margin: 0px auto;
                text-align: center;
            }

            h1 {
                color: #0F3376;
                padding: 2vh;
            }

            p {
                font-size: 1.5rem;
            }

            .button {
                display: inline-block;
                background-color: #e7bd3b;
                border: none;
                border-radius: 4px;
                color: white;
                padding: 16px 40px;
                text-decoration: none;
                font-size: 30px;
                margin: 2px;
                cursor: pointer;
            }

            .button2 {
                background-color: #4286f4;
            }
        </style>
    </head>

    <body>
        <h1>ESP32 Web Server</h1>
        <p>LED State: <strong>""" + led_state + """</strong></p>
        <p><a href="/led_on"><button class="button">ON</button></a></p>
        <p><a href="/led_off"><button class="button button2">OFF</button></a></p>
    </body>

    </html>"""
  
  return html

