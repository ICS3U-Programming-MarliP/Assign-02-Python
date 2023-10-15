#!usr/bin/env/ python3
# Created By: Marli Peters
# Date: Oct. 15, 2023
# This program calculates surface area and
# volume of a triangular prism.
import math

def main():
    # asking for dimensions
    a = float(input("Enter the length of triangle base side (side A)(cm): "))
    b = float(input("Enter the length of triangle side B(cm): "))
    c = float(input("Enter the length of triangle side C(cm): "))
    length = float(input("Enter the length of the prism(cm): "))

    # calculations
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    surface_area = area * 2 + length * a + length * b + length * c
    volume = length * area

    # display
    print("Surface area is {:.2f}cm^2".format(surface_area))
    print("Volume is {:.2f}cm^2".format(volume))

if __name__ == "__main__":
    main()
