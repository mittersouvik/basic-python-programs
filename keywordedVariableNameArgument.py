def person(name, **data): # data is of dict type
    print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)




person("Souvik", age = 23, city = "Kolkata", mob = 9874192013)
