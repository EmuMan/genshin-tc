

class DamageInstance:
    
    base_dmg: float
    special_mult: float
    flat_dmg_bonus: float
    percent_dmg_bonus: float
    target_dmg_reduction: float
    target_def_mult: float
    target_res_mult: float
    amplifying_mult: float
    crit_damage: float
    crit_rate: float
    
    @property
    def crit_mult(self):
        return 1 + self.crit_rate * self.crit_damage
    
    def __init__(self):
        self.base_dmg = 100
        self.special_mult = 1.0
        self.flat_dmg_bonus = 0.0
        self.percent_dmg_bonus = 1.0
        self.target_dmg_reduction = 0.0
        self.target_def_mult = 0.5
        self.target_res_mult = 1.0
        self.amplifying_mult = 1.0
        self.crit_rate = 0.05
        self.crit_damage = 0.50
        
    def get_non_crit(self) -> float:
        return ((self.base_dmg * self.special_mult) + self.flat_dmg_bonus) \
            * (1 + self.percent_dmg_bonus - self.target_dmg_reduction) \
            * self.target_def_mult * self.target_res_mult * self.amplifying_mult
    
    def get(self) -> float:
        return self.get_non_crit() * self.crit_mult
            
    def get_crit(self) -> float:
        return self.get_non_crit() * (1 + self.crit_damage)
        
    def with_base_dmg(self, base_dmg: float) -> 'DamageInstance':
        self.base_dmg = base_dmg
        return self
        
    def with_special_multiplier(self, special_mult: float) -> 'DamageInstance':
        self.special_mult = special_mult
        return self
    
    def with_flat_dmg_bonus(self, flat_dmg_bonus: float) -> 'DamageInstance':
        self.flat_dmg_bonus = flat_dmg_bonus
        return self
        
    def with_percent_dmg_bonus(self, percent_dmg_bonus: float) -> 'DamageInstance':
        self.percent_dmg_bonus = percent_dmg_bonus
        return self
    
    def with_target_dmg_reduction(self, target_dmg_reduction: float) -> 'DamageInstance':
        self.target_dmg_reduction = target_dmg_reduction
        return self
    
    def with_target_def_mult(self, target_def_mult: float) -> 'DamageInstance':
        self.target_def_mult = target_def_mult
        return self
    
    def with_target_res_mult(self, target_res_mult: float) -> 'DamageInstance':
        self.target_res_mult = target_res_mult
        return self
    
    def with_amplifying_mult(self, amplifying_mult: float) -> 'DamageInstance':
        self.amplifying_mult = amplifying_mult
        return self
    
    def with_crit(self, cr: float, cd: float) -> 'DamageInstance':
        self.crit_rate = cr
        self.crit_damage = cd
        return self
    
    def with_crit_val(self, cv: float) -> 'DamageInstance':
        self.crit_rate = cv / 4
        self.crit_damage = cv / 2
        return self
    
def get_def_mult(character_lvl: float, enemy_lvl: float) -> float:
    return (character_lvl + 100) / (enemy_lvl + character_lvl + 200)
