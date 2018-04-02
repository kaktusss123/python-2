import json
import sys


class Knight:
    MAX_HEALTH = 100
    MAX_defence = 170
    MAX_ATTACK = 150

    def __init__(self, health, defence, attack, exp, id, lord):
        self.health = health
        self.defence = defence
        self.attack = attack
        self.exp = exp
        self.id = id
        self.lord = lord


class Warlock:
    MAX_HEALTH = 70
    MAX_defence = 50
    MAX_ATTACK = 100
    MAX_MANA = 180

    def __init__(self, health, defence, attack, exp, mana, id, lord):
        self.health = health
        self.defence = defence
        self.attack = attack
        self.exp = exp
        self.mana = mana
        self.id = id
        self.lord = lord


class Barbarian:
    MAX_HEALTH = 120
    MAX_defence = 150
    MAX_ATTACK = 180

    def __init__(self, health, defence, attack, exp, id, lord):
        self.health = health
        self.defence = defence
        self.attack = attack
        self.exp = exp
        self.id = id
        self.lord = lord


class Sorceress:
    MAX_HEALTH = 50
    MAX_defence = 42
    MAX_ATTACK = 90
    MAX_MANA = 200

    def __init__(self, health, defence, attack, exp, mana, id, lord):
        self.health = health
        self.defence = defence
        self.attack = attack
        self.exp = exp
        self.mana = mana
        self.id = id
        self.lord = lord


def fight(army, battle_steps):
    for step in battle_steps:
        fin = False
        if step['action'] == 'cast_health_spell':
            for attacker in army:
                if attacker.id == step['id_from']:
                    if (attacker.health <= 0):
                        break
                    attacker.mana -= step['power']
                    attacker.mana = max(0, attacker.mana)
                    attacker.exp += 1
                    for defender in army:
                        if step['id_to'] == defender.id:
                            defender.health += step['power']
                            defender.health = max(defender.health,
                                                  defender.MAX_HEALTH)
                            defender.exp += 1
                            break
                    break
        elif step['action'] == 'attack':
            for attacker in army:
                if attacker.id == step['id_from']:
                    if (attacker.health <= 0):
                        break
                    for defender in army:
                        if step['id_to'] == defender.id and \
                                step['power'] > defender.defence:
                            defender.health -= (step['power'] -
                                                defender.defence)
                            defender.defence -= step['power']
                            defender.defence = max(0, defender.defence)
                            if defender.health > 0:
                                attacker.exp += 1
                                defender.exp += 1
                            else:
                                attacker.exp += 5
                                break
                    break
        elif step['action'] == 'cast_damage_spell':
            for attacker in army:
                if attacker.id == step['id_from']:
                    if (attacker.health <= 0):
                        break
                    attacker.mana -= step['power']
                    attacker.mana = max(0, attacker.mana)
                    for defender in army:
                        if step['id_to'] == defender.id and \
                                step['power'] > defender.defence:
                            defender.health -= (step['power'] -
                                                defender.defence)
                            defender.defence -= step['power']
                            defender.defence = max(0, defender.defence)
                            if defender.health > 0:
                                attacker.exp += 1
                                defender.exp += 1
                            else:
                                attacker.exp += 5
                            break
                    break
    arch_score = 0
    ron_score = 0
    for unit in army:
        if unit.lord == 'Archibald':
            arch_score += unit.exp + 2 * unit.defence + 3 * unit.attack
            if type(unit) is Warlock or type(unit) is Sorceress:
                arch_score += 10 * unit.mana
        else:
            ron_score += unit.exp + 2 * unit.defence + 3 * unit.attack
            if type(unit) is Warlock or type(unit) is Sorceress:
                ron_score += 10 * unit.mana

    if arch_score > ron_score:
        print('Archibald')
    elif arch_score < ron_score:
        print('Ronald')
    else:
        print('unknown')


if __name__ == '__main__':
    js = json.load(sys.stdin)
    army = []
    unit = None
    for unit_id in js['armies']:
        unit_info = js['armies'][unit_id]
        if unit_info['race'] == 'Knight':
            unit = Knight(unit_info['health'], unit_info['defence'],
                          unit_info['attack'], unit_info['experience'],
                          unit_id, unit_info['lord'])
        elif unit_info['race'] == 'Warlock':
            unit = Warlock(unit_info['health'], unit_info['defence'],
                           unit_info['attack'], unit_info['experience'],
                           unit_info['mana'], unit_id, unit_info['lord'])
        elif unit_info['race'] == 'Sorceress':
            unit = Sorceress(unit_info['health'], unit_info['defence'],
                             unit_info['attack'], unit_info['experience'],
                             unit_info['mana'], unit_id, unit_info['lord'])
        elif unit_info['race'] == 'Barbarian':
            unit = Barbarian(unit_info['health'], unit_info['defence'],
                             unit_info['attack'], unit_info['experience'],
                             unit_id, unit_info['lord'])

        army.append(unit)

    fight(army, js['battle_steps'])