#!/usr/bin/env python3

import zipfile

file01 = input("Enter file to check: ")
if zipfile.is_zipfile(file01):
	print(f"This is an archive file")
else:
	print(f"This is not an archive file")
