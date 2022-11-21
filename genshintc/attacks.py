from enum import Enum, auto

class AttackScaling(Enum):
    HP = auto()
    ATK = auto()
    DEF = auto()
    
class DamageType(Enum):
    TRUE = auto()
    PHYSICAL = auto()
    ANEMO = auto()
    GEO = auto()
    ELECTRO = auto()
    DENDRO = auto()
    HYDRO = auto()
    PYRO = auto()
    CRYO = auto()
    
class AttackType(Enum):
    NORMAL = 'normal'
    CHARGED = 'charged'
    PLUNGE = 'plunge'
    ELEMENTAL_SKILL = 'elemental_skill'
    ELEMENTAL_BURST = 'elemental_burst'

class Attack:
    
    damage_type: DamageType
    scales_on: AttackScaling
    hit_count: int
    attack_type: AttackType
    scale_vals: tuple[float, ...]
    
    @property
    def talent_index(self):
        return 0 if self.attack_type in (AttackType.NORMAL, AttackType.CHARGED, AttackType.PLUNGE) else \
            1 if self.attack_type == AttackType.ELEMENTAL_SKILL else 2
    
    def __init__(self, damage_type: DamageType, scales_on: AttackScaling, attack_type: AttackType,
                 hit_count: int, scale_vals: tuple[float, ...]):
        self.damage_type = damage_type
        self.scales_on = scales_on
        self.hit_count = hit_count
        self.attack_type = attack_type
        self.scale_vals = scale_vals
