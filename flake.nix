{
  description = "norfetch - python fetch based off of norway";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      perSystem = {pkgs, ...}: {
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [
            python312
          ];
        };
        formatter = pkgs.alejandra;
        packages.default = pkgs.callPackage ./wrapper.nix {};
      };
      systems = [
        "x86_64-linux"
        "aarch64-darwin"
      ];
    };
}
