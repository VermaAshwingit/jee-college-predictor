import streamlit as st
import json

# Load data
def load_data():
    with open("college_data.json", "r") as f:
        return json.load(f)

# Filter colleges
def suggest_colleges(rank, category, state, data):
    results = []
    for row in data:
        if row["category"].upper() != category.upper():
            continue

        # Match home state quota
        if row["quota"] == "HS" and row["state"].lower() != state.lower():
            continue

        if rank <= row["closing_rank"]:
            results.append(f"{row['college']} - {row['branch']} ({row['quota']})")

    return results

# UI
st.title("🎓 JEE College Predictor")

rank = st.number_input("Enter your JEE Rank", min_value=1)
category = st.selectbox("Select Category", ["GEN", "OBC", "SC", "ST"])
state = st.text_input("Your Home State (e.g., Tamil Nadu)")

if st.button("Predict Colleges"):
    data = load_data()
    matches = suggest_colleges(rank, category, state, data)
    
    if matches:
        st.success("Eligible Colleges:")
        for college in matches:
            st.write("✅", college)
    else:
        st.error("No matching colleges found.")
