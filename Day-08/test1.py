# list

# list1 = ["raman", "sati", "kumar"]
# list2 = [1, 2, 3, 4, 5] 
# combined_list = list1 + list2
# print("Combined List:", combined_list)



# s3_buckets = ["bucket1", "bucket2", "bucket3"]
# for bucket in s3_buckets:
#     print(f"Creating S3 bucket: {bucket}")
    
    
# tuples - > list are mutable whereas tuples are immutable

# tuple1 = ("apple", "banana", "cherry")
# # tuple1[1] = "orange"  # This will raise a TypeError
# print(tuple1)

list_example = [10, 20, 30, 40, 50]
# Accessing elements
print("Original List:", list_example)
first_element = list_example[0]
print("First Element:", first_element)

list_example[2] = 35

print(first_element+ list_example[2])
print("Modified List:", list_example)
