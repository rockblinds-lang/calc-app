import streamlit as st

# 1. Наш словник перекладів
translations = {
    "UA": {
        "header_current": "⬅️ Ваші поточні шини",
        "header_new": "➡️ Нові шини (плановані)",
        "width": "Ширина",
        "profile": "Профіль",
        "rim": "Діаметр диска (дюйми)",
        "warning_text": "Увага! Зміна кліренсу:"
    },
    "result_warn": "⚠️ Увага! Зміна кліренсу:",
"danger_msg": "**Перед купівлею шин проаналізуйте, як зміняться параметри вашої ходової!**"

    "EN": {
        "header_current": "⬅️ Your current tires",
        "header_new": "➡️ New tires (planned)",
        "width": "Width",
        "profile": "Profile",
        "rim": "Rim diameter (inches)",
        "warning_text": "Warning! Clearance change:"
    },
"result_warn": "⚠️ Warning! Clearance change:",
"danger_msg": "**Before buying tires, analyze how your suspension parameters will change!**"
    "PL": {
        "header_current": "⬅️ Twoje aktualne opony",
        "header_new": "➡️ Nowe opony (planowane)",
        "width": "Szerokość",
        "profile": "Profil",
        "rim": "Średnica felgi (cale)",
        "warning_text": "Uwaga! Zmiana prześwitu:"
    },
"result_warn": "⚠️ Uwaga! Zmiana prześwitu:",
"danger_msg": "**Przed zakupem opon przeanalizuj, jak zmienią się parametry Twojego zawieszenia!**"
}

# Вибір мови в боковій панелі
lang = st.sidebar.selectbox("Language / Мова", ["UA", "EN", "PL"])
t = translations[lang]

# 3. Створюємо коротку змінну 't', яка буде містити слова обраної мови
t = translations[lang]

import streamlit as st

# 1. Налаштування сторінки
st.set_page_config(page_title="ProTyre", layout="centered")

st.title("ProTyre: Твій персональний шинний експерт")
st.info("**Перед купівлею шин проаналізуйте, чи не будуть колеса зачіпати арки та як зміняться параметри ходової!**")

# --- ВВІД ДАНИХ У ДВІ КОЛОНКИ ---
# --- ВАШ ОНОВЛЕНИЙ ВВІД ДАНИХ ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(t["header_current"]) # Використовуємо словник
    w1 = st.select_slider(f"{t['width']} (1)", options=list(range(135, 355, 5)), value=295, key="w1")
    p1 = st.select_slider(f"{t['profile']} (1)", options=list(range(20, 85, 5)), value=35, key="p1")
    r1 = st.number_input(f"{t['rim']} (1)", value=21, step=1, key="r1")
with col2:
    st.subheader(t["header_new"]) # Використовуємо словник
    w2 = st.select_slider(f"{t['width']} (2)", options=list(range(135, 355, 5)), value=275, key="w2")
    p2 = st.select_slider(f"{t['profile']} (2)", options=list(range(20, 85, 5)), value=45, key="p2")
    r2 = st.number_input(f"{t['rim']} (2)", value=21, step=1, key="r2")

# --- МАТЕМАТИКА (повна версія) ---
# --- МАТЕМАТИКА ---
diam1 = (w1 * p1 / 100 * 2) + (r1 * 25.4)
diam2 = (w2 * p2 / 100 * 2) + (r2 * 25.4)
diff = diam2 - diam1
cl_change_mm = diff / 2
cl_change_cm = cl_change_mm / 10

# Розрахунок швидкості
ratio = diam2 / diam1
real_speed = 100 * ratio
speed_diff = real_speed - 100

st.divider()

# --- ВИВІД РЕЗУЛЬТАТІВ ---
st.write("### 📊 Порівняння результатів:")

# Створюємо 4 колонки
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

m_col1.metric("Діаметр 1", f"{diam1:.0f} мм")
m_col2.metric("Діаметр 2", f"{diam2:.1f} мм", f"{diff:.1f} мм")
m_col3.metric("Кліренс", f"{cl_change_mm:.1f} мм", f"{cl_change_cm:.1f} см")
m_col4.metric("Швидкість", f"{real_speed:.1f} км/год", f"{speed_diff:.1f}%")

# --- ПОПЕРЕДЖЕННЯ ---
if abs(speed_diff) > 3:
    st.error(f"⚠️ Похибка спідометра: {speed_diff:.1f}%. Це забагато!")
elif abs(speed_diff) > 1.5:
    st.warning(f"🔔 Похибка спідометра: {speed_diff:.1f}%")

if abs(cl_change_mm) > 15:
    st.warning(f"⚠️ Кліренс зміниться на {cl_change_cm:.1f} см. Перевірте арки!")

# --- РЕКЛАМНИЙ БЛОК (Тепер він помітний!) ---
st.success("🎁 СПЕЦІАЛЬНА ПРОПОЗИЦІЯ ВІД РОЗРОБНИКА")
st.markdown("""
**Якісні жалюзі та ролети від "РОМАН"**  
☀️ Захистіть свою оселю від палкого сонця!  
📍 м. Львів, вул. [Твоя адреса]  
📞 **Телефонуйте: [Твій номер]**
""")
if st.button("🌐 Перейти на наш сайт"):
    st.write("Тут буде перехід на твій сайт...")

st.caption("Розроблено спеціально для відповідальних автовласників.")
if abs(real_speed - 100) > 3:
    st.warning("⚠️ Велика похибка швидкості!")

# Твій Рекламний Блок
with st.expander("🎁 Отримати бонус від розробника"):
    st.success("Якісні жалюзі та ролети від 'РОМІГО'")
    st.write("☀️ Захистіть свою оселю від сонця!")
    st.markdown("📞 **Телефонуйте: 067 244 45 03 **")
    if st.button("🌐 www.zaluzi.com.ua"):
        st.write("Перенаправлення...")
import segno
from io import BytesIO

# Створюємо бічну панель для QR-коду
with st.sidebar:
    st.write("### Поділитися додатком")
    
    # Створюємо QR-код, який веде на адресу вашого сайту
    url = " https://calc-app-bpnejes72n7bpfuukqudzb.streamlit.app/" # Перевірте, чи це ваша адреса
    qr = segno.make(url)
    
    # Зберігаємо QR-код у пам'ять, щоб Streamlit міг його показати
    out = BytesIO()
    qr.save(out, kind='png', scale=10)
    st.image(out.getvalue(), caption="Скануй та рахуй у смартфоні")
