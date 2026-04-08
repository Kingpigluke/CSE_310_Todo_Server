from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client.from_service_account_json("serviceAccountKey.json")

# Collection name (table)
COLLECTION = "tasks"

# -----------------------------
# CREATE
# -----------------------------
def add_task(task_id, description, completed=False):
    doc_ref = db.collection(COLLECTION).document(task_id)
    doc_ref.set({
        "description": description,
        "completed": completed
    })
    print(f"Added task: {description}")

# -----------------------------
# READ / QUERY
# -----------------------------
def get_all_tasks():
    tasks = db.collection(COLLECTION).stream()
    print("\nCurrent Tasks:")
    for task in tasks:
        print(task.id, task.to_dict())

# -----------------------------
# UPDATE
# -----------------------------
def update_task(task_id, completed=None, description=None):
    doc_ref = db.collection(COLLECTION).document(task_id)
    updates = {}

    if completed is not None:
        updates["completed"] = completed
    if description is not None:
        updates["description"] = description

    doc_ref.update(updates)
    print(f"Updated task {task_id}")

# -----------------------------
# DELETE
# -----------------------------
def delete_task(task_id):
    db.collection(COLLECTION).document(task_id).delete()
    print(f"Deleted task {task_id}")

# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    # Add tasks
    add_task("t001", "Buy groceries")
    add_task("t002", "Finish homework")
    add_task("t003", "Clean the kitchen")

    # Query tasks
    get_all_tasks()

    # Update a task
    update_task("t002", completed=True)

    # Query again
    get_all_tasks()

    # Delete a task
    delete_task("t003")

    # Final query
    get_all_tasks()
