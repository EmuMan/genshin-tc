from enum import Enum

from genshintc.modifiers import Modifier, ModifierType, QualifierType
from genshintc.attacks import DamageType, AttackType

class ArtifactSet(Enum):
    INITIATE = 'initiate'
    
    ADVENTURER = 'adventurer'
    LUCKY_DOG = 'lucky_dog'
    TRAVELING_DOCTOR = 'traveling_doctor'
    
    RESOLUTION_OF_SOJOURNER = 'resolution_of_sojourner'
    TINY_MIRACLE = 'tiny_miracle'
    BERSERKER = 'berserker'
    INSTRUCTOR = 'instructor'
    THE_EXILE = 'the_exile'
    DEFENDERS_WILL = 'defenders_will'
    BRAVE_HEART = 'brave_heart'
    MARTIAL_ARTIST = 'martial_artist'
    GAMBLER = 'gambler'
    SCHOLAR = 'scholar'
    
    PRAYERS_FOR_WISDOM = 'prayers_for_wisdom'
    PRAYERS_FOR_DESTINY = 'prayers_for_destiny'
    PRAYERS_FOR_ILLUMINATION = 'prayers_for_illumination'
    PRAYERS_TO_SPRINGTIME = 'prayers_to_springtime'
    
    GLADIATORS_FINALE = 'gladiators_finale'
    WANDERERS_TROUPE = 'wanderers_troupe'
    NOBLESSE_OBLIGE = 'noblesse_oblige'
    BLOODSTAINED_CHIVALRY = 'bloodstained_chivalry'
    MAIDEN_BELOVED = 'maiden_beloved'
    VIRIDESCENT_VENERER = 'viridescent_venerer'
    ARCHAIC_PETRA = 'archaic_petra'
    RETRACING_BOLIDE = 'retracing_bolide'
    THUNDERSOOTHER = 'thundersoother'
    THUNDERING_FURY = 'thundering_fury'
    LAVAWALKER = 'lavawalker'
    CRIMSON_WITCH_OF_FLAMES = 'crimson_witch_of_flames'
    BLIZZARD_STRAYER = 'blizzard_strayer'
    HEART_OF_DEPTH = 'heart_of_depth'
    TENACITY_OF_THE_MILLELITH = 'tenacity_of_the_millelith'
    PALE_FLAME = 'pale_flame'
    SHIMENAWAS_REMINISCENCE = 'shimenawas_reminiscence'
    EMBLEM_OF_SEVERED_FATE = 'emblem_of_severed_fate'
    HUSK_OF_OPULENT_DREAMS = 'husk_of_opulent_dreams'
    OCEAN_HUED_CLAM = 'ocean_hued_clam'
    VERMILLION_HEREAFTER = 'vermillion_hereafter'
    ECHOES_OF_AN_OFFERING = 'echoes_of_an_offering'
    DEEPWOOD_MEMORIES = 'deepwood_memories'
    GILDED_DREAMS = 'gilded_dreams'
    

class ArtifactStatType(Enum):
    
    FLAT_ATTACK = 'flat_atk'
    FLAT_DEFENSE = 'flat_def'
    FLAT_HEALTH = 'flat_hp'
    ATTACK_PERCENT = 'atk_percent'
    DEFENSE_PERCENT = 'def_percent'
    HEALTH_PERCENT = 'hp_percent'
    
    ENERGY_RECHARGE = 'energy_recharge'
    ELEMENTAL_MASTERY = 'elemental_mastery'
    
    CRIT_RATE = 'crit_rate'
    CRIT_DAMAGE = 'crit_dmg'
    
    PHYSICAL_DMG_BONUS = 'physical_dmg_bonus'
    ANEMO_DMG_BONUS = 'anemo_dmg_bonus'
    GEO_DMG_BONUS = 'geo_dmg_bonus'
    ELECTRO_DMG_BONUS = 'electro_dmg_bonus'
    DENDRO_DMG_BONUS = 'dendro_dmg_bonus'
    HYDRO_DMG_BONUS = 'hydro_dmg_bonus'
    PYRO_DMG_BONUS = 'pyro_dmg_bonus'
    CRYO_DMG_BONUS = 'cryo_dmg_bonus'


