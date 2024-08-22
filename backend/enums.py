from enum import Enum

class FormatEnum(Enum):
    letter = "Letter"
    legal = "Legal"
    tabloid = "Tabloid"
    ledger = "Ledger"
    a0 = "A0"
    a1 = "A1"
    a2 = "A2"
    a3 = "A3"
    a4 = "A4"
    a5 = "A5"
    a6 = "A6"

class WaitUntilEnum(Enum):
    domcontentloaded = "domcontentloaded"
    load = "load"
    networkidle = "networkidle"
    commit = "commit"