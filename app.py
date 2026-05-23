import streamlit as st

# --- CALCULATION FUNCTION ---
def calculate_rug_cost(size, colour_orders, difficulty):
    base_prices = {
        "Small": 50,
        "Medium": 100,
        "Large": 150
    }

    difficulty_multiplier = {
        "Easy": 0.15,
        "Regular": 0.25,
        "Hard": 0.35
    }

    total_cost = 0

    for colour, quantity in colour_orders.items():
        cost = base_prices[size] * quantity

        # Rainbow colour pricing rules
        if colour == "red":
            cost *= 0.8
        elif colour == "orange":
            cost *= 0.85
        elif colour == "yellow":
            cost *= 0.9
        elif colour == "green":
            cost *= 0.95
        elif colour == "blue":
            cost *= 0.9
        elif colour == "white":
            cost *= 0.8
        elif colour == "purple":
            cost *= 0.8
        elif colour == "brown":
            cost *= 0.8
        elif colour == "gold":
            cost *= 0.85
        elif colour == "grey":
            cost *= 0.85
        
        

        total_cost += cost

    # Apply difficulty increase
    total_cost += total_cost * difficulty_multiplier[difficulty]

    return total_cost


# --- UI ---
st.title("🧶 Rug Cost Calculator")

st.subheader("Select Rug Options")

size = st.selectbox("Rug Size", ["small", "medium", "large"])
difficulty = st.selectbox("Difficulty", ["easy", "regular", "hard"])

st.subheader("Enter Quantity per Colour")

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colour_orders = {}

for colour in colours:
    qty = st.number_input(f"{colour.capitalize()} quantity", min_value=0, step=1)
    if qty > 0:
        colour_orders[colour] = qty


# --- CALCULATE ---
if st.button("Calculate Total Cost"):
    if not colour_orders:
        st.warning("Please enter at least one colour quantity.")
    else:
        total = calculate_rug_cost(size, colour_orders, difficulty)

        st.success(f"Total Cost: £{round(total, 2)}")

        # Optional breakdown (nice touch)
        st.subheader("Order Breakdown")
        for colour, qty in colour_orders.items():
            st.write(f"{colour.capitalize()}: {qty}")