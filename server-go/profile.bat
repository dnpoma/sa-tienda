@echo off

rem Carga la configuración de Bash si está disponible
if defined BASH_VERSION (
    if exist "%HOME%/.bashrc" (
        call "%HOME%/.bashrc"
    )
)

rem Agrega el directorio HOME/bin al PATH si existe
if exist "%HOME%/bin" (
    set "PATH=%HOME%/bin;C:\Program Files\Go\bin"
)

rem Agrega el directorio de instalación de Go al PATH
set "PATH=%PATH%;C:\Program Files\Go\bin"

rem Define la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
set "GOOGLE_APPLICATION_CREDENTIALS=C:\Users\nicol\Downloads\a-3a604-firebase-adminsdk-puwnr-4bab63e116.json"
