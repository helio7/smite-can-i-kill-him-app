def calculate(current_god, sk_states, skills_levels,
              sk1_info, sk2_info, sk3_info, sk4_info,
              ba_info, inputs, ba_flat_buff, hydras_multiplier_buff,
              hydras_affected_bas, heartseeker_buff, poly_buff_based_on_power,
              polys_affected_bas, mages_blessing_buff, crusher_flat_buff,
              crusher_buff_based_on_power, skills_num):

        def approximate_number_to_int(number):
            if number - int(number) >= 0.5:
                number = int(number) + 1
                return number
            elif number - int(number) < 0.5:
                number = int(number)
                return number
    
        #global current_god
        god_name = current_god

        #sk1a_state = self.n_diamonds_hud.state_sk1a
        #sk2a_state = self.n_diamonds_hud.state_sk2a
        #sk3a_state = self.n_diamonds_hud.state_sk3a
        #sk4a_state = self.n_diamonds_hud.state_sk4a
        #sk1b_state = self.n_diamonds_hud.state_sk1b
        #sk2b_state = self.n_diamonds_hud.state_sk2b
        #sk3b_state = self.n_diamonds_hud.state_sk3b
        #sk4b_state = self.n_diamonds_hud.state_sk4b
        sk1a_state = sk_states[0]
        sk2a_state = sk_states[1]
        sk3a_state = sk_states[2]
        sk4a_state = sk_states[3]
        sk1b_state = sk_states[4]
        sk2b_state = sk_states[5]
        sk3b_state = sk_states[6]
        sk4b_state = sk_states[7]

        #sk1_l = self.n_skills_hud.skill_1_level_num
        #sk2_l = self.n_skills_hud.skill_2_level_num
        #sk3_l = self.n_skills_hud.skill_3_level_num
        #sk4_l = self.n_skills_hud.skill_4_level_num
        sk1_l = skills_levels[0]
        sk2_l = skills_levels[1]
        sk3_l = skills_levels[2]
        sk4_l = skills_levels[3]

        
        #sk1_bs = self.sk1_bs
        #sk1_ps = self.sk1_ps
        #sk1_bs2 = self.sk1_bs2
        #sk1_ps2 = self.sk1_ps2
        sk1_bs = sk1_info[0]
        sk1_ps = sk1_info[1]
        sk1_bs2 = sk1_info[2]
        sk1_ps2 = sk1_info[3]
                
        #sk2_bs = self.sk2_bs
        #sk2_ps = self.sk2_ps
        #sk2_bs2 = self.sk2_bs2
        #sk2_ps2 = self.sk2_ps2
        sk2_bs = sk2_info[0]
        sk2_ps = sk2_info[1]
        sk2_bs2 = sk2_info[2]
        sk2_ps2 = sk2_info[3]
                
        #sk3_bs = self.sk3_bs
        #sk3_ps = self.sk3_ps
        #sk3_bs2 = self.sk3_bs2
        #sk3_ps2 = self.sk3_ps2
        sk3_bs = sk3_info[0]
        sk3_ps = sk3_info[1]
        sk3_bs2 = sk3_info[2]
        sk3_ps2 = sk3_info[3]
                
        #sk4_bs = self.sk4_bs
        #sk4_ps = self.sk4_ps
        #sk4_bs2 = self.sk4_bs2
        #sk4_ps2 = self.sk4_ps2
        sk4_bs = sk4_info[0]
        sk4_ps = sk4_info[1]
        sk4_bs2 = sk4_info[2]
        sk4_ps2 = sk4_info[3]

        ###############################################################################################################################################

        #base_ba_d_simple = self.base_ba_d_simple
        #base_ba_d_per_level = self.base_ba_d_per_level
        #base_ba_d_power_multiplier = self.base_ba_d_power_multiplier
        #ba_progression = self.ba_progression
        base_ba_d_simple = ba_info[0]
        base_ba_d_per_level = ba_info[1]
        base_ba_d_power_multiplier = ba_info[2]
        ba_progression = ba_info[3]
        
        #ba_n = self.three_inputs_widget.int_input_1.int_input_num
        #power = self.three_inputs_widget.int_input_2.int_input_num
        #god_l = self.three_inputs_widget.int_input_3.int_input_num
        #sp_input_n = self.special_input_widget.int_input_num
        ba_n = inputs[0]
        power = inputs[1]
        god_l = inputs[2]
        sp_input_n = inputs[3]
        #self.ba_n = ba_n

        if god_name == "bacchus" and sk3_l != 0 and sk3a_state == 1:
            power = power + sk3_bs2[sk3_l - 1]
        if god_name == "ullr" and sk2_l != 0:
            power = power + sk2_bs[sk2_l - 1]

        #global ba_flat_buff
        base_ba_d = float(base_ba_d_simple + base_ba_d_per_level * god_l + base_ba_d_power_multiplier * power + ba_flat_buff)
        
        ba_totald = 0
        
        elements_n = 0
        for j in ba_progression:
            elements_n = elements_n + 1
        if ba_n != 0:
            index = 0
            while ba_n > 0:
                if index > (elements_n - 1):
                    index = index - elements_n
                current_basic_attack_damage = 0.0
                current_basic_attack_damage = base_ba_d*(float(ba_progression[index]))
                if current_basic_attack_damage - int(current_basic_attack_damage) >= 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage) + 1
                elif current_basic_attack_damage - int(current_basic_attack_damage) < 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage)
                ba_totald = ba_totald + current_basic_attack_damage
                index = index + 1
                ba_n = ba_n - 1

        if god_name == "ymir" and ( sk1_l != 0 or sk2_l != 0 or sk3_l != 0 ):
            ba_totald = ba_totald * 2
        
        ###############################################################################################################################################

        #global hydras_multiplier_buff
        #global hydras_affected_bas
        hydras_damage = 0
        hydras_damage = base_ba_d * hydras_multiplier_buff * ba_progression[0]
        hydras_damage = approximate_number_to_int(hydras_damage)
        hydras_damage = hydras_damage * hydras_affected_bas

        #global heartseeker_buff
        heartseeker_damage = heartseeker_buff * power  

        #global poly_buff_based_on_power
        #global polys_affected_bas
        polys_damage = 0
        polys_damage = poly_buff_based_on_power * power
        polys_damage = approximate_number_to_int(polys_damage)
        polys_damage = polys_damage * polys_affected_bas

        abilities_states = [sk1_l, sk2_l, sk3_l, sk4_l]
        #global mages_blessing_buff
        #global crusher_flat_buff
        #global crusher_buff_based_on_power
        ability_flat_buff = mages_blessing_buff + crusher_flat_buff + crusher_buff_based_on_power * power
        ability_flat_buff_final = 0
        #global skills_num
        if skills_num == 3:
            abilities_states[3] = 0
        if skills_num == 2:
            abilities_states[2] = 0
            abilities_states[3] = 0
        if god_name == "artio":
            if sk1_l != 0:
                if sk1a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk1b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk2_l != 0:
                if sk2a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk2b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
        elif god_name == "ullr":
            if sk1_l != 0:
                if sk1a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk1b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk3_l != 0:
                if sk3a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk3b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
        elif god_name == "cu-chulainn":
            if sk1_l != 0:
                if sk1a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk1b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk2_l != 0:
                ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk3_l != 0:
                if sk3a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk3b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk4_l != 0:
                if sk4a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk4b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
        elif god_name == "tyr":
            if sk1_l != 0:
                if sk1a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk1b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk2_l != 0:
                if sk2a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk2b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk3_l != 0:
                ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
        elif god_name == "agni":
            if sk1_l != 0:
                ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk2_l != 0:
                ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk3_l != 0:
                ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk4_l != 0:
                if sk4a_state == 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk4a_state == 1:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff * 2
                if sk4a_state == 2:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff * 3
        elif god_name == "hel":
            if sk1_l != 0:
                if sk1a_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
                if sk1b_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if sk2_l != 0:
                ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
        else:
            for sk_state in abilities_states:
                if sk_state != 0:
                    ability_flat_buff_final = ability_flat_buff_final + ability_flat_buff
            if (god_name == "anhur" or god_name == "cernunnos" or god_name == "hachiman"
                or god_name == "rama" or god_name == "xbalanque") and sk1_l != 0:
                ability_flat_buff_final = ability_flat_buff_final - ability_flat_buff
            if (god_name == "jing-wei" or god_name == "skadi" or god_name == "freya"
                or god_name == "kuzenbo" or god_name == "nu-wa") and sk2_l != 0:
                ability_flat_buff_final = ability_flat_buff_final - ability_flat_buff
            if god_name == "" and sk3_l != 0:
                ability_flat_buff_final = ability_flat_buff_final - ability_flat_buff
            if god_name == "vamana" and sk4_l != 0:
                ability_flat_buff_final = ability_flat_buff_final - ability_flat_buff
            if ability_flat_buff_final < 0:
                ability_flat_buff_final = 0

        sk1_d = 0
        sk1_d2 = 0
        sk2_d = 0
        sk2_d2 = 0
        sk3_d = 0
        sk3_d2 = 0
        sk4_d = 0
        sk4_d2 = 0
        index1 = 0
        text = ""
        if god_name == "ares":
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] * 5 + sk1_ps * power * 5
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs[sk1_l - 1] * 10 + sk1_ps * power * 10
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 8 + sk2_ps * power * 8
                sk2_percent_d = sk2_bs2[sk2_l - 1] * 8
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            if sk2_l != 0:
                text = "Damage: " + str(int(total_d)) + " + " + str(sk2_percent_d) + "%"
            if sk2_l == 0:
                text = "Damage: " + str(int(total_d))

        if god_name == "artio":
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk1_l != 0 and sk1b_state == 1:
                sk1_d2 = sk1_bs2[sk1_l - 1] * 2 + sk1_ps2 * power * 2
            if sk2_l != 0 and sk2a_state == 1:
                sk2_d = sk2_bs[sk2_l - 1] * 5 + sk2_ps * power * 5
            if sk2_l != 0 and sk2b_state == 1:
                sk2_d2 = sk2_bs2[sk2_l - 1] + sk2_ps2 * power
            total_d = sk1_d + sk1_d2 + sk2_d + sk2_d2 + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "athena":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0 and sk2a_state == 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk2_l != 0 and sk2a_state == 1:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            passive_d = sp_input_n * base_ba_d * 1.75
            total_d = sk1_d + sk2_d + sk3_d + passive_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "bacchus":
            if sk3_l != 0 and sk3a_state == 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk3_l != 0 and sk3a_state == 1:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                power = power + sk3_bs2[sk3_l - 1]
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 4 + sk2_ps * power * 4     
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "cabrakan":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0 and sk3a_state == 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk3_l != 0 and sk3a_state == 1:
                sk3_d = sk3_bs[sk3_l - 1] * 6 + sk3_ps * power * 6
            if sk3_l != 0 and sk3a_state == 2:
                sk3_d = sk3_bs[sk3_l - 1] * 21 + sk3_ps * power * 21
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "cerberus":
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs[sk1_l - 1] * 1.8 + sk1_ps * power * 1.8
            if sk1_l != 0 and sk1a_state == 2:
                sk1_d = sk1_bs[sk1_l - 1] * 2.4 + sk1_ps * power * 2.4
            if sk1_l != 0 and sk1a_state == 3:
                sk1_d = sk1_bs[sk1_l - 1] * 2.9 + sk1_ps * power * 2.9
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 7 + sk2_ps * power * 7
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ganesha":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0 and sk3a_state == 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk3_l != 0 and sk3a_state == 1:
                sk3_d = sk3_bs[sk3_l - 1] * 2 + sk3_ps * power * 2
            if sk3_l != 0 and sk3a_state == 2:
                sk3_d = sk3_bs[sk3_l - 1] * 3 + sk3_ps * power * 3
            if sk3_l != 0 and sk3a_state == 3:
                sk3_d = sk3_bs[sk3_l - 1] * 4 + sk3_ps * power * 4   
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "geb":

            sk3_percent_d = 0
            
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] * 0.5 + sk1_ps * power * 0.5
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs[sk1_l - 1] * 0.75 + sk1_ps * power * 0.75
            if sk1_l != 0 and sk1a_state == 2:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                
            if sk2_l != 0 and sk2a_state == 0:
                sk2_d = sk2_bs[sk2_l - 1] * 0.5 + sk2_ps * power * 0.5
            if sk2_l != 0 and sk2a_state == 1:
                sk2_d = sk2_bs[sk2_l - 1] * 0.75 + sk2_ps * power * 0.75
            if sk2_l != 0 and sk2a_state == 2:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                
            if sk3_l != 0:
                sk3_percent_d = sk3_bs[sk3_l - 1]

            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + polys_damage
            if sk3_l != 0:
                text = "Damage: " + str(int(total_d)) + " + " + str(sk3_percent_d) + "%"
            if sk3_l == 0:
                text = "Damage: " + str(int(total_d))

        if god_name == "khepri":
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 10 + sk2_ps * power * 10
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "kumbhakarna":
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs2[sk1_l - 1] + sk1_ps2 * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "kuzenbo":
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + sk1_bs2[sk1_l - 1]
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + sk1_bs2[sk1_l - 1] * 5
                
            if sk2_l != 0:
                sk2_percent_d = sk2_bs[sk2_l - 1]
                
            if sk3_l != 0 and sk3a_state == 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk3_l != 0 and sk3a_state == 1:
                sk3_d = sk3_bs[sk3_l - 1] * 2 + sk3_ps * power * 2
            if sk3_l != 0 and sk3a_state == 2:
                sk3_d = sk3_bs[sk3_l - 1] * 3 + sk3_ps * power * 3

            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                sk4_d = sk4_d + sk4_bs2[sk4_l - 1] * 2 + sk4_ps2 * power * 2
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            if sk2_l != 0:
                text = "Damage: " + str(int(total_d)) + " + " + str(sk2_percent_d) + "%"
            if sk2_l == 0:
                text = "Damage: " + str(int(total_d))

        if god_name == "sobek":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0 and sk4a_state == 0:
                sk4_d = sk4_bs[sk4_l - 1] * 0.25 + sk4_ps * power * 0.25
            if sk4_l != 0 and sk4a_state == 1:
                sk4_d = sk4_bs[sk4_l - 1] * 0.6 + sk4_ps * power * 0.6
            if sk4_l != 0 and sk4a_state == 2:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "sylvanus":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 5 + sk2_ps * power * 5
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] * 5 + sk3_ps * power * 5
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "xing-tian":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_percent_d = sk1_bs2[sk1_l - 1]
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
            if sk3_l != 0 and sk3a_state == 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk3_l != 0 and sk3a_state == 1:
                sk3_d = sk3_bs[sk3_l - 1] * 2 + sk3_ps * power * 2
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] * 5 + sk4_ps * power * 5
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            
            if sk1_l != 0:
                text = "Damage: " + str(int(total_d)) + " + " + str(sk1_percent_d) + "%"
            if sk1_l == 0:
                text = "Damage: " + str(int(total_d))

        if god_name == "ymir":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0 and sk3a_state == 0:
                sk3_d = sk3_bs[sk3_l - 1] * 0.3 + sk3_ps * power * 0.3
            if sk3_l != 0 and sk3a_state == 1:
                sk3_d = sk3_bs[sk3_l - 1] * 0.65 + sk3_ps * power * 0.65
            if sk3_l != 0 and sk3a_state == 2:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ah-muzen-cab":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + 9 * 4 + 0.06 * power * 4
            if sk2_l != 0 and sk2a_state == 0:
                sk2_d = sk2_bs[sk2_l - 1] * 2 + sk2_ps * power * 2
            if sk2_l != 0 and sk2a_state == 1:
                sk2_d = sk2_bs[sk2_l - 1] * 4 + sk2_ps * power * 4
            if sk2_l != 0 and sk2a_state == 2:
                sk2_d = sk2_bs[sk2_l - 1] * 7 + sk2_ps * power * 7
            if sk2_l != 0:
                sk2_d = sk2_d + 9 * 4 + 0.06 * power * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                sk3_d = sk3_d + 9 * 4 + 0.06 * power * 4
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "anhur":
            if sk1_l != 0:
                sk1_d = sp_input_n * base_ba_d * sk1_bs[sk1_l - 1]
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                
            if sk4_l != 0 and sk4a_state == 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            if sk4_l != 0 and sk4a_state == 1:
                sk4_d = sk4_bs[sk4_l - 1] * 4 + sk4_ps * power * 4
            if sk4_l != 0 and sk4a_state == 2:
                sk4_d = sk4_bs[sk4_l - 1] * 8 + sk4_ps * power * 8
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "apollo":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] * 4 + sk3_ps * power * 4
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "artemis":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] * 3 + sk1_ps * power * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "cernunnos":
            if sk1_l != 0:
                sk1_d = sp_input_n * ( sk1_bs[sk1_l - 1] )
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk2_l != 0 and sk2a_state == 0:
                sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2
            if sk2_l != 0 and sk2a_state == 1:
                sk2_d = sk2_d + sk2_bs2[sk2_l - 1] * 3 + sk2_ps2 * 3
            if sk2_l != 0 and sk2a_state == 2:
                sk2_d = sk2_d + sk2_bs2[sk2_l - 1] * 10 + sk2_ps2 * 10
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "chernobog":
            passive_d = sp_input_n * base_ba_d * ( 0.15 + god_l * 0.01 )
            if sk1_l != 0 and sk1a_state == 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk1_l != 0 and sk1a_state == 1:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + sk1_bs2[sk1_l - 1] + sk1_ps2 * power
            if sk2_l != 0 and sk2a_state == 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk2_l != 0 and sk2a_state == 1:
                sk2_d = sk2_bs[sk2_l - 1] * 2 + sk2_ps * power * 2
                
            total_d = passive_d + sk1_d + sk2_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        sk3_d_2 = 0

        if god_name == "chiron":
            sk3_d_2 = sp_input_n * (base_ba_d + sk3_bs2[sk3_l - 1])
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0 and sk4a_state == 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            if sk4_l != 0 and sk4a_state == 1:
                sk4_d = sk4_bs[sk4_l - 1] * 2 + sk4_ps * power * 2
            if sk4_l != 0 and sk4a_state == 2:
                sk4_d = sk4_bs[sk4_l - 1] * 3 + sk4_ps * power * 3
                
            total_d = sk1_d + sk2_d + sk3_d + sk3_d_2 + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        percent_d = 0

        if god_name == "cupid":
            if sp_input_n > 8:
                sp_input_n = 8
            percent_d = 0.02 * sp_input_n
            
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] * 2 + sk1_ps * power * 2
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_d * percent_d
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_d * percent_d
                
            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "hachiman":

            if sp_input_n > sk1_ps[sk1_l - 1]:
                sp_input_n = sk1_ps[sk1_l - 1]
            
            if sk1_l != 0:
                sk1_d = sp_input_n * (base_ba_d + sk1_bs[sk1_l - 1] ) + ( sk1_ps[sk1_l - 1] - sp_input_n ) * (base_ba_d + (sk1_bs2[sk1_l - 1]))
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 2
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "hou-yi":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d * 1.4
                if sk1a_state == 2:
                    sk1_d = sk1_d * 1.8
            if sk2_l != 0:
                sk2_d = sk3_bs[sk2_l - 1] + sk3_ps * power
            if sk3_l != 0:
                sk3_d = sk4_bs[sk3_l - 1] + sk4_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 4
                if sk3a_state == 2:
                    sk3_d = sk3_d * 9
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "izanami":
            if sk1_l != 0:
                sk1_d = sp_input_n * sk1_bs[sk1_l - 1]
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "jing-wei":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + sk1_bs2[sk1_l - 1] + sk1_ps2
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_bs2[sk1_l - 1] * 2  + sk1_ps2 * 2
                if sk1a_state == 2:
                    sk1_d = sk1_d + sk1_bs2[sk1_l - 1] * 4  + sk1_ps2 * 4
            if sk2_l != 0:
                sk2_d = sp_input_n * sk2_bs[sk2_l - 1]
                if sk2a_state == 1:
                    sk2_d = sp_input_n * sk2_bs2[sk2_l - 1]
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "medusa":
            if sk1_l != 0:
                sk1_d = base_ba_d + sk1_bs[sk1_l - 1] * 3 + sk1_ps * power * 3
                if sk1a_state == 1:
                    sk1_d = base_ba_d * 2 + sk1_bs[sk1_l - 1] * 6 + sk1_ps * power * 6
                if sk1a_state == 2:
                    sk1_d = base_ba_d * 3 + sk1_bs[sk1_l - 1] * 9 + sk1_ps * power * 9
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] * 0.75 + sk4_ps * power * 0.75
                if sk4a_state == 1:
                    sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "neith":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_bs[sk1_l - 1] * 2 + sk1_ps * power * 2
                if sk1a_state == 2:
                    sk1_d = sk1_bs[sk1_l - 1] * 3 + sk1_ps * power * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] * 0.5 + sk4_ps * power * 0.5
                if sk4a_state == 1:
                    sk4_d = sk4_bs[sk4_l - 1] * 0.65 + sk4_ps * power * 0.65
                if sk4a_state == 2:
                    sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power     
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "rama":
            if sk1_l != 0:
                sk1_d = sp_input_n * sk1_bs[sk1_l - 1]
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1]
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] * 0.5 + sk3_ps * power * 0.5
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] * 1.25 + sk3_ps * power * 1.25
                if sk3a_state == 2:
                    sk3_d = sk3_bs[sk3_l - 1] * 2.25 + sk3_ps * power * 2.25             

            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "skadi":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sp_input_n * base_ba_d * sk2_bs[sk2_l - 1]
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
                if sk3a_state == 1:
                    sk3_d = sk3_d + sk3_bs2[sk3_l - 1] * 2 + sk3_ps2 * power * 2
                if sk3a_state == 2:
                    sk3_d = sk3_d + sk3_bs2[sk3_l - 1] * 4 + sk3_ps2 * power * 4        
                    
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] * 4 + sk4_ps * power * 4
                if sk4a_state == 1:
                    sk4_d = sk4_bs[sk4_l - 1] * 8 + sk4_ps * power * 8
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ullr":
            if sk2_l != 0:
                power = power + sk2_bs[sk2_l - 1]
            if sk1_l != 0:
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1b_state == 1:
                    sk1_d = sk1_d + sk1_bs2[sk1_l - 1] + sk1_ps2 * power
            if sk3_l != 0:
                if sk3a_state == 1:
                    sk3_d = sk3_d + sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3b_state == 1:
                    sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
                
            total_d = sk1_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "xbalanque":
            if sk1_l != 0:
                sk1_d = sp_input_n * sk1_bs[sk1_l - 1]
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                sk2_d = sk2_d + (sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 6
                if sk2a_state == 1:
                    sk2_d = sk2_d + (sk2_bs[sk2_l - 1] + sk2_ps * power) * 0.3
                if sk2a_state == 2:
                    sk2_d = sk2_d + (sk2_bs[sk2_l - 1] + sk2_ps * power) * 0.6
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 1.3
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage
            text = "Damage: " + str(int(total_d))
             
        if god_name == "achilles":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] * 0.7 + sk1_ps * power * 0.7
                if sk1a_state == 1:
                    sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] * 2 + sk2_ps * power * 2
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))
             
        if god_name == "amaterasu":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_bs[sk1_l - 1] * 1.5 + sk1_ps * power
                if sk1a_state == 2:
                    sk1_d = sk1_bs[sk1_l - 1] * 2+ sk1_ps * power
                if sk2_l != 0:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk3_l != 0:
                    sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                    if sk3a_state == 1:
                        sk3_d = sk3_bs[sk3_l - 1] * 2.2 + sk3_ps * power * 2
                    if sk3a_state == 2:
                        sk3_d = sk3_bs[sk3_l - 1] * 3.6 + sk3_ps * power * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 2.2
                if sk3a_state == 2:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 3.6
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "bellona":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                    sk2_d = sk2_d + (sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 1.25
                if sk2a_state == 2:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                    sk2_d = (sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 1.5
                if sk2a_state == 3:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                    sk2_d = (sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 1.75
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "chaac":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] * 1.5 + sk2_ps * power * 1.5
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "cu-chulainn":
            if sk1_l != 0:
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1b_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sp_input_n * (sk2_bs[sk2_l - 1] + sk2_ps * power)
            if sk3_l != 0:
                if sk3a_state == 1:
                    sk3_d = sk3_d + sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3b_state == 1:
                    sk3_d = sk3_d + sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = 0
                if sk4a_state == 1:
                    sk4_d = sk4_d + sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4b_state == 1:
                    sk4_d = sk4_d + sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "erlang-shen":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                if sk2a_state == 0:
                    sk2_d = sk2_bs2[sk2_l - 1] + sk2_ps2 * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "guan-yu":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] * 5 + sk2_ps * power * 5
                if sk2a_state == 2:
                    sk2_d = sk2_bs[sk2_l - 1] * 10 + sk2_ps * power * 10
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                guan_index = sp_input_n
                current_progression = 1.2
                while guan_index > 0:
                    sk3_d = sk3_d + (sk3_bs[sk3_l - 1] + sk3_ps * power) * current_progression
                    current_progression = current_progression + 0.2
                    guan_index = guan_index - 1
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "hercules":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] * 1.5 + sk3_ps * power * 1.5
                if sk3a_state == 2:
                    sk3_d = sk3_bs[sk3_l - 1] * 1.75 + sk3_ps * power * 1.75
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "nike":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_bs[sk1_l - 1] * 2 + sk1_ps * power * 2
                if sk1a_state == 2:
                    sk1_d = sk1_bs[sk1_l - 1] * 3 + sk1_ps * power * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "odin":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 0.25 + sk2_ps * power * 0.25
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] * 0.5 + sk2_ps * power * 0.5
                if sk2a_state == 2:
                    sk2_d = sk2_bs[sk2_l - 1] * 0.75 + sk2_ps * power * 0.75
                if sk2a_state == 3:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] * 2 + sk3_ps * power * 2
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "osiris":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "sun-wukong":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs2[sk3_l - 1] + sk3_ps2 * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                sk4_d = sk4_d + sp_input_n * base_ba_d * 0.5
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "tyr":
            if sk1_l != 0:
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 2:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] * 2 + sk1_ps * power * 2
                if sk1b_state == 1:
                    sk1_d = sk1_d + sk1_bs2[sk1_l - 1] + sk1_ps2 * power
            if sk2_l != 0:
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2b_state == 1:
                    sk2_d = sk2_d + sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "vamana":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] * 2 + sk3_ps * power * 2
            if sk4_l != 0:
                sk4_d = sp_input_n * ( base_ba_d + sk4_bs[sk4_l - 1] )
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "agni":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d * 3
                if sk1a_state == 2:
                    sk1_d = sk1_d * 10
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 4
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 7
                if sk3a_state == 2:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 10
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_bs[sk4_l - 1] * 2 + sk4_ps * power * 2
                if sk4a_state == 2:
                    sk4_d = sk4_bs[sk4_l - 1] * 3 + sk4_ps * power * 3
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ah-puch":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
                if sk2a_state == 2:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] * 2 + sk2_ps2 * power * 2
                if sk2a_state == 3:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] * 3 + sk2_ps2 * power * 3
            if sk3_l != 0:
                sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 5
                if sk3a_state == 1:
                    sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_d * 7
                if sk4a_state == 2:
                    sk4_d = sk4_d * 14
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "anubis":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_bs[sk1_l - 1] * 3 + sk1_ps * power * 3
                if sk1a_state == 2:
                    sk1_d = sk1_bs[sk1_l - 1] * 6 + sk1_ps * power * 6
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] * 2 + sk2_ps * power * 2
                if sk2a_state == 2:
                    sk2_d = sk2_bs[sk2_l - 1] * 4 + sk2_ps * power * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] * 15 + sk3_ps * power * 15
                if sk3a_state == 2:
                    sk3_d = sk3_bs[sk3_l - 1] * 30 + sk3_ps * power * 30
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ao-kuang":
            if sp_input_n > 6:
                sp_input_n = 6
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sp_input_n * sk2_bs[sk2_l - 1] + sp_input_n * sk2_ps
                sk2_d = sk2_d + ( 6 - sp_input_n ) * sk2_bs2[sk2_l - 1]
                sk2_d = sk2_d + ( 6 - sp_input_n ) * sk2_ps2
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "aphrodite":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 6 + sk2_ps * power * 6
            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "baron-samedi":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 1.15
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] * 5 + sk3_ps * power * 5
            if sk4_l != 0:
                sk4_d = sp_input_n * (sk4_bs[sk4_l - 1] + sk4_ps * power)
                sk4_d = sk4_d + sk4_bs2[sk4_l - 1] + sk4_ps2 * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "change":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "chronos":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] * 2 + sk2_ps * power * 2
            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "discordia":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + sp_input_n * sk1_bs2[sk1_l - 1]
                sk1_d = sk1_d + sp_input_n * sk1_ps2 * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
                if sk2a_state == 2:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] * 2 + sk2_ps2 * power * 2
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "freya":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                if sk2a_state == 0:
                    sk2_d = sp_input_n * (sk2_bs[sk2_l - 1] + sk2_ps * power)
                if sk2a_state == 1:
                    sk2_d = sp_input_n * (sk2_bs2[sk2_l - 1] + sk2_ps2 * power)    
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] * 2 + sk3_ps * power * 2
                if sk3a_state == 2:
                    sk3_d = sk3_bs[sk3_l - 1] * 3 + sk3_ps * power * 3
                if sk3a_state == 3:
                    sk3_d = sk3_bs[sk3_l - 1] * 4 + sk3_ps * power * 4
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))       

        if god_name == "hades":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] * 4 + sk3_ps * power * 4
                if sk3a_state == 2:
                    sk3_d = sk3_bs[sk3_l - 1] * 8 + sk3_ps * power * 8
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "he-bo":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "hel":
            if sk1_l != 0:
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1b_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "isis":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_bs[sk1_l - 1] * 2 + sk1_ps * power * 2
                if sk1a_state == 2:
                    sk1_d = sk1_bs[sk1_l - 1] * 3 + sk1_ps * power * 3
                if sk1a_state == 3:
                    sk1_d = sk1_bs[sk1_l - 1] * 4 + sk1_ps * power * 4
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] * 1.25 + sk2_ps * power * 1.25
                if sk2a_state == 2:
                    sk2_d = sk2_bs[sk2_l - 1] * 1.5 + sk2_ps * power * 1.5
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * (sk3_bs2[sk3_l - 1] - (sk3_bs2[sk3_l - 1] - 1)*0.5)
                if sk3a_state == 2:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * sk3_bs2[sk3_l - 1]
                    
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "janus":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = ( sk2_bs[sk2_l - 1] + sk2_ps * power ) * 1.15
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power * 1.5
                if sk3a_state == 2:
                    sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power * 2
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "kukulkan":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = ( sk2_bs[sk2_l - 1] + sk2_ps * power ) * 5
                if sk2a_state == 1:
                    sk2_d = ( sk2_bs[sk2_l - 1] + sk2_ps * power ) * 9
                if sk2a_state == 2:
                    sk2_d = ( sk2_bs[sk2_l - 1] + sk2_ps * power ) * 13
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "nox":
            if sk1_l != 0:
                sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 4
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 2
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                sk4_d = sk4_d + (sk4_bs2[sk4_l - 1] + sk4_ps2 * power) * 5
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "nu-wa":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d + (sk1_bs2[sk1_l - 1] + sk1_ps2 * power) * 2
                if sk1a_state == 2:
                    sk1_d = sk1_d + (sk1_bs2[sk1_l - 1] + sk1_ps2 * power) * 5
            if sk2_l != 0:
                sk2_d = sp_input_n * sk2_bs[sk2_l - 1]
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
                if sk3a_state == 2:
                    sk3_d = sk3_d + (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 2
                if sk3a_state == 3:
                    sk3_d = sk3_d + (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 3
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "poseidon":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sp_input_n * (sk2_bs[sk2_l - 1] + 0.2 * power)
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 3
                if sk3a_state == 2:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 6
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_d * 2
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ra":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 3
                if sk3a_state == 2:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 6
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "raijin":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 2
                if sk1a_state == 2:
                    sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 4
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                sk3_d = sk3_d + sk3_bs2[sk3_l - 1] + sk3_ps2 * power
            if sk4_l != 0:
                sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.3
                if sk4a_state == 1:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 1.6
                if sk4a_state == 2:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 2.3
                if sk4a_state == 3:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 3                 
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "scylla":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "sol":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 3
                if sk1a_state == 2:
                    sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 5
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d * 2
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 3
                if sk3a_state == 2:
                    sk3_d = sk3_d * 6
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_d * 1.9
                if sk4a_state == 1:
                    sk4_d = sk4_d * 3.1
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "the-morrigan":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "thoth":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d * 2
                if sk1a_state == 2:
                    sk1_d = sk1_d * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                if sk1_l != 0:
                    sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                    if sk1a_state == 1:
                        sk3_d = sk3_d * 2
                    if sk1a_state == 2:
                        sk3_d = sk3_d * 3
            if sk4_l != 0:
                sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.4
                if sk4a_state == 1:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.6
                if sk4a_state == 2:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.8
                if sk4a_state == 3:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power)
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "vulcan":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sp_input_n * (sk2_bs[sk2_l - 1] + sk2_ps * power)
                if sk2a_state == 1:
                    sk2_d = sk2_d * 1.15
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.6
                if sk4a_state == 1:
                    sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.8
                if sk4a_state == 2:
                    sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "zeus":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d * 2
                if sk1a_state == 2:
                    sk1_d = sk1_d * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs2[sk2_l - 1] + sk2_ps2 * power
                if sk2a_state == 2:
                    sk2_d = sk2_d + (sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 2
                if sk2a_state == 3:
                    sk2_d = sk2_d + (sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 3
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 2
                if sk3a_state == 2:
                    sk3_d = sk3_d * 3
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d == sk4_d * 3
                if sk4a_state == 2:
                    sk4_d == sk4_d * 5
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "zhong-kui":
            if sk1_l != 0:
                sk1_d = ((sk1_bs[sk1_l - 1] + sk1_ps * power) * 5) * 0.75
                if sk1a_state == 1:
                    sk1_d = ((sk1_bs[sk1_l - 1] + sk1_ps * power) * 5)
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_d * 3
                if sk4a_state == 2:
                    sk4_d = sk4_d * 5
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + polys_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "arachne":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + (sk1_bs2[sk1_l - 1] + sk1_ps2 * power) * 6
            if sk2_l != 0:
                sk2_d = sp_input_n * sk2_bs[sk2_l - 1]
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "awilix":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d * 1.5
                if sk2a_state == 2:
                    sk2_d = sk2_d * 2
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "bakasura":
            true_damage = 0
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                true_damage = self.ba_n * sk2_bs2[sk2_l - 1]
            if sk3_l != 0:
                sk3_d = sp_input_n * (sk3_bs + sk3_ps * power)
                
            if sk2_l == 0:
                total_d = sk1_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
                text = "Damage: " + str(int(total_d))
            if sk2_l != 0:
                total_d = sk1_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
                text = "Damage: " + str(int(total_d)) + " + " + str(true_damage) + " true"

        if god_name == "bastet":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = (sk2_bs[sk2_l - 1] + sk2_ps * power) * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sp_input_n * (sk4_bs[sk4_l - 1] + sk4_ps * power)
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "camazotz":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                sk2_d = sk2_d + (sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 6
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_d * 2
                if sk4a_state == 2:
                    sk4_d = sk4_d * 3
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "da-ji":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                sk1_d = sk1_d + (sk1_bs2[sk1_l - 1] + sk1_ps2 * power) * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d * 2
                if sk2a_state == 2:
                    sk2_d = sk2_d * 3
                if sk2a_state == 3:
                    sk2_d = sk2_d * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                sk4_d = sk4_d + sk4_bs2[sk4_l - 1] + sk4_ps2 * power
                if sk4a_state == 1:
                    sk4_d = sk4_d + sk4_bs2[sk4_l - 1] + sk4_ps2 * power
                if sk4a_state == 2:
                    sk4_d = sk4_d + (sk4_bs2[sk4_l - 1] + sk4_ps2 * power) * 2
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "fenrir":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d * 2
                if sk2a_state == 2:
                    sk2_d = sk2_d * 3
                if sk2a_state == 3:
                    sk2_d = sk2_d * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "hun-batz":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
                if sk4a_state == 1:
                    sk4_d = sk4_d * 3
                if sk4a_state == 2:
                    sk4_d = sk4_d * sk4_bs2[sk4_l - 1]
                    
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "kali":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                sk2_d = sk2_d + (sk2_bs2[sk2_l - 1] + sk2_ps2 * power) * 6
                if sk2a_state == 1:
                    sk2_d = sk2_d + sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 2:
                    sk2_d = (sk2_d + sk2_bs[sk2_l - 1] + sk2_ps * power) * 2
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 4
                if sk3a_state == 2:
                    sk3_d = sk3_d * sk3_bs2[sk3_l - 1]
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "loki":
            if sk1_l != 0:
                sk1_d = (sk1_bs[sk1_l - 1] + sk1_ps * power) * 4
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "mercury":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = (sk2_bs[sk2_l - 1] + sk2_ps * power) * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ne-zha":
            if sk1_l != 0:
                sk1_d = sp_input_n * (sk1_bs[sk1_l - 1] + sk1_ps * power)
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 2
                sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 3
                if sk3a_state == 1:
                    sk3_d = sk3_d + sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 2:
                    sk3_d = sk3_d + (sk3_bs[sk3_l - 1] + sk3_ps * power) * 2
                if sk3a_state == 3:
                    sk3_d = sk3_d + (sk3_bs[sk3_l - 1] + sk3_ps * power) * 3
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "nemesis":
            percent_damage = 0
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d * 2
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d * 2
            if sk3_l != 0:
                percent_damage = sk3_bs[sk3_l - 1]

            total_d = sk1_d + sk2_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            if sk3_l == 0:
                text = "Damage: " + str(int(total_d))
            if sk3_l != 0:
                text = "Damage: " + str(int(total_d)) + " + " + str(percent_damage) + "%" 

        if god_name == "pele":
            if sk1_l != 0:
                if sk1a_state == 0:
                    sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    if sk1_l == 1:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                    if sk1_l == 2 or sk1_l == 3:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + sk1_bs2 + sk1_ps2 * power
                    if sk1_l == 4 or sk1_l == 5:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 2
                if sk1a_state == 2:
                    if sk1_l == 1:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power)
                    if sk1_l == 2:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 2
                    if sk1_l == 3:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 3
                    if sk1_l == 4:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 4
                    if sk1_l == 5:
                        sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 5
                if sk1b_state == 0:
                    sk1_d2 = 0
                if sk1b_state == 1:
                    sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1b_state == 2:
                    if sk1_l == 1:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power
                    if sk1_l == 2 or sk1_l == 3:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power)
                    if sk1_l == 4 or sk1_l == 5:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 2
                if sk1b_state == 3:
                    if sk1_l == 1:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power)
                    if sk1_l == 2:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 2
                    if sk1_l == 3:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 3
                    if sk1_l == 4:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 4
                    if sk1_l == 5:
                        sk1_d2 = sk1_bs[sk1_l - 1] + sk1_ps * power + (sk1_bs2 + sk1_ps2 * power) * 5 
                sk1_d = sk1_d + sk1_d2
            if sk2_l != 0:
                if sk2a_state == 0:
                    sk2_d = sk2_bs2[sk2_l - 1] + sk2_ps2 * power
                if sk2a_state == 1:
                    sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                if sk3a_state == 0:
                    sk3_d = 0
                if sk3a_state == 1:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 2
                if sk3a_state == 2:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 4
                if sk3a_state == 3:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 6
                if sk3a_state == 4:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 8
                if sk3a_state == 5:
                    sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 10
                if sk3b_state == 0:
                    sk3_d2 = 0
                if sk3b_state == 1:
                    sk3_d2 = sk3_bs2[sk3_l - 1] + sk3_ps2 * power * 1
                if sk3b_state == 2:
                    sk3_d2 = (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 2
                if sk3b_state == 3:
                    sk3_d2 = (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 3
                if sk3b_state == 4:
                    sk3_d2 = (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 4
                if sk3b_state == 5:
                    sk3_d2 = (sk3_bs2[sk3_l - 1] + sk3_ps2 * power) * 5
                sk3_d = sk3_d + sk3_d2
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ratatoskr":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
                if sk2a_state == 1:
                    sk2_d = sk2_d * 2
                if sk2a_state == 2:
                    sk2_d = sk2_d * 3
                if sk2a_state == 3:
                    sk2_d = sk2_d * 4
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 2
                if sk3a_state == 2:
                    sk3_d = sk3_d * 3
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "ravana":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "serqet":
            true_damage = 0
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            if sk4_l != 0:
                true_damage = sk4_bs[sk4_l - 1]
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            if sk4_l == 0:
                text = "Damage: " + str(int(total_d))
            if sk4_l != 0:
                text = "Damage: " + str(int(total_d)) + " + " + str(true_damage) + " true"

        if god_name == "susano":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d + sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 2:
                    sk1_d = sk1_d + (sk1_bs[sk1_l - 1] + sk1_ps * power) * 1.5
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = (sk3_bs[sk3_l - 1] + sk3_ps * power) * 4
            if sk4_l != 0:
                sk4_d = (sk4_bs[sk4_l - 1] + sk4_ps * power) * 0.85
                if sk4a_state == 1:
                    sk4_d = sk4_bs[sk4_l - 1] + sk4_ps * power
            total_d = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        if god_name == "thanatos":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            if sk1_l == 0:
                text = "Damage: " + str(int(total_d))
            if sk1_l != 0:
                text = "Damage: " + str(int(total_d)) + " + 10%"

        if god_name == "thor":
            if sk1_l != 0:
                sk1_d = sk1_bs[sk1_l - 1] + sk1_ps * power
                if sk1a_state == 1:
                    sk1_d = sk1_d * 3
            if sk2_l != 0:
                sk2_d = sk2_bs[sk2_l - 1] + sk2_ps * power
            if sk3_l != 0:
                sk3_d = sk3_bs[sk3_l - 1] + sk3_ps * power
                if sk3a_state == 1:
                    sk3_d = sk3_d * 3
                if sk3a_state == 2:
                    sk3_d = sk3_d * 5
            total_d = sk1_d + sk2_d + sk3_d + ba_totald + ability_flat_buff_final + hydras_damage + heartseeker_damage
            text = "Damage: " + str(int(total_d))

        return text, ba_n
