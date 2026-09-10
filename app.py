import streamlit as st
from pathlib import Path
import base64

# ============================================================
# RUANG USAHA
# Berdasarkan Proposal Bisnis terbaru - Kelompok 3
# Konsep: "Belajar, Berbagi, dan Bertumbuh Bersama"
# ============================================================

st.set_page_config(
    page_title="Ruang Usaha | Belajar, Berbagi, dan Bertumbuh Bersama",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent

# ============================================================
# LINK PLATFORM
# GANTI DENGAN LINK ASLI RUANG USAHA
# ============================================================

LINKS = {
    "whatsapp": "https://chat.whatsapp.com/Bew1bpB1vxYGge8z1PMmrX",
    "zoom": "https://zoom.us/",
    "youtube": "https://youtube.com/",
    "instagram": "https://instagram.com/",
    "tiktok": "https://tiktok.com/",
    "facebook": "https://facebook.com/",
}

# ============================================================
# ASSET
# Mendukung folder Assets maupun assets
# ============================================================

def find_asset(filename):
    possible = [
        BASE_DIR / "Assets" / filename,
        BASE_DIR / "assets" / filename,
        BASE_DIR / filename,
    ]

    for item in possible:
        if item.exists():
            return item

    for item in BASE_DIR.rglob("*"):
        if item.is_file() and item.name.lower() == filename.lower():
            return item

    return None


def get_image_data(filename):
    path = find_asset(filename)
    if not path:
        return ""

    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(path.suffix.lower(), "image/png")

    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


LOGO_RUANG = get_image_data("logo-ruang-usaha.png")
LOGO_UNIMED = get_image_data("logo-unimed.png")


# ============================================================
# SESSION
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

:root {
    --green: #174d40;
    --green-dark: #10392f;
    --green-light: #e8f1ec;
    --cream: #f8f6ef;
    --gold: #c68c43;
    --text: #17352e;
    --muted: #68746f;
    --line: #deddd4;
    --white: #ffffff;
}

.stApp {
    background: var(--cream);
    color: var(--text);
    font-family: "DM Sans", sans-serif;
}

.block-container {
    max-width: 1450px !important;
    padding: 0 5vw 4rem !important;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"],
footer {
    display: none !important;
}

html {
    scroll-behavior: smooth;
}

/* ---------------- TOP BAR ---------------- */

.ru-topbar {
    margin: 0 -5vw;
    padding: 10px 5vw;
    background: var(--green);
    color: white;
    text-align: center;
    font-size: 13px;
}

.ru-topbar b {
    color: #f2d092;
}

/* ---------------- HEADER ---------------- */

.ru-header {
    padding: 20px 0;
    border-bottom: 1px solid var(--line);
}

.ru-header-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 30px;
}

.ru-brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.ru-brand img {
    width: 55px;
    height: 55px;
    object-fit: contain;
}

.ru-brand-name {
    font-family: "Plus Jakarta Sans", sans-serif;
    color: var(--green);
    font-size: 22px;
    font-weight: 800;
}

.ru-brand-tagline {
    color: var(--muted);
    font-size: 11px;
    margin-top: 2px;
}

.ru-nav {
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
    justify-content: flex-end;
}

.ru-nav a {
    color: #40534d;
    text-decoration: none;
    padding: 9px 12px;
    border-radius: 9px;
    font-size: 13px;
    font-weight: 700;
}

.ru-nav a:hover {
    background: var(--green-light);
    color: var(--green);
}

/* ---------------- HERO ---------------- */

.ru-hero {
    margin-top: 34px;
    padding: 70px 7%;
    border-radius: 30px;
    background: var(--green);
    color: white;
}

.ru-eyebrow {
    display: inline-block;
    background: #e1eee7;
    color: var(--green);
    padding: 8px 13px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 20px;
}

.ru-hero h1 {
    font-family: "Plus Jakarta Sans", sans-serif;
    color: white;
    font-size: clamp(40px, 5vw, 70px);
    line-height: 1.05;
    margin: 0 0 20px;
}

.ru-hero h1 em {
    color: #e2b35f;
    font-style: normal;
}

.ru-hero p {
    color: #dce9e4;
    font-size: 16px;
    line-height: 1.8;
    max-width: 760px;
}

.ru-hero-highlight {
    margin-top: 20px;
    color: #f1f5f2;
    font-size: 13px;
}

.ru-logo-hero {
    text-align: center;
}

.ru-logo-hero img {
    width: min(100%, 390px);
    max-height: 360px;
    object-fit: contain;
}

/* ---------------- STATS ---------------- */

.ru-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 20px 0 20px;
}

.ru-stat {
    background: white;
    border: 1px solid var(--line);
    border-radius: 17px;
    padding: 20px;
}

.ru-stat strong {
    display: block;
    color: var(--green);
    font-family: "Plus Jakarta Sans", sans-serif;
    font-size: 25px;
}

