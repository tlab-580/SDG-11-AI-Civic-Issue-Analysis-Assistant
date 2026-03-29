# SDG 11: Smart City Civic Issue Analysis Assistant
# ---------------- INTAKE AGENT ----------------
def intake_agent(text):
    text = text.lower()
    text = text.strip()
    return text


# ---------------- CLASSIFICATION AGENT ----------------
def classify_agent(text):
    if "garbage" in text or "waste" in text or "trash" in text:
        return "Waste Management"
    elif "road" in text or "pothole" in text:
        return "Road Infrastructure"
    elif "light" in text:
        return "Street Lighting"
    else:
        return "General Civic Issue"


# ---------------- ANALYSIS AGENT ----------------
def analysis_agent(text, category):
    if "days" in text or "overflow" in text or "not working" in text:
        return "High"
    elif "sometimes" in text:
        return "Medium"
    else:
        return "Low"


# ---------------- RAG AGENT (Knowledge Base) ----------------
def rag_agent(category):
    policies = {
        "Waste Management": """
Municipal waste should be collected daily.
Overflowing garbage bins must be cleared immediately.
Waste segregation into wet and dry is mandatory.
""",
        "Road Infrastructure": """
Potholes must be repaired within 48 hours.
Damaged roads should be barricaded.
Regular inspections are required.
""",
        "Street Lighting": """
Street lights should work from sunset to sunrise.
Faulty lights must be repaired within 24 hours.
Energy-efficient LED lights are recommended.
"""
    }

    return policies.get(category, "No policy available for this issue.")


# ---------------- RECOMMENDATION AGENT ----------------
def recommendation_agent(category, priority, policy):
    if category == "Waste Management":
        return "Increase garbage collection frequency and promote waste segregation."
    elif category == "Road Infrastructure":
        return "Repair damaged roads and schedule regular maintenance."
    elif category == "Street Lighting":
        return "Fix street lights and replace with energy-efficient LED systems."
    else:
        return "Forward issue to the concerned municipal department."


# ---------------- MAIN PROGRAM ----------------
print("Smart City Civic Issue Analysis Assistant (SDG 11)")
print("------------------------------------------------")

complaint = input("Enter civic complaint: ")

clean_text = intake_agent(complaint)
category = classify_agent(clean_text)
priority = analysis_agent(clean_text, category)
policy = rag_agent(category)
recommendation = recommendation_agent(category, priority, policy)

print("\n--- AI ANALYSIS RESULT ---")
print("Category:", category)
print("Priority:", priority)

print("\nPolicy Reference:")
print(policy)

print("\nRecommendation:")
print(recommendation)
