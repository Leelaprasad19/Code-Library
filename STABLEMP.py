def function(preferencesOfMen,preferencesOfWomen,n):

    # -1 For all unmarried men and women
    marriedMen = [-1 for i in range(n)]
    marriedWomen = [-1 for i in range(n)]

    # While any women is free
    while -1 in marriedWomen:

        # Traverse men
        for i in range(n):
            
            # If any unmarried man found
            if marriedMen[i] == -1:

                # Check his first preference
                preffered = preferencesOfMen[i][0] - 1

                # Remove his first preference
                preferencesOfMen[i].pop(0)

                # If top preffered women is unmarrried
                if marriedWomen[preffered] == -1:

                    # Assign the man to the woman he prefers  
                    marriedWomen[preffered] = i
                    marriedMen[i] = preffered

                # Else if that preffered women is already asiigned to that man 
                else:

                    # Get the man whom the woman is already assigned to
                    marriedPerson = marriedWomen[preffered]

                    # Get the preferences of both married and proposed man
                    proposedManPreference = preferencesOfWomen[preffered].index(i+1)
                    marriedManPreference = preferencesOfWomen[preffered].index(marriedPerson+1)
                    
                    # If the index of newly proposed man is less than the index of man already assigned to the women 
                    
                    if proposedManPreference < marriedManPreference:
                        
                        # Replace proposed by married
                        marriedWomen[preffered] = i
                        marriedMen[i] = preffered

                        # Make the already amrried person to unmarried
                        marriedMen[marriedPerson] = -1
    

    for i in range(n):

        # Printing Final matches of women with men
        print(i+1," ",marriedMen[i]+1)


t = int(input())
for i in range(t):
    n = int(input())

    preferencesOfMen = []
    preferencesOfWomen = []

    men = []
    women = []

    for i in range(n):
        temp = list(map(int,input().split()))
        women.append(temp.pop(0))
        preferencesOfWomen.append(temp)

    for i in range(n):
        temp = list(map(int,input().split()))
        men.append(temp.pop(0))
        preferencesOfMen.append(temp)

    function(preferencesOfMen,preferencesOfWomen,n)
    