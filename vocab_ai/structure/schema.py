from typing_extensions import TypedDict

# Graph state
class State(TypedDict):
    link: str  # link of the video
    transcript: str  # transcript of the video
    vocabs: str # vocabs

