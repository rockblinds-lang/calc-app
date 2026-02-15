import streamlit as st

# Налаштування сторінки, щоб вона не була занадто широкою
st.set_page_config(page_title="Шинний Експерт", layout="centered")

st.title("ProTyre: Твій персональний шинний експерт")
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
import matplotlib.pyplot as plt

st.write("---")
st.write("### 📸 Візуалізація змін")

# Створюємо малюнок
fig, ax = plt.subplots(figsize=(6, 6))

# Розрахуємо радіуси для малювання (приклад спрощений)
# r1 - старий радіус, r2 - новий радіус (візьмемо з ваших змінних)
# Припустимо, у вас є змінні d1 та d2 (діаметри)
r1 = diam1 / 2
r2 = diam2 / 2

# Малюємо колеса як кола
circle1 = plt.Circle((0, 0), r1, color='gray', fill=False, linestyle='--', label='Старе колесо')
circle2 = plt.Circle((0, 0), r2, color='blue', fill=False, linewidth=2, label='Нове колесо')

ax.add_patch(circle1)
ax.add_patch(circle2)

# Налаштування осей
limit = max(r1, r2) * 1.2
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_aspect('equal')
plt.legend()
plt.axis('off') # Ховаємо цифри координат

# Відображаємо графік у Streamlit
st.pyplot(fig)

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
