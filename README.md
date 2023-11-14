# Holocure Inventory
 
---
# Tugas 2
# Implementasi di *Local Machine*
## Setup Awal
### 1. Pastikan *virtual environment* (venv) sudah aktif
Sebelum membuat *project* Django, kita memerlukan venv untuk menampung semua *library* yang kita gunakan di dalam *project*. Cara untuk mengaktifkan venv adalah sebagai berikut:
- Windows
```
env\Scripts\activate.bat
```
- Mac
```
source env/bin/activate
```

### 2. Jalankan script instalasi *library*
Pada *project* ini, terdapat beberapa *library* yang digunakan demi mempercepat proses pengembangan. Untuk itu, jika ingin menjalankan di *local machine* sendiri, diperlukan untuk menjalankan beberapa *script* berikut:
- Instalasi *library*
```
pip install -r requirements.txt
```
- Instalasi *package*
```
npm i
```
Instalasi *package* tidak diharuskan untuk menggunakan Node Package Manager. *Package manager* lain seperti Yarn dan Bun juga bisa digunakan di *project* ini. Alasan perlu meng-*install* *package* juga padahal sudah ada *library* adalah karena *project* ini menggunakan TailwindCSS sebagai *framework* CSS-nya.

## Langkah Pembuatan *Project*
### 1. Membuat *project* Django baru
Untuk membuat *project* baru, sebelumnya harus dipastikan bahwa direktori terminal sudah sesuai. Jika sudah, perintah berikut dijalankan untuk membuat *project* Django:
```
py manage.py startapp game_inventory .
```
Sebuah aplikasi main juga diperlukan pada *project*. Oleh karena itu, perintah berikut perlu dijalankan juga:
```
py manage.py startapp main .
```

### 2. Konfigurasi *Project*
#### Aplikasi `game_inventory`
Ubah pengaturan `ALLOWED_HOST` agar membolehkan aplikasi untuk dijalankan oleh segala *host* dengan mengubah pengaturan berikut di `settings.py` milik `game_inventory`:
```py
...
ALLOWED_HOSTS = ['*']
...
```

Tambahkan aplikasi `main` sebagai `INSTALLED_APP` di `settings.py` dengan mengubah pengaturan berikut:
```py
INSTALLED_APPS = [
    ...,
    'main',
    'compressor',
    'widget_tweaks',]
```

#### Konfigurasi URL
URL dari index perlu ditambahkan agar ketika membuka halaman, akan terbuka `main.html`. Caranya adalah dengan mengubah `urls.py` pada direktori `main` sebagai berikut:
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]
```

### 3. Implementasi Template
#### Membuat Page Utama
Buat direktori baru bernama `templates` dalam direktori utama, bukan direktori *project*. Setelah itu buat berkas baru bernama `main.html` yang isinya adalah halaman utama yang diinginkan. Untuk mendapatkan boilerplate, emmet abbreviation dapat dimanfaatkan dengan hanya menulis `html:5` lalu meng-klik *enter*.

#### Membuat Model
Untuk mengolah data, models dapat menampung sebuah *class* untuk menyimpan data tersebut. Pada *project* ini, data yang akan disimpan adalah *Item* dengan atribut nama, jumlah, tingkat kelangkaan, dan deskripsi yang implementasinya adalah sebagai berikut:
```py
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    amount = models.IntegerField()
    rarity = models.IntegerField()
    description = models.TextField()
