import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Tes Bakat & Minat Jurusan Kuliah",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Tes Bakat & Minat Jurusan Kuliah")
st.write(
    "Jawab pertanyaan-pertanyaan berikut dengan jujur sesuai dengan kepribadian "
    "dan kebiasaanmu sehari-hari untuk menemukan jurusan kuliah yang paling cocok!"
)
st.divider()

# 2. Form Pertanyaan Lanjutan & Komprehensif
with st.form("quiz_form"):
    st.subheader("📋 Kuesioner Bakat & Minat")

    q1 = st.radio(
        "1. Kegiatan apa yang paling kamu nikmati saat mengisi waktu luang?",
        [
            "Mencoba software baru, ngoding, atau mengotak-atik perangkat elektronik",
            "Menggambar, melukis, edit video, atau menulis cerita ide kreatif",
            "Membaca berita bisnis, jualan produk, atau mengatur strategi keuangan",
            "Membaca buku psikologi/sosial, berdiskusi isu masyarakat, atau kegiatan relawan",
            "Eksperimen sains, mengamati hewan/tumbuhan, atau membaca literatur medis"
        ]
    )

    q2 = st.radio(
        "2. Mata pelajaran sekolah mana yang paling kamu sukai?",
        [
            "Matematika, Fisika, atau Informatika",
            "Seni Budaya, Bahasa, atau Prakarya",
            "Ekonomi, Akuntansi, atau Kewirausahaan",
            "Sosiologi, Sejarah, PPKn, atau Geografi",
            "Biologi, Kimia, atau IPA Terpadu"
        ]
    )

    q3 = st.radio(
        "3. Jika ada masalah atau tantangan di sekitarmu, bagaimana caramu menyelesaikannya?",
        [
            "Menganalisis logika masalah dan mencari solusi berbasis data/sistem",
            "Memikirkan ide out-of-the-box dan membuat konten visual/konseptual",
            "Membuat perhitungan efisiensi, alokasi sumber daya, atau analisis biaya-manfaat",
            "Mengajak orang lain berdiskusi, mediasi, dan mencari solusi sosial yang humanis",
            "Melakukan observasi eksperimental, metode ilmiah, dan analisis medis/biologis"
        ]
    )

    q4 = st.radio(
        "4. Peran apa yang paling sering kamu ambil saat mengerjakan tugas kelompok?",
        [
            "Anak teknik/logika yang fokus pada penyelesaian struktur dan pemrograman tugas",
            "Pendesain slide presentasi, pembuat konsep video, atau pembuat narasi",
            "Bendahara, manajer proyek, atau pembagi tugas agar efisien",
            "Juru bicara (presenter), penengah argumen, atau penyusun materi hubungan masyarakat",
            "Peneliti materi, pemeriksa keakuratan data ilmiah, dan pengumpul referensi"
        ]
    )

    q5 = st.radio(
        "5. Lingkungan kerja seperti apa yang impianmu di masa depan?",
        [
            "Perusahaan teknologi, lab komputer, atau startup pengembang software",
            "Studio kreatif, agensi desain, media, atau industri hiburan",
            "Dunia korporasi, perbankan, konsultan bisnis, atau menjadi pengusaha",
            "Lembaga hukum, organisasi internasional, LSM, atau instansi pemerintahan",
            "Rumah sakit, laboratorium penelitian, klinik, atau perusahaan farmasi"
        ]
    )

    q6 = st.radio(
        "6. Pencapaian mana yang membuatmu paling bangga?",
        [
            "Berhasil memecahkan teka-teki logika yang rumit atau membuat alat yang berfungsi",
            "Karya senimu dipuji orang lain atau tulisanmu menyentuh perasaan pembaca",
            "Mendapatkan keuntungan dari jualan atau sukses mengorganisasi acara besar",
            "Berhasil membantu kawan menyelesaikan masalah pribadinya atau memenangkan debat",
            "Memahami bagaimana organ tubuh atau fenomena alam bekerja secara mendalam"
        ]
    )

    submitted = st.form_submit_button("🎯 Analisis Rekomendasi Jurusan")

