#MAIN PAGE
from product import fuji_film, sharp, gucci, atomic_habit, detektif_conan_v1
from Chart import chart

def main():
    data = {}
    print ("===WELCOME TO QUR ONLINE SHOP SYSTEM===")
    print("----------------------------------------")
    print()
    print("Available Product :")
    print("===================")
    print(f"1. {fuji_film.name} (Electronics) - Price Rp.{fuji_film.price}, Quantity:{fuji_film.quantity} -- Warranty Period is {fuji_film.warranty_period} month")
    print(f"2. {sharp.name} (Electronics) - Price Rp.{sharp.price}, Quantity:{sharp.quantity} -- Warranty Period is {sharp.warranty_period} month")
    print(f"3. {gucci.name} (Clothing) - Price Rp.{gucci.price}, Quantity:{gucci.quantity} -- Warranty Period is {gucci.size} month")
    print(f"4. {atomic_habit.name} (Book) - Price Rp.{atomic_habit.price}, Quantity:{atomic_habit.quantity} -- Warranty Period is {atomic_habit.author} month")
    print(f"5. {detektif_conan_v1.name} (Book) - Price Rp.{detektif_conan_v1.price}, Quantity:{detektif_conan_v1.quantity} -- Warranty Period is {detektif_conan_v1.author} month")
    print()
    choise = input("input the number for add product to chart (or 0 for exit to chart):")
    print()
    if choise == "1":
        data.update({
        "name" : fuji_film.getName(),
        "price" : fuji_film.getprice(),
        "Quantity" : fuji_film.getQuantity(),
        })
        chart.addChart(data)
        fuji_film.updateQuantity(-1)
    elif choise == "2":
        data.update({
        "name" : sharp.getName(),
        "price" : sharp.getprice(),
        "Quantity" : sharp.getQuantity(),
        })
        chart.addChart(data)
        gucci.updateQuantity(-1)
    elif choise == "3":
        data.update({
        "name" : gucci.getName(),
        "price" : gucci.getprice(),
        "Quantity" : gucci.getQuantity(),
        })
        chart.addChart(data)
        sharp.updateQuantity(-1)
    elif choise == "4":
        data.update({
        "name" : atomic_habit.getName(),
        "price" : atomic_habit.getprice(),
        "Quantity" : atomic_habit.getQuantity(),
        })
        chart.addChart(data)
        atomic_habit.updateQuantity(-1)
    elif choise == "5":
        data.update({
        "name" : detektif_conan_v1.getName(),
        "price" : detektif_conan_v1.getprice(),
        "Quantity" : detektif_conan_v1.getQuantity(),
        })
        chart.addChart(data)
        detektif_conan_v1.updateQuantity(-1)
    elif choise == "0":
        return False
    else:
        print("Not validated input")


while True:
    print("===CHART===")
    print("-----------") 
    for i in chart.items:
        print(f"{1['name']}, Rp.{i['quantity']}, - buah")
        print()
    choice = input("Enter 1 to place order, 2 to remove product, or 0  to exit :")
    if choice == "1":
        chart.placeOrder()
    elif choice == "2":
        product = input("Masukan nomor barang : ")
        product2 = chart.removeFromchart(product)
    elif choice == "0":
        chart.addTochart()



#kelanjang
def chaets():
    print("=== CGART ===")
    print("--------------")
    chart.viewchart()
    print()
    choice = input("Enter 1 to place order, 2 to remove product, or 0 to exit")
    if choice == "1":
         chart.placeOrder()
    elif choice == "2":
        product2 = input("Enter the number of product :")
        product2 = chart.removeFromChart(product)
        if product2['name'] == "Fuji film":
            fuji_film.updateQuantity(product2['quantity'])
            product2 = chart.removeFromChart(product)
        elif product2['name'] == "sharp":
            sharp.updateQuantity(product2['quantity'])
            product2 = chart.removeFromChart(product)
        elif product2['name'] == "gucci":
            gucci.updateQuantity(product2['quantity'])
            product2 = chart.removeFromChart(product)
        elif product2['name'] == "atomic_habit":
            atomic_habit.updateQuantity(product2['quantity'])
            product2 = chart.removeFromChart(product)
        elif product2['name'] == "detektif_conan_v1":
            detektif_conan_v1.updateQuantity(product2['quantity'])
            product2 = chart.removeFromChart(product)
    elif choice == "0":
        return False
    else:
        print("not validate input")
      
while True:
    kondisi = main()
    if kondisi == False:
        break
while True:
    kondisi = charts()
    if kondisi == False:
        break