import numpy as np
X = input("")
if X == 'E':
    st = input()
    K =float(st.split(" ")[0])
    N = int(st.split(" ")[1])
    i = 0
    K2 = []
    P2 = []
    First_deriv = []
    Sec_deriv = []
    while i<N+1:
        st = input()
        try:
            temp_k =float(st.split("\t")[0])
            temp_p = float(st.split("\t")[1])
        except:
            temp_k =float(st.split(" ")[0])
            temp_p = float(st.split(" ")[1])
        K2.append(temp_k)
        P2.append(temp_p)
        i=i+1
    i = 1
    First_deriv.append(0)
    while i<N:
        x = (P2[i+1]-P2[i-1])/(K2[i+1]-K2[i-1])
        First_deriv.append(x)
        i=i+1
    First_deriv.append(1)
    i=1
    Sec_deriv.append(0)
    while i<N:
        if K<K2[i] and K>K2[i-1]:
            k=i
        x = (First_deriv[i+1]-First_deriv[i-1])/2
        Sec_deriv.append(x)
        i=i+1
    ans = 0
    
    while k<N-1:
        x = (K2[k]-K)*Sec_deriv[k]
        ans =ans+x
        #print(x)
        k=k+1
    print(ans)
    
if X == 'A':
    st = input()
    K =float(st.split(" ")[0])
    N = int(st.split(" ")[1])
    M = int(st.split(" ")[2])
    i = 0
    K2 = []
    P2 = []
    First_deriv = []
    Sec_deriv = []
    while i<N+1:
        st = input()
        try:
            temp_k =float(st.split("\t")[0])
            temp_p = float(st.split("\t")[1])
        except:
            temp_k =float(st.split(" ")[0])
            temp_p = float(st.split(" ")[1])
        K2.append(temp_k)
        P2.append(temp_p)
        i=i+1
    i = 1
    First_deriv.append(0)
    while i<N:
        x = (P2[i+1]-P2[i-1])/(K2[i+1]-K2[i-1])
        First_deriv.append(x)
        i=i+1
    First_deriv.append(1)
    i=1
    Sec_deriv.append(0)
    while i<N:
        if K<K2[i] and K>K2[i-1]:
            k=i
        x = (First_deriv[i+1]-First_deriv[i-1])/2
        Sec_deriv.append(x)
        i=i+1
    ans = 0
    i = 0
    K3 = []
    P3 = []
    First_deriv2 = []
    Sec_deriv2 = []
    while i<N+1:
        st = input()
        try:
            temp_k =float(st.split("\t")[0])
            temp_p = float(st.split("\t")[1])
        except:
            temp_k =float(st.split(" ")[0])
            temp_p = float(st.split(" ")[1])
        K3.append(temp_k)
        P3.append(temp_p)
        i=i+1
    i = 1
    First_deriv2.append(0)
    while i<N:
        x = (P3[i+1]-P3[i-1])/(K3[i+1]-K3[i-1])
        First_deriv2.append(x)
        i=i+1
    First_deriv2.append(1)
    i=1
    Sec_deriv2.append(0)
    while i<N:
        if K<K3[i] and K>K3[i-1]:
            k=i
        x = (First_deriv2[i+1]-First_deriv2[i-1])/2
        Sec_deriv2.append(x)
        i=i+1
    ans = 0
    
    copula = []
    i=0
    j=0
    while i<M+1:
        copula.append([])
        while j<N+1:
            copula[i].append(First_deriv[i]*First_deriv[j]/(1-0.95*(1-First_deriv[i])*(1-First_deriv2[i])))
            j=j+1
        i=i+1
    S = []
    i=0
    j=0
    ans = 0
    pdf = []
    while i <M+1:
        pdf.append([])
        while j<N+1:
            pdf[i].append(copula[i][j]*Sec_deriv[i]*Sec_deriv2[j])
            ans += (K2[i]+K3[i])*pdf[i][j]
            j=j+1
        i=i+1       
    ans = ans/2
    print(max(ans,0))
