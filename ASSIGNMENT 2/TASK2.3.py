'''TASK 2.3'''
# Explain a Python function (to calculate area of various shapes) line by line.

# Example: calculate area for circle, rectangle, triangle
import math

def area(shape: str, **kwargs) -> float:
    shape = shape.lower()
    if shape == "circle":
        r = kwargs.get("radius")
        if r is None:
            raise ValueError("circle requires radius")
        return math.pi * r * r
    elif shape == "rectangle":
        w = kwargs.get("width")
        h = kwargs.get("height")
        if w is None or h is None:
            raise ValueError("rectangle requires width and height")
        return w * h
    elif shape == "triangle":
        b = kwargs.get("base")
        h = kwargs.get("height")
        if b is None or h is None:
            raise ValueError("triangle requires base and height")
        return 0.5 * b * h
    else:
        raise ValueError(f"unsupported shape: {shape}")
# Changed / added code: user input loop to get shape & dimensions and print area
def prompt_non_negative_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            val = float(s)
            if val < 0:
                print("Please enter a non-negative number.")
                continue
            return val
        except ValueError:
            print("Invalid number. Please try again.")

if __name__ == "__main__":
    print("Calculate area for shapes: circle, rectangle, triangle")
    print("Type 'exit' or press Enter at shape prompt to quit.\n")

    while True:
        shp = input("Enter shape (circle/rectangle/triangle): ").strip()
        if shp == "" or shp.lower() in ("exit", "quit", "q"):
            print("Exiting.")
            break

        shp_l = shp.lower()
        try:
            if shp_l == "circle":
                r = prompt_non_negative_float("Enter radius: ")
                a = area("circle", radius=r)
            elif shp_l == "rectangle":
                w = prompt_non_negative_float("Enter width: ")
                h = prompt_non_negative_float("Enter height: ")
                a = area("rectangle", width=w, height=h)
            elif shp_l == "triangle":
                b = prompt_non_negative_float("Enter base: ")
                h = prompt_non_negative_float("Enter height: ")
                a = area("triangle", base=b, height=h)
            else:
                print(f"Unsupported shape '{shp}'. Supported: circle, rectangle, triangle.\n")
                continue
        except ValueError as e:
            print("Error:", e)
            continue

        print(f"Area of {shp_l} = {a}\n")