from jinja2 import Template
from datetime import datetime

current_time = datetime.now()
current_minute = current_time.minute

def func(minute):
    if minute%2==0:
        return "open_dialog"
    else:
        return "shake"

json = """
    {
        "page_action" : [
            { 
                "type" : {{message}}
            }
        ]
    }
"""

message = func(current_minute)

tm = Template(json)

response = tm.render(message=message)

print(response)