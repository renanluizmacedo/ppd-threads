import threading

def imprime(vet,res):
    #print(f"Thread {threading.current_thread().name}")
    for i in range(len(vet)):
        if ((i % 2 == res)):
            print(f'vet[{i}]={vet[i]}')


if __name__ == '__main__':
    
    vet = [1,2,3,4,5,6,7,8,9,10]
    print('Posições Pares')
    thread1 = threading.Thread(target=imprime,args=(vet,0))
    print('Posições Impares')
    thread2 = threading.Thread(target=imprime,args=(vet,1))

    thread1.start()
    thread2.start()
    

    