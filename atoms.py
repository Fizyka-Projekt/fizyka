import random
import math
import settings


class AtomBlue:
    atoms_list = []

    def __init__(self):
        self.v_x, self.v_y = random.randint(-settings.max_v, settings.max_v), random.randint(-settings.max_v,
                                                                                             settings.max_v)
        while True:
            test = True
            x = random.randint(0 + settings.radius, settings.width - settings.radius)
            y = random.randint(0 + settings.radius, settings.height - settings.radius)
            for i in range(len(AtomBlue.atoms_list)):
                if math.sqrt((AtomBlue.atoms_list[i].x - x) ** 2 + (
                        AtomBlue.atoms_list[i].y - y) ** 2) < 2 * settings.radius:
                    test = False
            if test:
                self.x = x
                self.y = y
                break
        AtomBlue.atoms_list.append(self)

    # def collision(self):
    #     for i in range(settings.M):
    #         for j in range(settings.M):
    #             if (math.sqrt(
    #                     (AtomBlue.atoms_list[j].x - AtomBlue.atoms_list[i].x) ** 2 + (
    #                             AtomBlue.atoms_list[j].y - AtomBlue.atoms_list[
    #                         i].y) ** 2)) <= 2 * settings.radius + settings.d:
    #                 normal_x = (AtomBlue.atoms_list[j].x - AtomBlue.atoms_list[i].x) / (math.sqrt(
    #                     (AtomBlue.atoms_list[j].x - AtomBlue.atoms_list[i].x) ** 2 + (
    #                             AtomBlue.atoms_list[j].y - AtomBlue.atoms_list[i].y) ** 2))
    #                 normal_y = (AtomBlue.atoms_list[j].y - AtomBlue.atoms_list[i].y) / (math.sqrt(
    #                     (AtomBlue.atoms_list[j].x - AtomBlue.atoms_list[i].x) ** 2 + (
    #                             AtomBlue.atoms_list[j].y - AtomBlue.atoms_list[i].y) ** 2))
    #                 tangential_x = (-(AtomBlue.atoms_list[j].y - AtomBlue.atoms_list[i].y)) / (math.sqrt(
    #                     (AtomBlue.atoms_list[j].x - AtomBlue.atoms_list[i].x) ** 2 + (
    #                             AtomBlue.atoms_list[j].y - AtomBlue.atoms_list[i].y) ** 2))
    #                 tangential_y = normal_x
    #                 velo_norm_1_x = AtomBlue.atoms_list[i].x * normal_x
    #                 velo_norm_1_y = AtomBlue.atoms_list[i].y * normal_y
    #                 velo_tange_1_x = AtomBlue.atoms_list[i].x * tangential_x
    #                 velo_tange_1_y = AtomBlue.atoms_list[i].y * tangential_y
    #                 velo_norm_2_x = AtomBlue.atoms_list[j].x * normal_x
    #                 velo_norm_2_y = AtomBlue.atoms_list[j].y * normal_y
    #                 velo_tange_2_x = AtomBlue.atoms_list[j].x * tangential_x
    #                 velo_tange_2_y = AtomBlue.atoms_list[j].y * tangential_y
    #                 velo_norm_1_p_x = velo_norm_2_x
    #                 velo_norm_1_p_y = velo_norm_2_y
    #                 velo_norm_2_p_x = velo_norm_1_x
    #                 velo_norm_2_p_y = velo_norm_1_y
    #                 v_1_prim_x = velo_norm_1_p_x * normal_x + velo_tange_1_x * tangential_x
    #                 v_1_prim_y = velo_norm_1_p_y * normal_y + velo_tange_1_y * tangential_y
    #                 v_2_prim_x = velo_norm_2_p_x * normal_x + velo_tange_2_x * tangential_x
    #                 v_2_prim_y = velo_norm_2_p_y * normal_y + velo_tange_2_y * tangential_y
    #                 AtomBlue.atoms_list[i].x = int(v_1_prim_x)
    #                 AtomBlue.atoms_list[i].y = int(v_1_prim_y)
    #                 AtomBlue.atoms_list[j].x = int(v_2_prim_x)
    #                 AtomBlue.atoms_list[j].y = int(v_2_prim_y)
