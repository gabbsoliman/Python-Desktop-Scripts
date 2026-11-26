import qrcode
from pathlib import Path

def generate_qr_code(url):
    file_path = Path.home() / "Downloads" / "py_qrcode.png"

    qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=2
                    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    return file_path

def main():
    url = input("Enter URL: ").strip()

    if not url:
        print("Invalid URL.")

    file_path = generate_qr_code(url)

    print("QR Code successfully generated!")
    print(f"SAVED TO: {file_path}")

if __name__ == "__main__":
    main()


