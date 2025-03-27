{
  description = "permalik auto";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/release-24.11";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    systems = ["x86_64-linux" "aarch64-darwin"];
    forAllSystems = f:
      builtins.listToAttrs (map (system: {
          name = system;
          value = f system;
        })
        systems);
  in {
    devShells = forAllSystems (system: let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = false;
      };

      myPython = pkgs.python312;
      pythonWithPkgs = myPython.withPackages (pythonPkgs:
        with pythonPkgs; [
          pip
          virtualenvwrapper
        ]);

      shell = pkgs.mkShell {
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
          export PS1="\[\e[1;32m\][devshell](.venv) \w \$\[\e[0m\]\n❯ "
        '';
      };
    in {
      default = shell;
    });
  };
}
