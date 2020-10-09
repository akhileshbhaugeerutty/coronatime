# -*- coding: utf-8 -*-
"""exampleSMAJupyterColab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rurr8YOAn6CRzyW-cqhT7tpAmHSV7vEQ
"""

import random
class Agent:
    
    def __init__(self):
        self.pnl = 0
        self.nb_trades = {"buyer" : 0 , "seller" : 0}
    
    def Buy(self, price):
      self.nb_trades["buyer"] = self.nb_trades["buyer"]+ 1
      self.pnl = round(self.pnl - price,2)
    
    def Sell(self, price):
      self.nb_trades["seller"] = self.nb_trades["seller"] + 1
      self.pnl = round(self.pnl + price,2)


# Market maker hérite de la classe agent
class Trader(Agent):
    def __init__(self):
        super().__init__()
        self.strategy = "PairImpair"
        self.direction = "Sell"
    
    def DisplayTrader(self):
        print("Strategy : {} , Direction : {}, PnL : {}".format(self.strategy,self.direction, self.pnl))

    def ApplyStrategy(self, nb_iteraction):
      if nb_iteraction % 2 ==0 :
        self.direction = "Buy"
      else:
        self.direction = "Sell"
    
    def Interact(self, prices):
      if self.direction == "Buy":
        self.Buy(prices["ask"])
      else:
        self.Sell(prices["bid"])
    
    
      

# Market maker hérite de la classe agent
class MarketMaker(Agent):
    def __init__(self):
        super().__init__()
        self.prices = {"bid" : 15 , "ask" : 16}
    
    def DisplayMarketMaker(self):
        print("Price Bid : {} , Price Ask : {}".format(self.prices["bid"],self.prices["ask"]))

    def SetPrices(self, ticksize):
      self.prices["bid"] = round(self.prices["bid"] + round(random.random()*2 -1, 2),2)
      self.prices["ask"] = round(self.prices["bid"] + round(ticksize*random.randrange(1,3),2),2)

    def GetMidPrice(self):
      return round((self.prices["bid"] +self.prices["ask"])/2,2)


# j'instancie mes 3 acteurs
trader_1 =Trader()
trader_2 = Trader()
mm = MarketMaker()

trader_1.DisplayTrader()
mm.DisplayMarketMaker()

#je créé ma classe StockMarket
class StockMarket:
    def __init__(self,list_traders, mm, nb_iterations,ticksize):
        self.list_traders = list_traders
        self.market_maker = mm
        self.nb_iterations = nb_iterations
        self.tick_size = ticksize
        self.mid_prices = []
    
    def DisplayStockMaket(self):
        print("Nb de traders : {} , nb iteration : {}".format(len(self.list_traders),
                                                                  self.nb_iterations))
    
    def RunMarket(self):
      for i in range(1,self.nb_iterations+1):
        self.market_maker.SetPrices(self.tick_size)
        self.mid_prices.append(self.market_maker.GetMidPrice())
        #self.market_maker.DisplayMarketMaker()
        for trader_i in self.list_traders:
          trader_i.ApplyStrategy(i)
          trader_i.Interact(self.market_maker.prices)
          #trader_i.DisplayTrader()
        

result = []        
for i in range(100):
  #print("nouvelle trajectoire {}".format(i))
  #j'instancie mon marché
  my_market = StockMarket([trader_1,trader_2],mm,5,0.5)
  #my_market.DisplayStockMaket()
  my_market.RunMarket()
  result.append(my_market.mid_prices)

"""Ci-dessous élements pour comment sortir des "variables output" du système"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#je concatène tous mes résultats (ici mid_price) dans une dataframe pour étudier la donnée
df = pd.DataFrame(result,columns = ["first_it","second_it","third_it","fourth_it","fifth_it"])

#je visualise la donnée pour voir à quoi elle ressemble
#df.T.plot()
# aller plus loins dans les librairies seaborn
df.head()

#au lieu de conserver toute l'information je choisis de ne retenir que les statistiques principales de la distribution de mes données
final = pd.DataFrame(df.median(axis=0)).T.append(pd.DataFrame(df.quantile(q = 0.25,axis=0)).T).append(pd.DataFrame(df.quantile(q = 0.75,axis=0)).T).append(pd.DataFrame(df.min(axis=0)).T).append(pd.DataFrame(df.max(axis=0)).T)
print(final.head())
#j'exporte les données sous csv
#final.to_csv("export.csv")
final.T.plot()

#final.describe()

"""Exemple pour initialiser un marché"""

import numpy as np
import random
list_traders = []


for i in range(5):
  trader_i = Trader()
  if random.randint(0,100) > 50:
    trader_i.strategy = "strategy_1"
  else:
    trader_i.strategy = "strategy_2"
  list_traders.append(trader_i)

for tmp in list_traders:
  tmp.DisplayTrader()