def segitiga(n):
    if(n == 1):
        return ""
    if(n == input_num):
        return "*\n"
    pola = ""
    for i in range(1, n+1):
        pola += "*" * i + "\n"
    return pola

def pola(input_num):
    hasil = ""
    for i in range(1, input_num+1):
        hasil += segitiga(i)
    return hasil
input_num = int(input("Masukkan angka: "))
print(pola(input_num))