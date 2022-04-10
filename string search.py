def search(string,key):
    
    return a.find(key)

n = int(input('Enter the number of elements - '))
key = input('Enter the key to be searched - ')

a = input()

ind = search(a,key)

if(ind != -1):
    print("The element is at index -",ind)
else:
    print("Not found")
    