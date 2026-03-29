# AI-Based Waste Segregation Assistant
# Extended with RAG + Sustainability
# Internship Submission Ready

# ---------------- KNOWLEDGE BASE (RAG) ----------------
waste_knowledge_base = {
    "banana peel": "Organic waste that can be composted.",
    "food waste": "Biodegradable waste suitable for composting.",
    "paper": "Dry waste that can be recycled.",
    "plastic bottle": "Recyclable waste. Should be cleaned before recycling.",
    "glass bottle": "Recyclable but must be handled carefully.",
    "battery": "Hazardous waste. Contains harmful chemicals.",
    "medicine": "Expired medicines are hazardous waste.",
    "e-waste": "Electronic waste contains toxic materials."
}

# ---------------- AI LOGIC ----------------
def waste_segregation(item):
    item = item.lower()

    # RAG: Retrieve information
    retrieved_info = waste_knowledge_base.get(
        item,
        "No exact match found. Follow local waste management rules."
    )

    wet_waste = ["banana peel", "food waste"]
    dry_waste = ["paper"]
    recyclable_waste = ["plastic bottle", "glass bottle"]
    hazardous_waste = ["battery", "medicine", "e-waste"]

    if item in wet_waste:
        category = "Wet Waste"
        disposal = "Put in green bin for composting."

    elif item in dry_waste:
        category = "Dry Waste"
        disposal = "Put in blue bin."

    elif item in recyclable_waste:
        category = "Recyclable Waste"
        disposal = "Clean and put in recycling bin."

    elif item in hazardous_waste:
        category = "Hazardous Waste"
        disposal = "Hand over to authorized collection center."

    else:
        category = "Unknown Waste"
        disposal = "Check municipal waste guidelines."

    # Sustainability message
    sustainability_note = (
        "Sustainability Impact: Proper waste segregation "
        "reduces pollution, improves recycling, and supports "
        "a cleaner environment."
    )

    return (
        f"Category: {category}\n"
        f"Disposal Method: {disposal}\n\n"
        f"Retrieved Knowledge (RAG): {retrieved_info}\n\n"
        f"{sustainability_note}"
    )

# ---------------- MAIN PROGRAM ----------------
print("AI-Based Waste Segregation Assistant (RAG Enabled)")
print("-------------------------------------------------")

user_input = input("Enter waste item: ")
result = waste_segregation(user_input)

print("\nResult:")
print(result)
