# Grab-Vault
GrabVault – An all-in-one web-based file conversion platform built with Python and Django. Convert images, audio, and video files, resize images, extract audio from videos, and explore additional media tools through a simple, user-friendly interface.

# 🚀 GrabVault – Online File Converter

**GrabVault** is a web-based file conversion platform developed using **Python and Django**. It provides users with a simple and convenient way to convert and manage different types of media files through a single website.

The main goal of GrabVault is to make file conversion easy, accessible, and user-friendly without requiring users to install separate desktop applications for basic media conversion tasks.

## ✨ Features

### 🖼️ Image Converter
- Convert images from one supported format to another.
- Upload image files through a simple interface.
- Easily access the image conversion tool.

### 🎵 Audio Converter
- Convert audio files between supported formats.
- Upload audio files for conversion.
- Simple and user-friendly conversion process.

### 🎬 Video to Audio Converter
- Extract audio from video files.
- Convert video content into an audio file.
- Useful when users only need the sound from a video.

### 📐 Image Resizer
- Resize images according to the required dimensions.
- Preview the selected image before processing.
- Helps users prepare images for different purposes.

### 📥 YouTube Downloader
- Includes a dedicated YouTube downloader interface.
- Currently under development.

### ❓ FAQ Section
- Provides answers to common questions.
- Helps users understand the available tools and their usage.

### 📩 Contact Section
- Includes a contact interface for users to reach out.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Backend web framework |
| HTML5 | Website structure |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactions and animations |
| Canvas API | Animated particle background |
| Git & GitHub | Version control and project hosting |

## 🎨 User Interface

GrabVault features a modern dark-themed interface with:

- Purple gradient background.
- Responsive navigation bar.
- Animated particle background.
- Interactive tool cards.
- Smooth navigation between sections.
- Image preview functionality.
- Animated rocket effect.

## ⚙️ Installation and Setup

Follow these steps to run GrabVault on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/GrabVault.git
```

### 2. Navigate to the project directory

```bash
cd GrabVault
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install django
```

Install any additional dependencies required by the conversion features. If a `requirements.txt` file is included, use:

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the website

Visit:

```text
http://127.0.0.1:8000/
```

## 📂 Project Structure

```text
GrabVault/
│
├── manage.py
│
├── grabvault/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── home.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── requirements.txt
```

*Note: The structure above is an example. Your actual folder structure may differ.*

## 🎯 Project Objective

The objective of GrabVault is to develop a centralized web application that simplifies common file conversion tasks. By combining multiple media tools into one platform, users can conveniently convert, resize, and extract media files through an easy-to-use interface.

## 🚧 Future Improvements

- Add more image, audio, and video formats.
- Complete the YouTube downloader functionality.
- Improve file upload and conversion performance.
- Add file size and format validation.
- Improve mobile responsiveness.
- Add user accounts and conversion history.
- Enhance security and error handling.

## 👨‍💻 Developer

Developed as a web application project using Python, Django, HTML, CSS, and JavaScript.

## 📄 License

This project is available for educational and personal use. Add a suitable open-source license if you intend to distribute it under specific reuse terms.
