# -*- mode: python ; coding: utf-8 -*-


from PyInstaller.utils.hooks import collect_data_files

# Ubicación del entorno virtual y el directorio donde se encuentra 'mediapipe'
venv_path = 'c:/users/carli/onedrive/documentos/dmovimiento y rfacial/venv/lib/site-packages/'

# Aquí se incluye la carpeta completa de mediapipe y sus módulos necesarios
mediapipe_modules = collect_data_files('mediapipe', venv_path)

a = Analysis(
    ['app.py'],
    pathex=['C:/Users/carli/OneDrive/Documentos/DMovimiento y RFacial'],  # Asegúrate de poner la ruta correcta de tu código fuente
    binaries=[],
    datas=mediapipe_modules,  # Esto incluirá los archivos binarios de mediapipe correctamente
    hiddenimports=[
        'mediapipe.python._framework_bindings',  # Asegúrate de que se incluyan las dependencias ocultas
        'tensorflow.python.framework',
        'tensorflow.python.keras',
        'tensorflow.python.keras.engine',
        'tensorflow.python.keras.layers',
        'tensorflow.python.keras.models',
        'tensorflow.python.framework.ops',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Cambia a True si necesitas consola para ver los logs
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
