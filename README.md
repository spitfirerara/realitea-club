Tugas Individu 2 PBP - Implementasi Model-View-Template (MVT) pada Django
Nama Project : Realitea Club
Link PWS : https://naira-ammara-realiteaclub.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
• Pertama-tama, saya membuat direktori bernama "realitea-club". Lalu, pada direktori tersebut, saya membuat/mengaktifkan virtual environment melalui terminal.

• Kemudian pada direktori yang sama, saya membentuk berkas requirements.txt dan menambahkan beberapa dependencies & melakukan instalasi terhadap dependencies.

• Selanjutnya, saya membuat proyek Django bernama realitea_club dengan command django-admin startproject realitea_club .

• Setelah proyek Django terbentuk, saya membuat aplikasi main dalam proyek realitea-club, dengan menjalankan python manage.py startapp main. Nantinya ini akan digunakan sebagai inti aplikasi.

• Setelah aplikasi main terbentuk, saya mendaftarkan aplikasi main ke dalam daftar aplikasi (INSTALLED_APPS) yang terdapat di dalam berkas settings.py (direktori proyek realitea_club).
  INSTALLED_APPS = [
      ...,
      'main'
  ]

• Lalu, pada direktori main, kita akan menambahkan direktori templates. Pada direktori templates, saya membuat berkas main.html

• Kemudian, saya akan membuat model pada aplikasi main dengan nama "Product" dan memiliki atribut sebagai berikut:
  - name sebagai nama item dengan tipe CharField.
  - price sebagai harga item dengan tipe IntegerField.
  - description sebagai deskripsi item dengan tipe TextField.
  - thumbnail sebagai gambar item dengan tipe URLField.
  - category sebagai kategori item dengan tipe CharField.
  - is_featured sebagai status unggulan item dengan tipe BooleanField.

• Membuat migrasi model dan menerapkan migrasi ke dalam database dengan kau command python manage.py makemigrations dan python manage.py migrate

• Membuat sebuah fungsi pada views.py yaitu show_main yang akan mengembalikan template main.html yang berisi nama toko, npm, nama, dan kelas.

• Setelah itu, saya memodifikasi template html agar dapat menampilkan data yang telah diambil dari "Product"

• Saya membuat berkas urls.py pada aplikasi main dan mendefinisikan path yang mengarah ke fungsi show_main. Selanjutnya, saya mendaftarkan main/urls.py agar terhubung dengan realiteaclub/urls.py.

• Kemudian, saya me-run server dengan menjalankan command `python manage.py runserver. Melalui hal ini, saya bisa mengecek bahwa halaman bisa diakses melalui browser.

• Selanjutnya, saya membentuk unit test dengan membuat file "test.py". Test ini berfungsi untuk memastikan bahwa URL Utama bisa diakses dan data yang ingin ditampilkan muncul di browser.

• Terakhir, proyek Django yang telah berhasil dibentuk saya push ke repository GitHub dan saya deploy ke PWS agar nantinya bisa diakses secara public melalui internet.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
= <img width="1920" height="1080" alt="Bagan" src="https://github.com/user-attachments/assets/9b8a90cc-afc2-4117-8940-a7f99767087f" />


3. Jelaskan peran settings.py dalam proyek Django!

= settings.py adalah file konfigurasi utama pada proyek Django dan berisi pengaturan global yang mengontrol cara aplikasi berjalan.Contoh isi di dalam settings.py:

- DATABASES → konfigurasi database yang digunakan (SQLite, PostgreSQL, MySQL, dll).

- INSTALLED_APPS → daftar aplikasi yang aktif di dalam proyek.

- MIDDLEWARE → daftar middleware yang menangani request/response.

- TEMPLATES → pengaturan template engine (misalnya Jinja2 atau bawaan Django).

- STATICFILES_DIRS → lokasi file statis (CSS, JS, gambar).

- DEBUG, ALLOWED_HOSTS, SECRET_KEY → pengaturan keamanan & debugging. 

4. Bagaimana cara kerja migrasi database di Django? 

= Migrasi database di Django digunakan untuk menyamakan struktur database dengan model Python (models.py). Cara kerjanya adalah sebagai berikut:

• Melakukan perubahan model di models.py.

• Menjalankan perintah python manage.py makemigrations. Nantinya, Django akan membaca perubahan model dan membuat file migrasi.

• Menjalankan python manage.py migrate. Dengan menjalankan command ini, Django akan mengeksekusi migrasi ke database & model akan tetap sinkron.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

=  Beberapa alasan Django dijadikan permulaan pembelajaran pengembangan perangkat lunak, yaitu:

- Full-stack framework: Django menyediakan banyak fitur bawaan yang dapat membantu proses pembelajaran lebih mudah

- Konsep MVT (Model-View-Template) membantu memahami arsitektur aplikasi dengan rapi & membantu web developing lebih cepat

- Memiliki perlindungan mutakhir dan cryptographic hash

- Fleksibilitas Penggunaan

- Pengembangan dan Perawatannya Mudah

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

= Menurut saya, penjelasan terkait tutorial 1 jelas, runtut, dan mudah dipahami. Dengan adanya tutorial 1, saya dengan lebih mudah mengerjakan tutorial 1 dan juga tugas individu 2. Tutorial 1 juga membantu saya memahami alur request-response dengan baik.

