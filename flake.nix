{
  description = "permalik auto";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/release-24.11";
  };

  outputs = { self, nixpkgs }: let
    pkgs = import nixpkgs {
      config = {
        allowUnfree = false;
      };
    };

    myPython = pkgs.python312;
    pythonWithPkgs = myPython.withPackages (pythonPkgs: with pythonPkgs; [
      pip
      virtualenvwrapper
    ]);

    shell = pkgs.mkShell {
      buildInputs = [
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
      '';
    };
  in {
    devShell = shell;
  };
}