.ru-stat span {
    color: var(--muted);
    font-size: 12px;
}

/* ---------------- SECTIONS ---------------- */

.ru-section {
    padding: 80px 0;
    scroll-margin-top: 30px;
}

.ru-soft {
    margin-left: -5vw;
    margin-right: -5vw;
    padding-left: 5vw;
    padding-right: 5vw;
    background: #f0f3ed;
}

.ru-label {
    color: var(--gold);
    font-size: 11px;
    font-weight: 900;
    letter-spacing: .09em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.ru-section h2 {
    font-family: "Plus Jakarta Sans", sans-serif;
    color: var(--green);
    font-size: clamp(31px, 4vw, 48px);
    line-height: 1.15;
    margin: 0 0 18px;
}

.ru-section h2 em {
    color: var(--gold);
    font-style: normal;
}

.ru-copy {
    color: var(--muted);
    line-height: 1.85;
    font-size: 14px;
}

/* ---------------- CARDS ---------------- */

.ru-card {
    height: 100%;
    box-sizing: border-box;
    background: white;
    border: 1px solid var(--line);
    border-radius: 21px;
    padding: 25px;
}

.ru-card-number {
    color: var(--gold);
    font-size: 12px;
    font-weight: 900;
}

.ru-card h3 {
    color: var(--green);
    font-family: "Plus Jakarta Sans", sans-serif;
    margin: 11px 0 8px;
}

.ru-card p {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.7;
}

/* ---------------- SERVICES ---------------- */

.ru-service {
    height: 100%;
    min-height: 270px;
    box-sizing: border-box;
    background: white;
    border: 1px solid var(--line);
    border-radius: 21px;
    padding: 25px;
}

.ru-service.featured {
    background: var(--green);
}

.ru-service.featured h3,
.ru-service.featured p {
    color: white;
}

.ru-service-number {
    color: var(--gold);
    font-weight: 900;
    font-size: 11px;
}

.ru-service h3 {
    color: var(--green);
    font-family: "Plus Jakarta Sans", sans-serif;
    font-size: 17px;
    line-height: 1.35;
    margin: 14px 0 9px;
}

.ru-service p {
    color: var(--muted);
    line-height: 1.7;
    font-size: 13px;
}

.ru-tag {
    display: inline-block;
    margin-top: 12px;
    padding: 6px 10px;
    border-radius: 999px;
    background: var(--green-light);
    color: var(--green);
    font-size: 10px;
    font-weight: 900;
}

/* ---------------- LEARNING STEPS ---------------- */

.ru-step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 20px 0;
    border-bottom: 1px solid var(--line);
}

.ru-step-no {
    min-width: 40px;
    height: 40px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: var(--green);
    color: white;
    font-size: 12px;
    font-weight: 900;
}

.ru-step h3 {
    color: var(--green);
    font-family: "Plus Jakarta Sans", sans-serif;
    font-size: 16px;
    margin: 0 0 5px;
}

.ru-step p {
    color: var(--muted);
    margin: 0;
    line-height: 1.65;
    font-size: 13px;
}

/* ---------------- DIGITAL ---------------- */

.ru-digital {
    text-align: center;
    min-height: 150px;
    background: white;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 20px 12px;
}

.ru-digital-icon {
    font-size: 26px;
    margin-bottom: 7px;
}

.ru-digital h3 {
    color: var(--green);
    margin: 0 0 5px;
    font-size: 14px;
}

.ru-digital p {
    color: var(--muted);
    font-size: 11px;
    line-height: 1.5;
    margin: 0;
}

/* ---------------- TARGET ---------------- */

.ru-target {
    background: var(--green);
    border-radius: 28px;
    padding: 55px 7%;
}

.ru-target h2 {
    color: white;
}

.ru-target p {
    color: #dce9e4;
    line-height: 1.8;
}

.ru-target-item {
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,.15);
    color: white;
}

/* ---------------- PRICE ---------------- */

.ru-price {
    background: white;
    border: 1px solid var(--line);
    border-radius: 25px;
    padding: 35px;
    text-align: center;
}

.ru-price-main {
    color: var(--green);
    font-family: "Plus Jakarta Sans", sans-serif;
    font-size: 48px;
    font-weight: 800;
}

.ru-price-note {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.6;
}

/* ---------------- CTA ---------------- */

.ru-cta {
    padding: 55px;
    text-align: center;
    border-radius: 28px;
    background: #e8efe9;
}

/* ---------------- FOOTER ---------------- */

.ru-footer {
    margin: 60px -5vw -4rem;
    padding: 45px 5vw;
    background: #10392f;
    color: white;
}

.ru-footer-brand {
    display: flex;
    align-items: center;
    gap: 13px;
}

.ru-footer-brand img {
    width: 55px;
    height: 55px;
    object-fit: contain;
}

