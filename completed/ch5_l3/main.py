def take_magic_damage(health, resist, amp, spell_power):
    damage_taken = (spell_power * amp) - resist
    return health - damage_taken
