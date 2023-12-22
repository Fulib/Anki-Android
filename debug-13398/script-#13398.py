# coding: utf-8
#
import uiautomator2 as u2
import time
d=u2.connect()
d.app_start('com.ichi2.anki')
d.click(0.05,0.05)
d(text='Settings').click()
d(text='Sync').click()
d(text='AnkiWeb account').click()