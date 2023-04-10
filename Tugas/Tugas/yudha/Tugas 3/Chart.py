#class chart

class chart:
    def __init__(self):
        self.items= []
   
    def addTochart(self,data):
      sama = False
      for i in range(len(self.items)):
        if self.items[1]['name'] == data['name']:
            sama = True
   
        if sama == True:
            self.items[1]['quantity'] +=1
        else:
            self.items.append(data)
            self.items.append(data)
        print()


    #tmpilan
    def removeFromChart(self, product):
        product2 = {}
        product2['name'] = self.items[int(product) - 1]['name']
        product2['quantity'] = self.items [int(product) - 1]['quantity']
        self.items.pop(int(product) - 1)
        return product2

    def viewChart(self):
       j = 0
       for i in self.items:
          j += 1
          print(f"{i['name']}, Rp.{['price']}, - {i['quantity']} buah")


    def placeOrder(self):
        total_price = 0
        for i in self.items:
            total_price  += (i['price'] * i ['quantity'])
        print(f"Total price : {total_price}")
        print("Thank you for shoping with us!!")

chart = chart()