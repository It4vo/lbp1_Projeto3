

print("Digite a ordem n da matriz:")
n = int(input())

if n < 2:
    print("Ordem inválida. A matriz deve ser de ordem >= 2.")
else:
    matriz = []
    i = 0
    while i < n:
        print(f"Digite os n valores da linha {i+1}, separados por espaço:")
        partes = input().split()
        if len(partes) != n:
            print(f"Erro: você digitou {len(partes)} valores. A linha deve conter exatamente n valores.")
            continue
        linha = []
        ok = True
        for p in partes:
            try:
                linha.append(int(p))
            except ValueError:
                print("Erro: digite apenas números inteiros.")
                ok = False
                break
        if not ok:
            continue
        matriz.append(linha)
        i += 1

    def det2(m):
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    def det3(m):
        d1 = m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
        d2 = m[0][2]*m[1][1]*m[2][0] + m[0][0]*m[1][2]*m[2][1] + m[0][1]*m[1][0]*m[2][2]
        return d1 - d2

    def submatriz(m, linha_remover, coluna_remover):
        nova = []
        for i in range(len(m)):
            if i == linha_remover:
                continue
            linha = []
            for j in range(len(m)):
                if j == coluna_remover:
                    continue
                linha.append(m[i][j])
            nova.append(linha)
        return nova

    def laplace(m):
        ordem = len(m)
        if ordem == 2:
            return det2(m)
        elif ordem == 3:
            return det3(m)
        else:
            soma = 0
            for j in range(ordem):
                cofator = ((-1) ** j) * m[0][j] * laplace(submatriz(m, 0, j))
                soma += cofator
            return soma

    det = laplace(matriz)
    print(f"ordem={n}")
    print(f"det={det}")



