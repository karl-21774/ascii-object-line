import random
import argparse

VIEW_DEPTH = 10

def generate_world(length, seed, width):
    rng = random.Random(seed)

    max_width = length * width
    inner_width = max(10, int(max_width * 0.5))

    objects = ["S", "D"]

    world_objects = {}

    # pregenerated persistent objects
    # for obj_id in range(rng.randint(2, 5)):
    for obj_id in range(rng.randint(10, 25)):
        obj = rng.choice(objects)
        pos_x = rng.randrange(inner_width)
        pos_z = rng.randrange(0, 100)  # depth in corridor
        # pos_z = rng.randrange(0, 50)

        world_objects[obj_id] = {
            "type": obj,
            "x": pos_x,
            "z": pos_z
        }
    
    return {
        "width": inner_width,
        "objects": world_objects
    }

def render_frame(world, frame):
    line = [" "] * world["width"]

    camera_z = frame

    for obj in world["objects"].values():
        distance = obj["z"] - camera_z

        if distance < 0:
            continue  # already passed

        if distance > 15:
            continue  # too far to perceive

        x = obj["x"]

        # clamp x safely
        if 0 <= x < len(line):
            line[x] = symbol_for(obj["type"], distance)

    return "|" + "".join(line) + "|"


def symbol_for(obj_type, distance):
    if distance <= 2:
        return obj_type.upper()   # near: S, D
    elif distance <= 5:
        return obj_type.lower()   # mid: s, d
    elif distance <= 10:
        return "."
    else:
        return " "

def generate_sequence(length, seed, width, start_frame, count):
    world = generate_world(length, seed, width)

    return [
        render_frame(world, frame)
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