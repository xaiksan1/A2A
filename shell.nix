{ system ? builtins.currentSystem, ... }@inputs:
let
  pkgs = import <nixpkgs> { inherit system; };
in pkgs.mkShell rec {

  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  buildInputs = [
      pkgs.go
      pkgs.nodejs_20
      pkgs.nodePackages.nodemon
      pkgs.sudo
      pkgs.bun
      pkgs.trunk
      (
        pkgs.python311.withPackages (ps: [
          ps.pipx
          ps.build
          ps.virtualenv
          ps.wheel
          ps.poetry
          ps.mesop
        ])
      )
    ];

    # Sets environment variables in the workspace
    shellHook = ''
      echo "Welcome to the Nix shell!"
    '';
    idx = {
      # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
      extensions = [
        # "vscodevim.vim"
        "ms-python.debugpy"
        "ms-python.python"
      ];

       # Enable previews
      previews = {
        enable = true;
        previews = {
          web = {
            # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
            # and show it in IDX's web preview panel
            command = ["npm" "run" "start"];
            manager = "web";          
            env = {
              # Environment variables to set for your server
              PORT = "$PORT";
            };
          };
        };
      };

      # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Example: install JS dependencies from NPM
        # npm-install = "npm install";
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: start a background task to watch and re-build backend code
        watch-backend = "npm run watch-backend";
      };
    };
  };
}
