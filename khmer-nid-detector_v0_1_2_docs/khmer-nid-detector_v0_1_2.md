# Khmer NID Detector v0.1.2 🇰🇭

![Khmer NID Detector](example.png)

Unlock the power of AI for Cambodian document automation!  
**Khmer NID Detector** is a cutting-edge Python package that leverages advanced OCR and Computer Vision to **detect and extract key information from Khmer National ID cards**. Streamline your workflow and boost accuracy for Cambodian ID recognition.

---

## 🌐 PyPI Project Page

Discover more and get the latest updates on [PyPI](https://pypi.org/project/khmer-nid-detector/)

---

## 📦 Quick Installation

Install instantly from PyPI:

```bash
pip install khmer-nid-detector
```

---

## 🚀 Features

- **🔍 Smart Card Type Detection** – Instantly identifies card or document type.
- **🇰🇭 Khmer NID Focused** – Optimized for Cambodian National ID cards.
- **📄 Rich Information Extraction** – Extracts NID number, name, and date of birth.
- **🖼️ Image Preprocessing** – Enhances image clarity for superior OCR results.
- **⚡ Lightweight & User-Friendly** – Minimal dependencies, simple API.
- **🧠 Intelligent Parsing** – Combines regex, heuristics, and OCR for robust data extraction.

---

## 🪪 Supported Card Types

| Type           | Description                    |
|----------------|-------------------------------|
| nid_card       | Khmer National ID card         |
| credit_card    | Credit card                    |
| debit_card     | Debit card                     |
| driver_license | Driver’s license               |
| business_card  | Business card                  |
| other_document | Other document types           |
| not_a_card     | Not a card or unsupported doc  |

---

## 💡 Example Usage

```python
from khmer_nid_detector import detect_card_type, process_nid_card

with open("nid_card.jpg", "rb") as f:
    image_bytes = f.read()

card_type = detect_card_type(image_bytes)
print(f"Detected card type: {card_type}")

if card_type == "nid_card":
    result = process_nid_card(image_bytes)

    if result.success:
        print(f"NID Number: {result.nid_number}")
        print(f"Name: {result.name}")
        print(f"Date of Birth: {result.dob}")
        print(f"Is Khmer NID: {result.is_khmer_nid}")
        print(f"Message: {result.message}")
        print(f"Suggestion: {result.suggestion}")
    else:
        print(f"Error: {result.message}")

```

---

## 📁 Example Project Structure

```
.
├── IMG_20251005_154748.png
├── nid_card.jpg
├── nid_env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── pyvenv.cfg
│   └── share
└── v2.py
```

---

## ▶️ Run Example Code

```bash
python3 v2.py
```

---

## ⚙️ Requirements

- Python 3.8+
- easyocr
- opencv-python
- Pillow
- pytesseract
- numpy

Install dependencies manually if needed:

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. **Preprocessing:** Cleans and enhances the input image.
2. **Card Type Detection:** Classifies the image into supported types.
3. **Text Extraction (OCR):** Extracts Khmer and English text using EasyOCR and Tesseract.
4. **Information Parsing:** Detects NID number, name, and date of birth.

---

## 🧑‍💻 Author

**Roem Reaksmey**  
AI Developer / Computer Vision Researcher  
📧 roemreaksmey7@gmail.com

---

## 📄 License

Licensed under the MIT License – see the LICENSE file for details.

---

## ❤️ Acknowledgments

- OpenCV, EasyOCR & Tesseract OCR for image processing
- Khmer OCR research community
- Contributors supporting Khmer AI development

---

## ✨ Example Output

```yaml
Detected card type: nid_card
NID Number: 012345678
Name: Sok Dara
Date of Birth: 1998-03-25
Is Khmer NID: True
Message: Khmer NID detected successfully
```