from memory_store import add_memory, find_memory

choice = input("Do you want to add a memory or find a memory? (add/find): ")
if choice == "add":
    memory = input("Enter your memory:")
    add_memory(memory)
elif choice == "find":
    query = input("Enter your query:")
    results = find_memory(query)
    print(results)
else:
    print("Sorry I couldn't understand that, please type 'add' or 'find'")