set_bonuses = {
    ArtifactSet.BLOODSTAINED_CHIVALRY: (
        [
            Modifier(ModifierType.PERCENT_DAMAGE_BONUS, 0.25, {QualifierType.DAMAGE_TYPE: DamageType.PHYSICAL})
        ],
        [
            Modifier(ModifierType.PERCENT_DAMAGE_BONUS, 0.5, {QualifierType.ATTACK_TYPE: AttackType.NORMAL})
        ]
    ),
    ArtifactSet.PALE_FLAME: (
        [
            Modifier(ModifierType.PERCENT_DAMAGE_BONUS, 0.25, {QualifierType.DAMAGE_TYPE: DamageType.PHYSICAL})
        ],
        [
            Modifier(ModifierType.ATTACK_PERCENT_BONUS, 0.18, {QualifierType.ATTACK_TYPE: AttackType.NORMAL}),
            Modifier(ModifierType.PERCENT_DAMAGE_BONUS, 0.25, {QualifierType.DAMAGE_TYPE: DamageType.PHYSICAL})
        ]
    )
}

class ArtifactStat:
    
    _type: ArtifactStatType
    value: float
    
    def __init__(self, _type: ArtifactStatType, value: float):
        self._type = _type
        self.value = value
    
    def to_modifier(self) -> Modifier:
        match (self._type):
            case ArtifactStatType.FLAT_ATTACK: return Modifier(ModifierType.FLAT_ATTACK_BONUS, self.value)
            case ArtifactStatType.FLAT_DEFENSE: return Modifier(ModifierType.DEFENSE_PERCENT_BONUS, self.value)
            case ArtifactStatType.FLAT_HEALTH: return Modifier(ModifierType.HEALTH_PERCENT_BONUS, self.value)
            case ArtifactStatType.ATTACK_PERCENT: return Modifier(ModifierType.ATTACK_PERCENT_BONUS, self.value)
            case ArtifactStatType.DEFENSE_PERCENT: return Modifier(ModifierType.DEFENSE_PERCENT_BONUS, self.value)
            case ArtifactStatType.HEALTH_PERCENT: return Modifier(ModifierType.HEALTH_PERCENT_BONUS, self.value)
            
            case ArtifactStatType.ELEMENTAL_MASTERY: return Modifier(ModifierType.ELEMENTAL_MASTERY, self.value)
            case ArtifactStatType.ENERGY_RECHARGE: return Modifier(ModifierType.ENERGY_RECHARGE, self.value)
            
            case ArtifactStatType.CRIT_RATE: return Modifier(ModifierType.CRIT_RATE, self.value)
            case ArtifactStatType.CRIT_DAMAGE: return Modifier(ModifierType.CRIT_DAMAGE, self.value)
            
            case ArtifactStatType.PHYSICAL_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.PHYSICAL})
            case ArtifactStatType.ANEMO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.ANEMO})
            case ArtifactStatType.GEO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.GEO})
            case ArtifactStatType.ELECTRO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.ELECTRO})
            case ArtifactStatType.DENDRO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.DENDRO})
            case ArtifactStatType.HYDRO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.HYDRO})
            case ArtifactStatType.PYRO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.PYRO})
            case ArtifactStatType.CRYO_DMG_BONUS:
                return Modifier(ModifierType.PERCENT_DAMAGE_BONUS, self.value, {QualifierType.DAMAGE_TYPE: DamageType.CRYO})
                

class Artifact:
    
    _set: ArtifactSet
    main_stat: ArtifactStat
    substats: list[ArtifactStat]
    
    def __init__(self, _set: ArtifactSet, main_stat: ArtifactStat, substats: list[ArtifactStat]):
        self._set = _set
        self.main_stat = main_stat
        self.substats = substats
    
    def to_modifiers(self) -> list[Modifier]:
        return [self.main_stat.to_modifier()] + [ss.to_modifier() for ss in self.substats]

class ArtifactCollection:
    
    artifacts: list[Artifact]
    
    def __init__(self, artifacts: list[Artifact] = None):
        self.artifacts = [] if artifacts is None else artifacts
    
    def get_stat_total(self, stat: ArtifactStatType) -> float:
        total = 0.0
        for artifact in self.artifacts:
            if artifact is None: continue
            if artifact.main_stat._type == stat:
                total += artifact.main_stat.value
            for substat in artifact.substats:
                if substat._type == stat:
                    total += substat.value
        return total
    
    def get_set_bonus_modifiers(self) -> list[Modifier]:
        modifiers: list[Modifier] = []
        all_sets: list[ArtifactSet] = [artifact._set for artifact in self.artifacts]
        for set_name, bonuses in set_bonuses.items():
            count = all_sets.count(set_name)
            if count >= 2:
                modifiers.extend(bonuses[0])
            if count >= 4:
                modifiers.extend(bonuses[1])
        return modifiers
    
    def get_artifact_modifiers(self) -> list[Modifier]:
        return sum((a.to_modifiers() for a in self.artifacts), [])

    def get_all_modifiers(self) -> list[Modifier]:
        return self.get_artifact_modifiers() + self.get_set_bonus_modifiers()