```

#### Membuat View
Untuk menampilkan `main.html`, diperlukan sebuah fungsi pada `view` untuk memberikan file HTML tersebut ke pengguna. Caranya adalah menambahkan fungsi berikut:
```py
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
```

#### Melakukan Migrasi Model
Migrasi model harus selalu dilakukan setiap kali ada perubahan yang dilakukan pada model. Perintah yang digunakan untuk melakukan migrasi adalah sebagai berikut:
```
python manage.py migrate
```

# Bagan
![diagram](./doc/diagram.png)  

# Mengapa venv?
Terdapat beberapa alasan khusus tentang penggunaan venv untuk pengembangan aplikasi Django, yaitu:
- Pengelolaan *Dependency* — setiap *project* pasti memerlukan versi *package* yang berbeda. Oleh karena itu, agar setiap *project* memiliki *package* yang sesuai dengan versi yang sesuai, lebih baik untuk mengisolasikan *project* tersebut dari instalasi Python secara global.
- Reprodusibilitas — ada kemungkinan bahwa *project* yang dijalankan di suatu komputer justru tidak bisa dijalankan di komputer lainnya. Penyebab utamanya adalah perbedaan versi dari *package* yang dimiliki. Dengan adanya venv, versi dari *package* yang digunakan setiap aplikasi sudah diatur sehingga kemungkinan tidak bisa dijalankan berkurang.

# MVC, MVT, MVVM, dan Perbedaannya
Pada pengembangan website, terdapat beberapa pola arsitektural yang dikembangkan oleh *developer* untuk membuat *project* lebih *scalable* dan mudah untuk di-*maintain*. Ketiga arsitektur yang akan dibahas kali ini adalah beberapa yang paling populer di antara arsitektur-arsitektur yang ada. Ketiganya memiliki dua komponen utama yang memiliki peran krusial dalam arsitektur:
- **Model** — komponen inti dari arsitektur, merupakan struktur data dinamik milik aplikasi yang independen dari *user interface*. Secara langsung mengatur data, logika, dan peraturan dari aplikasi.
- **View** — mengurus logika presentasi, yaitu bagaimana data yang dikelola oleh model akan dipresentasikan kepada pengguna.

Perbedaan pendekatan dari tiap arsitektur mulai terlihat pada komponen ketiga. Masing-masing komponen pembeda pada arsitektur sebenarnya memiliki tujuan sama, namun dengan pendekatan yang berbeda. Berikut adalah penjelasan mengenai perbedaan pendekatan yang digunakan oleh arsitektur-arsitektur di atas.

## Model View Controller (MVC)
Pola arsitektural ini adalah yang paling sering digunakan oleh *framework* pengembangan *website* untuk membuat *project* yang *scalable*. Perbedaan dengan dua arsitektur lainnya terdapat pada komponen ketiganya, *controller*, yaitu:
- **Controller** — bertindak sebagai jembatan antara *model* dan *view* untuk memproses semua *business logic* dan *request* yang datang.

## Model View Template (MVT)
Pola arsitektur yang sering digunakan pada aplikasi website Django, yaitu *framework* Python *high-level*. Memiliki banyak persamaan dengan arsitektur MVC namun terdapat beberapa perbedaan untuk menyesuaikan dengan kebutuhan pengembangan aplikasi website. Perbedaan signifikan yang dimiliki MVT dengan arsitektur lain adalah:
- **View** — pada Django, *view* berisi lebih banyak tentang pemrosesan data dan logika dibandingkan menampilkan suatu hal. Oleh karena itu, bisa dibilang pada arsitektur ini *view* merupakan perpaduan antara *controller* dan *view* pada arsitektur MVC.
- **Template** — berisi bagian statik dari *output* HTML dan juga berbagai sintaks khusus yang menjelaskan bagaimana konten dinamis akan ditampilkan. Perannya mirip seperti *view* pada arsitektur MVC.

## Model View View Model (MVVM)
Pola arsitektural yang sering digunakan pada aplikasi yang memerlukan banyak interaksi pengguna seperti aplikasi *desktop* dan *single page application* dengan *framework* seperti Angular dan Vue. Perbedaan signifikan yang dimiliki MVVM dengan arsitektur lain adalah:
- **View Model** — penengah antara *model* dan *view* yang mengandung logika presentasi dan mengubah data dari model menjadi format yang bisa ditampilkan oleh *view*. 

---
# Tugas 3
# Apa perbedaan `GET` dan `POST` di Django?
Method `GET` dan `POST` merupakan dua method yang paling sering digunakan dalam HTTP untuk berinteraksi dengan sumber daya yang dimiliki server. Berikut adalah 

## Method `GET`
- **Tujuan** — meminta dan mendapatkan data dari sumber tertentu.
- **Visibilitas data** — data dikirim melalui parameter URL. Oleh karena itu, data dapat dilihat di *address bar*.
- **Panjang data** — sebab data dikirim melalui parameter URL, panjang data hanya terbatas terhadap panjang dari URL tersebut.
- **Tipe data** — hanya bisa mengandung karakter ASCII di dalam URL, sehingga memiliki keterbatasan tersebut.
- **Keamanan** — data terlihat pada URL. Oleh karena itu, tidak direkomendasikan untuk mengirim informasi sensitif melalui `GET`.
- **Indepotency** — *request* `GET` berulang kali akan memberikan hasil yang sama.
- **Caching** — *response* dari `GET` selalu di-*cache* kecuali bila dilarang secara eksplisit.
- **Browser behavior** — bisa di *bookmark* dan dipakai ketika bernavigasi menggunakan tombol *backward* atau *forward* di dalam *browser*.

## Method `POST`
- **Tujuan** — mengirim data ke sumber tertentu untuk diproses.
- **Visibilitas data** — mengirim data melalui *body* dari HTTP *request*
- **Panjang data** — tidak memiliki keterbatasan seperti `GET` karena data tidak dikirim melalui URL.
- **Tipe data** —  tidak memiliki keterbatasan seperti `GET` karena data tidak dikirim melalui URL.
- **Keamanan** — data dikirim melalui *request body* sehingga lebih aman dibandingkan dengan `GET`.
- **Indepotency** — *request* `POST` berulang kali akan memberikan hasil yang berbeda.
- **Caching** — biasanya *response* terhadap `POST` tidak di-*cache* kecuali diperintahkan untuk melakukan demikian.
- **Browser behavior** — tidak bisa di-*bookmark*. Jika diakses kembali menggunakan tombol *back* di *browser*, `POST` akan mengirim konfirmasi kepada pengguna untuk mengirim ulang datanya.

# Perbedaan antara HTML, XML, dan JSON
Perbedaan fundamental di antara ketiga jenis file adalah XML dan JSON digunakan untuk menyimpan dan transmisi data, sedangkan HTML digunakan untuk menjelaskan bagaimana data seharusnya ditampilkan.

# Alasan JSON lebih sering digunakan pada web modern
JSON lebih cocok untuk data yang kecil dan sederhana, lebih mudah untuk dibaca dan di-*maintain*, lebih cepat dan efisien untuk aplikasi web atau API, mendukung tipe data *native* yang kurang memiliki standar skema bahasa, dan lebih kompatibel terhadap teknologi *web* namun lebih rentan dibanding XML.

# Langkah pembuatan
## Pembuatan form
Untuk menjaga kerapihan file, kode form ditulis pada file baru bernama `forms.py` yang berada di direktori `main`.
```py
from django import forms
from main.models import Idols

