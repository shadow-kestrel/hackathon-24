#!/usr/bin/bash

cp ../index.html ../style.css ../script.js ../cat-*-outline.png /var/www/html/catbot/
echo 'http://kestrel.gay/catte.gif' > /var/www/html/catbot/next_gif.url

# im not sure if python's socketserver will finish handling current requests
# on SIGTERM but oh well
kill -TERM $(ps -x | grep message_handler.py | awk '{print $1}')

cp Python/message_handler.py run

python run/message_handler.py 2>> run/catbot_ERR &


