from datetime import datetime, timedelta

dates = [
    "2025.12.13", "2025.12.20", "2026.01.03", "2026.01.10",
    "2026.01.17", "2026.01.24", "2026.01.31", "2026.02.07",
    "2026.02.14", "2026.02.21", "2026.02.28", "2026.03.07",
    "2026.03.14", "2026.03.21", "2026.03.28", "2026.04.04"
]

date_objs = [datetime.strptime(d, "%Y.%m.%d") for d in dates]
date_objs.sort()

start_date = date_objs[0]
end_date = date_objs[-1]

current = start_date
missing = []
while current <= end_date:
    if current not in date_objs:
        missing.append(current.strftime("%Y.%m.%d"))
    current += timedelta(days=7)

print("Missing Saturdays:", missing)
