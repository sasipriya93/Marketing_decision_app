{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c6b0e131-7985-4e75-b136-cc8c180b461e",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\splpt 1224\\downloads\\new floder\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "51583a5d-f47e-4334-b932-6db2f30185e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.set_page_config(page_title=\"Marketing Decision Support Tool\", page_icon=\"📊\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f939eb91-9e8f-4eb9-8f9b-f1a96cf5941e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-12 12:11:26.388 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\SPLPT 1224\\Downloads\\new floder\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title(\"📊 Marketing Decision Support Tool\")\n",
    "st.markdown(\"This app helps decision-makers evaluate marketing choices based on basic inputs.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c507c477-ecfe-4eca-98fd-de034e458b5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-12 12:11:53.295 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "# Input form\n",
    "with st.form(\"decision_form\"):\n",
    "    decision_type = st.selectbox(\n",
    "        \"What type of marketing decision do you want to make?\",\n",
    "        [\"Product\", \"Price\", \"Place\", \"Promotion\", \"People\", \"Process\", \"Physical Evidence\"]\n",
    "    )\n",
    "    \n",
    "    goal = st.text_input(\"What is the goal of this decision? (e.g. Increase sales, brand awareness)\")\n",
    "    budget = st.number_input(\"Approximate budget (in ₹)\", min_value=0, step=500)\n",
    "    target_market = st.text_input(\"Who is your target market? (e.g. Gen Z, Working Professionals)\")\n",
    "    timeline = st.text_input(\"When do you want to execute this decision? (e.g. July 2025)\")\n",
    "\n",
    "    submitted = st.form_submit_button(\"Submit Decision\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "127680bf-ae64-4bbb-9f76-d2e0a6a58671",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Logic\n",
    "if submitted:\n",
    "    verdict = \"\"\n",
    "    reason = \"\"\n",
    "    suggestion = \"\"\n",
    "\n",
    "    dt = decision_type.lower()\n",
    "    tm = target_market.lower()\n",
    "    goal_lower = goal.lower()\n",
    "\n",
    "    # Rules logic\n",
    "    if dt == \"price\" and \"student\" in tm:\n",
    "        verdict = \"❌ Not Recommended\"\n",
    "        reason = \"Target market is price-sensitive. A price increase may reduce interest.\"\n",
    "        suggestion = \"Try offering added value or discounts.\"\n",
    "\n",
    "    elif dt == \"promotion\" and \"instagram\" in goal_lower:\n",
    "        verdict = \"✅ Good to Go\"\n",
    "        reason = \"Instagram performs well for awareness in young demographics.\"\n",
    "        suggestion = \"Use reels and influencer partnerships.\"\n",
    "\n",
    "    elif dt == \"product\" and \"vegan\" in goal_lower:\n",
    "        verdict = \"⚠️ Moderate Risk\"\n",
    "        reason = \"Vegan demand is rising but competition is intense.\"\n",
    "        suggestion = \"Run a pilot launch in key cities first.\"\n",
    "\n",
    "    elif dt == \"place\" and \"tier 2\" in tm:\n",
    "        verdict = \"✅ Good to Go\"\n",
    "        reason = \"Tier 2 cities are emerging markets. Low competition, good potential.\"\n",
    "        suggestion = \"Focus on regional channels and local influencers.\"\n",
    "\n",
    "    elif dt == \"people\" and \"retention\" in goal_lower:\n",
    "        verdict = \"⚠️ Needs Attention\"\n",
    "        reason = \"High employee turnover affects customer trust.\"\n",
    "        suggestion = \"Invest in internal marketing and employee engagement.\"\n",
    "\n",
    "    elif dt == \"process\" and \"delay\" in goal_lower:\n",
    "        verdict = \"❌ Not Recommended\"\n",
    "        reason = \"Delays in marketing operations reduce campaign effectiveness.\"\n",
    "        suggestion = \"Automate repetitive tasks and adopt workflow tools.\"\n",
    "\n",
    "    elif dt == \"physical evidence\" and \"rebrand\" in goal_lower:\n",
    "        verdict = \"⚠️ Moderate Risk\"\n",
    "        reason = \"Rebranding affects customer trust. Needs testing.\"\n",
    "        suggestion = \"Test new visuals with focus groups before full rollout.\"\n",
    "\n",
    "    elif dt == \"promotion\" and \"email\" in goal_lower:\n",
    "        verdict = \"⚠️ Moderate Risk\"\n",
    "        reason = \"Email campaigns work only with high-quality leads.\"\n",
    "        suggestion = \"Segment your list and use A/B testing.\"\n",
    "\n",
    "    elif dt == \"product\" and \"premium\" in goal_lower:\n",
    "        verdict = \"⚠️ Moderate Risk\"\n",
    "        reason = \"Premium product launches need strong branding.\"\n",
    "        suggestion = \"Build brand story and justify price with features.\"\n",
    "\n",
    "    else:\n",
    "        verdict = \"⚠️ Needs Review\"\n",
    "        reason = \"No specific rule matched. Requires deeper data review or expert input.\"\n",
    "        suggestion = \"Collect past data or test on small group before launch.\"\n",
    "\n",
    "    # Show report\n",
    "    st.subheader(\"📄 Decision Support Report\")\n",
    "    st.write(f\"**Decision Type:** {decision_type}\")\n",
    "    st.write(f\"**Goal:** {goal}\")\n",
    "    st.write(f\"**Budget:** ₹{budget}\")\n",
    "    st.write(f\"**Target Market:** {target_market}\")\n",
    "    st.write(f\"**Timeline:** {timeline}\")\n",
    "\n",
    "    st.markdown(\"---\")\n",
    "    st.write(f\"### ✅ Verdict: {verdict}\")\n",
    "    st.write(f\"📌 **Reason:** {reason}\")\n",
    "    st.write(f\"💡 **Suggestion:** {suggestion}\")\n",
    "    st.markdown(\"---\")\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "40c67895-839b-4824-a32e-a83323558b15",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base]",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
import streamlit as st

st.title("My First Streamlit App 🚀")
st.write("Hello! This is a test app.")
