# list is a data structure which can hold multiple values of multiple type
#array is a data structure which can hold multiple values of same type

list_of_cloud = ["aws","azure","gcp","alibaba","oracle"]

print(list_of_cloud)

# add new cloud
list_of_cloud.append("sales force") # adds to the end

print(list_of_cloud)

list_of_cloud.insert(3,"mcloud")
print(list_of_cloud)

# iteration of list
for cloud in list_of_cloud:
    print(cloud)
