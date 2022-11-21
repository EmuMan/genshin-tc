from enum import Enum
from typing import Any

class ModifierType(Enum):
    FLAT_ATTACK_BONUS = 'flat_attack_bonus'
    FLAT_HEALTH_BONUS = 'flat_health_bonus'
    FLAT_DEFENSE_BONUS = 'flat_defense_bonus'
    ATTACK_PERCENT_BONUS = 'attack_percent_bonus'
    HEALTH_PERCENT_BONUS = 'health_percent_bonus'
    DEFENSE_PERCENT_BONUS = 'defense_percent_bonus'
    
    ELEMENTAL_MASTERY = 'elemental_mastery'
    ENERGY_RECHARGE = 'energy_recharge'
    
    SPECIAL_MULTIPLIER = 'special_multiplier'
    FLAT_DAMAGE_BONUS = 'flat_damage_bonus'
    PERCENT_DAMAGE_BONUS = 'percent_damage_bonus'
    TARGET_DAMAGE_REDUCTION = 'target_damage_reduction'
    AMPLIFYING_MULTIPLIER = 'amplifying_multiplier'
    
    CRIT_RATE = 'crit_rate'
    CRIT_DAMAGE = 'crit_damage'

class QualifierType(Enum):
    ATTACK_TYPE = 'attack_type'
    DAMAGE_TYPE = 'element'

class Modifier:
    
    _type: ModifierType
    value: float
    qualifiers: dict[QualifierType, Any]
    
    def __init__(self, _type: ModifierType, value: float, qualifiers: dict[QualifierType, Any] = None):
        self._type = _type
        self.value = value
        self.qualifiers = qualifiers if qualifiers is not None else {}
