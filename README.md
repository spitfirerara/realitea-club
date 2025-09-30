# TUGAS INDIVIDU PBP
Nama: Naira Ammara Putri

Kelas: PBP B

NPM: 2406433112

Nama Project : Realitea Club

Link PWS : https://naira-ammara-realiteaclub.pbp.cs.ui.ac.id/

---

## Tugas Individu 2 PBP - Implementasi Model-View-Template (MVT) pada Django

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

---

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

--- 

## Tugas Individu 4 PBP - Implementasi Autentikasi, Session, dan Cookies pada Django

**1.	Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya**
= ``AuthenticationForm`` adalah form bawaan Django yang digunakan untuk melakukan proses login user. Form ini otomatis menyediakan field username dan password, serta menangani validasi login (misal, apakah username ada di database, password yang dimasukkan sesuai, dan lain-lain).

⦁	Kelebihan:

      ⦁	Praktis & Cepat → tidak perlu membuat form login dari nol
   
      ⦁	Terintegrasi dengan sistem auth Django → langsung bekerja dengan ``authenticate()`` dan ``login()``.
   
      ⦁	Aman secara default → sudah menggunakan mekanisme hashing password bawaan Django.
   
      ⦁	Menangani validasi otomatis → misalnya jika password salah atau akun tidak ada, error akan muncul di form.

⦁	Kekurangan:

      ⦁	Kurang fleksibel untuk kustomisasi → misalnya ketika ingin menambahkan field lain (email, captcha, dsb) harus membuat subclass.
   
      ⦁	Tampilan default sederhana → biasanya tetap perlu di-styling dengan CSS/Bootstrap agar lebih bagus.
   
      ⦁	Tidak cocok untuk login non-standar → misalnya login via email atau OAuth (Google, GitHub, dll), perlu modifikasi tambahan.

**2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**
⦁	Autentikasi (Authentication): proses memverifikasi identitas user. 
Contoh: ketika user memasukkan username dan password di form login, sistem akan mengecek apakah data itu valid dan cocok dengan yang ada di database. Jika cocok, berarti user tersebut ada dan bisa masuk.

⦁	Otorisasi (Authorization): proses menentukan hak akses setelah pengguna berhasil login. Misalnya, seorang admin bisa menambah atau menghapus data produk, tapi user biasa hanya bisa melihat produk saja.

Implementasi di Django:
⦁	Autentikasi: Django menyediakan sistem built-in, misalnya dengan AuthenticationForm, fungsi authenticate(), dan login(). Semua itu membantu memvalidasi username dan password user.

⦁	Otorisasi: Django memakai decorators dan permissions. Contoh paling umum adalah @login_required untuk memastikan halaman hanya bisa diakses user yang sudah login. 

**3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**
= *Cookies:*

⦁	Kelebihan:

      ⦁	Disimpan langsung di browser pengguna, jadi server tidak perlu banyak resource.
   
      ⦁	Bisa dipakai untuk menyimpan preferensi user (misalnya tema, bahasa) atau data sederhana lain.
   
      ⦁	Memungkinkan pengguna tetap login meskipun menutup browser (jika persistent cookie).
   
⦁	Kekurangan:

      ⦁	Kurang aman karena data tersimpan di sisi klien, bisa dilihat atau dimodifikasi kalau tidak dienkripsi.
   
      ⦁	Tidak cocok untuk menyimpan data yang sensitif atau besar.

*Sessions:*

⦁	Kelebihan: 

      ⦁	Lebih aman karena data utama disimpan di server, sementara di browser hanya ada session ID.

      ⦁	Bisa menyimpan data lebih banyak dan lebih kompleks dibanding cookie.
   
      ⦁	Mendukung user-specific data yang berbeda tiap sesi login.

⦁	Kekurangan:

      ⦁	Membebani server karena harus menyimpan informasi session untuk banyak pengguna.
   
      ⦁	Biasanya hanya bertahan selama sesi browser atau sampai pengguna logout

**4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**
= Secara default, cookies tidak sepenuhnya aman. Ada beberapa risiko potensial, misalnya:

