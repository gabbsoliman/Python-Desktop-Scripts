# QR Code Generator

A simple Python QR Code Generator Program that converts URLs into downloadable PNG images.

## Requirements

- Python 3.x
- [`qrcode`](https://pypi.org/project/qrcode/) with Pillow support

Install the required library:

```bash
pip install "qrcode[pil]"
```

## Usage

Run the program:

```bash
python qrcode_generator.py
```

Enter a URL when prompted:

```text
Enter URL: https://github.com
QR Code successfully generated!
SAVED TO: C:\Users\<you>\Downloads\py_qrcode.png
```

The generated QR code is saved as `py_qrcode.png` in your **Downloads** folder.

## Settings

You can modify the following settings in `generate_qr_code()`:

| Option | Default | Description |
|---|---|---|
| `version` | `1` | Initial QR code version; automatically adjusts when needed |
| `box_size` | `50` | Size of each box in pixels |
| `border` | `2` | Border width in boxes |
| `error_correction` | `L` (~7%) | Error correction capability |
| `fill_color` | `black` | QR code color |
| `back_color` | `white` | Background color |
