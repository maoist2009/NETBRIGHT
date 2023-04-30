[app]

title = DPI Tunnel
package.name = dpitunnel
package.domain = org.yebekhe

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
icon.filename = icon.png

version = 0.1
requirements = python3,kivy,requests,urllib3,charset_normalizer_recipe

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
