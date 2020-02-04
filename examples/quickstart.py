"""
This example script imports the test package and
prints out the version.
"""

import test


def main():
    print(
        f"test version: {test.__version__}"
    )


if __name__ == "__main__":
    main()
