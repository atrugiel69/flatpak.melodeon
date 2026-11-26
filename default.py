# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2026-present Team LibreELEC (https://libreelec.tv)

import os
import xbmcaddon
from flatpakhelper.addon import FlatpakAddon

addon = xbmcaddon.Addon()
settings = addon.getSettings()

flatpak = FlatpakAddon(addon=addon, appid='io.github.cdrummond.melodeon')

# Route execution through melodeon-wrapper so Squeezelite starts after Kodi stops
# and terminates as soon as Melodeon exits
wrapper = os.path.join(addon.getAddonInfo('path'), 'bin', 'melodeon-wrapper')
flatpak.gui.flatpak.flatpak_run = wrapper

enable_sq = settings.getBool('squeezelite_enable')
use_custom_bin = settings.getBool('squeezelite_custom_bin')
custom_bin = settings.getString('squeezelite_bin').strip()
sq_args = settings.getString('squeezelite_args').strip()

sq_bin = custom_bin if (use_custom_bin and custom_bin) else 'squeezelite'

run_env = {
    'MELODEON_SQUEEZELITE_ENABLE': '1' if enable_sq else '0',
    'MELODEON_SQUEEZELITE_BIN': sq_bin,
    'MELODEON_SQUEEZELITE_ARGS': sq_args,
}

# pulseaudio=False keeps Flatpak's PulseAudio layer from opening ALSA
flatpak.start(
    env={
        'QTWEBENGINE_CHROMIUM_FLAGS': '--no-sandbox',
        'XCURSOR_SIZE': '96',
        'XCURSOR_THEME': 'Breeze_Light',
    },
    flatpak_args=['--socket=wayland'],
    pulseaudio=False,
    run_env=run_env,
)
