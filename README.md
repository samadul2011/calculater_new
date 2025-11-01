# Kivy Calculator - Android APK

A simple calculator application built with Kivy that can be compiled to Android APK using Buildozer.

## Files Included

- `main.py` - Main application code (converted from tkinter to Kivy)
- `buildozer.spec` - Buildozer configuration file for Android build
- `build.yml` - GitHub Actions workflow for automated APK building
- `requirements.txt` - Python dependencies
- `icon.png` - Application icon

## Features

- Basic arithmetic operations (+, -, ×, ÷)
- Memory functions (MC, MR, M+, M-)
- Clear functions (C, CE, Backspace)
- Sign toggle (±)
- Keyboard support
- Dark theme interface
- Responsive design

## Local Development

### Prerequisites

1. Install Python 3.9+
2. Install Buildozer:
   ```bash
   pip install buildozer
   ```

### Running on Desktop

```bash
python main.py
```

### Building APK Locally

1. Make sure Android SDK and NDK are installed and configured
2. Run the build command:
   ```bash
   buildozer android debug
   ```

3. The APK will be generated in the `bin/` directory

## GitHub Actions Setup

The included `build.yml` file will automatically build and upload APK artifacts when you push to the main branch.

### Setup Steps:

1. Create a new GitHub repository
2. Upload all files to your repository
3. The workflow will automatically run and produce APK files as artifacts

### Downloading APK

1. Go to the "Actions" tab in your GitHub repository
2. Click on the latest workflow run
3. Scroll down to the "Artifacts" section
4. Click on `calculator-debug.apk` to download

## Project Structure

```
├── main.py              # Main Kivy application
├── buildozer.spec       # Buildozer configuration
├── build.yml           # GitHub Actions workflow
├── requirements.txt    # Python dependencies
├── icon.png           # Application icon
└── README.md          # This file
```

## Converting from tkinter

The original tkinter calculator has been converted to Kivy with the following changes:

1. **Widgets**: Replaced tkinter widgets with Kivy equivalents
   - `tk.Entry` → `TextInput`
   - `tk.Button` → `Button`
   - `tk.Frame` → `BoxLayout` and `GridLayout`

2. **Layout**: Used Kivy's layout system for responsive design

3. **Events**: Replaced tkinter command bindings with Kivy event system

4. **Keyboard**: Implemented keyboard handling using Kivy's window events

5. **Styling**: Maintained dark theme using Kivy's styling properties

## Dependencies

- Python 3.9+
- Kivy 2.1.0
- Buildozer (for Android builds)

## License

This project is provided as-is for educational purposes.