from random import choice


def wippyfy(name='This project'):
    """
    Generate a random Work In Progress message similar to one used on the
     the Rust Language website (http://www.rust-lang.org)

    """

    verbs = ['adopting', 'annoying', 'attacking', 'beating', 'boiling',
             'bumping', 'burying', 'buying', 'cleaning', 'crashing', 'dating',
             'drowning', 'dumping', 'eating', 'exploding', 'glueing',
             'ironing', 'kicking', 'licking', 'locking', 'losing', 'meeting',
             'moving', 'poking', 'possessing', 'punching', 'replacing',
             'rinsing', 'shampooing', 'stabbing', 'stalking', 'swallowing',
             'using', 'vacuuming', 'vaporising', 'whipping']

    nouns = ['boss', 'flashlight', 'furniture', 'laundry', 'neighbour',
             'pet cat', 'pet dog', 'pet frog', 'pet hamster', 'pet llama',
             'pet parrot', 'refrigerator', 'shower', 'sink', 'smartphone',
             'underpants', 'users', 'vacuum']

    verb = choice(verbs)
    noun = choice(nouns)
    msg = ("{0} is a work in progress and may do anything it likes up to and"
            " including {1} your {2}").format(name, verb, noun)

    return msg
