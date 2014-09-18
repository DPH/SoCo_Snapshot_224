# -*- coding: utf-8 -*-
"""
Test for #224
"""

import time
import soco
from soco.snapshot import Snapshot

# alert = "x-file-cifs://DoorPi/DoorPiPublic/doorbell/sounds/Tinkle5sec.mp3"
alert = 'http://archive.org/download/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy_64kb.mp3'

device = soco.SoCo('192.168.1.73')

#take snapshot of current state
snap = Snapshot(device)
is_coord = snap.snapshot

# print 'playlist_pos:', snap.playlist_position
# print 'track_pos:', snap.track_position
# #print 'stream_uri:', snap.stream_uri
# #print 'meta:', snap.metadata
# print 'media uri:', snap.media_uri
# #print 'media meta:', snap.media_metadata
# print 'Transport state:', snap.transport_state

# Do something here that changes what's playing etc.
device.volume = 20
if is_coord:
    device.play_uri(uri=alert)
time.sleep(4)

#restore with fade = True
snap.restore(True)