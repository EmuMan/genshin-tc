from genshintc.artifacts import Artifact, ArtifactCollection, ArtifactStatType
from genshintc.modifiers import Modifier, ModifierType, QualifierType
from genshintc.weapons import Weapon
from genshintc.attacks import AttackScaling, AttackType, DamageType, Attack
from genshintc.damage import DamageInstance, get_def_mult

class Character:
    
    base_attack: float
    base_health: float
    base_defense: float
    level: int
    ascension: int
    weapon: Weapon
    artifacts: ArtifactCollection
    talents: tuple[int, int, int]
    attacks: dict[str, list[Attack]]
    modifiers: list[Modifier]
    
    @property
    def health(self):
        return (self.base_health) * \
               (1 + self.get_modifier_total(ModifierType.HEALTH_PERCENT_BONUS)) + \
               self.get_modifier_total(ModifierType.FLAT_HEALTH_BONUS)

    @property
    def defense(self):
        return (self.base_defense) * \
               (1 + self.get_modifier_total(ModifierType.DEFENSE_PERCENT_BONUS)) + \
               self.get_modifier_total(ModifierType.FLAT_DEFENSE_BONUS)
    
    @property
    def attack(self):
        return (self.base_attack + self.weapon.base_atk) * \
               (1 + self.get_modifier_total(ModifierType.ATTACK_PERCENT_BONUS)) + \
               self.get_modifier_total(ModifierType.FLAT_ATTACK_BONUS)
               
    @property
    def crit_rate(self):
        return self.get_crit_rate()
    
    @property
    def crit_damage(self):
        return self.get_crit_damage()
    
    def __init__(self, base_attack: float, base_health: float, base_defense: float, level: int, 
                 ascension: int, weapon: Weapon, artifacts: ArtifactCollection, talents: tuple[int, int, int],
                 attacks: dict[str, list[Attack]], modifiers: list[Modifier] = None):
        self.base_attack = base_attack
        self.base_health = base_health
        self.base_defense = base_defense
        self.level = level
        self.ascension = ascension
        self.weapon = weapon
        self.artifacts = artifacts
        self.talents = talents
        self.attacks = attacks
        self.modifiers = modifiers if modifiers is not None else []

    def get_modifier_total(self, modifier_type: ModifierType, attack_type: AttackType = None,
                           damage_type: DamageType = None) -> float:
        total = 0
        all_modifiers: list[Modifier] = self.modifiers.copy()
        all_modifiers.extend(self.artifacts.get_all_modifiers())
        all_modifiers.extend(self.weapon.modifiers)
        all_modifiers.append(self.weapon.substat)
        for modifier in all_modifiers:
            if modifier is not None and modifier._type == modifier_type:
                meets_all_qualifiers = True
                if modifier.qualifiers is not None:
                    for qualifier, value in modifier.qualifiers.items():
                        if (qualifier == QualifierType.ATTACK_TYPE and attack_type != value) or \
                           (qualifier == QualifierType.DAMAGE_TYPE and damage_type != value):
                            meets_all_qualifiers = False
                            break
                if meets_all_qualifiers:
                    total += modifier.value
        return total
    
    def get_damage(self, attack: str) -> list[DamageInstance]:
        
        instances: list[DamageInstance] = []
        
        atk_list = self.attacks[attack]
        
        for atk in atk_list:
            instance = DamageInstance()
            dmg_mult = atk.hit_count * atk.scale_vals[self.talents[atk.talent_index] - 1]
            instance.base_dmg = (self.attack if atk.scales_on == AttackScaling.ATK else
                                 self.health if atk.scales_on == AttackScaling.HP else
                                 self.defense) * dmg_mult
            instance.special_mult = 1.0 + self.get_modifier_total(ModifierType.SPECIAL_MULTIPLIER, attack_type=atk.attack_type, damage_type=atk.damage_type) # TODO: Make percent-based, also figure out wtf it is
            instance.flat_dmg_bonus = self.get_modifier_total(ModifierType.FLAT_DAMAGE_BONUS, attack_type=atk.attack_type, damage_type=atk.damage_type)
            instance.percent_dmg_bonus = self.get_modifier_total(ModifierType.PERCENT_DAMAGE_BONUS, attack_type=atk.attack_type, damage_type=atk.damage_type)
            instance.target_dmg_reduction = 0.0 # TODO: Implement dynamic value
            instance.target_def_mult = 0.5 # TODO: Implement dynamic value
            instance.target_res_mult = 0.9 # TODO: Implement dynamic value
            instance.amplifying_mult = 1.0 + self.get_modifier_total(ModifierType.AMPLIFYING_MULTIPLIER, attack_type=atk.attack_type, damage_type=atk.damage_type)
            instance.crit_rate = self.get_crit_rate(atk.attack_type, atk.damage_type)
            instance.crit_damage = self.get_crit_damage(atk.attack_type, atk.damage_type)
            instances.append(instance)
        
        return instances
        
    def get_crit_rate(self, attack_type: AttackType = None, damage_type: DamageType = None) -> float:
        return 0.05 + self.get_modifier_total(ModifierType.CRIT_RATE, attack_type=attack_type, damage_type=damage_type)

    def get_crit_damage(self, attack_type: AttackType = None, damage_type: DamageType = None) -> float:
        return 0.50 + self.get_modifier_total(ModifierType.CRIT_DAMAGE, attack_type=attack_type, damage_type=damage_type)
            