.ru-footer h3 {
    color: white;
    font-family: "Plus Jakarta Sans", sans-serif;
    margin: 0;
}

.ru-footer p {
    color: #cbdcd5;
    font-size: 13px;
    line-height: 1.7;
}

.ru-footer-unimed {
    width: 65px;
    height: 65px;
    object-fit: contain;
    background: white;
    border-radius: 12px;
    padding: 4px;
}

.ru-footer-bottom {
    border-top: 1px solid rgba(255,255,255,.15);
    margin-top: 30px;
    padding-top: 20px;
    color: #b7cdc4;
    font-size: 11px;
}

/* ---------------- STREAMLIT / LOGIN ---------------- */

.stApp {
    background: #f8f6ef !important;
}

/* Tombol */
div[data-testid="stButton"] > button,
div[data-testid="stLinkButton"] a {
    border-radius: 11px !important;
    font-weight: 800 !important;
    min-height: 45px !important;
}

div[data-testid="stButton"] > button {
    background: #174d40 !important;
    color: #ffffff !important;
    border: 1px solid #174d40 !important;
}

div[data-testid="stButton"] > button p {
    color: #ffffff !important;
}

/* Expander login */
div[data-testid="stExpander"] {
    background: #ffffff !important;
    border: 1px solid #dddcd4 !important;
    border-radius: 18px !important;
    overflow: hidden !important;
    margin: 18px 0 30px !important;
}

div[data-testid="stExpander"] details {
    background: #ffffff !important;
}

div[data-testid="stExpander"] summary {
    background: #ffffff !important;
    color: #17352e !important;
    padding: 17px 19px !important;
    border-bottom: 1px solid #e8e6de !important;
}

div[data-testid="stExpander"] summary *,
div[data-testid="stExpander"] summary p,
div[data-testid="stExpander"] summary span {
    color: #17352e !important;
    font-weight: 800 !important;
}

/* Semua label form */
div[data-testid="stTextInput"] label,
div[data-testid="stTextInput"] label *,
div[data-testid="stSelectbox"] label,
div[data-testid="stSelectbox"] label *,
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label *,
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label * {
    color: #17352e !important;
    font-weight: 700 !important;
}

/* Kolom text input BaseWeb */
div[data-testid="stTextInput"] div[data-baseweb="input"] {
    background: #ffffff !important;
    border: 1.5px solid #d5ddd8 !important;
    border-radius: 11px !important;
    box-shadow: none !important;
}

div[data-testid="stTextInput"] div[data-baseweb="input"] > div {
    background: #ffffff !important;
}

div[data-testid="stTextInput"] input {
    background: #ffffff !important;
    color: #17352e !important;
    -webkit-text-fill-color: #17352e !important;
    caret-color: #17352e !important;
    font-size: 14px !important;
    min-height: 45px !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #8b9791 !important;
    -webkit-text-fill-color: #8b9791 !important;
    opacity: 1 !important;
}

div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
    border-color: #246b55 !important;
    box-shadow: 0 0 0 3px rgba(36,107,85,.10) !important;
}

/* Selectbox */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #17352e !important;
    border: 1.5px solid #d5ddd8 !important;
    border-radius: 11px !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #17352e !important;
}

/* Radio */
div[data-testid="stRadio"] > div {
    color: #17352e !important;
}

div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p {
    color: #17352e !important;
}

/* Checkbox */
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label p {
    color: #17352e !important;
}

/* Success/error/caption */
div[data-testid="stAlert"] {
    border-radius: 11px !important;
}

div[data-testid="stCaptionContainer"] p {
    color: #68746f !important;
}

