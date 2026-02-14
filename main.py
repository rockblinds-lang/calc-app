import streamlit as st

# Налаштування сторінки, щоб вона не була занадто широкою
st.set_page_config(page_title="Шинний Експерт", layout="centered")

st.title("🚗 Шинний Калькулятор")
st.write("Порівняйте параметри для вашого авто:")

# --- ВВІД ДАНИХ (Великі повзунки для пальців) ---
st.subheader("🏁 Заводський стандарт")
w1 = st.select_slider("Ширина (1)", options=list(range(155, 355, 5)), value=295)
p1 = st.select_slider("Профіль (1)", options=list(range(20, 85, 5)), value=35)
r1 = st.number_input("Диск (1), дюймів", value=21, step=1)

st.divider()

st.subheader("🆕 Нові шини")
w2 = st.select_slider("Ширина (2)", options=list(range(155, 355, 5)), value=275)
p2 = st.select_slider("Профіль (2)", options=list(range(20, 85, 5)), value=45)
r2 = st.number_input("Диск (2), дюймів", value=21, step=1)

# --- МАТЕМАТИКА ---
diam1 = (w1 * p1 / 100 * 2) + (r1 * 25.4)
diam2 = (w2 * p2 / 100 * 2) + (r2 * 25.4)
diff = diam2 - diam1
ratio = diam2 / diam1
real_speed = 100 * ratio
cl_change = diff / 2

# --- РЕЗУЛЬТАТ (Великі плашки) ---
st.info("📊 ВЕРДИКТ:")
st.metric("Кліренс змінить на", f"{round(cl_change, 2)} мм")
st.metric("Реальна швидкість", f"{round(real_speed, 2)} км/год", delta=f"{round(real_speed-100, 2)} км/год")

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
    st.success("Якісні жалюзі та ролети від 'РОМАН'")
    st.write("☀️ Захистіть свою оселю від сонця!")
    st.markdown("📞 **Телефонуйте: [Твій номер]**")
    if st.button("🌐 Перейти на сайт"):
        st.write("Перенаправлення...")
