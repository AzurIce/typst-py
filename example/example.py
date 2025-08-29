import typst
import time

start = time.perf_counter()
compiler = typst.CompilerBuilder()
end = time.perf_counter()
print(f"font init cost: {end - start} seconds")

# world = compiler.build_path("hello.typ")
# res = world.compile(format="png", ppi=144.0)
# with open("hello.png", "wb") as f:
#     f.write(res)

sources = [
    b"""$ A = pi r^2 $""",
    b"""$ "area" = pi dot "radius"^2 $""",
    b"""$ cal(A) := { x in RR | x "is natural" } $""",
    b"""#let x = 5
$ #x < 17 $""",
]

for idx, source in enumerate(sources):
    start = time.perf_counter()
    world = compiler.build_bytes(source)
    res = world.compile(format="pdf")
    with open(f"math-{idx}.pdf", "wb") as f:
        f.write(res)
    end = time.perf_counter()
    print(f"{idx} cost {end - start} seconds")
