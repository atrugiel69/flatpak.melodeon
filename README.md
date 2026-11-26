# flatpak.melodeon

Standalone Kodi launcher add-on for running the Melodeon Flatpak on LibreELEC via Wayland (`labwc`).

## Requirements
- LibreELEC with `tools.flatpak` and `tools.externalhelper` installed
- Melodeon installed via Flatpak

## Packaging the Kodi `.zip`
Run from the parent directory so `flatpak.melodeon/` is the archive root:
```bash
cd /home/gorman/LMS_mch
zip -r flatpak.melodeon-1.0.0.zip flatpak.melodeon \
  -x "flatpak.melodeon/.git*" "flatpak.melodeon/__pycache__/*" "flatpak.melodeon/*.zip"
```

## Optional LibreELEC Wayland & Cursor Tuning
1. Copy the default `labwc` config to persistent storage:
   ```bash
   mkdir -p /storage/.config/labwc
   cp -rn /storage/.kodi/addons/tools.externalhelper/labwc-config/* /storage/.config/labwc/
   ```
2. Adjust pointer and wheel speed inside `<labwc_config>` in `/storage/.config/labwc/rc.xml`:
   ```xml
   <libinput>
     <device category="default">
       <pointerSpeed>0.8</pointerSpeed>
       <accelProfile>adaptive</accelProfile>
       <scrollFactor>2.5</scrollFactor>
     </device>
   </libinput>
   ```
3. Copy Breeze cursors from the KDE Flatpak runtime and set cursor size in `/storage/.config/labwc/environment`:
   ```bash
   mkdir -p /storage/.icons
   cp -r /storage/flatpak/runtime/org.kde.Platform/x86_64/*/active/files/share/icons/breeze_cursors /storage/.icons/
   cat << 'EOV' > /storage/.config/labwc/environment
   XCURSOR_PATH=/storage/.icons
   XCURSOR_THEME=breeze_cursors
   XCURSOR_SIZE=64
   EOV
   ```
