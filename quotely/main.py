from models.quote import Quote
from models.category import Category



try:
    # # Create instances for quotes and categories
    # humor = Category.find_by_id(1)  
    # programming = Category.find_by_id(2)  
    # motivational = Category.find_by_id(3)  
    # whiskey = Category.find_by_id(4)  
    # life = Category.find_by_id(5)  
    # happiness = Category.find_by_id(6)  
 
    #create instances for find by name 
    humor = Category.find_by_name("humor")  
    programming = Category.find_by_name("programming")  
    motivational = Category.find_by_name("motivational")  
    whiskey = Category.find_by_name("whiskey")  
    life = Category.find_by_name("life")  
    happiness = Category.find_by_name("happiness")  

    #create instances for quotes
    quote1 = Quote("So Stephen Hawking walks into a bar... just kidding.", "Storypick", humor.id)
    quote2 = Quote("Why do programmers prefer dark mode? Cause light attracts bugs.", "ShivamLH", programming.id)
    quote3 = Quote("Don't wish for it, work for it.", "Rachael Robbins", motivational.id )
    quote4 = Quote("I like my whiskey like I like my opinions, straight up and strong","Abby Leigh", whiskey.id)
    quote5 = Quote("life is soup and I'm a fork", "unknown", life.id)
    quote6 = Quote("Smile with your eyes, smise", "Marie", happiness.id)    

    
    #crud nethods for quotes
    #1. retrieve all quotes
    all_quotes = Quote.get_all_quotes()
    for quote in all_quotes:
        print(quote)


    
except Exception as e:
    print("error occured while retrieving quotes:", e)    

try:
    #create instances for categories
    humor = Category.find_by_name("humor")  
    programming = Category.find_by_name("programming")  
    motivational = Category.find_by_name("motivational")  
    whiskey = Category.find_by_name("whiskey")  
    life = Category.find_by_name("life")  
    happiness = Category.find_by_name("happiness")
    
    #categories methods
    #1. Get all categories
   # Get all categories
    all_categories = Category.get_all_categories()
    if all_categories:
        for category in all_categories:
            print(category)
    else:
        print("No categories found.")

except Exception as e:
    print("error occured while creating category instances")        