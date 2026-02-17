import os
import re


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def logo():
    print(
        r"""
      (  )   (   )  )
       ) (   )  (  (
       ( )  (    ) )
       _____________
      <_____________> ___
      |             |/ _ \
      |  PythonCAFE | | | |
      |             |_| |_|
      |_____________|\___/
      \_____________/
    """
    )


def header(txt):
    print("=" * 40)
    print(f"{txt.center(40)}")
    print("=" * 40)


def valid(pat, txt):
    if re.match(pat, txt):
        return True
    return False


def pause():
    input("\nPress Enter To Continue...")
