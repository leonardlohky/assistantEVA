# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['assistantEVA.py'],
             pathex=['C:\\Users\\7590\\spyder-workspace\\assistantEVA\\assistantEVA'],
             binaries=[('C:\Program Files\VideoLAN\VLC\plugins', 'plugins')],
             datas=[('./VLC/libvlc.dll', '.'), ('./VLC/axvlc.dll', '.'), ('./VLC/libvlccore.dll', '.'), ('./VLC/npvlc.dll', '.')],
             hiddenimports=[('pkg_resources.py2_warn'),('pyttsx3.drivers'),('pyttsx3.drivers.sapi5')],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='assistantEVA',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
