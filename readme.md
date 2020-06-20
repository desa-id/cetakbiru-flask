# Flask Blueprint

Boilerplate proyek Flask menggunakan Blueprint. Gunakan template ini untuk membuat aplikasi Flask yang fleksibel.

## Kebutuhan Dasar
- Python versi 3.7 atau yang lebih baru + Pipenv
- NodeJS versi 12.8 atau yang lebih baru
- NPM (sudah terpaket dengan Nodejs)

## Panduan Dasar

### 1. Clone proyek
Nama folder `myapp` ganti sesuai dengan nama aplikasi yang akan dibuat.

```sh
git clone https://github.com/desa-id/cetakbiru-flask myapp
```

### 2. Buat environment dan install dependensi Python menggunakan pipenv
```sh
cd myapp
pipenv install
pipenv shell
```

### 3. Compile asset javascript dan css
```sh
npm install --no-optional --no-audit
npm run build
```

### 4. Jalankan aplikasi
```sh
# Persiapkan file konfigurasi (sesuaikan parameternya)
cp .env.example .env

# Menjalankan menggunakan flask
export FLASK_APP=src
flask run
```

Cara lain menjalankan aplikasi (_disarankan saat mode production_):

```sh
# Jika ingin menjalankan menggunakan gunicorn
gunicorn -c config/gunicorn.py wsgi

# Jika ingin menjalankan menggunakan uwsgi
uwsgi --http-socket :5000 --plugin python3 --module wsgi:application
```

> Penting: pastikan selalu mengaktifkan `pipenv shell` saat development!

---

Aplikasi akan berjalan di url berikut:

- Halaman index : http://localhost:5000
- Halaman API : http://localhost:5000/api
- Contoh halaman : http://localhost:5000/hello
- Cek koneksi dabase : http://localhost:5000/testdb

## Deploy ke Heroku

Boilerplate ini sudah dapat di-deploy ke Heroku, hanya perlu sedikit penyesuaian seperti berikut:

```sh
# Konfigurasi runtime di Heroku
heroku buildpacks:set heroku/python
heroku buildpacks:set heroku/nodejs

# Heroku environment variable
heroku config:set WEB_CONCURRENCY=3
heroku config:set APP_HOST=127.0.0.1
heroku config:set APP_PORT=5000
heroku config:set APP_KEY=secretkey123
heroku config:set APP_ENV=production
heroku config:set APP_DEBUG=False
heroku config:set DB_TYPE=sqlite
heroku config:set DB_PORT=5432
heroku config:set DB_HOST=127.0.0.1
heroku config:set DB_DATABASE=flask_app
heroku config:set DB_USERNAME=postgres
heroku config:set DB_PASSWORD=secret
heroku config:set MAIL_USERNAME=
heroku config:set MAIL_PASSWORD=
heroku config:set MAIL_HOST=smtp.mailtrap.io
heroku config:set MAIL_PORT=587

# Deploy ke Heroku
git push heroku master
```

> Pastikan `heroku-cli` sudah terinstal, panduan instalasi `heroku-cli` dapat ditemukan [disini](https://devcenter.heroku.com/articles/heroku-cli).

## License

Copyright 2020 - datadesa.id

Licensed under the [Apache License][choosealicense], Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of the License at:
<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
ANY KIND, either express or implied. See the License for the specific language
governing permissions and limitations under the License.

[choosealicense]:https://choosealicense.com/licenses/apache-2.0/
