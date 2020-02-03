import numpy as np
import random

#inisiasi dari semua variabel yang akan dibutuhkan
win_state = [14,14] #menginisiasi nilai yang menjadi goals
alfa = 1 #alfa di set bebas bisa juga disebut dengan learning rate
gamma = 0.9 #gamma di set bebas bisa juga disebut dengan discount rate

#menginisiasi seluruh nilai q awal yakni dengan menginisiasi dengan 0
def initial_q():
    q_matrix = [[0 for i in range(4)] for j in range(225)]
    return q_matrix

#menyimpan seluruh nilai dengan merepresntasikan indeks ke dalam array indeks agar bisa membuat bentuk q 225 x 4 arah
#bertujuan untuk dapat mengetahui baris dan kolom mana yang akan diperlukan untuk dijadikan current state dan next state
indeks = []
def indexing_data(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            a = [i,j]
            indeks.append(a)

#fungsi aksi berguna untuk dapat meneetahui arah dari masing-masing nilai di dalam kotak dan beserta menampung apabila arah tersebut memiliki isi akan dimasukkan dengan nilai dan apabila tidak akan dimasukkan dengan None
def aksi(current_state, data):
    heading = []
    #tahap pertama menguji pada bagian atas
    if (current_state[0] == 0 ):
        heading.append(None)
        heading.append(data[current_state[0]+1][current_state[1]])
    #tahap kedua menguji pada bagian bawah
    else:
        heading.append(data[current_state[0]-1][current_state[1]])
        if(current_state[0] == (14)):
            heading.append(None)
        else:
            heading.append(data[current_state[0]+1][current_state[1]])
    #tahap ketiga menguji pada bagian kiri
    if (current_state[1] == 0 ):
        heading.append(None)
        heading.append(data[current_state[0]][current_state[1]+1])
    else:
    #tahap keempat menguji pada bagian kanan
        heading.append(data[current_state[0]][current_state[1]-1])
        if(current_state[1] == (14)):
            heading.append(None)
        else:
            heading.append(data[current_state[0]][current_state[1]+1])
    return heading

#petpindahan state untuk dapat mengetahui aksi yang diperlukan ketika akan berpindah dengan menambahkan dan mengurangi nilai berdasarkan indeks
def perpindahan_state(aksi_sekarang, simpan_angka_baru):
    pindah_state = aksi_sekarang
    #indeks pertama atau ke 0
    if (simpan_angka_baru == 0):
        pindah_state[0] -= 1
    #indeks kedua atau ke 1
    elif (simpan_angka_baru == 1):
        pindah_state[0] += 1
    #indeks ketiga atau ke 2
    elif (simpan_angka_baru == 2):
        pindah_state[1] -= 1
    #indeks keempat atau ke 3
    elif (simpan_angka_baru == 3):
        pindah_state[1] += 1
    return pindah_state

#menghitung keseluruhan jumlah dari reward yang dihasilkan per episode
yuk_disimpan = []
def jum_reward(indeks, intial_q_l):
    #menginisiasi current state dengan start awal
    current_state = [0,0]
    #menginisiasi nilai reward dari indeks current state
    reward = data[current_state[0]][current_state[1]]
    print(reward)
    #melakukan pengecekan apabila current belum sampai dari tujuan maka dilakukan terus perulangan hingga bertemu dengan tujuan
    while current_state != win_state:
        #mengembalikan nilai indeks pada current state
        state_q = indeks.index(current_state)
        #mengambil nilai maksimum yang akan merepresentasikan sebuah arah dari satu data tersebut
        maksimum = max(intial_q_l[state_q])
        indeks_maksimum = intial_q_l[state_q].index(maksimum)
        #apabila indeks_maksimum = 0 maka akan menyatakan arah ke atas
        if indeks_maksimum == 0:
            current_state[0] -= 1
            reward = reward + data[current_state[0]][current_state[1]]
            simpan = ('reward: ', reward, 'ke kanan: ', current_state)
            print('reward: ', reward, 'keatas: ', current_state)
        #apabila indeks_maksimum = 1 maka akan menyatakan arah ke bawah
        elif indeks_maksimum == 1:
            current_state[0] += 1
            reward = reward + data[current_state[0]][current_state[1]]
            simpan = ('reward: ', reward, 'ke kanan: ', current_state)
            print('reward: ', reward, 'ke bawah: ', current_state)
        #apabila indeks_maksimum = 2 maka akan menyatakan arah ke kiri
        elif indeks_maksimum == 2:
            current_state[1] -= 1
            reward = reward + data[current_state[0]][current_state[1]]
            simpan = ('reward: ', reward, 'ke kanan: ', current_state)
            print('reward: ', reward, 'ke kiri: ', current_state)
        #apabila indeks_maksimum = 3 maka akan menyatakan arah ke kanan
        elif indeks_maksimum == 3:
            current_state[1] += 1
            reward = reward + data[current_state[0]][current_state[1]]
            simpan = ('reward: ', reward, 'ke kanan: ', current_state)
            print('reward: ', reward, 'ke kanan: ', current_state)
        yuk_disimpan.append(simpan)

if __name__ == '__main__':
    #membaca file DataTugas3ML2019.txt dan mentranspose nilai tersebut
    data = np.loadtxt('DataTugas3ML2019.txt', usecols=range(15)).astype(int) [::-1]
    print(data)

    #membuat tabel yang akan merepresentasikan 15x15x4
    indexing_data(data)
    print(indeks)

    #menginisialisasi q dengan 0
    intial_q_l = []
    intial_q_l = initial_q()
    print(intial_q_l)

    #melakukan sebanyak 1000 untuk mencari optimum nilai optimum tidak harus konstan 1000 dapat diubah apabila diperlukan
    for x in range(0,2012):
        #melakukan random untuk mengetahui nilai acak dengan range 0-14 atau 1-15
        current_state = [random.randint(0,14), random.randint(0,14)]
        # print(current_state)
        # current_state = [1,0]
        # y = aksi(current_state, data)
        # print(current_state)
        # print(y)
        # melakukan pengecekan apabila current belum sampai dari tujuan maka dilakukan terus perulangan hingga bertemu dengan tujuan
        while current_state != win_state:
            #menyimpan state_q dengan mengembalikan indeks pada current state yang berisi nilai random
            state_q = indeks.index(current_state)
            #menyimpan isi value dari indeks state_q
            temp = indeks[state_q]
            # print(state_q)
            # print(temp)
            #mengetahui aksi dari current state
            y = aksi(current_state, data)
            # print(y)
            #melakukan random untuk mengetahui arah yang akan membantu untuk mengetahui arah mana yang akan diambil dengan mencoba mencari nilai acak
            simpan_angka_baru = random.randint(0,3)
            #melakukan pengecekan hingga next tidak bernilai None
            while y[simpan_angka_baru] == None:
                simpan_angka_baru = random.randint(0,3)
            # print(simpan_angka_baru)
            #menentukan nilai next state selanjutnya
            next_state = perpindahan_state(current_state, simpan_angka_baru)
            # print(next_state)
            #next q menyimpan indeks dari next state
            next_q = indeks.index(next_state)
            #mengupdate nilai q dengan rumus yang disesuaikan dengan isi slide
            intial_q_l[state_q][simpan_angka_baru] = intial_q_l[state_q][simpan_angka_baru] + alfa * (data[next_state[0]][next_state[1]] + gamma * max(intial_q_l[next_q]) - intial_q_l[state_q][simpan_angka_baru])
   # mencetak hasil akhir dari q yang sudah diupdate
    print(intial_q_l)
    #menghitung berapa banyak reward dan juga mengetahui episode terbaik
    jum_reward(indeks, intial_q_l)
    #hasil akhir
    print(yuk_disimpan)
    # np.savetxt('hasil.csv', delimiter=',')
