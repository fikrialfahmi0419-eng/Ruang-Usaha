import streamlit as st
from pathlib import Path
import base64
import html

# ============================================================
# RUANG USAHA — STREAMLIT APP
# Versi bersih: tidak menampilkan kode HTML sebagai teks
# ============================================================

st.set_page_config(
    page_title="Ruang Usaha | Belajar, Berbagi, dan Bertumbuh Bersama",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# Helper
# ------------------------------------------------------------
def find_asset(filename):
    """Mencari file aset dengan nama yang sama tanpa peduli huruf besar/kecil."""
    roots = [
        Path("."),
        Path("Assets"),
        Path("assets"),
        Path("/workspaces/Ruang-Usaha"),
        Path("/workspaces/Ruang-Usaha/Assets"),
        Path("/workspaces/Ruang-Usaha/assets"),
    ]
    target = filename.lower()
    for root in roots:
        try:
            if root.is_file() and root.name.lower() == target:
                return root
            if root.exists():
                for p in root.rglob("*"):
                    if p.is_file() and p.name.lower() == target:
                        return p
        except Exception:
            pass
    return None


def image_data_uri(filename):
    p = find_asset(filename)
    if not p:
        return ""
    try:
        mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
        data = base64.b64encode(p.read_bytes()).decode("utf-8")
        return f"data:{mime};base64,{data}"
    except Exception:
        return ""


def clean(text):
    return html.escape(str(text))


def section_html(content):
    """Render satu blok HTML lengkap. Tidak pernah membuka/menutup tag
    pada st.markdown yang berbeda."""
    st.html(content)


LOGO_RUANG = image_data_uri("logo-ruang-usaha.png")
LOGO_UNIMED = image_data_uri("logo-unimed.png")

if LOGO_RUANG:
    logo_html = f'<img src="{LOGO_RUANG}" alt="Logo Ruang Usaha">'
else:
    logo_html = '<div class="logo-fallback">🌱</div>'

# ============================================================
# CSS
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

html { scroll-behavior: smooth; }
.stApp {
    background: #f8f6ef;
    color: #17352e;
    font-family: 'DM Sans', sans-serif;
}
.block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}
[data-testid="stHeader"] { background: transparent; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

.ru-topbar {
    background: #174d40;
    color: #fff;
    padding: 12px 18px;
    text-align: center;
    font-size: 14px;
    border-radius: 0 0 12px 12px;
    margin-bottom: 24px;
}
.ru-topbar b { color: #f2c36b; }

.ru-header {
    background: rgba(248,246,239,.96);
    padding: 10px 0 20px;
}
.ru-header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 25px;
}
.ru-brand {
    display: flex;
    align-items: center;
    gap: 13px;
}
.ru-brand img {
    width: 58px;
    height: 58px;
    object-fit: contain;
    border-radius: 12px;
}
.logo-fallback {
    width: 58px;
    height: 58px;
    display: grid;
    place-items: center;
    font-size: 36px;
}
.ru-brand-name {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    font-size: 27px;
    color: #174d40;
}
.ru-brand-tagline {
    color: #68746f;
    font-size: 13px;
    margin-top: 3px;
}
.ru-nav {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    gap: 7px;
}
.ru-nav a {
    color: #17352e;
    text-decoration: none;
    padding: 9px 11px;
    border-radius: 9px;
    font-weight: 600;
    font-size: 13px;
}
.ru-nav a:hover {
    background: #e8f1ec;
    color: #174d40;
}

.hero {
    background: #174d40;
    color: #fff;
    border-radius: 28px;
    padding: 62px 58px;
    margin-top: 20px;
    margin-bottom: 25px;
}
.hero-grid {
    display: grid;
    grid-template-columns: 1.45fr .75fr;
    gap: 40px;
    align-items: center;
}
.eyebrow {
    display: inline-block;
    background: #e8f1ec;
    color: #174d40;
    padding: 9px 14px;
    border-radius: 99px;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 18px;
}
.hero h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(38px, 5vw, 66px);
    line-height: 1.08;
    margin: 0 0 20px;
    color: #fff;
}
.hero h1 em { color: #f2c36b; font-style: normal; }
.hero p {
    font-size: 17px;
    line-height: 1.8;
    color: #e7f0eb;
    max-width: 760px;
}
.hero-points {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin-top: 24px;
}
.hero-points span {
    border: 1px solid rgba(255,255,255,.22);
    padding: 8px 12px;
    border-radius: 99px;
    font-size: 13px;
}
.hero-logo {
    background: #f8f6ef;
    border-radius: 24px;
    padding: 25px;
    text-align: center;
}
.hero-logo img {
    width: 100%;
    max-width: 350px;
    max-height: 310px;
    object-fit: contain;
}

.stats {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 16px;
    margin: 20px 0 65px;
}
.stat {
    background: #fff;
    border: 1px solid #e4e2da;
    border-radius: 18px;
    padding: 24px;
}
.stat strong {
    display: block;
    color: #174d40;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 29px;
}
.stat span { color: #68746f; font-size: 13px; }

.section {
    padding: 50px 0;
    scroll-margin-top: 30px;
}
.section-soft {
    background: #edf3ef;
    border-radius: 28px;
    padding: 45px;
    margin: 25px 0;
}
.section-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 35px;
    color: #174d40;
    margin: 0 0 12px;
}
.section-title em { color: #c68c43; font-style: normal; }
.section-desc {
    color: #68746f;
    line-height: 1.75;
    max-width: 850px;
}
.cards {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 17px;
    margin-top: 28px;
}
.card {
    background: #fff;
    border: 1px solid #e4e2da;
    border-radius: 19px;
    padding: 24px;
    min-height: 170px;
}
.card .icon { font-size: 30px; margin-bottom: 13px; }
.card h3 {
    margin: 0 0 9px;
    color: #174d40;
    font-size: 18px;
}
.card p {
    margin: 0;
    color: #68746f;
    line-height: 1.65;
    font-size: 14px;
}

.target-grid, .digital-grid {
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 14px;
    margin-top: 25px;
}
.target-item, .digital-item {
    background: #fff;
    border: 1px solid #e4e2da;
    border-radius: 16px;
    padding: 18px;
}
.target-item b, .digital-item b { color: #174d40; }
.target-item p, .digital-item span {
    display: block;
    color: #68746f;
    margin: 7px 0 0;
    line-height: 1.55;
    font-size: 14px;
}

.steps {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 13px;
    margin-top: 25px;
}
.step {
    background: #fff;
    border: 1px solid #e4e2da;
    border-radius: 16px;
    padding: 18px;
}
.step-number {
    color: #c68c43;
    font-weight: 800;
    font-size: 13px;
}
.step h3 { color: #174d40; font-size: 16px; margin: 8px 0; }
.step p { color: #68746f; font-size: 13px; line-height: 1.55; margin: 0; }

.price-box {
    background: #174d40;
    color: #fff;
    border-radius: 25px;
    padding: 42px;
    margin-top: 25px;
}
.price-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 35px;
    align-items: center;
}
.price-label { color: #bcd5cb; font-size: 14px; }
.price-main {
    color: #f2c36b;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 47px;
    font-weight: 800;
    margin: 7px 0;
}
.price-note { color: #e6eee9; line-height: 1.7; }
.price-note b { color: #fff; }
.price-side {
    background: rgba(255,255,255,.09);
    border-radius: 18px;
    padding: 22px;
}
.price-side h3 { margin-top: 0; color: #fff; }
.price-side p { color: #d9e6e0; line-height: 1.6; font-size: 14px; }

.footer {
    border-top: 1px solid #dddcd4;
    margin-top: 55px;
    padding: 30px 0;
    color: #68746f;
}
.footer-brand {
    display: flex;
    align-items: center;
    gap: 15px;
}
.footer-brand img {
    width: 50px;
    height: 50px;
    object-fit: contain;
}
.footer-brand b { color: #174d40; }
.footer-logos { display:flex; align-items:center; gap:10px; }

@media (max-width: 850px) {
    .ru-header-inner, .hero-grid, .price-grid { grid-template-columns: 1fr; display:grid; }
    .ru-header-inner { display:flex; flex-direction:column; align-items:flex-start; }
    .ru-nav { justify-content:flex-start; }
    .hero { padding: 38px 25px; }
    .stats, .cards, .target-grid, .digital-grid { grid-template-columns: 1fr; }
    .steps { grid-template-columns: repeat(2,1fr); }
    .section-soft { padding: 28px 20px; }
}

/* ============================================================
   STYLING WIDGET NATIVE STREAMLIT (Login/Daftar, dsb)
   Supaya menyatu dengan tema krem-hijau, bukan tema gelap default
   ============================================================ */

/* Expander "Login / Daftar Peserta" */
div[data-testid="stExpander"] {
    background: #fff;
    border: 1px solid #e4e2da;
    border-radius: 19px;
    overflow: hidden;
    margin: 10px 0 20px;
}
div[data-testid="stExpander"] summary {
    background: #edf3ef !important;
    padding: 14px 18px;
}
div[data-testid="stExpander"] summary span,
div[data-testid="stExpander"] summary p {
    color: #174d40 !important;
    font-weight: 700 !important;
}
div[data-testid="stExpander"] > div {
    background: #fff;
    padding: 20px 18px;
}

/* Semua label & teks di dalam widget form */
div[data-testid="stExpander"] label,
div[data-testid="stExpander"] p,
div[data-testid="stExpander"] span {
    color: #17352e !important;
}

/* Input teks & password */
div[data-testid="stTextInput"] input {
    background: #f8f6ef !important;
    border: 1px solid #cfd6cf !important;
    border-radius: 10px !important;
    color: #17352e !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #174d40 !important;
    box-shadow: 0 0 0 1px #174d40 !important;
}

/* Selectbox (Kategori Peserta) */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #f8f6ef !important;
    border: 1px solid #cfd6cf !important;
    border-radius: 10px !important;
    color: #17352e !important;
}

/* Radio (Login / Daftar) */
div[data-testid="stRadio"] label span {
    color: #17352e !important;
}

/* Checkbox (persetujuan) */
div[data-testid="stCheckbox"] label span {
    color: #17352e !important;
}

/* Tombol umum (Masuk, Daftar, Keluar) */
.stButton button {
    background: #174d40 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}
.stButton button:hover {
    background: #123c32 !important;
    color: #fff !important;
}

/* Tombol link platform (WhatsApp, Zoom, dst) */
.stLinkButton a {
    background: #174d40 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
}
.stLinkButton a:hover {
    background: #123c32 !important;
}

/* Alert bawaan Streamlit (error, success, warning) biar tidak nabrak tema gelap */
div[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* Heading "Akses Platform Ruang Usaha" biar konsisten dgn section-title lain */
h3 {
    color: #174d40;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# TOP BAR + HEADER — satu blok HTML utuh
# ============================================================
section_html(f"""
<div class="ru-topbar">
    Program Ruang Usaha
    <b>DISKON 30% UNTUK 50 PESERTA PERTAMA</b>
    <span> • Harga normal Rp150.000</span>
</div>

<div class="ru-header">
    <div class="ru-header-inner">
        <div class="ru-brand">
            {logo_html}
            <div>
                <div class="ru-brand-name">Ruang Usaha</div>
                <div class="ru-brand-tagline">Belajar, Berbagi, dan Bertumbuh Bersama</div>
            </div>
        </div>
        <div class="ru-nav">
            <a href="#beranda">Beranda</a>
            <a href="#profil">Profil</a>
            <a href="#layanan">Layanan</a>
            <a href="#target">Target</a>
            <a href="#operasional">Operasional</a>
            <a href="#digital">Digital</a>
            <a href="#harga">Harga</a>
        </div>
    </div>
</div>
""")

# ============================================================
# LOGIN / DAFTAR
# ============================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

with st.expander(
    "👤 " + (
        f"Peserta: {st.session_state.user_name}"
        if st.session_state.logged_in
        else "Login / Daftar Peserta"
    )
):
    if st.session_state.logged_in:
        st.success(f"Selamat datang, {st.session_state.user_name}!")
        st.caption(
            "Login pada versi ini masih berupa simulasi. "
            "Untuk akun permanen diperlukan database."
        )
        if st.button("Keluar", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.rerun()
    else:
        mode = st.radio("Akun", ["Login", "Daftar"], horizontal=True)
        if mode == "Login":
            identity = st.text_input("Email / Nomor WhatsApp")
            password = st.text_input("Kata Sandi", type="password")
            if st.button("🔐 Masuk", use_container_width=True):
                if not identity.strip():
                    st.error("Email atau nomor WhatsApp wajib diisi.")
                elif len(password) < 6:
                    st.error("Kata sandi minimal 6 karakter.")
                else:
                    st.session_state.logged_in = True
                    st.session_state.user_name = identity.split("@")[0]
                    st.rerun()
        else:
            name = st.text_input("Nama Lengkap")
            participant = st.selectbox(
                "Kategori Peserta",
                [
                    "Mahasiswa yang sedang menjalankan usaha",
                    "UMKM baru memulai usaha",
                    "UMKM yang sedang mengembangkan usaha",
                    "Pelaku usaha yang belum memiliki pencatatan keuangan",
                    "UMKM yang ingin meningkatkan pemasaran",
                    "Calon wirausaha",
                ],
            )
            email = st.text_input("Email")
            whatsapp = st.text_input("Nomor WhatsApp")
            password = st.text_input("Kata Sandi", type="password")
            agreement = st.checkbox("Saya menyetujui pendaftaran Ruang Usaha.")
            if st.button("🚀 Daftar", use_container_width=True):
                if not name.strip() or not email.strip() or not whatsapp.strip():
                    st.error("Nama, email, dan nomor WhatsApp wajib diisi.")
                elif len(password) < 6:
                    st.error("Kata sandi minimal 6 karakter.")
                elif not agreement:
                    st.warning("Centang persetujuan pendaftaran terlebih dahulu.")
                else:
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.success(f"Pendaftaran berhasil. Selamat datang, {name}!")
                    st.rerun()

# ============================================================
# HERO
# ============================================================
section_html(f"""
<section id="beranda" class="hero">
    <div class="hero-grid">
        <div>
            <div class="eyebrow">Jasa Layanan Kelas & Pendampingan UMKM</div>
            <h1>Belajar, Berbagi, dan <em>Bertumbuh Bersama.</em></h1>
            <p>
                Ruang Usaha merupakan wadah pembelajaran dan pendampingan bisnis
                bagi UMKM, calon wirausaha, dan mahasiswa yang menjalankan usaha.
                Pembelajaran diarahkan agar materi dapat langsung diterapkan
                pada usaha masing-masing.
            </p>
            <div class="hero-points">
                <span>✓ Kelas Bisnis</span>
                <span>✓ Pendampingan</span>
                <span>✓ Curhat Usaha</span>
                <span>✓ Praktik Langsung</span>
                <span>✓ Komunitas</span>
            </div>
        </div>
        <div class="hero-logo">
            {logo_html}
        </div>
    </div>
</section>
""")

section_html("""
<div class="stats">
    <div class="stat">
        <strong>Rp150.000</strong>
        <span>Harga normal per kegiatan</span>
    </div>
    <div class="stat">
        <strong>30%</strong>
        <span>Diskon untuk 50 peserta pertama</span>
    </div>
    <div class="stat">
        <strong>5 Hari</strong>
        <span>Jadwal kegiatan sesuai konsep operasional</span>
    </div>
</div>
""")

# ============================================================
# PROFIL
# ============================================================
section_html("""
<section id="profil" class="section">
    <h2 class="section-title">Tentang <em>Ruang Usaha</em></h2>
    <p class="section-desc">
        Ruang Usaha hadir sebagai layanan edukasi dan pendampingan bisnis yang
        menggabungkan pembelajaran, praktik, konsultasi, komunitas, dan dukungan
        digital. Tujuannya membantu peserta memahami usaha secara lebih terarah
        dan menerapkan materi pada kondisi usahanya sendiri.
    </p>
    <div class="cards">
        <div class="card">
            <div class="icon">🎯</div>
            <h3>Pembelajaran Praktis</h3>
            <p>Materi bisnis disampaikan dengan pendekatan yang mudah dipahami dan diarahkan pada praktik.</p>
        </div>
        <div class="card">
            <div class="icon">🤝</div>
            <h3>Pendampingan</h3>
            <p>Peserta mendapatkan ruang untuk menyampaikan masalah usaha dan memperoleh arahan.</p>
        </div>
        <div class="card">
            <div class="icon">🌱</div>
            <h3>Bertumbuh Bersama</h3>
            <p>Komunitas menjadi tempat berbagi pengalaman, masalah, solusi, dan peluang kolaborasi.</p>
        </div>
    </div>
</section>
""")

# ============================================================
# LAYANAN
# ============================================================
section_html("""
<section id="layanan" class="section section-soft">
    <h2 class="section-title">Layanan <em>Ruang Usaha</em></h2>
    <p class="section-desc">Layanan disusun untuk menjawab kebutuhan pembelajaran dan pendampingan pelaku usaha.</p>
    <div class="cards">
        <div class="card">
            <div class="icon">📚</div>
            <h3>Kelas Edukasi Bisnis Dasar</h3>
            <p>Materi keuangan, pemasaran, penentuan harga, perencanaan, dan pengembangan usaha.</p>
        </div>
        <div class="card">
            <div class="icon">🧑‍🏫</div>
            <h3>Pendampingan & Konsultasi</h3>
            <p>Pendampingan disesuaikan dengan kondisi dan kebutuhan usaha peserta.</p>
        </div>
        <div class="card">
            <div class="icon">💬</div>
            <h3>Forum Diskusi & Komunitas</h3>
            <p>Ruang untuk berbagi pengalaman, masalah usaha, solusi, dan kolaborasi.</p>
        </div>
        <div class="card">
            <div class="icon">▶️</div>
            <h3>Pembelajaran Digital & Dokumentasi</h3>
            <p>Materi dan dokumentasi kegiatan dapat didukung melalui platform digital.</p>
        </div>
        <div class="card">
            <div class="icon">📈</div>
            <h3>Program Pengembangan Berkelanjutan</h3>
            <p>Peserta diarahkan untuk melakukan evaluasi dan pengembangan usaha secara berkelanjutan.</p>
        </div>
        <div class="card">
            <div class="icon">🗣️</div>
            <h3>Curhat Usaha</h3>
            <p>Sesi untuk menyampaikan kendala usaha dan mendiskusikannya secara langsung.</p>
        </div>
    </div>
</section>
""")

# ============================================================
# TARGET
# ============================================================
section_html("""
<section id="target" class="section">
    <h2 class="section-title">Target <em>Peserta</em></h2>
    <p class="section-desc">Ruang Usaha ditujukan untuk peserta yang membutuhkan pembelajaran dan pendampingan usaha.</p>
    <div class="target-grid">
        <div class="target-item"><b>01. Mahasiswa yang menjalankan usaha</b><p>Membutuhkan dasar pengelolaan dan pengembangan usaha.</p></div>
        <div class="target-item"><b>02. UMKM baru memulai usaha</b><p>Membutuhkan fondasi bisnis dan arahan awal.</p></div>
        <div class="target-item"><b>03. UMKM yang sedang berkembang</b><p>Membutuhkan strategi untuk meningkatkan dan mengembangkan usaha.</p></div>
        <div class="target-item"><b>04. Usaha tanpa pencatatan keuangan</b><p>Membutuhkan pemahaman pencatatan dan pengelolaan keuangan.</p></div>
        <div class="target-item"><b>05. UMKM yang ingin meningkatkan pemasaran</b><p>Membutuhkan strategi pemasaran dan pemanfaatan media digital.</p></div>
        <div class="target-item"><b>06. Calon wirausaha</b><p>Membutuhkan bekal sebelum memulai usaha.</p></div>
    </div>
</section>
""")

# ============================================================
# OPERASIONAL / CARA BELAJAR
# ============================================================
section_html("""
<section id="operasional" class="section section-soft">
    <h2 class="section-title">Cara <em>Pembelajaran</em></h2>
    <p class="section-desc">
        Kegiatan dirancang melalui alur pembelajaran yang menggabungkan materi,
        diskusi, praktik, evaluasi, dan pendampingan.
    </p>
    <div class="steps">
        <div class="step"><div class="step-number">01</div><h3>Pembukaan</h3><p>Pengenalan kegiatan dan tujuan pembelajaran.</p></div>
        <div class="step"><div class="step-number">02</div><h3>Materi</h3><p>Penyampaian materi bisnis yang relevan.</p></div>
        <div class="step"><div class="step-number">03</div><h3>Curhat Usaha</h3><p>Peserta menyampaikan kondisi dan kendala usaha.</p></div>
        <div class="step"><div class="step-number">04</div><h3>Diskusi</h3><p>Membahas masalah dan alternatif solusi.</p></div>
        <div class="step"><div class="step-number">05</div><h3>Praktik</h3><p>Peserta menerapkan materi secara langsung.</p></div>
        <div class="step"><div class="step-number">06</div><h3>Tanya Jawab</h3><p>Memperjelas materi dan pengalaman peserta.</p></div>
        <div class="step"><div class="step-number">07</div><h3>Evaluasi</h3><p>Melihat pemahaman dan hasil praktik.</p></div>
        <div class="step"><div class="step-number">08</div><h3>Penutup</h3><p>Kesimpulan dan arahan tindak lanjut.</p></div>
    </div>
</section>
""")

# ============================================================
# PRAKTIK
# ============================================================
section_html("""
<section class="section">
    <h2 class="section-title">Contoh <em>Praktik</em></h2>
    <div class="cards">
        <div class="card"><div class="icon">🧾</div><h3>Pencatatan Keuangan</h3><p>Latihan mencatat transaksi usaha agar kondisi keuangan lebih mudah dipahami.</p></div>
        <div class="card"><div class="icon">🧮</div><h3>Biaya Produksi</h3><p>Latihan mengidentifikasi dan menghitung biaya yang berkaitan dengan produk.</p></div>
        <div class="card"><div class="icon">🏷️</div><h3>Harga Jual</h3><p>Latihan menentukan harga berdasarkan biaya dan pertimbangan usaha.</p></div>
        <div class="card"><div class="icon">📣</div><h3>Pemasaran</h3><p>Menyusun ide pemasaran dan konten media sosial untuk usaha.</p></div>
        <div class="card"><div class="icon">📝</div><h3>Rencana Usaha</h3><p>Menyusun ide dan rencana pengembangan usaha.</p></div>
        <div class="card"><div class="icon">🔍</div><h3>Evaluasi Usaha</h3><p>Meninjau hasil praktik dan menentukan langkah perbaikan.</p></div>
    </div>
</section>
""")

# ============================================================
# DIGITAL
# ============================================================
section_html("""
<section id="digital" class="section section-soft">
    <h2 class="section-title">Ekosistem <em>Digital</em></h2>
    <p class="section-desc">Platform digital mendukung komunikasi, pembelajaran, dokumentasi, dan promosi Ruang Usaha.</p>
    <div class="digital-grid">
        <div class="digital-item"><b>🌐 Website</b><span>Pusat informasi program dan kegiatan Ruang Usaha.</span></div>
        <div class="digital-item"><b>💬 WhatsApp Community</b><span>Komunikasi peserta, diskusi, dan koordinasi.</span></div>
        <div class="digital-item"><b>💻 Zoom</b><span>Pembelajaran dan pendampingan secara daring.</span></div>
        <div class="digital-item"><b>▶️ YouTube</b><span>Dokumentasi kegiatan dan materi pembelajaran.</span></div>
        <div class="digital-item"><b>📸 Instagram</b><span>Promosi dan edukasi bisnis.</span></div>
        <div class="digital-item"><b>🎵 TikTok</b><span>Video edukasi singkat dan konten promosi.</span></div>
        <div class="digital-item"><b>📘 Facebook</b><span>Media informasi dan promosi.</span></div>
        <div class="digital-item"><b>🤝 Komunitas UMKM</b><span>Jaringan berbagi pengalaman dan kolaborasi.</span></div>
    </div>
</section>
""")

# Tombol platform menggunakan URL placeholder yang bisa diganti pemilik usaha.
st.markdown("### Akses Platform Ruang Usaha")
c1,c2,c3,c4 = st.columns(4)
with c1:
    st.link_button("💬 WhatsApp", "https://chat.whatsapp.com/Bew1bpB1vxYGge8z1PMmrX", use_container_width=True)
with c2:
    st.link_button("💻 Zoom", "https://us05web.zoom.us/j/3799765498?pwd=Y16zpswb0ymqkgTa1U46jCrn4YlVkX.1", use_container_width=True)
with c3:
    st.link_button("▶️ YouTube", "https://youtube.com/@ruangusaha-q1g?si=jITpG2S7u1uLwUE1", use_container_width=True)
with c4:
    st.link_button("📸 Instagram", "https://www.instagram.com/ruangusaha_109?stkn=MWNtaHY0ZWN4YXdhYw==", use_container_width=True)

# ============================================================
# HARGA
# ============================================================
section_html("""
<section id="harga" class="section">
    <h2 class="section-title">Harga & <em>Promo</em></h2>
    <div class="price-box">
        <div class="price-grid">
            <div>
                <div class="price-label">Harga Normal</div>
                <div class="price-main">Rp150.000</div>
                <div class="price-note">
                    <b>DISKON 30% UNTUK 50 PESERTA PERTAMA</b><br>
                    Promo pengguna awal sesuai ketentuan dalam proposal.
                </div>
            </div>
            <div class="price-side">
                <h3>🎉 Promo Pengguna Awal</h3>
                <p>
                    Program memberikan diskon <b>30%</b> untuk
                    <b>50 peserta pertama</b>. Harga normal yang dicantumkan
                    dalam proposal adalah <b>Rp150.000</b>.
                </p>
                <p>
                    Catatan: proposal juga mencantumkan angka Rp50.000 sebagai
                    harga promo. Angka tersebut dipertahankan sebagai informasi
                    dokumen, meskipun secara hitungan Rp150.000 dikurangi 30%
                    menghasilkan Rp105.000.
                </p>
            </div>
        </div>
    </div>
</section>
""")

# ============================================================
# ORGANISASI
# ============================================================
section_html("""
<section class="section">
    <h2 class="section-title">Tim <em>Pengelola</em></h2>
    <div class="cards">
        <div class="card"><div class="icon">👤</div><h3>Pengelola Utama</h3><p>Mengatur arah program, koordinasi, keputusan, dan keberlangsungan Ruang Usaha.</p></div>
        <div class="card"><div class="icon">🧑‍🏫</div><h3>Tim Pembelajaran & Pendampingan</h3><p>Menyiapkan materi, pelaksanaan kelas, pendampingan, dan evaluasi pembelajaran.</p></div>
        <div class="card"><div class="icon">💻</div><h3>Tim Operasional & Digital</h3><p>Mendukung administrasi kegiatan serta pengelolaan platform digital dan komunikasi.</p></div>
    </div>
</section>
""")

# ============================================================
# FOOTER
# ============================================================
unimed_html = (
    f'<img src="{LOGO_UNIMED}" alt="Logo UNIMED">'
    if LOGO_UNIMED else ""
)
section_html(f"""
<div class="footer">
    <div class="footer-brand">
        <div class="footer-logos">
            {logo_html}
            {unimed_html}
        </div>
        <div>
            <b>Ruang Usaha</b><br>
            <span>Belajar, Berbagi, dan Bertumbuh Bersama.</span><br>
            <small>Platform pembelajaran dan pendampingan UMKM.</small>
        </div>
    </div>
</div>
""")