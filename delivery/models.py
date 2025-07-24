from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.username} {self.password} {self.email} {self.number}"

class Restaurant(models.Model):
    resname = models.CharField(max_length=20)
    resimage = models.CharField(max_length=200,default="https://in.images.search.yahoo.com/images/view;_ylt=AwrPrsWcjm9ong0VP2q9HAx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkAzgzYzc4N2UzNDQzZWFkNWUzOGZkMGI3NjQ0ZDgzN2NiBGdwb3MDMTE1BGl0A2Jpbmc-?back=https%3A%2F%2Fin.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Drestaurant%2Bplaceholder%2Bimage%26type%3DE210IN885G0%26fr%3Dmcafee%26fr2%3Dpiv-web%26nost%3D1%26tab%3Dorganic%26ri%3D115&w=675&h=500&imgurl=findapatriot.org%2Fwp-content%2Fuploads%2F2021%2F12%2FRestaurants-Placeholder-Image.png&rurl=https%3A%2F%2Ffindapatriot.org%2Flisting%2Ftequilas-mexican-grill%2F&size=10KB&p=restaurant+placeholder+image&oid=83c787e3443ead5e38fd0b7644d837cb&fr2=piv-web&fr=mcafee&tt=Tequilas+Mexican+Grill+-+Find+A+Patriot&b=61&ni=21&no=115&ts=&tab=organic&sigr=HvjmeuBY8mbE&sigb=69AnFqvHGXRj&sigi=p5DUVhlMAsS4&sigt=IiPUt6Kfhx3p&.crumb=YYWqQ3UPFg1&fr=mcafee&fr2=piv-web&type=E210IN885G0")
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.resname}  {self.cuisine} {self.rating}/5"
    
class MenuItem(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="menu_items")

    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200,default="https://tse4.mm.bing.net/th/id/OIP.5Uy16-H5NnlOh-XJjztaMwHaHa?pid=Api&P=0&h=180")
    description = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    isVeg =models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}  {self.description} {self.price}"

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="cart")

    items=models.ManyToManyField("MenuItem",related_name="cart")
    
    def total_price(self):
        return sum(item.price for item in self.items.all())
    def __str__(self):
        return f"{self.customer.username} {self.total_price}"