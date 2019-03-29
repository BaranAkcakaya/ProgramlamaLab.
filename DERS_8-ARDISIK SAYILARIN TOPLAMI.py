#ARDISIK SAYILARIN TOPLAMININ EN BUYUGUNU YAZDIR.

liste=[-4,-3,-2,-1,21,22,-2,-6,-5]
def max_sequential (liste):
    maxSum = liste[0]
    maxSumIndexs = []
    for i in range (len(liste)):
        sum_n=0
        for j in range (i,len(liste)):
            sum_n += liste[j]
            if maxSum < sum_n :
                maxSum = sum_n
    return maxSum
print("ARDISIK SAYILARIN TOPLAMININ EN BUYUGU :"+str(max_sequential(liste)))
