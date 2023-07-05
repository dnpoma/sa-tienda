if [-n "$BASH_VERSION" ]; then
  if [ -f "$HOME/.bashrc" ]; then
  . "$HOME/.bashrc"
  fi
fi


if [ -d "HOME/bin" ] ; then
  PATH="$HOME/bin:$PATH"
if

export PATH=$PATH:/usr/local/go/bin

export GOOGLE_APPLICATION_CREDENTIALS="home/.json"