# 3. Logika Perhitungan Skor
if submitted:
    # Inisialisasi Skor per Kategori Jurusan
    scores = {
        "Teknik & IT": 0,
        "Seni & Desain Kreatif": 0,
        "Bisnis, Manajemen & Ekonomi": 0,
        "Hukum, Sosial & Humaniora": 0,
        "Kesehatan & Sains Alam": 0
    }

    # Pembobotan Skor Q1
    if "software" in q1: scores["Teknik & IT"] += 3
    elif "Menggambar" in q1: scores["Seni & Desain Kreatif"] += 3
    elif "bisnis" in q1: scores["Bisnis, Manajemen & Ekonomi"] += 3
    elif "psikologi" in q1: scores["Hukum, Sosial & Humaniora"] += 3
    elif "Eksperimen" in q1: scores["Kesehatan & Sains Alam"] += 3

    # Pembobotan Skor Q2
    if "Matematika" in q2: scores["Teknik & IT"] += 3
    elif "Seni" in q2: scores["Seni & Desain Kreatif"] += 3
    elif "Ekonomi" in q2: scores["Bisnis, Manajemen & Ekonomi"] += 3
    elif "Sosiologi" in q2: scores["Hukum, Sosial & Humaniora"] += 3
    elif "Biologi" in q2: scores["Kesehatan & Sains Alam"] += 3

    # Pembobotan Skor Q3
    if "logika" in q3: scores["Teknik & IT"] += 2
    elif "out-of-the-box" in q3: scores["Seni & Desain Kreatif"] += 2
    elif "perhitungan" in q3: scores["Bisnis, Manajemen & Ekonomi"] += 2
    elif "diskusi" in q3: scores["Hukum, Sosial & Humaniora"] += 2
    elif "observasi" in q3: scores["Kesehatan & Sains Alam"] += 2

    # Pembobotan Skor Q4
    if "teknik" in q4: scores["Teknik & IT"] += 2
    elif "Pendesain" in q4: scores["Seni & Desain Kreatif"] += 2
    elif "Bendahara" in q4: scores["Bisnis, Manajemen & Ekonomi"] += 2
    elif "Juru bicara" in q4: scores["Hukum, Sosial & Humaniora"] += 2
    elif "Peneliti" in q4: scores["Kesehatan & Sains Alam"] += 2

    # Pembobotan Skor Q5
    if "teknologi" in q5: scores["Teknik & IT"] += 3
    elif "Studio" in q5: scores["Seni & Desain Kreatif"] += 3
    elif "korporasi" in q5: scores["Bisnis, Manajemen & Ekonomi"] += 3
    elif "hukum" in q5: scores["Hukum, Sosial & Humaniora"] += 3
    elif "Rumah sakit" in q5: scores["Kesehatan & Sains Alam"] += 3

    # Pembobotan Skor Q6
    if "teka-teki" in q6: scores["Teknik & IT"] += 2
    elif "Karya" in q6: scores["Seni & Desain Kreatif"] += 2
    elif "keuntungan" in q6: scores["Bisnis, Manajemen & Ekonomi"] += 2
    elif "membantu" in q6: scores["Hukum, Sosial & Humaniora"] += 2
    elif "organ tubuh" in q6: scores["Kesehatan & Sains Alam"] += 2

    # Pemrosesan Data Hasil
    df = pd.DataFrame(list(scores.items()), columns=['Rumpun Jurusan', 'Skor'])
    total_skor = df['Skor'].sum()
    
    # Menghindari pembagian dengan 0 jika tidak ada pilihan
    if total_skor > 0:
        df['Persentase (%)'] = (df['Skor'] / total_skor) * 100
    else:
        df['Persentase (%)'] = 0

    df_sorted = df.sort_values(by='Skor', ascending=False)
    top_jurusan = df_sorted.iloc[0]['Rumpun Jurusan']

    st.divider()
    st.success(f"🎉 Rumpun Jurusan yang Paling Cocok Untukmu: **{top_jurusan}**")

    # Visualisasi Grafik Pie
    st.subheader("📊 Grafik Distribusi Minat dan Bakat")
    fig = px.pie(
        df,
        values='Persentase (%)',
        names='Rumpun Jurusan',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig, use_container_width=True)

    # Rekomendasi Jurusan Spesifik & Prospek Karir
    st.subheader("💡 Rekomendasi Jurusan Kuliah & Karir")

    detail_jurusan = {
        "Teknik & IT": {
            "jurusan": ["Teknik Informatika", "Sistem Informasi", "Teknik Elektro", "Data Science", "Teknik Mesin"],
            "karir": "Software Engineer, Data Scientist, Cyber Security Specialist, Cloud Architect, Robotics Engineer."
        },
        "Seni & Desain Kreatif": {
            "jurusan": ["Desain Komunikasi Visual (DKV)", "Desain Interior", "Seni Rupa", "Animasi", "Film & Televisi"],
            "karir": "UI/UX Designer, Illustrator, Animator, Concept Artist, Art Director, Content Creator."
        },
        "Bisnis, Manajemen & Ekonomi": {
            "jurusan": ["Manajemen", "Akuntansi", "Ekonomi Pembangunan", "Bisnis Digital", "Pemasaran (Marketing)"],
            "karir": "Entrepreneur, Financial Analyst, Marketing Strategist, Management Consultant, Business Development."
        },
        "Hukum, Sosial & Humaniora": {
            "jurusan": ["Ilmu Hukum", "Ilmu Komunikasi", "Hubungan Internasional", "Psikologi", "Sosiologi"],
            "karir": "Pengacara/Konsultan Hukum, Diplomat, Public Relations, HRD/Recruiter, Jurnalis."
        },
        "Kesehatan & Sains Alam": {
            "jurusan": ["Kedokteran", "Farmasi", "Ilmu Keperawatan", "Bioteknologi", "Kesehatan Masyarakat"],
            "karir": "Dokter, Apoteker, Peneliti Biomedis, Konsultan Kesehatan, Epidemiolog."
        }
    }

    info = detail_jurusan[top_jurusan]

    st.write("**Pilihan Jurusan Spesifik yang Disarankan:**")
    for j in info["jurusan"]:
        st.write(f"- {j}")

    st.info(f"🚀 **Prospek Karir Utama:** {info['karir']}")