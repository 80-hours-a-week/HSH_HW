import GameVariableData, MessageGenerator

class MonsterConquest(GameVariableData):
  def __init__(self):
    super().__init__()
    self.msg_gen = MessageGenerator(self)

  def fightprocess(self: int):
    for msg in self.msg_gen.initial_messages():
        print(msg)

    while self.monster_hp > 0:
        for msg in self.msg_gen.turn_start_messages():
            print(msg)

        choice = input(next(self.msg_gen.input_prompt_message()))

        try:
            skill_name, damage = self.skills[choice]
        except KeyError:
            print("잘못된 입력입니다.")
            exit()

        self.monster_hp -= damage
        if self.monster_hp < 0:
          self.monster_hp = 0

        for msg in self.msg_gen.damage_report_message(damage):
            print(msg)

        if self.monster_hp > 0:
            for msg in self.msg_gen.counter_attack_message():
                print(msg)
        else:
            for msg in self.msg_gen.victory_message():
                print(msg)
            break

game_instance = MonsterConquest()
game_instance.fightprocess()