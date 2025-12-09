# for i in range(5):
#     print(i+1, "iteration completed")
#     print("Hello, World!")
    
for i in range(1, 6):
    print(f"{i} iteration completed")
    if i == 3:
        # break
        print("This will not be printed when i is 3")
        continue
        
    print("Hello, World!")