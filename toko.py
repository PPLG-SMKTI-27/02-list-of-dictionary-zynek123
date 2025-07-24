def bersih():
   import os
   os.system('cls' if os.name == 'nt' else 'clear')   

#dictionary
barang1={"nama": "Polibag","stock": "20","harga":3500}
barang2={"nama": "Topsoil","stock": "15", "harga":20000}
barang3={"nama": "Pupuk","stock": "25", "harga" : 4500}
barang4={"nama": "Bibit","stock": "30", "harga":7500}
barang5={"nama": "Jangkrik","stock": "40", "harga" : 6500}



#list of dictionary
barang= [barang1,barang2,barang3,barang4,barang5]
print(barang)

#crud read
print("no\tnama\tsock\tharga")
for i in range(len(barang)):
    print(i+1,"\t",barang[i]["nama"],"\t",barang[i]["stock"],"\t",barang[i]["harga"])
    print("nama\tstock\tharga")
    for s in barang:
        print(s["nama"], "\t", s["stock"], "\t", s["harga"])


#crud create
nama = str(input("Masukkan barang yang mau di beli:"))
stock = int(input("Masukkan jumlah stock:"))
harga = int(input("Masukkan harga:"))
barang6 = {"nama":nama,"stock":stock,"harga":harga}
barang.append(barang6)
print(barang6)



