from pathlib import Path, PurePath, PureWindowsPath

p = PureWindowsPath("D:\\Programing\\MyProject\\SplashConverter\\test_slash.py")

str1 = "D:\\Programing\\MyProject\\SplashConverter\\test_slash.py"
str2 = str1.replace("\\", "\\\\")

print(str(p))