[app]

# App Info
title = Vietnam Currency
package.name = vnc_calc
package.domain = org.test

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,ttf

# Version
version = 0.1

# Requirements
requirements = python3==3.10,kivy,requests

# Orientation
orientation = portrait

# Permissions
android.permissions = INTERNET

# Android Settings
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.arch = arm64-v8a

# Build settings
android.allow_backup = True
android.accept_sdk_license = True

# Fix build issues
p4a.branch = develop

# Logging
log_level = 2
warn_on_root = 0

# Fullscreen
fullscreen = 0
