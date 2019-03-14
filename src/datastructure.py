L = [123, 'spam', 1.23]
# print(len(L))
# print(L[0])
# print(L[:-1])
# print(L + [4, 5, 6])
# print(L)

L.append('NI')
# print(L)
L.pop(2)
# print(L)

M = ['bb', 'aa', 'cc']
M.sort()
# print(M)
M.reverse()
# print(M)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(M)
# print(M[1])
# print(M[1][2])

col2 = [row[1] for row in M]
# print(col2)
# print([row[1] + 1 for row in M])
# print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]]
# print(diag)

doubles = [c * 2 for c in 'spam']
# print(doubles)

G = (sum(row) for row in M)
# print(next(G))
# print(next(G))

# print(list(map(sum, M)))
# print({sum(row) for row in M})
# print({i : sum(M[i]) for i in range(3)})


# print([ord(x) for x in 'spaam'])
# print({ord(x) for x in 'spaam'})
# print({x:ord(x) for x in 'spaam'})

D = {'food':'Spam', 'quantity':4, 'color':'pink'}
print(D['food'])
D['quantity'] += 1
print (D)