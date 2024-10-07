import streamlit as st
import json
import os

# Set page configuration for wider layout and better mobile experience
st.set_page_config(
    page_title="Feature Progress Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Path to the JSON file
DATA_FILE = 'features.json'

# Custom CSS for styling and responsiveness
st.markdown("""
<style>
    /* General Styling */
    .stDataFrame {
        font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    }
    .stDataFrame table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }
    .stDataFrame th {
        background-color: #f3f4f6;
        font-weight: 600;
        text-align: left;
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e5e7eb;
    }
    .stDataFrame td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e5e7eb;
    }
    .stDataFrame tr:hover {
        background-color: #f9fafb;
    }

    /* Difficulty Badges */
    .difficulty-easy {
        background-color: #d1fae5;
        color: #065f46;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .difficulty-medium {
        background-color: #fef3c7;
        color: #92400e;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .difficulty-hard {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Impact Badges */
    .impact-low {
        background-color: #e0e7ff;
        color: #3730a3;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .impact-medium {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .impact-high {
        background-color: #f3e8ff;
        color: #6b21a8;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Edit Button Styling */
    .edit-button {
        background-color: #3b82f6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .edit-button:hover {
        background-color: #2563eb;
    }

    /* Add Feature Bar */
    .add-feature-bar {
        background-color: #f3f4f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .add-feature-bar:hover {
        background-color: #e5e7eb;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        /* Stack columns vertically on small screens */
        .feature-row {
            display: flex;
            flex-direction: column;
            margin-bottom: 1rem;
            padding: 0.5rem;
            border: 1px solid #e5e7eb;
            border-radius: 0.5rem;
        }
        .feature-row > div {
            margin-bottom: 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Password protection (same as before)
def check_password():
    def password_entered():
        if st.session_state["password"] == "writebetter":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        return True

# Function to load features from JSON file
def load_features():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                features = json.load(f)
            return features
        except json.JSONDecodeError:
            st.error("Error decoding JSON data. Initializing with default features.")
    # Default features if file doesn't exist or is corrupted
    return [
        {"name": "Word add in", "progress": 20, "difficulty": "Hard", "impact": "Medium"},
        {"name": "Word compare docs with styling intact", "progress": 70, "difficulty": "Hard", "impact": "High"},
        {"name": "Chrome extension", "progress": 70, "difficulty": "Medium", "impact": "High"},
        {"name": "Reference docs", "progress": 0, "difficulty": "Easy", "impact": "Low"},
        {"name": "Maintain rich text when editing", "progress": 0, "difficulty": "Medium", "impact": "Medium"},
        {"name": "CV editor", "progress": 90, "difficulty": "Easy", "impact": "Low"},
        {"name": "Prompt lab", "progress": 0, "difficulty": "Easy", "impact": "Medium"},
        {"name": "Shareable links", "progress": 0, "difficulty": "Easy", "impact": "Low"},
        {"name": "Chatbot", "progress": 80, "difficulty": "Medium", "impact": "Medium"},
        {"name": "iOS app", "progress": 0, "difficulty": "Hard", "impact": "High"},
        {"name": "WhatsApp bot", "progress": 0, "difficulty": "Medium", "impact": "Medium"},
        {"name": "Chatbot with control of document", "progress": 0, "difficulty": "Hard", "impact": "Medium"},
        {"name": "Revision / History", "progress": 0, "difficulty": "Medium", "impact": "Medium"}
    ]

# Function to save features to JSON file
def save_features(features):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(features, f, indent=4)
    except Exception as e:
        st.error(f"Failed to save features: {e}")

# Main app
def main():
    st.title("🚀 Feature Progress Dashboard")

    # Initialize session state
    if 'features' not in st.session_state:
        st.session_state.features = load_features()

    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False

    if 'delete_feature_index' not in st.session_state:
        st.session_state.delete_feature_index = None

    if 'show_add_form' not in st.session_state:
        st.session_state.show_add_form = False

    # Edit mode toggle button
    edit_button_label = "Save" if st.session_state.edit_mode else "Edit"
    if st.button(edit_button_label, key="edit_button"):
        st.session_state.edit_mode = not st.session_state.edit_mode

    st.markdown("---")  # Separator

    # Custom function to format the progress bar
    def format_progress(progress):
        return f'''
        <div style="background-color: #dbeafe; width: 100%; height: 24px; border-radius: 4px; overflow: hidden;">
            <div style="background-color: #3b82f6; width: {progress}%; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 8px;">
                <span style="color: white; font-size: 12px; font-weight: 600;">{progress}%</span>
            </div>
        </div>
        '''

    # Custom function to format difficulty and impact
    def format_difficulty(difficulty):
        return f'<span class="difficulty-{difficulty.lower()}">{difficulty}</span>'

    def format_impact(impact):
        return f'<span class="impact-{impact.lower()}">{impact}</span>'

    # Display header for features
    header_cols = st.columns([3, 2, 1, 1, 1])
    with header_cols[0]:
        st.markdown("**Feature Name**")
    with header_cols[1]:
        st.markdown("**Progress**")
    with header_cols[2]:
        st.markdown("**Difficulty**")
    with header_cols[3]:
        st.markdown("**Impact**")
    with header_cols[4]:
        if st.session_state.edit_mode:
            st.markdown("**Actions**")
    st.markdown("---")  # Separator

    # Display and edit features
    for i, feature in enumerate(st.session_state.features):
        feature_container = st.container()
        with feature_container:
            # Use columns for layout; adjust for responsiveness
            cols = st.columns([3, 2, 1, 1, 1], gap="small")
            with cols[0]:
                st.write(feature['name'])
            with cols[1]:
                st.markdown(format_progress(feature['progress']), unsafe_allow_html=True)
            with cols[2]:
                st.markdown(format_difficulty(feature['difficulty']), unsafe_allow_html=True)
            with cols[3]:
                st.markdown(format_impact(feature['impact']), unsafe_allow_html=True)
            with cols[4]:
                if st.session_state.edit_mode:
                    if st.session_state.delete_feature_index == i:
                        st.warning(f"Are you sure you want to delete '{feature['name']}'?")
                        confirm_cols = st.columns([1, 1])
                        with confirm_cols[0]:
                            if st.button("Yes", key=f"confirm_yes_{i}"):
                                del st.session_state.features[i]
                                save_features(st.session_state.features)
                                st.session_state.delete_feature_index = None
                                st.success(f"Deleted '{feature['name']}'")
                                st.experimental_rerun()
                        with confirm_cols[1]:
                            if st.button("No", key=f"confirm_no_{i}"):
                                st.session_state.delete_feature_index = None
                    else:
                        if st.button("Delete", key=f"delete_{i}"):
                            st.session_state.delete_feature_index = i

    # Add Feature Bar
    if st.session_state.edit_mode:
        add_feature_bar = st.container()
        with add_feature_bar:
            if not st.session_state.show_add_form:
                st.markdown("<div class='add-feature-bar'>➕ Add New Feature</div>", unsafe_allow_html=True)
                if st.button("Show Add Form", key="show_add_form"):
                    st.session_state.show_add_form = True
            else:
                st.markdown("<div class='add-feature-bar'>➖ Hide Add Feature Form</div>", unsafe_allow_html=True)
                if st.button("Hide Add Form", key="hide_add_form"):
                    st.session_state.show_add_form = False

    # Add new feature form
    if st.session_state.edit_mode and st.session_state.show_add_form:
        st.subheader("Add New Feature")
        with st.form("add_feature_form", clear_on_submit=True):
            new_name = st.text_input("Feature Name", max_chars=100)
            new_progress = st.slider("Progress (%)", 0, 100, 0)
            new_difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
            new_impact = st.selectbox("Impact", ["Low", "Medium", "High"])
            submitted = st.form_submit_button("Add Feature")
            if submitted:
                if new_name.strip() == "":
                    st.error("❗ Feature name cannot be empty.")
                else:
                    new_feature = {
                        "name": new_name.strip(),
                        "progress": new_progress,
                        "difficulty": new_difficulty,
                        "impact": new_impact
                    }
                    st.session_state.features.append(new_feature)
                    save_features(st.session_state.features)
                    st.success(f"✅ Added feature '{new_name}'")
                    st.session_state.show_add_form = False

    st.markdown("---")  # Separator

    # Low-hanging fruit
    st.subheader("🥇 Low-Hanging Fruit")
    low_hanging_fruit = [
        f for f in st.session_state.features 
        if f['difficulty'] == 'Easy' and f['impact'] in ['Medium', 'High'] and f['progress'] < 100
    ]
    if low_hanging_fruit:
        for feature in low_hanging_fruit:
            st.markdown(f"- **{feature['name']}** - Impact: {feature['impact']}")
    else:
        st.write("No low-hanging fruit available at the moment.")

if __name__ == "__main__":
    if check_password():
        main()
