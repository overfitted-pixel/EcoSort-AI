import streamlit as st
from waste_data import waste_database

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻️",
    layout="centered"
)
#css
st.markdown("""
<style>

.main{
    background-color:#f7faf7;
}

.stButton>button{
    background:#16a34a;
    color:white;
    border-radius:10px;
    height:50px;
    width:220px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#15803d;
}

h1,h2,h3{
    color:#15803d;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.title("♻️ EcoSort AI")

st.markdown("""
### 🌍 Intelligent Waste Segregation & Sustainable Recycling Assistant

Helping people dispose of waste correctly using AI while supporting **UN Sustainable Development Goals (SDG 12).**
""")
st.subheader("Intelligent Waste Segregation & Sustainable Recycling Assistant")
st.success("♻️ AI for Sustainability Project | IBM SkillsBuild | 1M1B Internship")

st.write("""
Welcome to **EcoSort AI**.

This AI assistant helps users identify different types of waste and provides sustainable disposal recommendations aligned with **UN SDG 12 - Responsible Consumption and Production**.
""")

st.divider()

with st.sidebar:

    st.title("🌍 SDG Information")

    st.success("Primary SDG")

    st.write("SDG 12 - Responsible Consumption and Production")

    st.info("AI Technologies Used")

    st.write("""
- IBM Granite (Concept)
- Prompt Engineering
- Python
- Streamlit
""")

    st.success("Version")

    st.write("EcoSort AI v1.0")

# ---------------- User Input ----------------
col1,col2,col3 = st.columns(3)

with col1:
    st.metric("SDG", "12")

with col2:
    st.metric("AI Model", "Granite")

with col3:
    st.metric("Version", "1.0")

waste = st.text_input("🗑️ Enter Waste Item", placeholder="Example: Plastic Bottle")

if st.button("Analyze Waste"):

    if waste.strip() == "":
        st.warning("Please enter a waste item.")
    else:

        key = waste.lower().strip()

        if key in waste_database:

            data = waste_database[key]

            st.success("Analysis Completed Successfully ✅")

            st.markdown("### Waste Classification")

            st.info(f"**Category:** {data['category']}")

            st.markdown("### Proper Disposal")

            st.write(data["disposal"])

            st.markdown("### Environmental Impact")

            st.write(data["impact"])

            st.markdown("### Eco Score")

            score = int(data["eco_score"].split("/")[0])

            st.progress(score)

            st.metric("🌱 Eco Score", data["eco_score"])

            st.markdown("### Sustainability Tip 🌱")

            st.write(
                "Reduce • Reuse • Recycle whenever possible to protect our environment."
            )

        else:

            st.error("Item not found in database.")

            st.write("Try one of these examples:")

            st.code("""
Plastic Bottle
Banana Peel
Battery
Paper
Glass Bottle
""")

st.divider()

st.markdown("---")

st.subheader("🚀 Future Enhancements")

st.write("""
✅ Image Upload Classification

✅ IBM Granite Integration

✅ AI Chatbot

✅ Nearby Recycling Center Locator

✅ Carbon Footprint Calculator

✅ RAG using Municipal Waste Policies
""")
#footer

st.markdown("---")
st.caption("Developed by Abhishek Gupta | 1M1B AI for Sustainability Internship 2026 | IBM SkillsBuild")