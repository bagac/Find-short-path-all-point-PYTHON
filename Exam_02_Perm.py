def Permutation(data, k=0):
    if k == len(data):
        print(data)
    else:
        for i in range(k, len(data)):
            data[k], data[i] = data[i], data[k]
            Permutation(data, k + 1)
            data[k], data[i] = data[i], data[k]
if __name__ == '__main__':
    Data = ['a', 'b', 'c', 'd']
    print(f'với tập dữ liệu {Data} Ta có thể hoán vị như sau: ')
    Permutation(data= Data)