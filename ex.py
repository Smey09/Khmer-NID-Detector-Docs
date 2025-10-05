# from khmer_nid_detector import detect_card_type, process_nid_card

from khmer_nid_detector import detect_card_type, process_nid_card

# Read image as bytes
with open("nid_card.jpg", "rb") as f:
    image_bytes = f.read()

# Detect card type
card_type = detect_card_type(image_bytes)
print(f"Detected card type: {card_type}")

# If it's an NID card, process it
if card_type == "nid_card":
    result = process_nid_card(image_bytes)

    if result["success"]:
        print(f"NID Number: {result['nid_number']}")
        print(f"Name: {result['name']}")
        print(f"Date of Birth: {result['dob']}")
        print(f"Is Khmer NID: {result['is_khmer_nid']}")
        print(f"Message: {result['message']}")
    else:
        print(f"Error: {result['message']}")
