from jinja2 import Template
from datetime import datetime

current_time = datetime.now()
current_minute = current_time.minute

json = """
    {
        "page_action" : [
            { 
                "type" : You are {% if minute%2==0 %} a "open_dialog" {% else %} an "shake" {% endif %} 
            }
        ]
    }
"""

tm = Template(json)

response = tm.render(minute=current_minute)

print(response)