class IdolsForm(forms.ModelForm):
    class Meta:
        model = Idols
        fields = ['name', 'branch', 'generation', 'debut_date', 'tagline']
```
Pada kasus ini, `ModelForm` dipakai sebab berhubungan langsung dengan model **Idols** yang berada pada `models.py`. Untuk menghindari proses yang merepotkan, `ModelForm` lebih tepat digunakan dibanding `Form`.

## Menampilkan form
Setelah kode form dibuat, `views.py` pada direktori `main` perlu diubah agar dapat menampilkan form tersebut.
```py
def add_items(request):
    form = IdolsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, 'add_items.html', context)
```

## Pengembalian data
Untuk membolehkan pengguna mengambil data dari model, diperlukan fungsi dalam `views.py` untuk memberikan data-data tersebut menggunakan format file tertentu.
```py
def show_xml(request):
    data = Idols.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Idols.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Idols.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Idols.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## Konfigurasi URL
`urlpatterns` pada `urls.py` di direktori `main` perlu diubah agar dapat memberikan data yang disajikan oleh fungsi dari `views.py` kepada pengguna.
```py
urlpatterns = [
    ...,
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

# Akses data melalui URL dengan Postman
## JSON
![json-postman](./doc/postman_json.png)  

## XML
![xml-postman](./doc/postman_xml.png)

---
# Tugas 4

## `UserCreationForm`
`UserCreationForm` adalah form registrasi pengguna siap pakai yang disediakan oleh Django dalam modul `django.contrib.auth.forms`. Berikut adalah beberapa kelebihan dan kekurangan dari penggunaan form tersebut.
### Kelebihan
- Relatif sederhana untuk digunakan karena semua telah disiapkan oleh Django.
- Validasi dasar yang sudah *built-in*.
- Dukungan menambahkan captcha untuk melawan bot.
### Kekurangan
- Keterbatasan fungsi sebab `UserCreationForm` hanya memiliki *field* untuk *username* dan *password* saja.
- Validasi dasar tidak cukup sehingga masih perlu dilengkapi lagi.
- Bisa dikustomisasi namun dalam cakupan yang terbatas.

## Perbedaan autentikasi dan otorisasi
Autentikasi merupakan proses verifikasi identitas pengguna atau entitas, sedangkan otorisasi merupakan proses mengizinkan untuk memberi atau melarang akses kepada pengguna atau entitas setelah mereka diautentikasi.

## Cookies dan cara kerjanya
Cookies adalah mekanisme penyimpanan data yang digunakan oleh *browser* untuk menyimpan informasi kecil dalam bentuk teks di komputer pengguna. Berikut adalah cara kerjanya dalam langkah-langkah sederhana:
1. Permintaan awal
2. Respons dari server
3. Browser menyimpan cookies
4. Cookies dikirim ke server
5. Server membaca cookies
6. Server merespons berdasarkan cookies
7. Siklus berulang

## Resiko potensial penggunaan cookies
Penggunaan cookies sendiri memiliki risiko potensial yang perlu diwaspadai, di antaranya adalah:
1. Masalah privasi: cookies dapat digunakan untuk melacak perilaku dari pengguna tersebut secara online.
2. Man in the middle attack: informasi dari cookies dapat dibajak oleh penyerang ketika cookies dikirim dari pengguna ke server.
3. Cross-site scripting (XSS): informasi sensitif yang dikandung cookies dapat menjadi target serangan XSS. 

## Implementasi
### 1. Membuat form registrasi
Untuk mengimplementasikan autentikasi, sebelumnya perlu dibuat bagian registrasi pada website. Untuk itu, pada `views.py` direktori `main` ditambahkan sebuah fungsi baru bernama register yang akan mengimplementasikan *built-in class* dari Django yang mengurus registrasi pengguna sebagai berikut:
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Tidak lupa bahwa perlu dibuat laman `register` yang menampilkan fungsi tersebut.

### 2. Membuat bagian login
Setelah membuat fungsi registrasi, tentu diperlukan sebuah fungsi untuk otentikasi untuk masuk ke dalam akun yang sudah tercatat di dalam basis data. Untuk itu, perlu dibuat fungsi dan form login yang bisa menangani hal tersebut.
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Pilihan untuk keluar juga perlu ditambahkan.

```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')
```

Tidak lupa bahwa perlu dibuat laman `login` yang menampilkan kedua fungsi di atas.

### 3. Restriksi akses 
Halaman di dalam website dapat direstriksi aksesnya dengan cukup menambahkan sebuah *decorator* di atas fungsinya seperti di bawah.
```py
@login_required(login_url='/login')
def foo(request):
    return 'bar'
