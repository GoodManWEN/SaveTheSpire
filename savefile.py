import base64
import json

class SaveFile:

    def __init__(self, file_name):
        self.KEY = 'key'
        self.file_name = file_name
        self.content = self.load(self.file_name)

    def load(self, file_name):
        with open(file_name,'rb') as f:
            hal = f.read()

        bed = base64.b64decode(hal).decode("utf-8")

        result = ''
        for index, char in enumerate(bed):
            result += chr(ord(char) ^ ord(self.KEY[index % len(self.KEY)]))
        return json.loads(result)

    def save(self, ):
        byte = ''
        for char_index, char in enumerate(json.dumps(self.content)):
            byte += chr(ord(char) ^ ord(self.KEY[char_index % len(self.KEY)]))
        byte = base64.b64encode(byte.encode("utf-8"))

        with open(self.file_name,'wb') as f:
            f.write(byte)
        return self

    def max_gold(self):
        self.content['gold'] = 19999
        return self

    def all_upgrade(self):
        cards = self.content['cards']
        for card_index in range(len(cards)):
            cards[card_index]['upgrades'] = 1
        return self

    def max_handsize(self):
        self.content['hand_size'] = 9
        return self

    def max_health(self):
        self.content['max_health'] = 999
        self.content['current_health'] = 999
        return self

    def add_relic_from_boss(self, relic_name, red_plus = True):
        if relic_name not in self.content['relics']:
            self.content['relics'].append(relic_name)
            if red_plus:
                self.content['red'] = self.content['red'] + 1
        return self

    def add_relic_from_shop(self, relic_name):
        if relic_name not in self.content['relics']:
            self.content['relics'].append(relic_name)
            if relic_name not in self.content['metric_items_purchased']:
                self.content['metric_items_purchased'].append(relic_name)

    def add_relic_for_prepare(self, relic_name):
        if relic_name not in self.content['relics']:
            if relic_name not in self.content['shop_relics']:
                self.content['shop_relics'].pop(0)
                self.content['shop_relics'].append(relic_name)
            else:
                self.content['shop_relics'].remove(relic_name)
                self.content['shop_relics'].append(relic_name)
            if relic_name not in self.content['metric_items_purchased']:
                self.content['metric_items_purchased'].append(relic_name)

    def relic_mop(self):    # 痛苦印记
        self.add_relic_from_boss('Mark of Pain')
        return self

    def relic_coffeed(self):   # 咖啡机
        self.add_relic_from_boss('Coffee Dripper')
        return self

    def relic_slavers_collar(self):  # 奴隶项圈
        self.add_relic_from_boss('SlaversCollar', False)
        return self

    def relic_fusion_hammer(self):  # 融合之锤
        self.add_relic_from_boss('Fusion Hammer')
        return self

    def relic_mop(self):    # 痛苦印记
        self.add_relic_from_boss('Mark of Pain')
        return self

    def relic_sacred_bark(self):    # 树皮
        self.add_relic_from_boss('SacredBark', False)
        return self 

    def relic_icecream(self):
        self.add_relic_from_shop('Ice Cream')
        return self

    def relic_blue_candle(self):
        self.add_relic_from_shop('Blue Candle')
        return self

    def relic_prayer_wheel(self):
        self.add_relic_from_shop('Prayer Wheel')
        return self

    def relic_frozen_eye(self):
        self.add_relic_from_shop('Frozen Eye')
        return self

    def relic_clockwork_souvenir(self):    # 齿轮工艺品
        self.add_relic_from_shop('ClockworkSouvenir')  
        return self

    def relic_medical_kit(self):    # 医疗箱
        self.add_relic_from_shop('Medical Kit')
        return self

    def relic_prismatic_shard(self):  # 彩虹碎片
        self.add_relic_from_shop('PrismaticShard')
        return self

    def relic_courier(self):  # 送货员
        self.add_relic_from_shop('The Courier')
        return self

    def relic_vajra(self):  # 金刚杵
        self.add_relic_from_shop('Vajra')
        return self

    def relic_tungstenrod(self):   # 钨合金棍
        self.add_relic_from_shop('TungstenRod')
        return self

    def relic_omamori(self):   # 御守
        self.add_relic_from_shop('Omamori')
        return self

    def relic_calipers(self):   # 外卡钳
        self.add_relic_from_shop('Calipers')
        return self

    def relic_blood_vial(self):   # 小血瓶
        self.add_relic_from_shop('Blood Vial')
        return self

    def relic_question_card(self):   # 问号牌
        self.add_relic_from_shop('Question Card')
        return self

    def relic_singing_bowl(self):   # 颂钵
        self.add_relic_from_shop('Singing Bowl')
        return self
        

    def relic_peace_pipe(self):    # 宁静烟斗
        self.add_relic_from_shop('Peace Pipe')
        return self

    def relic_toxic_egg(self):    # 毒素蛋
        self.add_relic_from_shop('Toxic Egg 2')
        return self

    def relic_lantern(self):    # 提灯
        self.add_relic_from_shop('Lantern')
        return self

    def relic_smooth_stone(self):    # 意外光滑的石头
        self.add_relic_from_shop('Oddly Smooth Stone')
        return self

    def relic_mummified_hand(self):    # 干瘪的手
        self.add_relic_from_shop('Mummified Hand')
        return self

    def relic_molten_egg(self):    # 融化的蛋
        self.add_relic_from_shop('Molten Egg 2')
        return self

    def relic_strange_spoon(self):    # 奇怪的勺子
        self.add_relic_from_shop('Strange Spoon')
        return self

    def relic_unceasing_top(self):    # 不休陀螺
        self.add_relic_from_shop('Unceasing Top')
        return self

    def relic_membership_card(self):    # 打折卡
        self.add_relic_from_shop('Membership Card')
        return self
    
    def relic_chemical(self):    # x+2
        self.add_relic_from_shop('Chemical X')
        return self    
    
    def relic_the_specimen(self):  # 植物标本
        self.add_relic_from_shop('The Specimen')
        return self
    
    def relic_frozen_egg(self):
        self.add_relic_from_shop('Frozen Egg 2')
        return self

    def relic_bottled_tornado(self):
        self.add_relic_for_prepare('Bottled Tornado')
        return self

    def relic_dollys_mirror(self):
        self.add_relic_for_prepare('DollysMirror')
        return self

    def relic_posion_slot(self):
        if 'Potion Belt' not in self.content['relics']:
            self.content['relics'].append('Potion Belt')
            self.content['potion_slots'] = 5
            if len(self.content['potions']) != 5:
                for _ in range(5 - len(self.content['potions'])):
                    self.content['potions'].append('Potion Slot')
            if 'Potion Belt' not in self.content['metric_items_purchased']:
                self.content['metric_items_purchased'].append('Potion Belt')
        return self

    def potion_duplication(self):
        self.content['potions'] = [ 'DuplicationPotion' for _ in range(self.content['potion_slots']) ]
        return self

    def potion_empty(self):
        self.content['potions'] = [ 'Potion Slot' for _ in range(self.content['potion_slots']) ]
        return self

    def __str__(self):
        return json.dumps(self.content, indent=2, separators=(', ', ': '))
