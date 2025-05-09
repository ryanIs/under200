# weightdata.py
#
# This module provides the back-end version of the primary weight data.

# Weight data (in-file, objective: pull from database like postgres or mongo!)
WEIGHT_DATA = """[WEIGHT]
MARCH:

  26-03-25  -  
  25-03-25  -  
  24-03-25  -  
  23-03-25  209.3  
  22-03-25  210.3  
  21-03-25  210.3  very fun family hang out! went for a run and we talked about lots of different topics; food: pizza, beers, hot dogs, bread, custom shake etc.
  20-03-25  210.3  
  19-03-25  210.8  
  18-03-25  210.8  
  17-03-25  211.8  
  16-03-25  212.8  
  15-03-25  212.8  
  14-03-25  212.8  
  13-03-25  212.8  
  12-03-25  213.4  
  11-03-25  214.7  
  10-03-25  215.3  
  09-03-25  215.3  todays food: eggs, salad, tuna, beans, black bean burger and guac; the guac makes everything amazing actually!
  08-03-25  216.3  
  07-03-25  216.3  
  06-03-25  217.8  
  02-03-25  218.4  
  01-03-25  218.9  

FEBRUARY:
  28-02-25  219.4  
  27-02-25  220.8  
  26-02-25  220.8  
  25-02-25  220.8  
  24-02-25  222.2  
  23-02-25  222.2  
  22-02-25  222.2  
  21-02-25  224.3  how long will this plateau last for?? 
  20-02-25  224.3  
  19-02-25  224.3  went for a run today!
  18-02-25  225.5  
  17-02-25  225.5  
  16-02-25  224.3  
  15-02-25  225.5  today_food: low cals low salt (eggs!) 211 lets go!! 
  14-02-25  225.5  yestfood: full food black container chili(beans: garbonzo, black, lentils, byndmeat, tons-salsa; min ), yogurt,shake.
  13-02-25  226.1  food: low cals regular 
  12-02-25  227.3  yestFood: 450cals: 1/2bean200,shake100,yogurt100===I will escape this double plateau!!! show me that lower number !!!
  11-02-25  227.3  yestFood: plate: 250egg, 100yog, 100seaweed, 100_1guac, 100shake = 650! lets see a 223 this morning!
  10-02-25  227.3  yestFood: beans, 2cup salsa (high salt! may keep weight--cals low though so fine), shake, proteinYogurt, ?seaweed?, brocoli, spinach, 1guac, 270:4_veg_metaball 
  09-02-25  227.4  food roto: BEANS__WHITES__TUNA
  08-02-25  227.9  reducefood
  07-02-25  227.9  reducefood
  06-02-25  229.7  
  05-02-25  230.7  
  04-02-25  230.7  
  03-02-25  231.8  
  02-02-25  231.9  ate pizza and some other yummy foods today. just noting it!
  01-02-25  233.8  

JANUARY:
  31-01-25  236.9  
  30-01-25  237.5  
  29-01-25  236.9  
  27-01-25  237.5  
  26-01-25  235.1  Nice progress!! continue running
  25-01-25  235.5  
  20-01-25  237.5  
  19-01-25  233.5  Nice progress!!!
  18-01-25  237.5  
  16-01-25  237.5  
  02-01-25  238.1  
  12-12-24  238.5  
  11-11-24  239.1  
  02-11-24  239.7  
  01-11-24  239.7  
  
[/WEIGHT]
"""

def get_weight():
  return WEIGHT_DATA