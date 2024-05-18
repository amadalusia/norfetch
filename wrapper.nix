{
  writeShellApplication,
  python311,
}:
writeShellApplication {
  name = "norfetch";

  runtimeInputs = [python311];

  text = ''
    if [[ -z "$1" ]]; then
      python3 ${./norfetch.py}
    fi

    python3 ${./norfetch.py} "$1"
  '';
}
