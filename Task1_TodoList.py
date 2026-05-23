# Shivam Dutta
# CODSOFT Internship - Task: To-Do List Web App

import streamlit as st

# Page configuration
st.set_page_config(page_title="To-Do List App", layout="centered")

# Title
st.title("📝 Task Management System")
st.write("Manage your daily tasks in a simple and efficient way.")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "message" not in st.session_state:
    st.session_state.message = ""

# ---------------------- Add Task ----------------------
st.subheader("Add New Task")
task_input = st.text_input("Enter your task")

if st.button("Add Task"):
    if task_input.strip() != "":
        st.session_state.tasks.append(task_input)
        st.session_state.message = "Task added successfully!"
    else:
        st.session_state.message = "Please enter a valid task."

# ---------------------- Show Tasks ----------------------
# ---------------------- Show Tasks ----------------------
st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks added yet.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([4, 1, 1])

        # Display task or edit input
        if f"edit_{index}" in st.session_state and st.session_state[f"edit_{index}"]:
            new_value = col1.text_input("Edit Task", value=task, key=f"input_{index}")

            if col2.button("Save", key=f"save_{index}"):
                if new_value.strip() != "":
                    st.session_state.tasks[index] = new_value
                    st.session_state[f"edit_{index}"] = False
                    st.session_state.message = "Task updated successfully!"
                    st.rerun()
        else:
            col1.write(f"{index + 1}. {task}")

            if col2.button("Edit", key=f"editbtn_{index}"):
                st.session_state[f"edit_{index}"] = True

        # Delete button (always visible)
        if col3.button("Delete", key=f"delete_{index}"):
            st.session_state.tasks.pop(index)
            st.session_state.message = "Task deleted successfully!"
            st.rerun()

# ---------------------- Clear All ----------------------
st.write("---")

if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()
    st.session_state.message = "All tasks have been removed."

# ---------------------- Show Message ----------------------
if st.session_state.message:
    if "added" in st.session_state.message:
        st.success(st.session_state.message)
    elif "deleted" in st.session_state.message:
        st.success(st.session_state.message)
    else:
        st.warning(st.session_state.message)

# Footer
st.caption("Developed by Shivam Dutta | CODSOFT Internship")
