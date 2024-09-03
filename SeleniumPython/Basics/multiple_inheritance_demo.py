class MoveCharacter:
    def mov_fwd(self):
        print('Move forward 1 step')

    def move_bwd(self):
        print('Move backward 1 step')

class JumpCharacter:
    def jump_1_level(self):
        print('Jump character 1 level')

    def jump_2_level(self):
        print('Jump character 2 level')

class Pokeman(MoveCharacter, JumpCharacter):
    def mov_fwd(self):
        print('Pokeman moving')

pokeman = Pokeman()
pokeman.mov_fwd()
pokeman.move_bwd()
pokeman.jump_1_level()
pokeman.jump_2_level()

class Micky(MoveCharacter, JumpCharacter):
    def jump_1_level(self):
        print('Micky is jumping')

micky = Micky()
micky.mov_fwd()
micky.move_bwd()
micky.jump_1_level()
micky.jump_2_level()
print(Pokeman.mro())
print(Micky.mro())
