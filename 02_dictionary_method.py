myDict={
"fast":"In a Quick Manner",
"harry": "A Coder",
"marks": [1, 2, 5],
"anotherdict": {'harry':'Player'},
}

#Dictionary Methods
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values()) #Print the keys of the dictionary
print(myDict.items()) #Prints the keys of the dictionarys
print(myDict)
updateDict = {
    "LOvish": "Friend",
    "Divya":"Friend",
    "Shubham":"Friend"
}
myDict.update(updateDict) #Update the dictionary by adding key-value pairs from updateDict
print(myDict)