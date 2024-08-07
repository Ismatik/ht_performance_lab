#Task 1. m - длина обхода/разделение. 
#n - круговой массив от 1 до n


def task_one(m , n):
    array = ""
    for i in range(1, m+1):
        array += str(i)
    
    k = array[:n]
    options = []
    while k[-1] != 1:
        options.append(k)
        k = array[n-1:] + array[:(m-n)+1]
        print(options)





if __name__ == '__main__':
    numbers = input("").split(" ")
    n,m = int(numbers[0]) , int(numbers[1])
    task_one(n, m)
