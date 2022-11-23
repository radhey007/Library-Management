from django_unicorn.components import UnicornView
from books.models import Categories

class CategoryunicornView(UnicornView):
    title = ""
    categories = ""
    message = ""
    id = 0
    def mount(self):
        self.categories = Categories.objects.all()
 
    def add(self):
        cat = Categories.objects.filter(pk = self.id)
        if not cat and self.title != "":
            cat = Categories()
        else:
            cat = cat[0]
        try:
            cat.name = self.title
            cat.save()
            self.title = ""
        except:
            self.message = "Category is Already Exist"
            print(cat)
        self.mount()
    
    def view(self,id):
        cat = Categories.objects.get(pk = id)
        self.title = cat.name
        self.id = id
        self.mount()
 
    def delete(self,id):
        cat = Categories.objects.get(pk = id)
        
        if cat.active is True:
            cat.active = False    
        else:
            cat.active = True
        cat.delete()
        self.mount()
        
    