⦁	Pencurian cookie (session hijacking) lewat serangan XSS (Cross-Site Scripting).

⦁	Manipulasi cookie karena data ada di sisi klien, sehingga bisa diubah pengguna jika tidak divalidasi.
Jadi, kalau cookies digunakan untuk menyimpan data penting (misalnya session login), harus ada perlindungan tambahan.

Bagaimana Django menanganinya?

⦁	CSRF token → Django otomatis me-generate token unik ke setiap form POST. Token ini diverifikasi server untuk mencegah Cross-Site Request Forgery, sehingga walaupun session ID ada di cookie, request membahayakan dari situs lain tidak bisa meng-clone user sah.

⦁	Session framework → Django tidak menyimpan data langsung di cookie, melainkan hanya ID. Data sebenarnya tetap ada di server, jadi lebih aman.

⦁	Session expiry & rotation → Django bisa otomatis menghapus session setelah waktu tertentu. Untuk mengurangi risiko session hijacking.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
= 1. Pertama-tama, saya menambahkan import ``UserCreationForm`` dan ``messages`` pada bagian paling atas ``views.py``. ``UserCreationForm`` adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran user dalam aplikasi web.

2. Kemudian di ``views.py`` saya menambahkan fungsi register. Fungsi ini berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

3. Kemudian, saya membuat berkas HTML baru dengan nama ``register.html`` agar nantinya muncul form register saat web dibuka.

4. Selanjutnya, pada ``urls,py`` saya meng-import fungsi register dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah di-import tadi (register).

5. Buka ``views.py`` dan import ``authenticate``, ``login``, dan ``AuthenticationForm`` pada bagian paling atas. fungsi ``authenticate`` dan ``login`` yang di-import adalah fungsi bawaan Django yang dapat digunakan untuk melakukan autentikasi dan login (jika autentikasi berhasil).

6. Menambahkan fungsi login_user ke dalam ``views.py`` yang berfungsi untuk autentikasi pengguna yang ingin login. Jika pengguna valid, fungsi ini akan membuat session untuk pengguna yang berhasil login.

7. Membuat berkas HTML baru dengan nama ``login.html``. Nantinya di local akan muncul tampilan untuk user agar bisa login.

8. Pada ``urls.py`` kita Kembali import fungsi login_user dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi login tadi.

9. Menambahkan import ``logout`` bersamaan dengan ``authenticate`` dan ``login``.

10. Menambahkan fungsi logout_user ke ``views.py`` agar user bisa melakukan mekanisme logout. Pada fungsi ``logout_user``, ``logout(request)`` digunakan untuk menghapus sesi pengguna yang saat ini masuk dan ``return redirect('main:login')`` mengarahkan pengguna ke halaman login dalam aplikasi Django.

11. Selanjutnya, pada ``urls.py`` saya menambahkan import fungsi ``logout_user`` dan menambahkannya ke urlpatterns.

12. Kemudian, menerapkan restriction dengan cara meng-import ``login_required`` di views.py. Merestriksi akses halaman tersebut berarti membatasi siapa saja yang boleh membuka halaman tersebut, misalnya hanya pengguna yang sudah login atau admin.

13. Menambahkan kode ``@login_required(login_url='/login')`` di atas fungsi ``show_main`` dan ``show_product``, tujuannya agar halaman utama dan product detail hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

14. Selanjutnya, pada views.py menambahkan ``HttpResponseRedirect, reverse, dan datetime``. Pada fungsi ``login_user`` tambahkan ``if form.is_valid()`` yang tujuannya agar kita bisa melihat timestamp terakhir kali user melakukan login. Agar last login muncul, maka kita tambahkan kode ``'last_login': request.COOKIES['last_login']`` ke dalam variable context di fungsi ``show_main``.

