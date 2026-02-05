#task1
contacts = {
    "Afnan": "9876543210",
    "Maaz": "9123456780",
    "Hamza": "9988776655"
}
contacts["Omer"] = "9012345678"
contacts["Maaz"] = "9000000000"
existing_contact = contacts.get("Afnan", "Contact not found")
missing_contact = contacts.get("Talah", "Contact not found")
print("Safe Lookup Results:")
print("Afnan:", existing_contact)
print("Talah:", missing_contact)
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
    

#task2
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

is_present = "ID05" in unique_users

print("Unique User IDs:", unique_users)
print("Is ID05 present?", is_present)
print("Total log entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))

#task3
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_a|friend_b)
print(friend_a&friend_b)
print(friend_a-friend_b)
print(friend_a^friend_b)