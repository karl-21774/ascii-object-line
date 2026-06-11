import random
import argparse

def generate_frame(length, seed, width, frame):
    # rng = random.Random((seed + frame))
    rng = random.Random(f"{seed}:{frame}")

    max_width = length * width
    inner_width = max(1, int(max_width * 0.5))

    line = [" "] * inner_width

    num_objects = rng.randint(0, 2)
    objects = ["S", "D"]

    used = set()

    for _ in range(num_objects):
        obj = rng.choice(objects)

        pos = rng.randrange(inner_width)
        while pos in used:
            pos = rng.randrange(inner_width)

        used.add(pos)
        line[pos] = obj

    return "|" + "".join(line) + "|"

def generate_sequence(length, seed, width, start_frame, count):
    return [
        generate_frame(length, seed, width, frame)
        for frame in range(start_frame, start_frame + count)
    ]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--length", type=int, default=20)
    parser.add_argument("--width", type=int, default=2)
    parser.add_argument("--start-frame", type=int, default=0)
    parser.add_argument("--count", type=int, default=4)
    args = parser.parse_args()

    frames = generate_sequence(
        args.length,
        args.seed,
        args.width,
        args.start_frame,
        args.count
    )

    for i, f in enumerate(frames):
        print(f"{args.start_frame + i}: {f}")

if __name__ == "__main__":
    main()