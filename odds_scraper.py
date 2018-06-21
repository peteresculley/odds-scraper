import time
import paddypower
import bet365
import williamhill

def calculate_odds(odds_str):
   return float(odds_str.split('/')[0]) / float(odds_str.split('/')[1])

def add_to_results(results, name, elements_to_add, running_total):
   for e in elements_to_add:
      found = False
      for r in results:
         if r['country'] == e[0]:
            r[name] = e[1]
            odds = calculate_odds(e[1])
            if odds > running_total[e[0]]:
               r['best'] = name
               running_total[e[0]] = odds
            found = True
      if not found:
         results.append({'country': e[0], name: e[1], 'best': name})
         running_total[e[0]] = calculate_odds(e[1])

def update_results():
   paddy_res = paddypower.scrape()
   bet_res = bet365.scrape()
   william_res = williamhill.scrape()

   results = []
   running_total = {}
   add_to_results(results, 'Paddypower', paddy_res, running_total)
   add_to_results(results, 'bet365', bet_res, running_total)
   add_to_results(results, 'William Hill', william_res, running_total)
   
   return results

def display_results(results):
   country_width = 15
   col_width = 14
   missing_test = 'missing'
   print('Country:'.ljust(country_width) + 'Paddypower:'.ljust(col_width) + 'bet365:'.ljust(col_width) + 'William Hill:'.ljust(col_width) + 'Best:'.ljust(col_width))
   for r in results:
      country = str(r.get('country'))
      if r.get('Paddypower'):
         paddy = str(r.get('Paddypower'))
      else:
         paddy = missing_test
      if r.get('bet365'):
         b365 = str(r.get('bet365'))
      else:
         b365 = missing_test
      if r.get('William Hill'):
         william = str(r.get('William Hill'))
      else:
         william = missing_test
      best = str(r.get('best'))
      
      print(country.ljust(country_width) + paddy.ljust(col_width) + b365.ljust(col_width) + william.ljust(col_width) + best.ljust(col_width))

def write_results_to_file(results):
   try:
      file = open('output.txt', 'w')
      country_width = 15
      col_width = 15
      missing_test = 'missing'
      file.write(time.asctime() + '\n')
      file.write('Country:'.ljust(country_width) + 'Paddypower:'.ljust(col_width) + 'bet365:'.ljust(col_width) + 'William Hill:'.ljust(col_width) + 'Best:'.ljust(col_width) + 'Best odds:'.ljust(col_width))
      file.write('\n')
      for r in results:
         country = str(r.get('country'))
         if r.get('Paddypower'):
            paddy = str(r.get('Paddypower'))
         else:
            paddy = missing_test
         if r.get('bet365'):
            b365 = str(r.get('bet365'))
         else:
            b365 = missing_test
         if r.get('William Hill'):
            william = str(r.get('William Hill'))
         else:
            william = missing_test
         best = str(r.get('best'))
         best_odds = r.get(r.get('best'))
         if best_odds:
            best_odds = str(best_odds)
         else:
            best_odds = ''
         
         file.write(country.ljust(country_width) + paddy.ljust(col_width) + b365.ljust(col_width) + william.ljust(col_width) + best.ljust(col_width) + best_odds.ljust(col_width))
         file.write('\n')
   except Exception as e:
      print('Error while trying to write results to output.txt: ', e)
   finally:
      file.close()

def update():
   results = update_results()
   display_results(results)
   write_results_to_file(results)
