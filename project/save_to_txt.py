from pathlib import Path
from .models import Visit

def save_to_file():
    desktop = Path.home() / "Desktop" / "visits.txt"

    with open(desktop, "w", encoding="utf-8") as file:
        for visit in Visit.objects.all():
            visit.created_at = str(visit.created_at).split('.')
            file.write(f"{visit.name} | {visit.created_at[0]}\n")