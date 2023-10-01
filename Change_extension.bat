@ECHO OFF
PUSHD .
FOR /R %%d IN (.) DO (
cd "%%d"
IF EXIST *.org (
REN *.org *.mp4
)
)
POPD