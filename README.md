# TUGAS PBP
Nama: Naira Ammara Putri
Kelas: PBP B
NPM: 2406433112

## Tugas Individu 2 PBP - Implementasi Model-View-Template (MVT) pada Django
Nama Project : Realitea Club
Link PWS : https://naira-ammara-realiteaclub.pbp.cs.ui.ac.id/

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
   
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


**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
= <img width="1920" height="1080" alt="Bagan" src="https://github.com/user-attachments/assets/9b8a90cc-afc2-4117-8940-a7f99767087f" />


**3. Jelaskan peran settings.py dalam proyek Django!**

= settings.py adalah file konfigurasi utama pada proyek Django dan berisi pengaturan global yang mengontrol cara aplikasi berjalan.Contoh isi di dalam settings.py:

- DATABASES → konfigurasi database yang digunakan (SQLite, PostgreSQL, MySQL, dll).

- INSTALLED_APPS → daftar aplikasi yang aktif di dalam proyek.

- MIDDLEWARE → daftar middleware yang menangani request/response.

- TEMPLATES → pengaturan template engine (misalnya Jinja2 atau bawaan Django).

- STATICFILES_DIRS → lokasi file statis (CSS, JS, gambar).

- DEBUG, ALLOWED_HOSTS, SECRET_KEY → pengaturan keamanan & debugging. 

**4. Bagaimana cara kerja migrasi database di Django?**

= Migrasi database di Django digunakan untuk menyamakan struktur database dengan model Python (models.py). Cara kerjanya adalah sebagai berikut:

• Melakukan perubahan model di models.py.

• Menjalankan perintah python manage.py makemigrations. Nantinya, Django akan membaca perubahan model dan membuat file migrasi.

• Menjalankan python manage.py migrate. Dengan menjalankan command ini, Django akan mengeksekusi migrasi ke database & model akan tetap sinkron.

**5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

=  Beberapa alasan Django dijadikan permulaan pembelajaran pengembangan perangkat lunak, yaitu:

- Full-stack framework: Django menyediakan banyak fitur bawaan yang dapat membantu proses pembelajaran lebih mudah

- Konsep MVT (Model-View-Template) membantu memahami arsitektur aplikasi dengan rapi & membantu web developing lebih cepat

- Memiliki perlindungan mutakhir dan cryptographic hash

- Fleksibilitas Penggunaan

- Pengembangan dan Perawatannya Mudah

**6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**

= Menurut saya, penjelasan terkait tutorial 1 jelas, runtut, dan mudah dipahami. Dengan adanya tutorial 1, saya dengan lebih mudah mengerjakan tutorial 1 dan juga tugas individu 2. Tutorial 1 juga membantu saya memahami alur request-response dengan baik.


## Tugas Individu 3 PBP
**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
= Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery memungkinkan developers untuk mengirim data dari server ke client dengan cepat dan efisien. Selain itu, data delivery memungkinkan batching, caching, pagination, dan penggunaan message queue untuk menangani beban besar tanpa memblokir request sinkron.

Kemudian, data delivery menyediakan format terstandar (JSON, XML) agar pihak ketiga/layanan internal dapat mengonsumsi data dengan konsisten. Data delivery juga memisahkan penyajian data (API) dari rendering UI mempercepat development dan memungkinkan multiple clients (web, mobile).

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih popular dibandingkan XML?**
= Menurut saya, JSON lebih baik apabila dibandingkan dengan XML terutama saat saya mengerjakan tugas ke-3 PBP. Karena, dengan menggunakan JSON, menjadi lebih ringkas & ringan, lebih mudah dibaca manusia maupun mesin/computer, cepat diproses, dan sudah menjadi standar umum untuk pertukaran data pada web modern. Selain itu, JSON lebih fleksibel dibandingkan XML sehingga lebih banyak digunakan dalam pengembangan aplikasi saat ini.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
= Fungsi method is_valid() pada form Django adalah untuk menjalankan proses validasi form dan mengembalikan dalam bentuk True/False. Method is_valid() akan mengembalikan nilai True saat data yang di-input user valid dan mengembalikan nilai False saat data yang di-input tidak valid.

