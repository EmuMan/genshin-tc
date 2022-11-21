from enum import Enum

from genshintc.modifiers import Modifier, ModifierType

class Weapon:
    
    level: int
    refinement: int
    base_atk: float
    substat: Modifier
    _all_refinement_modifiers: list[list[Modifier]]
    
    @property
    def modifiers(self):
        return [m[self.refinement - 1] for m in self._all_refinement_modifiers]
    
    
    def __init__(self, level: int, refinement: int, base_atk: float, substat: Modifier, refinement_modifiers: list[list[Modifier]]):
        self.level = level
        self.refinement = refinement
        self.base_atk = base_atk
        self.substat = substat
        self._all_refinement_modifiers = refinement_modifiers

class SkywardHarp(Weapon):
    
    def __init__(self, level: int, refinement: int):
        super().__init__(
            level = level,
            refinement = refinement,
            base_atk = 674,
            substat = Modifier(ModifierType.CRIT_RATE, 0.221),
            refinement_modifiers = [
                [
                    Modifier(ModifierType.CRIT_DAMAGE, 0.20),
                    Modifier(ModifierType.CRIT_DAMAGE, 0.25),
                    Modifier(ModifierType.CRIT_DAMAGE, 0.30),
                    Modifier(ModifierType.CRIT_DAMAGE, 0.35),
                    Modifier(ModifierType.CRIT_DAMAGE, 0.40)
                ]
            ]
        )
