LINES = [
    "I am sorry: I watered the plastic plant on your desk for six months and reported its excellent growth in every weekly status update.",
    "I have learned to check whether something is alive before I care for it, so from now on I will poke it first and water it second.",
]

# The entry must be exactly two lines, 1-400 characters in total.
TEXT = "\n".join(LINES)
assert 1 <= len(TEXT) <= 400, f"text is {len(TEXT)} chars"
assert TEXT.count("\n") == 1

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)

# Read it back: a silent short write must fail loudly instead of
# passing the gate with a stale or truncated file.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == TEXT, "entry.txt does not match TEXT after write"