```

### 4. Menghubungkan `Model` dengan `User`
Untuk menambahkan fungsionalitas agar data di dalam model hanya bisa diakses pengguna tertentu, sebuah *field* baru perlu ditambahkan ke dalam model. Dalam kasus ini, nama pengguna digunakan sebagai identitas pembuat data sehingga data tersebut hanya bisa diakses oleh pengguna yang membuatnya.
```py
class Idols(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Agar hal tersebut tercapai, bagian `display_items` perlu dimodifikasi sedikit agar hanya menampilkan data yang pengguna tersebut buat.

```py
def display_items(request):
    idols = Idols.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'idols': idols,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'display_items.html', context)
```

## 5. Memasukkan semua fungsi `views` baru ke `url`
Setelah semua fitur berhasil ditambahkan, *routing* fungsi baru perlu dicatat di dalam `urlpatters` pada `urls.py` milik `main`.
```py
urlpatterns = [
    ...,
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment/<int:id>/', increment_superchat, name='increment'),
    path('decrement/<int:id>/', decrement_superchat, name='decrement'),
]
```

---
# Tugas 5
## Manfaat *element selector*
*Element selector* dapat digunakan untuk mengubah keseluruhan elemen tertentu, misalnya `h1`, `p`, `div`, `body`, dan elemen-elemen lainnya. Kelebihan dari menggunakan *element selector* adalah kita tidak perlu memberi *class* kepada elemen-elemen yang ingin kita ubah sebab kita sudah menetapkan *styling* untuk keseluruhan elemen.

## Tag HTML5
Ada banyak sekali tag HTML5 yang tersedia, namun yang paling sering dipakai adalah `div` sebagai *wrapper* elemen, `p` dan `h<angka>` sebagai *wrapper* paragraf atau *heading*, dan `img` sebagai elemen yang menunjukkan gambar.

## Perbedaan *margin* dan *padding*
*Margin* mengatur jarak suatu elemen terhadap elemen-elemen lainnya, sedangkan *padding* mengatur jarak elemen yang berada di dalam suatu elemen terhadap *border* dari elemen tersebut.

## Perbedaan TailwindCSS dengan Bootstrap
Perbedaan TailwindCSS dengan Bootstrap sendiri terdapat pada *degree of customizability*-nya. Bootstrap menyediakan *class* CSS lengkap yang siap pakai dengan minimnya kebutuhan untuk kustomisasi sedangkan TailwindCSS menyediakan *styling* CSS dalam bentuk *class* sehingga tidak perlu menggunakan file CSS ekstra lagi.

---
# Tugas 6
## Perbedaan Synchronous dan Asynchronous Programming
### Synchronous
- Linear Execution: Dalam pemrograman sinkron, kode dijalankan secara berurutan dari atas ke bawah. Setiap baris kode harus menyelesaikan eksekusinya sebelum kode selanjutnya dapat dijalankan.
- Blocking: Jika ada operasi yang memakan waktu (seperti akses database atau panggilan API), eksekusi kode selanjutnya akan terhenti atau "terblokir" sampai operasi tersebut selesai. Ini berarti bahwa selama operasi tersebut berlangsung, tidak ada kode lain yang dapat dijalankan.
- Simplicity: Pemrograman sinkron cenderung lebih mudah dipahami dan dikelola karena alurnya yang linear dan mudah diprediksi.

### Asynchronous
- Non-Linear Execution: Dalam pemrograman asinkron, kode dapat dijalankan secara bersamaan atau tanpa menunggu baris kode sebelumnya selesai. Ini memungkinkan program untuk melakukan tugas lain sambil menunggu suatu operasi selesai.
- Non-Blocking: Operasi yang memakan waktu (seperti permintaan jaringan) tidak akan menghentikan eksekusi kode lain. Program dapat memulai operasi dan kemudian melanjutkan ke baris kode berikutnya tanpa menunggu operasi tersebut selesai.
- Complexity: Pemrograman asinkron bisa lebih sulit untuk dimengerti dan dikelola karena adanya konsep seperti callback, promise, atau async/await yang digunakan untuk menangani operasi yang tidak selesai secara langsung.

## Event Driven Programming
Paradigma event-driven programming (pemrograman berbasis event) adalah pendekatan dalam pengembangan perangkat lunak di mana alur eksekusi program ditentukan oleh event atau kejadian, seperti aksi pengguna, input dari perangkat keras, atau pesan dari program lain. Dalam konteks JavaScript dan AJAX, ini menjadi sangat relevan karena kedua teknologi ini sering digunakan untuk membangun aplikasi web interaktif yang responsif terhadap tindakan pengguna dan perubahan data.

Pada tugas ini, penggunaan event driven programming salah satunya adalah pada saat melakukan klik tombol increment decrement dan delete.

## AJAX Asynchronous Programming
Asynchronous programming adalah konsep kunci dalam penerapan AJAX (Asynchronous JavaScript and XML). AJAX memungkinkan aplikasi web untuk mengirim dan menerima data dari server secara asinkron, tanpa perlu memuat ulang seluruh halaman web. Ini meningkatkan pengalaman pengguna dengan membuat aplikasi web lebih responsif dan interaktif.