print("hi welcome to my shop (this shop is the simulate of apple store)")

class Information:
    def __init__(self, your_name):
        self.your_name = your_name

class Product:
    def shop(self):
        product1 = ["macbook", "iphone", "airpod", "apple watch"]
        print("This is our product:", product1)
        total = 0

        while True:
            product_name = input("Please enter your product name (or press s to stop): ").strip().lower()
            
            if product_name == "s":
                break
            elif product_name == "macbook":
                print("Oh, that's MacBook!") 
                print("The price is $1000")
                total += 1000
            elif product_name == "iphone":
                print("Oh, that's iPhone!") 
                print("The price is $500")
                total += 500
            elif product_name == "airpod":
                print("Oh, that's AirPod!") 
                print("The price is $500")
                total += 500
            elif product_name == "apple watch":
                print("Oh, that's Apple Watch!") 
                print("The price is $600")
                total += 600
            else:
                print("We can't help you with that product.")
        
        print(f"Dear {c1.your_name}, your total cost is ${total}")

c1 = Information(input("Please enter your name: ").strip())
c2 = Product()
c2.shop()
