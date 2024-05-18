{
  writeShellApplication,
  python311,
}:
writeShellApplication {
  name = "norfetch";

  runtimeInputs = [python311];

  text = ''
    python3 ${./norfetch.py} \$\1
  '';
}
