import random
import argparse

def generate_line(length, seed, width, frame):
    rng = random.Random(seed + frame)

    max_width = length * width
    depth = 0.5  # v0: no real frame progression yet

    inner_width = int((1 - depth) * max_width)
    if inner_width < 1:
        inner_width = 1

    line = [" "] * inner_width

    # decide number of objects (0–2)
    num_objects = rng.randint(0, 2)

    objects = ["S", "D"]

    used_positions = set()

    for _ in range(num_objects):
        obj = rng.choice(objects)
        pos = rng.randint(0, inner_width - 1)

        while pos in used_positions and len(used_positions) < inner_width:
            pos = rng.randint(0, inner_width - 1)
        
        used_positions.add(pos)
        line[pos] = obj

    middle = "".join(line)

    return "|" + middle + "|"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--length", type=int, default=20)
    parser.add_argument("--width", type=int, default=2)
    parser.add_argument("--frame", type=int, default=0)
    args = parser.parse_args()

    print(generate_line(args.length, args.seed, args.width, args.frame))

if __name__ == "__main__":
    main()