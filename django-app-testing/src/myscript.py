import os

bad = "1d8748281263e8e7efe7b85c828cd3f600d96bfc"
good = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system(f"git bisect start {bad} {good}")
os.system("git bisect run python manage.py test")