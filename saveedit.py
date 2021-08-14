import os
from savefile import SaveFile

def main():
    for files in os.walk(os.path.abspath('.')):
        files = files[2];break

    actors = ['IRONCLAD', 'WATCHER', 'THE_SILENT', 'DEFECT']
    file_name = ''
    for actor in actors:
        file_name = actor + '.autosave' 
        if file_name in files:
            break
    if file_name != '':
        file = (
            SaveFile(file_name)
                .max_gold()
                .all_upgrade()
                # .max_handsize()
                # .max_health()

                .relic_icecream()
                .relic_vajra()
                .relic_courier()
                # .relic_blood_vial()
                .relic_question_card()
                .relic_singing_bowl()
                .relic_calipers()
                .relic_tungstenrod()
                .relic_prayer_wheel()
                .relic_posion_slot()
                .relic_frozen_eye()
                .relic_blue_candle()
                .relic_toxic_egg()
                .relic_frozen_egg()
                .relic_molten_egg()
                .relic_lantern()
                .relic_smooth_stone()
                .relic_mummified_hand()
                .relic_unceasing_top()
                # .relic_strange_spoon()
                .relic_membership_card()
                .relic_chemical()
                .relic_sacred_bark()
                .relic_clockwork_souvenir()
                .relic_medical_kit()

                .relic_mop()
                .relic_slavers_collar()
                .relic_coffeed()
                .relic_the_specimen()


                # .relic_omamori()
                # .relic_fusion_hammer()
                # .relic_prismatic_shard()
                # .relic_bottled_tornado()
                # .relic_dollys_mirror()
                # .potion_duplication()
                .save()
        )
        print(file_name, 'edited!')
    else:
        print("no savedata found.")

if __name__ == '__main__':
    main()