from datetime import datetime

from django.utils import timezone

print(datetime.now())
# Часовой пояс не указан:
# 2022-03-08 15:44:47.919437 


print(timezone.now())