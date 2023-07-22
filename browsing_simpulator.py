import random
browsing = []

while True:
    search = input("search something (insert del to delete the search, insert clear to delete all): ")
    
    if search.lower() == "del":
        if browsing:
            browsing.pop()
            print(f"your history : {', '.join(browsing)}")
        if not browsing:
            break
    elif search.lower() == "clear":
        if browsing:
            browsing.clear()
            print("cleaning history...")
        if not browsing:
            break
    else:
        print(f"searching: {search}")
        random_bool = bool(random.choice([True, False]))
        if random_bool:
            print("The answer to the question you searched for was True")
        else:  
            print("The answer to the question you searched for was false")
        browsing.append(search)
        print(f"your history : {', '.join(browsing)}")

print("your history is empty")
print("done")