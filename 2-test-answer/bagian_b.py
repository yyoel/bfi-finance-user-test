def exercise_1():
    """
    ----------- Exercise 1 -----------
    Q: Tampilkan output seperti di bawah ini

    Output:
    ['"Budi makan ayam"', '"Budi makan bakso"', '"Budi makan sate"', '"Anto makan ayam"', '"Anto makan bakso"', '"Anto makan sate"']

    nama = ["Budi" , "Anto"]
    makanan = ["ayam", "bakso", "sate"]
    """

    nama = ["Budi" , "Anto"]
    makanan = ["ayam", "bakso", "sate"]

    output = []
    
    for n in nama:
        for m in makanan:
            word = '"' + n + " makan " + m + '"'
            output.append(word)
    print(output) 

def exercise_2():
    """
    ----------- Exercise 2 -----------
    Q: Buatlah program untuk mengetahui elemen yang paling sering muncul.

    angka = [22, 32, 42, 52, 22, 72, 22, 42, 72, 22]

    """

    angka = [22, 32, 42, 52, 22, 72, 22, 42, 72, 22]
    dict_angka_count = {}
    for a in angka:
        if a not in dict_angka_count:
            dict_angka_count[a] = 1
        else:
            dict_angka_count[a] += 1

    sorted_angka = sorted(dict_angka_count.items(), key=lambda x:x[1], reverse=True)
    
    print(sorted_angka[0][0], sorted_angka[0][1])

def exercise_3():
    """
    ----------- Exercise 3 -----------
    Q: Buatlah program untuk mengetahui siapa yang memiliki nilai paling tinggi dan paling rendah.

    data = {"Anton":70, "Pande": 100, "Malik": 83, "Roni": 99}

    """

    data = {"Anton":70, "Pande": 100, "Malik": 83, "Roni": 99}

    sorted_nilai = sorted(data.items(), key=lambda x:x[1], reverse=True)
    
    print(sorted_nilai[0][0], sorted_nilai[0][1])
def exercise_4():
    """
    ----------- Exercise 4 -----------
    Q: Tampilkan output seperti di bawah ini

    bahasa = ['Python', 'Java', 'Scala', 'Go']
    Output:
    0 Python
    1 Java
    2 Scala
    3 Go
    """
    bahasa = ['Python', 'Java', 'Scala', 'Go']

    for i, b in enumerate(bahasa):
        print(i, b)

def exercise_5():
    """
    ----------- Exercise 5 -----------
    Q: Ubah dari tipe list menjadi string

    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    """
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

    output = '-'.join(weekdays)
    print(output)

def exercise_6():
    """
    ----------- Exercise 6 -----------
    data_kasus = [
    {"Kota":"Bandung","Jumlah_Kasus":5300,"Kasus_Sembuh":2839,"Kasus_Meninggal":2461},
    {"Kota":"Tegal","Jumlah_Kasus":4910,"Kasus_Sembuh":3940,"Kasus_Meninggal":970},
    {"Kota":"Balikpapan","Jumlah_Kasus":1319,"Kasus_Sembuh":918,"Kasus_Meninggal":401},
    {"Kota":"Sibolga","Jumlah_Kasus":2319,"Kasus_Sembuh":974,"Kasus_Meninggal":1345},
    {"Kota":"Binjai","Jumlah_Kasus":1311,"Kasus_Sembuh":521,"Kasus_Meninggal":790},
    {"Kota":"Probolinggo","Jumlah_Kasus":3483,"Kasus_Sembuh":3193,"Kasus_Meninggal":238},
    {"Kota":"Depok","Jumlah_Kasus":1991,"Kasus_Sembuh":1413,"Kasus_Meninggal":578},
    {"Kota":"Magelang","Jumlah_Kasus":3381,"Kasus_Sembuh":3112,"Kasus_Meninggal":269},
    {"Kota":"Samarinda","Jumlah_Kasus":3991,"Kasus_Sembuh":2810,"Kasus_Meninggal":1311},
    {"Kota":"Batam","Jumlah_Kasus":2647,"Kasus_Sembuh":2344,"Kasus_Meninggal":303},
    {"Kota":"Medan","Jumlah_Kasus":4410,"Kasus_Sembuh":3344,"Kasus_Meninggal":1066}
    ]

    provinsi = {"Jawa Barat": ["Bandung","Depok"], "Jawa Tengah":["Tegal","Magelang"], "Sumatera Utara":["Sibolga","Binjai"], "Jawa Timur":["Probolinggo"],"Kalimantan Timur" : ["Balikpapan"]}

    Q:
    1.	Ubah ke dataframe dan lakukan EDA (Kasus_Sembuh + Kasus_Meninggal = Jumlah_Kasus)
    2.	Dengan menggunakan fungsi, buatlah kolom provinsi berdasarkan daftar provinsi di atas
    3.	Tampilkan provinsi yang persentase kesembuhannya paling tinggi ke rendah
    4.	Berapa rata2 tingkat kesembuhan provinsi Jawa Barat & Sumatera Utara
    """
    import pandas as pd

    # Membuat dataframe dari data_kasus
    df = pd.DataFrame(data_kasus)

    #2. Menambahkan kolom Provinsi berdasarkan daftar provinsi
    df['Provinsi'] = df['Kota'].map({k: prov for prov, kota_list in provinsi.items() for k in kota_list})

    # Menghitung Jumlah_Kasus baru berdasarkan Kasus_Sembuh dan Kasus_Meninggal
    df['Jumlah_Kasus_Baru'] = df['Kasus_Sembuh'] + df['Kasus_Meninggal']

    # 1.EDA: Menampilkan data kasus
    print("Data Kasus:")
    print(df)

    # Mengurutkan data berdasarkan persentase kesembuhan
    df['Persentase_Kesembuhan'] = df['Kasus_Sembuh'] / df['Jumlah_Kasus_Baru']
    sorted_df = df.sort_values('Persentase_Kesembuhan', ascending=False)

    #3. Menampilkan provinsi yang persentase kesembuhannya paling tinggi ke rendah
    print("\nProvinsi dengan persentase kesembuhan tertinggi ke terendah:")
    print(sorted_df[['Provinsi', 'Persentase_Kesembuhan']])

    #4. Menghitung rata-rata tingkat kesembuhan provinsi Jawa Barat dan Sumatera Utara
    average_jabar = df[df['Provinsi'] == 'Jawa Barat']['Persentase_Kesembuhan'].mean()
    average_sumut = df[df['Provinsi'] == 'Sumatera Utara']['Persentase_Kesembuhan'].mean()

    print("\nRata-rata tingkat kesembuhan:")
    print("Jawa Barat:", average_jabar)
    print("Sumatera Utara:", average_sumut)


def exercise_7(angka):
    """
    ----------- Exercise 7 -----------
    Q: Buatlah program untuk membentuk output di bawah ini

    Misalnya angka = 5 maka output seperti ini
    1****
    12***
    123**
    1234*
    12345

    Misalnya angka = 7 maka output seperti ini
    1******
    12*****
    123****
    1234***
    12345**
    123456*
    1234567
    """
    for i in range(1, angka + 1):
        pattern = ''.join(str(j) for j in range(1, i + 1))
        stars = '*' * (angka - i)
        print(pattern + stars)

def main():
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7(9)

if __name__ == "__main__":
    main()