@media (max-width: 900px) {
    .ru-header-inner {
        align-items: flex-start;
        flex-direction: column;
    }

    .ru-nav {
        justify-content: flex-start;
    }

    .ru-stats {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {
    .ru-stats {
        grid-template-columns: 1fr;
    }

    .ru-hero {
        padding: 45px 7%;
    }

    .ru-section {
        padding: 55px 0;
    }

    .ru-cta {
        padding: 35px 20px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# TOP BAR + HEADER
# ============================================================

logo = (
    f'<img src="{LOGO_RUANG}" alt="Logo Ruang Usaha">'
    if LOGO_RUANG
    else '<span style="font-size:40px">🌱</span>'
)

st.markdown(
    f"""
<div class="ru-topbar">
    Program Ruang Usaha
    <b>DISKON 30% UNTUK 50 PESERTA PERTAMA</b>
    <span> • Harga normal Rp150.000</span>
</div>

<div class="ru-header">
    <div class="ru-header-inner">
        <div class="ru-brand">
            {logo}
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
""",
    unsafe_allow_html=True,
)


# ============================================================
# ============================================================
# LOGIN / REGISTER
# ============================================================

st.markdown(
    """
<div style="
    margin-top:24px;
    padding:28px 30px 8px;
    background:#ffffff;
    border:1px solid #e4e2da;
    border-radius:22px 22px 0 0;
">
    <div style="
        display:inline-block;
        padding:7px 12px;
        background:#e8f1ec;
        color:#174d40;
        border-radius:999px;
        font-size:11px;
        font-weight:800;
        text-transform:uppercase;
        letter-spacing:.05em;
    ">
        Area Peserta
    </div>

    <h2 style="
        margin:13px 0 7px;
        color:#174d40;
        font-family:'Plus Jakarta Sans',sans-serif;
        font-size:29px;
    ">
        Masuk atau Daftar di Ruang Usaha
    </h2>

    <p style="
        margin:0 0 16px;
        color:#68746f;
        font-size:14px;
        line-height:1.6;
    ">
        Akses kelas, pendampingan, komunitas, dan informasi kegiatan Ruang Usaha.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

login_col, register_col = st.columns(2, gap="large")

with login_col:
    st.markdown(
        """
<div style="
    background:#ffffff;
    border:1px solid #e4e2da;
    border-radius:18px;
    padding:22px 23px 10px;
    margin-bottom:20px;
">
    <div style="font-size:25px;">🔐</div>
    <h3 style="color:#174d40;margin:7px 0 4px;">Login Peserta</h3>
    <p style="color:#68746f;font-size:13px;margin:0 0 15px;">
        Masuk menggunakan email atau nomor WhatsApp.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )

    with st.form("login_form", clear_on_submit=False):
        identity = st.text_input(
            "Email / Nomor WhatsApp",
            placeholder="contoh@email.com atau 08xxxxxxxxxx",
        )

        password = st.text_input(
            "Kata Sandi",
            type="password",
            placeholder="Masukkan kata sandi",
        )

        remember = st.checkbox("Ingat saya")

        login_submit = st.form_submit_button(
            "🔐 Masuk ke Ruang Usaha",
            use_container_width=True,
        )

    if login_submit:
        if not identity.strip():
            st.error("Email atau nomor WhatsApp wajib diisi.")
        elif len(password) < 6:
            st.error("Kata sandi minimal 6 karakter.")
        else:
            st.session_state.logged_in = True
            st.session_state.user_name = identity.split("@")[0]
            st.success("Login berhasil. Selamat datang di Ruang Usaha!")


with register_col:
    st.markdown(
        """
<div style="
    background:#174d40;
    border-radius:18px;
    padding:22px 23px 20px;
    margin-bottom:20px;
">
    <div style="font-size:25px;">🚀</div>
    <h3 style="color:#ffffff;margin:7px 0 4px;">Daftar Peserta</h3>
    <p style="color:#dce9e4;font-size:13px;margin:0;">
        Bergabung sebagai peserta Ruang Usaha.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )

    with st.form("register_form", clear_on_submit=False):
        name = st.text_input(
            "Nama Lengkap",
            placeholder="Nama lengkap",
        )

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

        email = st.text_input(
            "Email",
            placeholder="contoh@email.com",
        )

        whatsapp = st.text_input(
            "Nomor WhatsApp",
            placeholder="08xxxxxxxxxx",
        )

        password_register = st.text_input(
            "Kata Sandi",
            type="password",
            placeholder="Minimal 6 karakter",
        )

        agreement = st.checkbox(
            "Saya menyetujui pendaftaran Ruang Usaha."
        )

        register_submit = st.form_submit_button(
            "🚀 Buat Akun Peserta",
            use_container_width=True,
        )

    if register_submit:
        if len(name.strip()) < 3:
            st.error("Nama lengkap wajib diisi.")
        elif "@" not in email:
            st.error("Masukkan email yang valid.")
        elif len(whatsapp.strip()) < 9:
            st.error("Nomor WhatsApp belum valid.")
        elif len(password_register) < 6:
            st.error("Kata sandi minimal 6 karakter.")
        elif not agreement:
            st.warning("Centang persetujuan pendaftaran terlebih dahulu.")
        else:
            st.session_state.logged_in = True
            st.session_state.user_name = name.strip()
            st.success(
                f"Pendaftaran berhasil. Selamat datang, {name.strip()}!"
            )

if st.session_state.logged_in:
    st.markdown(
        f"""
<div style="
    margin:5px 0 28px;
    padding:13px 17px;
    background:#e8f1ec;
    border:1px solid #d1e2d9;
    border-radius:12px;
    color:#174d40;
    font-size:13px;
">
    👋 Kamu sedang masuk sebagai <b>{clean(st.session_state.user_name)}</b>.
    Login pada versi ini masih bersifat simulasi.
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("Keluar dari akun", key="logout_top"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()


# HERO
# ============================================================

st.markdown('<section id="beranda" class="ru-hero">', unsafe_allow_html=True)

c1, c2 = st.columns([1.5, .8], gap="large")

with c1:
    st.markdown(
        """
<div class="ru-eyebrow">Jasa layanan kelas & pendampingan UMKM</div>

<h1>Belajar, Berbagi, dan <em>Bertumbuh Bersama.</em></h1>

<p>
Ruang Usaha hadir sebagai wadah pembelajaran dan pendampingan bisnis
bagi pelaku UMKM maupun calon wirausaha. Materi tidak berhenti pada teori,
tetapi diarahkan untuk langsung diterapkan pada usaha masing-masing.
</p>

<div class="ru-hero-highlight">
✓ Kelas &nbsp;&nbsp; ✓ Pendampingan &nbsp;&nbsp; ✓ Curhat Usaha
&nbsp;&nbsp; ✓ Praktik langsung &nbsp;&nbsp; ✓ Komunitas
</div>
""",
        unsafe_allow_html=True,
    )

    b1, b2 = st.columns(2)
    with b1:
        st.link_button("Lihat Layanan →", "#layanan", use_container_width=True)
    with b2:
        st.link_button("Cara Pembelajaran", "#operasional", use_container_width=True)

with c2:
    if LOGO_RUANG:
        st.markdown(
            f"""
<div class="ru-logo-hero">
    <img src="{LOGO_RUANG}" alt="Logo Ruang Usaha">
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# RINGKASAN
# ============================================================

st.markdown(
    """
<div class="ru-stats">
    <div class="ru-stat">
        <strong>Rp150K</strong>
        <span>Harga sekitar per kegiatan</span>
    </div>
    <div class="ru-stat">
        <strong>30%</strong>
        <span>Diskon untuk 50 peserta pertama</span>
    </div>
    <div class="ru-stat">
        <strong>50</strong>
        <span>Kuota pengguna awal</span>
    </div>
    <div class="ru-stat">
        <strong>5 Hari</strong>
        <span>Interval kegiatan pembelajaran</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# PROFIL
# ============================================================

st.markdown(
    """
<section id="profil" class="ru-section">
<div class="ru-label">BAB II • Gambaran Umum Usaha</div>
""",
    unsafe_allow_html=True,
)

a1, a2 = st.columns([1, 1.15], gap="large")

with a1:
    st.markdown(
        """
<h2>Wadah belajar yang <em>dekat dengan masalah nyata.</em></h2>
""",
        unsafe_allow_html=True,
    )

with a2:
    st.markdown(
        """
<div class="ru-copy">
<p>
Ruang Usaha merupakan layanan edukasi dan pendampingan bisnis yang bergerak
dalam pengembangan kapasitas pelaku Usaha Mikro, Kecil, dan Menengah (UMKM).
</p>

<p>
Ruang Usaha membantu masyarakat yang sedang memulai usaha maupun pelaku usaha
yang ingin meningkatkan kemampuan dalam mengelola dan mengembangkan bisnisnya.
</p>

<p>
Pendekatannya menggabungkan <b>kelas, diskusi, pendampingan, praktik langsung,
Curhat Usaha, dan komunitas</b>, dengan dukungan teknologi digital.
</p>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("</section>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

profil_cards = [
    (
        "01",
        "Visi",
        "Menjadi wadah pembelajaran dan pendampingan bisnis berbasis digital yang membantu pelaku UMKM mengelola serta mengembangkan usaha secara mandiri, terarah, dan berkelanjutan.",
    ),
    (
        "02",
        "Pembelajaran Praktis",
        "Materi disampaikan dengan bahasa sederhana dan disertai praktik sehingga peserta dapat menerapkannya pada usaha masing-masing.",
    ),
    (
        "03",
        "Berbasis Komunitas",
        "Peserta dapat berbagi pengalaman, berdiskusi, menyampaikan kendala, dan menemukan solusi bersama mentor maupun pelaku usaha lain.",
    ),
]

for col, (num, title, desc) in zip([p1, p2, p3], profil_cards):
    with col:
        st.markdown(
            f"""
<div class="ru-card">
    <div class="ru-card-number">{num}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# LAYANAN
# ============================================================

st.markdown(
    """
<section id="layanan" class="ru-section ru-soft">
<div class="ru-label">Konsep & Layanan Usaha</div>
<h2>Layanan yang menghubungkan <em>ilmu dengan praktik.</em></h2>
<p class="ru-copy">
Berdasarkan proposal terbaru, Ruang Usaha memiliki lima layanan utama.
</p>
""",
    unsafe_allow_html=True,
)

services = [
    (
        "01",
        "Kelas Edukasi Bisnis Dasar",
        "Pencatatan keuangan sederhana, pengelolaan modal, strategi pemasaran, penentuan harga produk, dan perencanaan pengembangan usaha.",
        "Belajar",
        True,
    ),
    (
        "02",
        "Pendampingan & Konsultasi Usaha",
        "Membantu peserta memahami permasalahan usaha dan menemukan solusi yang sesuai dengan kondisi bisnis masing-masing.",
        "Pendampingan",
        False,
    ),
    (
        "03",
        "Forum Diskusi & Komunitas UMKM",
        "Ruang untuk berinteraksi, bertukar pengalaman, berbagi strategi, dan belajar dari pelaku usaha lain.",
        "Berbagi",
        False,
    ),
    (
        "04",
        "Pembelajaran Digital & Dokumentasi",
        "Website, WhatsApp Community, Zoom, YouTube, Instagram, TikTok, dan Facebook mendukung pembelajaran serta dokumentasi.",
        "Digital",
        False,
    ),
    (
        "05",
        "Program Pengembangan Berkelanjutan",
        "Pendampingan bertahap untuk membantu peserta terus meningkatkan kemampuan dan menghadapi tantangan pengembangan bisnis.",
        "Bertumbuh",
        False,
    ),
]

service_cols = st.columns(3)

for i, (num, title, desc, tag, featured) in enumerate(services):
    with service_cols[i % 3]:
        cls = "ru-service featured" if featured else "ru-service"
        st.markdown(
            f"""
<div class="{cls}">
    <div class="ru-service-number">{num}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
    <span class="ru-tag">{tag}</span>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown(
        """
<div class="ru-service">
    <div class="ru-service-number">SPECIAL SESSION</div>
    <h3>“Curhat Usaha”</h3>
    <p>
    Peserta dapat menceritakan kendala nyata yang sedang dihadapi.
    Masalah kemudian dibahas bersama berdasarkan materi yang sedang dipelajari,
    dengan arahan mentor dan pengalaman peserta lain.
    </p>
    <span class="ru-tag">Masalah nyata → diskusi → solusi → praktik</span>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# TARGET PASAR
# ============================================================

st.markdown(
    """
<section id="target" class="ru-section">
<div class="ru-label">Target Pasar</div>
<h2>Untuk siapa <em>Ruang Usaha?</em></h2>
<p class="ru-copy">
Target peserta disesuaikan dengan kebutuhan pelaku usaha pada tahap yang berbeda.
</p>
""",
    unsafe_allow_html=True,
)

targets = [
    (
        "UMKM Baru",
        "Pelaku UMKM yang baru memulai dan membutuhkan dasar pengelolaan keuangan, harga, pemasaran, dan kegiatan usaha.",
    ),
    (
        "UMKM Berkembang",
        "Usaha yang sudah berjalan tetapi masih menghadapi kendala keuangan, pemasaran, penjualan, atau pengambilan keputusan.",
    ),
    (
        "Belum Memiliki Pencatatan Keuangan",
        "Pelaku usaha yang belum mencatat transaksi secara teratur atau masih mencampur uang usaha dengan uang pribadi.",
    ),
    (
        "Ingin Meningkatkan Pemasaran",
        "Pelaku UMKM yang membutuhkan pembelajaran tentang pemasaran, media sosial, konten, dan cara memperkenalkan produk.",
    ),
    (
        "Calon Wirausaha",
        "Seseorang yang memiliki ide usaha dan ingin memahami hal-hal yang perlu dipersiapkan sebelum memulai bisnis.",
    ),
    (
        "Mahasiswa Berwirausaha",
        "Mahasiswa yang sedang menjalankan usaha dan membutuhkan pembelajaran maupun pendampingan dalam mengelola bisnis.",
    ),
]

target_cols = st.columns(3)

for i, (title, desc) in enumerate(targets):
    with target_cols[i % 3]:
        st.markdown(
            f"""
<div class="ru-card">
    <div class="ru-card-number">TARGET {i+1:02}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# OPERASIONAL / JADWAL PEMBELAJARAN
# ============================================================

st.markdown(
    """
<section id="operasional" class="ru-section ru-soft">
<div class="ru-label">BAB IV • Rencana Operasional</div>
<h2>Setiap pertemuan: <em>belajar, berbagi, praktik.</em></h2>
<p class="ru-copy">
Kegiatan dilakukan secara berkala setiap lima hari sekali. Satu pertemuan memiliki
satu topik utama yang dapat disesuaikan dengan kebutuhan dan masalah peserta.
</p>
""",
    unsafe_allow_html=True,
)

steps = [
    ("01", "Pembukaan & Pengenalan Topik", "Menjelaskan topik, tujuan, dan alasan materi penting bagi usaha."),
    ("02", "Penyampaian Materi", "Memberikan pemahaman dasar dengan bahasa sederhana dan contoh yang dekat dengan usaha."),
    ("03", "Curhat Usaha", "Mengidentifikasi kendala nyata yang sedang dihadapi peserta."),
    ("04", "Diskusi & Berbagi Pengalaman", "Membahas masalah dan solusi bersama mentor serta peserta lain."),
    ("05", "Praktik Langsung", "Menerapkan materi menggunakan kondisi usaha peserta sendiri."),
    ("06", "Tanya Jawab", "Menjawab hal-hal yang masih belum dipahami peserta."),
    ("07", "Evaluasi", "Melihat pemahaman dan perubahan yang telah diterapkan pada usaha."),
    ("08", "Penutup", "Menyimpulkan materi dan menyampaikan kegiatan berikutnya."),
]

for no, title, desc in steps:
    st.markdown(
        f"""
<div class="ru-step">
    <div class="ru-step-no">{no}</div>
    <div>
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="ru-card" style="margin-top:25px;">
<h3>Contoh praktik yang dilakukan peserta</h3>
<p>
✓ Membuat pencatatan keuangan berdasarkan transaksi usaha<br>
✓ Menghitung kembali biaya produksi<br>
✓ Menentukan harga jual<br>
✓ Membuat rencana pemasaran<br>
✓ Menyusun ide konten media sosial<br>
✓ Melakukan evaluasi sederhana terhadap usaha
</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# WEBSITE & MEDIA PENDUKUNG
# ============================================================

st.markdown(
    """
<section id="digital" class="ru-section">
<div class="ru-label">Website & Media Pendukung</div>
<h2>Satu ekosistem digital untuk <em>akses yang lebih fleksibel.</em></h2>
<p class="ru-copy">
Website menjadi pusat informasi resmi, sementara platform lain memiliki fungsi
masing-masing dalam komunikasi, pembelajaran, dokumentasi, dan promosi.
</p>
""",
    unsafe_allow_html=True,
)

digital = [
    ("🌐", "Website", "Pusat informasi resmi, profil, layanan, jadwal, harga, mentor, dan penghubung ke platform lain.", None),
    ("💬", "WhatsApp Community", "Komunikasi utama, penyampaian jadwal, diskusi, dan pendampingan setelah kelas.", LINKS["whatsapp"]),
    ("🎥", "Zoom", "Mendukung pembelajaran dan kegiatan kelas secara daring.", LINKS["zoom"]),
    ("▶️", "YouTube", "Dokumentasi dan materi pembelajaran agar dapat dipelajari kembali.", LINKS["youtube"]),
    ("📸", "Instagram", "Jadwal kelas, testimoni, kegiatan, edukasi, dan identitas Ruang Usaha.", LINKS["instagram"]),
    ("🎵", "TikTok", "Video singkat berupa tips usaha, kesalahan umum, cuplikan kelas, dan program.", LINKS["tiktok"]),
    ("📘", "Facebook", "Salah satu media promosi untuk menjangkau calon peserta.", LINKS["facebook"]),
]

dcols = st.columns(4)

for i, (icon, title, desc, link) in enumerate(digital):
    with dcols[i % 4]:
        st.markdown(
            f"""
<div class="ru-digital">
    <div class="ru-digital-icon">{icon}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
            unsafe_allow_html=True,
        )

        if link and link != "#":
            st.link_button(
                f"Buka {title}",
                link,
                use_container_width=True,
            )

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# HARGA
# ============================================================

st.markdown(
    """
<section id="harga" class="ru-section ru-soft">
<div class="ru-label">Strategi Harga</div>
<h2>Pembelajaran yang tetap <em>terjangkau.</em></h2>
""",
    unsafe_allow_html=True,
)

price1, price2 = st.columns(2, gap="large")

with price1:
    st.markdown(
        """
<div class="ru-price">
    <div class="ru-label">Harga Normal</div>
    <div class="ru-price-main">Rp150.000</div>
    <div class="ru-price-note">
        Kisaran biaya per peserta/per kegiatan, dapat disesuaikan
        dengan jenis materi, kegiatan, dan bentuk pendampingan.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

with price2:
    st.markdown(
        """
<div class="ru-price">
    <div class="ru-label">Promo Pengguna Awal</div>
    <div class="ru-price-main">DISKON 30%</div>
    <div class="ru-price-note">
        Promo khusus untuk <b>50 peserta pertama</b> yang menggunakan
        aplikasi/program Ruang Usaha.<br><br>
        Harga normal: <b>Rp150.000</b><br>
        Harga promo yang tercantum dalam proposal: <b>Rp50.000</b>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="ru-card" style="margin-top:20px;">
<h3>Promo pengguna awal</h3>
<p>
Proposal menetapkan <b>diskon 30% untuk 50 peserta pertama</b>. Proposal juga mencantumkan harga promo <b>Rp50.000</b> dari harga normal Rp150.000; angka tersebut ditampilkan apa adanya sesuai dokumen proposal.<br><br>
Harga mempertimbangkan kemampuan pelaku UMKM, biaya penyelenggaraan kegiatan,
materi dan pendampingan, kebutuhan keberlanjutan usaha, serta tujuan agar
pembelajaran dapat diakses oleh lebih banyak pelaku UMKM.
</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# KEUNGGULAN
# ============================================================

st.markdown(
    """
<section class="ru-section">
<div class="ru-label">Keunggulan Ruang Usaha</div>
<h2>Lebih dari sekadar <em>pelatihan bisnis.</em></h2>
""",
    unsafe_allow_html=True,
)

advantages = [
    ("Praktik Langsung", "Peserta menerapkan materi pada kondisi usaha sendiri."),
    ("Curhat Usaha", "Kendala nyata peserta menjadi bagian dari proses pembelajaran."),
    ("Komunitas", "Peserta belajar dari mentor sekaligus pengalaman pelaku usaha lain."),
    ("Fleksibel", "Website dan berbagai platform digital mendukung akses lintas lokasi."),
    ("Pendampingan Bertahap", "Hubungan dengan peserta dapat berlanjut setelah satu kegiatan."),
    ("Terjangkau", "Harga dirancang agar lebih mudah dijangkau oleh UMKM."),
]

acols = st.columns(3)

for i, (title, desc) in enumerate(advantages):
    with acols[i % 3]:
        st.markdown(
            f"""
<div class="ru-card">
    <div class="ru-card-number">{i+1:02}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# STRUKTUR ORGANISASI
# ============================================================

st.markdown(
    """
<section class="ru-section ru-soft">
<div class="ru-label">Struktur Organisasi</div>
<h2>Tim sederhana, fungsi tetap <em>jelas.</em></h2>
<p class="ru-copy">
Pada tahap awal, struktur dibuat sederhana untuk menjaga efisiensi biaya.
Tiga fungsi utama menjalankan pengelolaan, pembelajaran, serta operasional dan digital.
</p>
""",
    unsafe_allow_html=True,
)

orgs = [
    (
        "01",
        "Pengelola Utama",
        "Menentukan arah usaha, mengambil keputusan, mengawasi kegiatan, menyusun pengembangan, membangun hubungan eksternal, dan mengevaluasi jumlah pengguna, kepuasan, keuangan, serta efektivitas program.",
    ),
    (
        "02",
        "Tim Pembelajaran & Pendampingan",
        "Menyiapkan materi, menjalankan kelas, mendampingi peserta, mengelola diskusi, Curhat Usaha, praktik, dan membangun suasana belajar interaktif.",
    ),
    (
        "03",
        "Tim Operasional & Digital",
        "Mengelola data peserta, pendaftaran, jadwal, pembayaran, pencatatan keuangan, website/aplikasi, media sosial, dokumentasi, dan informasi peserta.",
    ),
]

ocols = st.columns(3)

for col, (num, title, desc) in zip(ocols, orgs):
    with col:
        st.markdown(
            f"""
<div class="ru-card">
    <div class="ru-card-number">{num}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("</section>", unsafe_allow_html=True)


# ============================================================
# CTA
# ============================================================

st.markdown(
    """
<section class="ru-section">
<div class="ru-cta">
<div class="ru-label">Mulai Bersama</div>
<h2>Bangun usaha lebih <em>terarah.</em></h2>
<p class="ru-copy">
Belajar dari dasar, bawa masalah usaha ke dalam diskusi,
praktikkan materi, dan berkembang bersama komunitas Ruang Usaha.
</p>
</div>
</section>
""",
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button(
        "💬 Gabung WhatsApp Community",
        LINKS["https://chat.whatsapp.com/Bew1bpB1vxYGge8z1PMmrX"],
        use_container_width=True,
    )

with c2:
    st.link_button(
        "▶️ Lihat YouTube",
        LINKS["https://youtube.com/@ruangusaha-q1g?si=jITpG2S7u1uLwUE1"],
        use_container_width=True,
    )

with c3:
    st.link_button(
        "📸 Instagram",
        LINKS["https://www.instagram.com/ruangusaha_109?stkn=MWNtaHY0ZWN4YXdhYw=="],
        use_container_width=True,
    )
with c4:
    st.link_button(
        "▶️ gabung Zoom",
        LINKS["https://us05web.zoom.us/j/3799765498?pwd=Y16zpswb0ymqkgTa1U46jCrn4YlVkX.1"],
        use_container_width=True,
    )

# ============================================================
# FOOTER
# ============================================================

unimed = (
    f'<img class="ru-footer-unimed" src="{LOGO_UNIMED}" alt="Logo UNIMED">'
    if LOGO_UNIMED
    else ""
)

st.markdown(
    f"""
<footer class="ru-footer">

<div class="ru-footer-brand">
    {logo}
    <div>
        <h3>Ruang Usaha</h3>
        <p>Belajar, Berbagi, dan Bertumbuh Bersama.</p>
    </div>
</div>

<div style="margin-top:22px;">
    {unimed}
</div>

<p style="margin-top:22px;">
Jasa layanan kelas dan pendampingan bisnis bagi pelaku UMKM dan calon wirausaha.
</p>

<div class="ru-footer-bottom">
© 2026 Ruang Usaha • Universitas Negeri Medan • Kelompok 3
</div>

</footer>
""",
    unsafe_allow_html=True,
)