Mengapa dibutuhkan?
- Mencegah penyimpanan data invalid, seperti typo, tipe data yang salah, dan lain-lain.
- Menyediakan feedback error/menampilkan pesan error ke user melalui form.errors jika data yang dimasukkan tidak valid.

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
= CSRF (Cross-Site Request Forgery) adalah serangan yang memaksa browser user yang sudah authenticated untuk mengirim request berbahaya ke aplikasi target. csrf_token penting saat membuat form di Django karena token ini unik per sesi/form dan diverifikasi server, sehingga mencegah request yang datang dari situs lain (forged request).

Apabila kita tidak menambahkan csrf_token pada form Django, maka sangat besar kemungkinan terjadinya CSRF dan dapat membahayakan user yang sudah login melakukan aksi tanpa sadar, seperti mengubah password, menghapus data penting, dan lainnya. Oleh karena itu, penting bagi kita untuk selalu menambahkan csrf_token saat membuat form di Django agar data tersimpan dengan baik dan terhindar dari CSRF.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
= • Pada direktori templates, saya membuat berkas HTML baru Bernama base.html yang berfungsi sebagai template dasar yang dapat digunakn sebagai kerangka umum untuk halaman web lainnya di dalam proyek.
• Kemudian, pada settings.py di proyek realitea_club, pada bagian TEMPLATES saya menambahkan 'APP_DIRS': True,.
• Membuat forms.py pada direktori main dan membuat fungsi create_product agar bisa menambahkan produk.
• Selanjutnya, menambahkan fungsi show product berdasarkan product yang telah ditambahkan sebelumnya. Jika objek tidak ditemukan, akan mengembalikan halaman 404.
• Kemudian, pada urls.py/main, saya mengimport fungsi-fungsi yang sudah dibuat dan menambahkan path url ke dalam variable urlpatterns.
• Lalu, pada main/templates saya membuat 2 berkas HTML baru yaitu create_product.html dan product_detail.html. Pada create_product.html saya menambahkan {% csrf_token %} yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya.
• Pada settings.py saya menambahkan CSRF_TRUSTED_ORIGINS dan menambahkan url deployment pws kita.
• Kemudian pada views.py saya mengimport HttpResponse dan Serializer pada bagian paling atas.
• Selanjutnya, saya menambahkan fungsi baru yang menerima parameter request yaitu def show_xml(request) dan def show_json(request)
• Lalu, saya membuat 2 fungsi baru yang menerima parameter request dan product_id dengan nama show_xml_by_id dan show_json_by_id. Pada fungsi itu saya juga menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON). Saya juga menambahkan try except untuk mengantisipasi kondisi ketika data dengan news_id tertentu tidak ditemukan dalam basis data. 
• Terakhir, saya mengimport fungsi from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id da urls.py dan menambahkan pada urlpaterns untuk mengakses fungsi yang sudah di-import.

**6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
= Menurut saya, penyampaian materi oleh asisten dosen pada tutorial 2 sudah jelas dan runtut sehingga mudah dipahami. Selain itu, penjelasan pada tutorial 2 dilengkapi dengan contoh dan penjelasan sehingga pengerjaan tutorial 2 dapat dengan lebih mudah dikerjakan.

**7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman**
Screenshot Postman:
• XML 
<img width="1920" height="1080" alt="XMLPostman png" src="https://github.com/user-attachments/assets/458afa48-276a-47a8-9af5-b5e76cef13c7" />

• JSON 
<img width="1920" height="1080" alt="JSONPostman png" src="https://github.com/user-attachments/assets/57cbb0d3-ce7a-4c71-8f73-5c71eaf4d854" />

• XML ID
<img width="1920" height="1080" alt="XMLPK png" src="https://github.com/user-attachments/assets/e684ea70-769a-4546-92c3-44004100610b" />

• JSON ID
<img width="1920" height="1080" alt="JSONPK png" src="https://github.com/user-attachments/assets/2b276ae5-3d0e-4b69-b06e-892d64decce8" />


