class MoveCharacter:
    def mov_fwd(self):
        print('Move forward 1 step')

    def move_bwd(self):
        print('Move backward 1 step')

class JumpCharacter(MoveCharacter):
    def jump_1_level(self):
        print('Jump character 1 level')

    def jump_2_level(self):
        print('Jump character 2 level')

class Pokeman(JumpCharacter):
    def mov_fwd(self):
        print('Pokeman moving')

class Micky(Pokeman):
    def jump_1_level(self):
        print('Micky is jumping')

    def mov_fwd(self):
        print('Micky moving')

micky = Micky()
micky.mov_fwd()
micky.move_bwd()
micky.jump_1_level()
micky.jump_2_level()
print(Micky.mro())