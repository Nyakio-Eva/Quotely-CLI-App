from models.quote import Quote
from models.category import Category



# try:
#     # Create instances for find by id
#     humor = Category.find_by_id(1)  
#     programming = Category.find_by_id(2)  
#     motivational = Category.find_by_id(3)  
#     whiskey = Category.find_by_id(4)  
#     life = Category.find_by_id(5)  
#     happiness = Category.find_by_id(6)  

#     #create instances for find by name 
#     humor = Category.find_by_name("humor")  
#     programming = Category.find_by_name("programming")  
#     motivational = Category.find_by_name("motivational")  
#     whiskey = Category.find_by_name("whiskey")  
#     life = Category.find_by_name("life")  
#     happiness = Category.find_by_name("happiness")  

#     #create instances for quotes
#     quote1 = Quote("So Stephen Hawking walks into a bar... just kidding.", "Storypick", humor.id)
#     quote2 = Quote("Why do programmers prefer dark mode? Cause light attracts bugs.", "ShivamLH", programming.id)
#     quote3 = Quote("Don't wish for it, work for it.", "Rachael Robbins", motivational.id )
#     quote4 = Quote("I like my whiskey like I like my opinions, straight up and strong","Abby Leigh", whiskey.id)
#     quote5 = Quote("life is soup and I'm a fork", "unknown", life.id)
#     quote6 = Quote("Smile with your eyes, smise", "Marie", happiness.id)    

    
#     #crud nethods for quotes
#     # Testing the create() method by a adding  a new quote
#     new_quote_text = "Coder girl, A girl with magical powers who can hack your day."
#     new_author = "Anonymous"
#     new_category_id = programming.id
 
#     new_quote_text2 = "Roses are Red, Violets are Blue, unexpeced '}' on line 32."
#     new_author2 = "Nathan Crowther"
#     new_category_id2 = programming.id

#     new_quote = Quote.create(new_quote_text,new_author,new_category_id)
#     new_quote2 = Quote.create(new_quote_text2,new_author2,new_category_id2)
#     print("New quote created successfully:", new_quote)
#     print("New quote created successfully:", new_quote2)

#     # retrieve all quotes
#     all_quotes = Quote.get_all_quotes()
#     print("All quotes after adding the new quote:")
#     for quote in all_quotes:
#         print(quote)
    
#     # # Retrieve quotes by a specific author
#     # author_name = "ShivamLH"
#     # quotes_by_author = quote2.get_quotes_by_author(author_name)
#     # if quotes_by_author:
#     #     for quote in quotes_by_author:
#     #         print(quote)
#     # else:
#     #     print(f"No quotes found for author: {author_name}")
    
#     # #Test get_category_ids_for_author method
#     # author_name = "Marie"
#     # author_category_ids = Quote.get_category_ids_for_author(author_name)
#     # print(f"Category IDs associated with author '{author_name}': {author_category_ids}")

#     # #Test get_categories for author method
#     # author_categories = Quote.get_categories_for_author(author_name)
#     # if author_categories:
#     #     print(f"The categories associated with author '{author_name}' are:")
#     #     for category in author_categories:
#     #         print(category)
#     # else:
#     #     print(f"No categories found for the author '{author_name}'.")        
    
    
# except Exception as e:
#     print("error occured while retrieving quotes:", e)    

try:

    #create instances for categories
    humor = Category.find_by_name("humor")  
    programming = Category.find_by_name("programming")  
    motivational = Category.find_by_name("motivational")  
    whiskey = Category.find_by_name("whiskey")  
    life = Category.find_by_name("life")  
    happiness = Category.find_by_name("happiness")
    
    #categories methods
    #create new category method
    new_category = Category.create("birthday")
    print(f"New category created:", {new_category})


    #1. Get all categories
    # Get all categories
    all_categories = Category.get_all_categories()
    if all_categories:
        for category in all_categories:
            print(category)
    else:
        print("No categories found.")

    # # Test the get_category_by_name method
    # category_name_to_find = "humor"
    # category = Category.find_by_name(category_name_to_find)
    
    # # Check if the category was found
    # if category:
    #     print(f"Category found: {category}")   
    # else:
    #     print(f"Category '{category_name_to_find}' not found.")

    # # Create instances for quotes and categories
    # humor = Category.find_by_id(1)  
    # programming = Category.find_by_id(2)  
    # motivational = Category.find_by_id(3)  
    # whiskey = Category.find_by_id(4)  
    # life = Category.find_by_id(5)  
    # happiness = Category.find_by_id(6)   

    # category_ids = [2,3]   

    # #get quotes belonging to this category
    # quotes_for_categories = category.get_quotes_for_categories(category_ids)

    # #display quotes for each category
    # for quote in quotes_for_categories:
    #     print(quote)

except Exception as e:
    print("error occured while creating category instances")        