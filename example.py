from genshintc.damage import DamageInstance, get_def_mult
from genshintc.characters import Character, Amber
from genshintc.weapons import Weapon, SkywardHarp
from genshintc.artifacts import *

def main():
    
    character = Amber(
        level=90,
        ascension=6,
        weapon=SkywardHarp(level=90, refinement=1),
        artifacts=ArtifactCollection([
            Artifact(ArtifactSet.PALE_FLAME, ArtifactStat(ArtifactStatType.FLAT_HEALTH, 4780.0), [
                ArtifactStat(ArtifactStatType.CRIT_RATE, 0.035),
                ArtifactStat(ArtifactStatType.CRIT_DAMAGE, 0.218),
                ArtifactStat(ArtifactStatType.FLAT_ATTACK, 18.0),
                ArtifactStat(ArtifactStatType.FLAT_DEFENSE, 63.0)
            ]),
            Artifact(ArtifactSet.PALE_FLAME, ArtifactStat(ArtifactStatType.FLAT_ATTACK, 311.0), [
                ArtifactStat(ArtifactStatType.CRIT_RATE, 0.062),
                ArtifactStat(ArtifactStatType.CRIT_DAMAGE, 0.187),
                ArtifactStat(ArtifactStatType.ELEMENTAL_MASTERY, 23.0),
                ArtifactStat(ArtifactStatType.FLAT_HEALTH, 448.0)
            ]),
            Artifact(ArtifactSet.BLOODSTAINED_CHIVALRY, ArtifactStat(ArtifactStatType.ATTACK_PERCENT, 0.466), [
                ArtifactStat(ArtifactStatType.CRIT_RATE, 0.101),
                ArtifactStat(ArtifactStatType.CRIT_DAMAGE, 0.140),
                ArtifactStat(ArtifactStatType.ELEMENTAL_MASTERY, 19.0),
                ArtifactStat(ArtifactStatType.FLAT_ATTACK, 47.0)
            ]),
            Artifact(ArtifactSet.NOBLESSE_OBLIGE, ArtifactStat(ArtifactStatType.PHYSICAL_DMG_BONUS, 0.583), [
                ArtifactStat(ArtifactStatType.CRIT_RATE, 0.035),
                ArtifactStat(ArtifactStatType.CRIT_DAMAGE, 0.202),
                ArtifactStat(ArtifactStatType.ELEMENTAL_MASTERY, 82.0),
                ArtifactStat(ArtifactStatType.FLAT_ATTACK, 14.0)
            ]),
            Artifact(ArtifactSet.BLOODSTAINED_CHIVALRY, ArtifactStat(ArtifactStatType.CRIT_RATE, 0.311), [
                ArtifactStat(ArtifactStatType.CRIT_DAMAGE, 0.264),
                ArtifactStat(ArtifactStatType.ELEMENTAL_MASTERY, 40.0),
                ArtifactStat(ArtifactStatType.DEFENSE_PERCENT, 0.124),
                ArtifactStat(ArtifactStatType.FLAT_DEFENSE, 19.0)
            ])
        ]),
        talents=(10, 10, 10),
        modifiers=None
    )
    
    damage_instances = character.get_damage('n1')
        
    print(f'\nFirst normal attack damage: {damage_instances[0].get_crit()}')
    
    for n, v in damage_instances[0].__dict__.items():
        print(f'\t{n}: {v}')

if __name__ == '__main__':
    main()
