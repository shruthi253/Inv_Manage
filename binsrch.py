pos = -1
def search(list,n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u)//2
        if n == list[mid]:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
                
if search([1,2,3,4,5,5,6,6],6) :
    print('Found at', pos+1 )
else:
    print('Not Found')