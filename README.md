# SpaceWarp

Currently, a bad game that barely works.
Run the main.py file to play the game until I upload a release.

To create an exe using Pyinstaller, run this command in the command line:
```shell
pyinstaller main.py --add-data "mask.json;./" --add-data "assets;assets" -w --clean -n SpaceWarp
```