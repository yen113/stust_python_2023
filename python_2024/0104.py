class FriedChicken: #定義類別

    def __init__(self, part, taste, spicy, bone, price): #定義屬性
        self.part = part
        self.taste = taste
        self.spicy = spicy
        self.bone = bone
        self.price = price

    #更改部位
    def get_Part(self):
        return self.part
    def set_part(self, new_part):
        self.part = new_part


    #計算服務費
    def ServiceFee(self):
        self.price = self.price + (self.price*0.1)
        return self.price

    #列印資料
    def print_details(self): 
        print(f"part: {self.part}")
        print(f"taste: {self.taste}")
        print(f"spicy: {self.spicy}")
        print(f"bone: {self.bone}")
        print(f"price: {self.price}")

#建立物件
chicken1 = FriedChicken("breast", "original", 1, "yes", 150)
chicken2 = FriedChicken("leg", "spicy cheese", 3, "no", 270)
chicken3 = FriedChicken("breast", "honeyjuice", 1, "no", 220)
chicken4 = FriedChicken("wings", "spicy", 4, "no", 180)

chicken1.set_part("wings")
chicken2.set_part("breast")
chicken3.set_part("leg")
chicken4.set_part("leg")

chicken1.ServiceFee()
chicken2.ServiceFee()
chicken3.ServiceFee()
chicken4.ServiceFee()

chicken1.print_details()
chicken2.print_details()
chicken3.print_details()
chicken4.print_details()