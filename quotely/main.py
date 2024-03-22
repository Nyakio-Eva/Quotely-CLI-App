from models.quote import Quote
from models.category import Category



try:
    #create instances for quotes
    quote1 = Quote()
    pass

    
except Exception as e:
    print("error occured while creating quote instances")    

try:
    #create instances for categories
    category1 = Category()
    pass

    
except Exception as e:
    print("error occured while creating category instances")        