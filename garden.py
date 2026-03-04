
if __name__ == '__main__':
    print('solid')
    for i in range(11): 
        for j in range(11):
             print('🌷', end='')
        print()

    print('horizontal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0:
                print('🌷', end='')
            else:
                print('🌱', end='')
        print('')

    print('vertical')
    for i in range(11):
        for j in range(11):
            if j % 2 == 0:
                 print('🌷', end='')
            else:
                 print('🌱', end='')
        print('')

    print('diagnol')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0 and j % 2 == 0:
                print('🌷', end='')
            elif i % 2 == 1 and j % 2 == 1:
                print('🌷', end='')
            else:
                print('🌱', end='')     
        print('')

    print('plaid')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0 or j % 2 == 0:
                print('🌷', end='')   
            else:
                print('🌱', end='')  
        print('') 

    print('bonus')
    for i in range(11):
        for j in range(11):
            if i == j or i + j == 10:
                print('🌷', end='')  
            else:
                print('🌱', end='')  
        print('')