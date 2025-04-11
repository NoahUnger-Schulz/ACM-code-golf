from datetime import datetime as d
print(d.strptime(input(), "%Y-%m-%d").strftime('%A'))
