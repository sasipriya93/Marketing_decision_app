#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.set_page_config(page_title="Marketing Decision Support Tool", page_icon="📊")

st.title("📊 Marketing Decision Support Tool")
st.markdown("This app helps decision-makers evaluate marketing choices based on basic inputs.")

# Input form
with st.form("decision_form"):
    decision_type = st.selectbox(
        "What type of marketing decision do you want to make?",
        ["Product", "Price", "Place", "Promotion", "People", "Process", "Physical Evidence"]
    )
    
    goal = st.text_input("What is the goal of this decision? (e.g. Increase sales, brand awareness)")
    budget = st.number_input("Approximate budget (in ₹)", min_value=0, step=500)
    target_market = st.text_input("Who is your target market? (e.g. Gen Z, Working Professionals)")
    timeline = st.text_input("When do you want to execute this decision? (e.g. July 2025)")

    submitted = st.form_submit_button("Submit Decision")

# Logic
if submitted:
    verdict = ""
    reason = ""
    suggestion = ""

    dt = decision_type.lower()
    tm = target_market.lower()
    goal_lower = goal.lower()

    # Rules logic
    if dt == "price" and "student" in tm:
        verdict = "❌ Not Recommended"
        reason = "Target market is price-sensitive. A price increase may reduce interest."
        suggestion = "Try offering added value or discounts."

    elif dt == "promotion" and "instagram" in goal_lower:
        verdict = "✅ Good to Go"
        reason = "Instagram performs well for awareness in young demographics."
        suggestion = "Use reels and influencer partnerships."

    elif dt == "product" and "vegan" in goal_lower:
        verdict = "⚠️ Moderate Risk"
        reason = "Vegan demand is rising but competition is intense."
        suggestion = "Run a pilot launch in key cities first."

    elif dt == "place" and "tier 2" in tm:
        verdict = "✅ Good to Go"
        reason = "Tier 2 cities are emerging markets. Low competition, good potential."
        suggestion = "Focus on regional channels and local influencers."

    elif dt == "people" and "retention" in goal_lower:
        verdict = "⚠️ Needs Attention"
        reason = "High employee turnover affects customer trust."
        suggestion = "Invest in internal marketing and employee engagement."

    elif dt == "process" and "delay" in goal_lower:
        verdict = "❌ Not Recommended"
        reason = "Delays in marketing operations reduce campaign effectiveness."
        suggestion = "Automate repetitive tasks and adopt workflow tools."

    elif dt == "physical evidence" and "rebrand" in goal_lower:
        verdict = "⚠️ Moderate Risk"
        reason = "Rebranding affects customer trust. Needs testing."
        suggestion = "Test new visuals with focus groups before full rollout."

    elif dt == "promotion" and "email" in goal_lower:
        verdict = "⚠️ Moderate Risk"
        reason = "Email campaigns work only with high-quality leads."
        suggestion = "Segment your list and use A/B testing."

    elif dt == "product" and "premium" in goal_lower:
        verdict = "⚠️ Moderate Risk"
        reason = "Premium product launches need strong branding."
        suggestion = "Build brand story and justify price with features."

    else:
        verdict = "⚠️ Needs Review"
        reason = "No specific rule matched. Requires deeper data review or expert input."
        suggestion = "Collect past data or test on small group before launch."

    # Show report
    st.subheader("📄 Decision Support Report")
    st.write(f"**Decision Type:** {decision_type}")
    st.write(f"**Goal:** {goal}")
    st.write(f"**Budget:** ₹{budget}")
    st.write(f"**Target Market:** {target_market}")
    st.write(f"**Timeline:** {timeline}")

    st.markdown("---")
    st.write(f"### ✅ Verdict: {verdict}")
    st.write(f"📌 **Reason:** {reason}")
    st.write(f"💡 **Suggestion:** {suggestion}")
    st.markdown("---")


# In[ ]:




