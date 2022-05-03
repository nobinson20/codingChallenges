if __name__ == '__main__':
    arr = [1,2,3,4,5,'a']
    removeset = {1, 'a'}

    result = [e for e in arr if e not in removeset]

    print(result)
