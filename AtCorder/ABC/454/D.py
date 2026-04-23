def F(S):
    st = []
    for i in S:
        st.append(i)
        while True:
            n = len(st)
            if n >= 4 and st[-4] == '(' and st[-3] == 'x' and st[-2] == 'x' and st[-1] == ')':
                st.pop()
                st.pop()
                st.pop()
                st.pop()
                st.append('x')
                st.append('x')
            else:
                break
    return st
for _ in range(int(input())):
    A = list(input())
    B = list(input())
    print("Yes" if F(A) == F(B) else "No")
