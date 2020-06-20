# Flask Blueprint

Boilerplate proyek Flask menggunakan Blueprint. Gunakan template ini untuk membuat aplikasi Flask yang fleksibel.

## Kebutuhan Dasar
- Python versi 3.6 atau yang lebih baru
- Python virtualenv untuk Python 3
- NodeJS versi 12.8 atau yang lebih baru
- NPM (sudah terpaket dengan NodeJS)

## Panduan Dasar

### 1. Clone proyek

Nama folder `myapp` ganti sesuai dengan nama aplikasi yang akan dibuat.

```sh
git clone https://github.com/desa-id/cetakbiru-flask myapp
```

### 2. Buat virtual environment di folder venv

Nama folder `venv` menyesuaikan saja, tidak harus `venv`

```sh
cd myapp
virtualenv --python=python3 venv
```

### 3. Instalasi dependensi
```sh
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Compile asset javascript dan css
```sh
npm install --no-optional --no-audit
npm run build
```

### 5. Jalankan aplikasi
```sh
# Persiapkan file konfigurasi (sesuaikan parameternya)
cp .env.example .env

# Menjalankan menggunakan flask
export FLASK_APP=src
export FLASK_ENV=development
flask run

# Jika ingin menjalankan menggunakan gunicorn
venv/bin/gunicorn -c config/gunicorn.py wsgi

# Jika ingin menjalankan menggunakan uwsgi
uwsgi --http-socket :5000 --plugin python3 --module wsgi:application
```

> Penting: pastikan selalu mengaktifkan virtualenv saat development!

---

Aplikasi akan berjalan di url berikut:

- Halaman index : http://localhost:5000
- Halaman API : http://localhost:5000/api
- Contoh halaman : http://localhost:5000/hello
- Cek koneksi dabase : http://localhost:5000/testdb

## Deploy ke Heroku
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
