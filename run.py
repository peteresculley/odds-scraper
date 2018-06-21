import time
import odds_scraper

interval = 300.0 # 5 minutes

start_time = time.time()
while True:
   print(time.asctime())
   odds_scraper.update()
   
   time.sleep(interval - ((time.time() - start_time) % interval))

   print()
   print()
