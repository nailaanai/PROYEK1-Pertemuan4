
phonebook = {}

def buatFile():
    with open("phonebook.txt","w") as file:
        pass
    file.close()

def insert(nama, nohp):    #untuk menambah kontak
    
    with open("phonebook.txt","a") as file:
        file.write(f"{nama} {nohp}\n")
    phonebook[nama] = nohp

def display():
    with open("phonebook.txt","r") as file:
        lines = file.read()
     
    if not lines:
        print("Buku Telepon kosong.")
    else:
        print(lines)
    file.close()

def findContact(nama):
    with open("phonebook.txt","r") as file:
        Isi = file.readlines()
        found = False
        for line in Isi:
            if nama in line:
             print("Ada")
             temp = line.split(" ")
             print("Nama : "+temp[0]+"\nNomor : "+temp[1][:-1])
             found = True
             break
        else:
            print(f"{nama} Tidak Ada dalam Daftar.")
    file.close()

def hapus(nama):
    with open("phonebook.txt","r") as file:
        lines = file.readlines()
    with open("phonebook.txt","w") as file:
        for line in lines:
            if line.split()[0] != nama:
                file.write(line)
    file.close()

def updateContact():
    nama = input("\nMasukkan Nama yang Akan Diupdate: ")
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()
    updated_lines = []
    found = False
    for line in lines:
        if nama in line:
            found = True
            nomor = input("Masukkan Nomor yang Baru: ")
            updated_lines.append(f"{nama} {nomor}\n")
        else:
            updated_lines.append(line)
    if not found:
        print(f"Kontak dengan nama {nama} tidak ditemukan")
        return
    with open("phonebook.txt", "w") as file:
        file.writelines(updated_lines)
    print(f"Kontak {nama} berhasil diperbarui")

def main():
    print("=============================")
    print("\t PHONE BOOK")
    print("=============================")

    print("1. Menambah Kontak")
    print("2. Menghapus Kontak")
    print("3. Mencari Kontak")
    print("4. Menampilkan Semua Kontak")
    print("5. Edit Kontak\n")

    i = -1
    while i != 0:
        i = int(input("Ketik Angka 1-5 : "))
        if i == 1:  #input
            name = input("\nNama :")
            number = input("No. HP : ")
            insert(name,number)
        elif i == 2:    #delete
            name = input("\nKetik Nama : ")
            hapus(name)
        elif i == 3:    #carikontak
            name = input("\nKetik Nama : ")
            findContact(name)
        elif i == 4:
            display()
        elif i == 5:
            updateContact()
            break
        elif (input("Keluar? y/n: ") !='y'):
            main()

if __name__ == "__main__":
    main()