15. Selain itu, saya juga mengubah fungsi `logout_user`` untuk menghapus cookie ``last_login`` setelah melakukan cookie dengan ``response.delete_cookie('last_login')``.

16. Agar data waktu terakhir pengguna login tampil/muncul di web, maka saya menambahkan ``<h5>Sesi terakhir login: {{ last_login }}</h5>`` pada ``main.html``

17. Selanjutnya, saya menghubungkan setiap object ``Product`` dengan pengguna yang membuatnya. Pada models.py saya mebambahkan kode ``user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)``. Dengan begitu, setiap user yang sedang login hanya dapat melihat product yang telah dibuat sendiri. 

18. Karena melakukan perubahan pada ``models.py`` saya melakukan migrations. 

19. Pada ``views.py`` saya menambahkan beberapa kode pada fungsi ``create_product``, misalnya parameter ``commit=False`` pada potongan kode digunakan agar Django tidak langsung menyimpan objek hasil form ke database. Dengan begitu, ada kesempatan untuk memodifikasi objek tersebut terlebih dahulu sebelum disimpan.

20. Menerapkan ``filter_type`` pada ``show_main`` agar menampilkan halaman utama setelah user login dan dilengkapi dengan filter product berdasarkan penulis. Filter ini diambil dari query parameter ``filter`` pada URL, dengan dua opsi: "my" untuk menampilkan hanya product yang ditulis oleh user yang sedang login, dan "all" untuk menampilkan semua product. Setelah itu, tambahkan juga button my dan all di ``main.html``.

21. Menambahkan kode agar nama author/yang meng-upload muncul di ``product_detail.html``. Informasi author merefleksikan pembuat artikel, bukan user yang sedang login.

22. Runserver dan push ke PWS agar memastikan bahwa program berjalan dengan baik.  

**Checklist nomor 2: Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.**
1. Akun 1: username -> spitfirerara
   <img width="1909" height="1066" alt="Screenshot 2025-09-24 081823" src="https://github.com/user-attachments/assets/c08b5382-288b-4acb-a260-f23124c8d036" />
   <img width="1919" height="1078" alt="Screenshot 2025-09-24 081934" src="https://github.com/user-attachments/assets/22af4191-a951-4bac-8f2b-aad23de4d05e" />
   <img width="1911" height="946" alt="Screenshot 2025-09-24 080727" src="https://github.com/user-attachments/assets/b2c812fe-ae6a-4a7c-bf8d-3e383564b987" />
   <img width="1912" height="957" alt="Screenshot 2025-09-24 080759" src="https://github.com/user-attachments/assets/baf78413-5097-4a82-9aeb-de126b197f01" />
   <img width="1919" height="942" alt="Screenshot 2025-09-24 081749" src="https://github.com/user-attachments/assets/3fcb2bb0-3f15-4926-82a7-57c708b759ba" />

2. Akun 2: username -> ILoveMihuMihu
   <img width="1919" height="1079" alt="Screenshot 2025-09-24 084544" src="https://github.com/user-attachments/assets/af886759-6e44-48bf-a4b3-050378a018d2" />
   <img width="1919" height="1079" alt="Screenshot 2025-09-24 084454" src="https://github.com/user-attachments/assets/39a9d021-2a86-46d5-a228-5854952115c5" />
   <img width="1919" height="1012" alt="Screenshot 2025-09-24 082621" src="https://github.com/user-attachments/assets/b01bb467-1495-40c6-ade3-7ac6888d2969" />
   <img width="1919" height="1077" alt="Screenshot 2025-09-24 084108" src="https://github.com/user-attachments/assets/2b3cfcfd-5164-4213-a2b6-3e8e141f78c6" />
   <img width="1919" height="1065" alt="Screenshot 2025-09-24 084310" src="https://github.com/user-attachments/assets/f37abaca-372f-4a24-a88c-0c64b81e6c2c" />

---

 ## Tugas Individu 5 PBP - Desain Web menggunakan HTML, CSS dan Framework CSS

 **1.	Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

= Dalam CSS, saat ada lebih dari satu selector yang mengatur properti untuk elemen yang sama, browser akan memilih aturan mana yang dipakai berdasarkan specificity (tingkat kekhususan selector) dan cascade (urutan aturan ditulis). Urutan prioritasnya adalah sebagai berikut:

   1. **Inline style** (ditulis langsung di atribut HTML, misalnya ``<p style="color: red;">``) memiliki prioritas tertinggi dibandingkan semua selector lainnya.

   2. **ID selector** (``#id-name {}``) lebih kuat daripada class, attribute, atau tag selector.

   3. **Class selector, attribute selector, dan pseudo-class** (``.class {}``, ``[type="text"] {}``, ``:hover {}``) berada satu level di bawah ID.

   4. **Element selector** (``div {}``, ``h1 {}``) dan pseudo-element (``::before``, ``::after``) memiliki prioritas paling rendah.

Selain itu, jika dua selector memiliki tingkat specificity yang sama, maka aturan yang ditulis paling terakhir dalam CSS (atau yang terakhir dimuat di file CSS) yang akan dipakai, karena konsep cascading (mengalir ke bawah).

**2.	Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**

= Responsive design adalah konsep/design yang membuat tampilan website bisa menyesuaikan ukuran layar, mulai dari laptop, tablet, sampai smartphone. Konsep ini penting karena:

- Memudahkan user untuk mengakses website dari berbagai macam device
- Dengan responsive design, layout otomatis berubah: teks tetap terbaca, tombol tetap mudah ditekan, dan gambar menyesuaikan ukuran layar.
- Hal ini meningkatkan user experience dan mengurangi bounce rate (user cepat pergi dari website).
- Responsive design juga membantu SEO, karena mesin pencari (seperti Google) mengutamakan website yang mobile-friendly.

**Contoh aplikasi yang sudah menerapkan responsive design:**

• Instagram web 
Saat dibuka melalui desktop, foto ditampilkan dalam grid besar. Sedangkan di smartphone, tampilannya akan menjadi feed yang rapat ke bawah, navigasi juga lebih sederhana, dan tombol lebih besar agar mudah ditekan. Ini menunjukkan desainnya fleksibel.

**Contoh aplikasi yang belum menerapkan responsive design:**

• Beberapa website pemerintah lama (misalnya portal pelayanan lama) → Misal, saat dibuka di HP teks menjadi terlalu kecil, harus zoom in/out saat ingin membaca/menekan tombol, tombol tidak proporsional. Hal ini nantinya akan menghambat user saat menggunakannya.

**3.	Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

= Margin, border, dan padding adalah bagian dari CSS box model:

   • Margin → area di luar border, memberi jarak antara elemen dengan elemen lain. Berguna untuk spacing antar card atau antar section.

   • Border → garis tepi elemen, dapat diberi warna, ketebalan, atau bentuk (misalnya border-radius untuk melengkung).

   • Padding → ruang di dalam border, memberi jarak antara konten (teks/gambar) dengan pinggiran kotaknya.

      Contoh implementasi dalam CSS:
      
      ``.card {``
      `` margin: 16px;                  /* jarak antar card */``
      `` border: 2px solid #43AA8B;     /* garis hijau di sekeliling card */``
      `` padding: 12px;                 /* jarak isi card dengan bordernya */``
      ``}``

**4.	Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

= **Flex box (Flexible Box Layout)**

Flexbox adalah metode layout CSS yang dirancang untuk mengatur elemen dalam satu dimensi (horizontal atau vertical).

   • Elemen utama (parent container) di-set dengan ``display: flex;``.
   
   • Flex items bisa otomatis menyesuaikan ukuran dan posisi tergantung ruang kosong.
   
   • Dapat mengatur alignment dengan properti seperti:
   
   	• ``justify-content`` → mengatur posisi horizontal (misalnya: rata kiri, tengah, spasi di antara elemen).
   
   	• ``align-items`` → mengatur posisi vertical.
   
   	• ``flex-grow``, ``flex-shrink``, ``flex-basis`` → untuk kontrol ukuran dinamis item.

**Kegunaan:**

   • Cocok untuk membuat navbar yang elemen-elemennya bisa menyesuaikan layar.
   
   • Membuat daftar tombol / kartu produk dalam satu baris yang rapi.
   
   • Mmebuat layout responsif sederhana dengan cepat.

**CSS Grid Layout**

Grid adalah metode layout dua dimensi, artinya bisa mengatur elemen baik dalam baris maupun kolom secara bersamaan.

   • Container utama di-set dengan ``display: grid;``
   
   • Menentukan baris dan kolom dengan ``grid-template-rows`` dan ``grid-template-columns``.
   
   • Elemen bisa ditempatkan di posisi tertentu menggunakan ``grid-row`` dan ``grid-column``.

**Kegunaan:**

   • Cocok untuk men-desain layout halaman penuh (misalnya: header, sidebar, content, footer).
   
   • Membuat galeri gambar atau card yang ukurannya rapi dalam baris & kolom.
   
   • Memberi kontrol presisi tinggi atas posisi tiap elemen di halaman.

**5.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

=  • Pertama-tama, saya menambahkan tailwind ke aplikasi saya untuk melakukan styling. Agar template Django saya dan tailwind terhubung, saya menambahkan script CDN tailwind di base.html

• Selanjutnya, pada ``views.py``, saya menambahkan fungsi baru ``edit_product`` yang menerima parameter ``request`` dan ``id``. Agar nantinya pada website saya muncul fitur mengedit product, saya membuat file baru bernama ``edit_product.html``. Kemudian, saya melakukan routing dengan menambahkan path ``edit_product`` di ``urlpatterns`` pada file ``urls.py``.

• Lalu, pada ``views.py``, saya menambahkan fungsi baru ``delete_product`` yang menerima parameter ``request`` dan ``id``. Agar nantinya pada website saya muncul fitur menghapus product. Kemudian, saya melakukan routing dengan menambahkan path ``delete_product`` di ``urlpatterns`` pada file ``urls.py``.

• Kemudian menambahkan navigation bar pada aplikasi. Pada aplikasi saya, saya menempatkan navbar saya pada bagian atas. Saya mengisi navbar saya dengan: Home, Jersey, Shoes, Ball, Accessory, dan Other. Nantinya, user bisa dengan mudah mengakses kategori yang mereka inginkan.

• Setelah itu, saya menambahkan global.css pada folder static. Agar style CSS yang ditambahkan di global.css tadi dapat digunakan dalam template Django, saya menambahkan file tersebut ke ``base.html``. Kemudian, pada ``global.css`` saya menyesuaikan warna untuk tampilan website, warna font, ukuran font, dan lain-lain agar tampilan website saya terlihat rapi dan mudah diakses di manapun

• Selanjutnya, karena telah membuat navbar, saya menambahkan styling agar navbar menjadi lebih responsive dan menarik. Navbar pada aplikasi saya juga sudah menyesuaikan Ketika user membuka aplikasi pada desktop ataupun pada device lain seperti HP, tablet, dan lain-lain

• Saya juga melakukan styling pada ``login.html``, ``register.html`` agar tampilan login & register lebih responsive. Diharapkan juga agar user menjadi lebih tertarik dalam melakukan register akun.

• Selain itu, saya juga melakukan styling pada home page aplikasi saya agar tampilannya lebih menarik. Pada home, saya menampilkan card product, yang di mana user nantinya bisa melihat tampilanproduk nya secara mudah dan membaca deskripsi/detail dari setiap produk yang sudah tertera di home page. Kemudian, apabila user sudah login & menambahkan suatu product, maka user tersebut bisa meng-edit & menghapus product yang telah di-upload. Tombol edit & delete juga ditampilkan pada card product.

• Selanjutnya, saya menambahkan ``no-product.png`` dan ``card_news,html`` ke dalam main.html`` agar nantinya saat belum ada product yang di-upload akan muncul gambar no-product di website, sedangkan saat sudah ada product yang di-upload, maka akan muncul dalam bentuk card product.

• Lalu, saya melakukan styling pada ``product_detail.html``, ``edit_product.html``, ``create_product.html`` agar tampilannya lebih menarik dan tidak monoton.

• Terakhir, untuk memastikan aplikasi dapat berjalan dan styling yang dilakukan sudah sesuai, saya menjalankan servernya dengan ``python manage.py runserver``.





