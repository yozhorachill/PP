from datetime import date, timedelta

today = date.today()
five_days_ago = today - timedelta(days=5)

print(f"Today's date: {today}")
print(f"Five days ago: {five_days_ago}")
