name: Build Kivy Android APK

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  build:
    name: Build APK using Buildozer
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Cache Buildozer global directory
        uses: actions/cache@v4
        with:
          path: .buildozer
          key: ${{ runner.os }}-buildozer-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-buildozer-

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential libltdl-dev libffi-dev tar bzip2 gzip unzip make gettext zip libssl-dev autoconf automake libtool patch openssl python3-pip
          sudo apt-get install -y libsqlite3-dev sqlite3
          sudo apt-get install -y uuid-dev
          pip3 install --user --upgrade buildozer Cython virtualenv

      # التعديل هنا: إضافة أمر yes | للموافقة التلقائية على الرخص
      - name: Build with Buildozer
        run: |
          export PATH=$PATH:~/.local/bin
          yes | buildozer android debug

      # رفع ملف الـ APK الناتج
      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: kivy-debug-apk
          path: bin/*.apk
