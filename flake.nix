{
  description = "norfetch - python fetch based off of norway";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    pydev.url = "github:oceansprint/pydev";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      perSystem = {
        devShells.default = {pkgs, ...}:
          pkgs.mkShell {
            nativeBuildInputs = with pkgs; [
              python312
            ];
          };
      };
      systems = [
        "x86_64-linux"
      ];
    };
}
