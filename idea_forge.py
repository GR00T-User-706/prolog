import random

adjectives = [
    "quantum", "synthetic", "chaotic", "neural", "stellar", "cosmic",
    "lunar", "digital", "recursive", "parallel", "dreaming", "fractured"
]

nouns = [
    "engine", "forge", "matrix", "core", "stream", "grid", "construct",
    "loop", "realm", "synth", "fabric", "stack", "kernel", "portal"
]

verbs = [
    "evolve", "simulate", "render", "compile", "link", "generate", "explore",
    "craft", "transform", "model", "train", "manifest"
]

def random_idea():
    adj = random.choice(adjectives).capitalize()
    noun = random.choice(nouns).capitalize()
    verb = random.choice(verbs)
    formats = [
        f"{adj}{noun}",
        f"Project_{adj}_{noun}",
        f"{verb}_{noun.lower()}",
        f"{adj}_{verb}_{noun}",
        f"{noun}{verb.capitalize()}",
    ]
    return random.choice(formats)