class Amber(Character):
    
    def __init__(self, level: int, ascension: int, weapon: Weapon, artifacts: ArtifactCollection,
                 talents: tuple[int, int, int], modifiers: list[Modifier] = None):
        new_modifiers = modifiers if modifiers is not None else []
        new_modifiers.append(Modifier(ModifierType.ATTACK_PERCENT_BONUS, 0.24))
        super().__init__(
            base_attack = 223.0,
            base_health = 9461.0,
            base_defense = 601.0,
            level = level,
            ascension = ascension,
            weapon = weapon,
            artifacts = artifacts,
            talents = talents,
            attacks = {
                'n1': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.NORMAL,          1,  (0.3612, 0.3906, 0.42, 0.462, 0.4914, 0.525, 0.5712, 0.6174, 0.6636, 0.714, 0.7644))],
                'n2': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.NORMAL,          1,  (0.3612, 0.3906, 0.42, 0.462, 0.4914, 0.525, 0.5712, 0.6174, 0.6636, 0.714, 0.7644))],
                'n3': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.NORMAL,          1,  (0.4644, 0.5022, 0.54, 0.594, 0.6318, 0.675, 0.7344, 0.7938, 0.8532, 0.918, 0.9828))],
                'n4': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.NORMAL,          1,  (0.473, 0.5115, 0.55, 0.605, 0.6435, 0.6875, 0.748, 0.8085, 0.869, 0.935, 1.001))],
                'n5': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.NORMAL,          1,  (0.5934, 0.6417, 0.69, 0.759, 0.8073, 0.8625, 0.9384, 1.0143, 1.0902, 1.173, 1.2558))],
                'c':  [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.CHARGED,         1,  (0.4386, 0.4743, 0.51, 0.561, 0.5967, 0.6375, 0.6936, 0.7497, 0.8058, 0.867, 0.9282))],
                'cf': [Attack(DamageType.PYRO,     AttackScaling.ATK, AttackType.CHARGED,         1,  (1.24, 1.333, 1.426, 1.55, 1.643, 1.736, 1.86, 1.984, 2.108, 2.232, 2.356))],
                'p':  [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.PLUNGE,          1,  (0.5683, 0.6145, 0.6608, 0.7269, 0.7731, 0.826, 0.8987, 0.9714, 1.0441, 1.1234, 1.2027))],
                'pl': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.PLUNGE,          1,  (1.1363, 1.2288, 1.3213, 1.4535, 1.5459, 1.6517, 1.797, 1.9423, 2.0877, 2.2462, 2.4048))],
                'ph': [Attack(DamageType.PHYSICAL, AttackScaling.ATK, AttackType.PLUNGE,          1,  (1.4193, 1.5349, 1.6504, 1.8154, 1.931, 2.063, 2.2445, 2.4261, 2.6076, 2.8057, 3.0037))],
                'e':  [Attack(DamageType.PYRO,     AttackScaling.ATK, AttackType.ELEMENTAL_SKILL, 1,  (1.232, 1.3244, 1.4168, 1.54, 1.6324, 1.7248, 1.848, 1.9712, 2.0944, 2.2176, 2.3408, 2.464, 2.618, 2.77))],
                'q':  [Attack(DamageType.PYRO,     AttackScaling.ATK, AttackType.ELEMENTAL_BURST, 18, (0.2808, 0.3019, 0.3229, 0.351, 0.3721, 0.3931, 0.4212, 0.4493, 0.4774, 0.5054, 0.5335, 0.5616, 0.5967, 0.632))]
            },
            modifiers = new_modifiers
        )
    