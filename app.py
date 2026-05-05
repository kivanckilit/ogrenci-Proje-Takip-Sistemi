# Öğrenci Proje Yönetim Sistemi

Flask + SQLite ile hazırlanmış detaylı öğrenci proje yönetim sistemi.

## İçerik

- Admin paneli
- Öğretmen paneli
- Öğrenci paneli
- Öğrenci ve öğretmen için ayrı kayıt ekranları
- Öğrenci numarası, bölüm, sınıf, telefon, e-posta bilgileri
- Öğretmen sicil no, branş, e-posta, telefon bilgileri
- Proje kodu, başlık, kategori, kontenjan, son başvuru tarihi
- Proje başvurusu
- Başvuru onaylama / reddetme / tamamlandı yapma
- Proje ilerleme yüzdesi
- Dosya yükleme
- Öğretmen yorumları
- Sistem duyuruları
- Admin kullanıcı/proje/duyuru yönetimi
- Admin panelinden öğrenci ve öğretmen silme
- Profesyonel resmi kurum arayüzü

## Kurulum

```bash
cd ogrenci_proje_yonetim_detayli
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Çalıştırma

```bash
python app.py
```

Tarayıcı:

```text
http://127.0.0.1:5000
```

## Varsayılan Admin

```text
Kullanıcı adı: admin
Şifre: admin123
```

## Not

Veritabanı `database.db` dosyası ilk çalıştırmada otomatik oluşur.
