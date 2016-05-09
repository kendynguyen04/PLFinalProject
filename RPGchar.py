# This block of code establish a class that is used to define a 
# character for a role playing game.

# Functional Programming Example

import random

class character(object):
    def f(self):
        stats = {
            'name': 'Unknown',
            '$name': lambda x: stats.update({'name': x}),
            'age': 'Unknown',
            '$age': lambda x: stats.update({'age': x}),
            'race': 'Unknown',
            'talent': 'Being obscure.',
            '$talent': lambda x: stats.update({'talent': x}),
            'quote' : '...',
            '$quote': lambda x: stats.update({'quote': x})
        }
        def scan (self, s):
           if s in stats:
                return stats[s]
           else:
                return None
        return scan
    run = f(1)

class human(character):
    def f(self):
        stats = {
            'race': 'Human',
            'talent': 'Excels at being unimpressive.',
            '$talent': lambda x: stats.update({'talent': x}),
            'quote' : 'Well met, adventurer!',
        }
        def scan (self, s):
            if s in stats:
                return stats[s]
            else:
                return super(human, self).run(s)
        return scan
    run = f(1)

class dwarf(character):
    def f(self):
        stats = {
            'race': 'Dwarf',
            'talent': 'Very strong despite stature. Adept at smithing.',
            '$talent': lambda x: stats.update({'talent': x}),
            'quote' : 'Aye, \'tis a fine day to tend the forge!',
        }
        def scan (self, s):
            if s in stats:
                return stats[s]
            else:
                return super(dwarf, self).run(s)
        return scan
    run = f(1)

class elf(character):
    def f(self):
        stats = {
            'race': 'Elf',
            'talent': 'Extremely agile and fleet of foot. A natural at complex acrobatics.',
            '$talent': lambda x: stats.update({'talent': x}),
            'quote' : 'Harmonious peace be with you on this day.',
        }
        def scan (self, s):
            if s in stats:
                return stats[s]
            else:
                return super(elf, self).run(s)
        return scan
    run = f(1)

def profile(char):
    print
    print 'Okay. Here\'s the full character profile.'
    print 'Name: ' + char.run('name')
    print 'Age: ' + char.run('age')
    print 'Race: ' + char.run('race')
    print 'Talent: ' + char.run('talent')
    print 'Quote: ' + char.run('quote')

def makeP1():
    P1 = character()
    P1.run('$name')('John')
    profile(P1)
    return P1

def makeP2():
    P2 = human()
    P2.run('$name')('Steve')
    P2.run('$age')('20')
    profile(P2)
    return P2

def formGuild(num):
    def randChar():
        genKey = random.randint(1, 3)
        if genKey == 1: return 'Human'
        elif genKey == 2: return 'Dwarf'
        else: return 'Elf'
    memList = []
    for i in range(num): memList.append(randChar())
    return memList

def combine(roster):
    def merge(members):
        return roster + members
    return merge

# Closure Example

def closure():
    guild1 = formGuild(5)
    print 'Guild 1\'s Roster: ' + str(guild1)
    guild2 = formGuild(4)
    print 'Guild 2\'s Roster: ' + str(guild2)
    guild3 = formGuild(3)
    print 'Guild 3\'s Roster: ' + str(guild3)

    addguild1 = combine(guild1)
    print addguild1(guild2)
    print addguild1(guild3)







