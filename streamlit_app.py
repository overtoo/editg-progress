import streamlit as st
import pandas as pd

# Custom CSS (same as before, with added button styling)
st.markdown("""
<style>
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
    .edit-button {
        background-color: #3b82f6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        font-weight: 600;
        cursor: pointer;
    }
    .edit-button:hover {
        background-color: #2563eb;
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

# Main app
def main():
    st.title("Feature Progress Dashboard")

    # Initialize session state
    if 'features' not in st.session_state:
        st.session_state.features = [
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
    
    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False

    # Edit mode toggle button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("Features")
    with col2:
        if st.button("Edit" if not st.session_state.edit_mode else "Save", key="edit_button"):
            st.session_state.edit_mode = not st.session_state.edit_mode
            st.experimental_rerun()

    # Custom function to format the progress bar
    def format_progress(progress):
        return f'<div style="background-color: #dbeafe; width: 100%; height: 24px; border-radius: 4px; overflow: hidden;"><div style="background-color: #3b82f6; width: {progress}%; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 8px;"><span style="color: white; font-size: 12px; font-weight: 600;">{progress}%</span></div></div>'

    # Custom function to format difficulty and impact
    def format_difficulty(difficulty):
        return f'<span class="difficulty-{difficulty.lower()}">{difficulty}</span>'

    def format_impact(impact):
        return f'<span class="impact-{impact.lower()}">{impact}</span>'

    # Display and edit features
    for i, feature in enumerate(st.session_state.features):
        col1, col2, col3, col4, col5 = st.columns([3, 2, 1, 1, 1])
        with col1:
            st.write(feature['name'])
        with col2:
            st.markdown(format_progress(feature['progress']), unsafe_allow_html=True)
        with col3:
            st.markdown(format_difficulty(feature['difficulty']), unsafe_allow_html=True)
        with col4:
            st.markdown(format_impact(feature['impact']), unsafe_allow_html=True)
        with col5:
            if st.session_state.edit_mode:
                if st.button(f"Delete {i}"):
                    if st.button(f"Are you sure you want to delete '{feature['name']}'?"):
                        del st.session_state.features[i]
                        st.experimental_rerun()

    # Add new feature
    if st.session_state.edit_mode:
        st.subheader("Add New Feature")
        new_name = st.text_input("Feature Name")
        new_progress = st.slider("Progress", 0, 100, 0)
        new_difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
        new_impact = st.selectbox("Impact", ["Low", "Medium", "High"])
        if st.button("Add Feature"):
            st.session_state.features.append({
                "name": new_name,
                "progress": new_progress,
                "difficulty": new_difficulty,
                "impact": new_impact
            })
            st.experimental_rerun()

    # Low-hanging fruit
    st.subheader("Low-Hanging Fruit")
    low_hanging_fruit = [f for f in st.session_state.features if f['difficulty'] == 'Easy' and f['impact'] != 'Low' and f['progress'] < 100]
    if low_hanging_fruit:
        st.write("Easy tasks with medium or high impact that are not yet completed:")
        for feature in low_hanging_fruit:
            st.write(f"- {feature['name']} - Impact: {feature['impact']}")
    else:
        st.write("No low-hanging fruit available at the moment.")

if __name__ == "__main__":
    if check_password():
        main()