from django_unicorn.components import UnicornView
from books.models import Gener


class GenerunicornView(UnicornView):
    title = ""
    categories = ""
    message = ""
    id = 0
    def mount(self):
        self.categories = Gener.objects.all()
 
    def add(self):
        cat = Gener.objects.filter(pk = self.id)
        if not cat and self.title != "":
            cat = Gener()
        else:
            cat = cat[0]
        try:
            cat.name = self.title
            cat.save()
            self.title = ""
        except:
            self.message = "Gener is Already Exist"
            print(cat)
        self.mount()
    
    def view(self,id):
        cat = Gener.objects.get(pk = id)
        self.title = cat.name
        self.id = id
        self.mount()
 
    def delete(self,id):
        cat = Gener.objects.get(pk = id)
        
        if cat.active is True:
            cat.active = False    
        else:
            cat.active = True
        cat.delete()
        self.mount()
        
    
