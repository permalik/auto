{
  description = "auto";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/release-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = false;
        };
        myPython = pkgs.python312;
        pythonWithPkgs = myPython.withPackages (pythonPkgs:
          with pythonPkgs; [
            pip
            virtualenvwrapper
            isort
            black
          ]);
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.alejandra
            pythonWithPkgs
            pkgs.readline
          ];

          shellHook = ''
            VENV=.venv
            if [ ! -d $VENV ]; then
                virtualenv $VENV
            fi
            source ./$VENV/bin/activate
            echo "Python virtual environment activated."

            # Custom Prompt
            export PS1="\n\[\e[1;32m\][devshell](.venv) \w\n❯ \[\e[0m\]"
          '';
        };
      }
    );
}
