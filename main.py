import atoms
import settings
import animation
import math

atom_list = atoms.AtomBlue.atoms_list

for i in range(settings.atoms_number):
    atoms.AtomBlue()

animation.draw()

for i in range(settings.M):
    for j in range(settings.atoms_number):
        for k in range(j + 1, settings.atoms_number):
            next_1_x = atom_list[j].x + atom_list[j].v_x * settings.dt
            next_1_y = atom_list[j].y + atom_list[j].v_y * settings.dt
            next_2_x = atom_list[k].x + atom_list[k].v_x * settings.dt
            next_2_y = atom_list[k].y + atom_list[k].v_y * settings.dt
            odl_po = math.sqrt((next_2_x - next_1_x) ** 2 + (next_2_y - next_1_y) ** 2)
            odl_przed = math.sqrt(
                (atom_list[k].x - atom_list[j].x) ** 2 + (
                        atom_list[k].y - atom_list[
                    j].y) ** 2)
            if 2 * settings.radius < odl_przed <= 2 * settings.radius + settings.d and odl_po < odl_przed:
                normal_x = (atom_list[k].x - atom_list[j].x) / (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[j].y) ** 2))
                normal_y = (atom_list[k].y - atom_list[j].y) / (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[j].y) ** 2))
                tangential_x = (-(atom_list[k].y - atom_list[j].y)) / (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[j].y) ** 2))
                tangential_y = normal_x
                velo_norm_1_x = atom_list[j].v_x * normal_x
                velo_norm_1_y = atom_list[j].v_y * normal_y
                velo_tange_1_x = atom_list[j].v_x * tangential_x
                velo_tange_1_y = atom_list[j].v_y * tangential_y
                velo_norm_2_x = atom_list[k].v_x * normal_x
                velo_norm_2_y = atom_list[k].v_y * normal_y
                velo_tange_2_x = atom_list[k].v_x * tangential_x
                velo_tange_2_y = atom_list[k].v_y * tangential_y
                velo_norm_1_p_x = velo_norm_2_x
                velo_norm_1_p_y = velo_norm_2_y
                velo_norm_2_p_x = velo_norm_1_x
                velo_norm_2_p_y = velo_norm_1_y
                v_1_prim_x = velo_norm_1_p_x * normal_x + velo_tange_1_x * tangential_x
                v_1_prim_y = velo_norm_1_p_y * normal_y + velo_tange_1_y * tangential_y
                v_2_prim_x = velo_norm_2_p_x * normal_x + velo_tange_2_x * tangential_x
                v_2_prim_y = velo_norm_2_p_y * normal_y + velo_tange_2_y * tangential_y
                atom_list[j].v_x = v_1_prim_x
                atom_list[j].v_y = v_1_prim_y
                atom_list[k].v_x = v_2_prim_x
                atom_list[k].v_y = v_2_prim_y
        if settings.radius + settings.d > atom_list[j].x > atom_list[j].x + atom_list[j].v_x * settings.dt or atom_list[
            j].x > settings.width - settings.radius - settings.d and atom_list[j].x + atom_list[j].v_x * settings.dt > \
                atom_list[j].x:
            atom_list[j].v_x = -atom_list[j].v_x
        if settings.radius + settings.d > atom_list[j].y > atom_list[j].y + atom_list[j].v_y * settings.dt or atom_list[
            j].y > settings.height - settings.radius - settings.d and atom_list[j].y + atom_list[j].v_y * settings.dt > \
                atom_list[j].y:
            atom_list[j].v_y = -atom_list[j].v_y

    for m in range(settings.atoms_number):

        test = True

        for n in range(0, settings.atoms_number):
            if n == m: break
            next_1_x = atom_list[m].x + atom_list[m].v_x * settings.dt
            next_1_y = atom_list[m].y + atom_list[m].v_y * settings.dt
            next_2_x = atom_list[n].x + atom_list[n].v_x * settings.dt
            next_2_y = atom_list[n].y + atom_list[n].v_y * settings.dt
            odl_po = math.sqrt((next_2_x - next_1_x) ** 2 + (next_2_y - next_1_y) ** 2)
            odl_przed = math.sqrt(
                (atom_list[n].x - atom_list[m].x) ** 2 + (
                        atom_list[n].y - atom_list[m].y) ** 2)
            if odl_po < odl_przed <= 2 * settings.radius + settings.d and odl_po <= 2 * settings.radius:
                normal_x = (atom_list[n].x - atom_list[m].x) / (math.sqrt(
                    (atom_list[n].x - atom_list[m].x) ** 2 + (
                            atom_list[n].y - atom_list[m].y) ** 2))
                normal_y = (atom_list[n].y - atom_list[m].y) / (math.sqrt(
                    (atom_list[n].x - atom_list[m].x) ** 2 + (
                            atom_list[n].y - atom_list[m].y) ** 2))
                tangential_x = (-(atom_list[n].y - atom_list[m].y)) / (math.sqrt(
                    (atom_list[n].x - atom_list[m].x) ** 2 + (
                            atom_list[n].y - atom_list[m].y) ** 2))

                tangential_y = normal_x
                velo_norm_1_x = atom_list[m].v_x * normal_x
                velo_norm_1_y = atom_list[m].v_y * normal_y
                velo_tange_1_x = atom_list[m].v_x * tangential_x
                velo_tange_1_y = atom_list[m].v_y * tangential_y
                velo_norm_2_x = atom_list[n].v_x * normal_x
                velo_norm_2_y = atom_list[n].v_y * normal_y
                velo_tange_2_x = atom_list[n].v_x * tangential_x
                velo_tange_2_y = atom_list[n].v_y * tangential_y
                velo_norm_1_p_x = velo_norm_2_x
                velo_norm_1_p_y = velo_norm_2_y
                velo_norm_2_p_x = velo_norm_1_x
                velo_norm_2_p_y = velo_norm_1_y
                v_1_prim_x = velo_norm_1_p_x * normal_x + velo_tange_1_x * tangential_x
                v_1_prim_y = velo_norm_1_p_y * normal_y + velo_tange_1_y * tangential_y
                v_2_prim_x = velo_norm_2_p_x * normal_x + velo_tange_2_x * tangential_x
                v_2_prim_y = velo_norm_2_p_y * normal_y + velo_tange_2_y * tangential_y
                atom_list[m].v_x = v_1_prim_x
                atom_list[m].v_y = v_1_prim_y
                atom_list[n].v_x = v_2_prim_x
                atom_list[n].v_y = v_2_prim_y
                test = False
                break
        if test:
            atom_list[m].x = atom_list[m].x + atom_list[m].v_x * settings.dt
            atom_list[m].y = atom_list[m].y + atom_list[m].v_y * settings.dt
        # else:
        #     for o in range(settings.atoms_number):
        #         if o != m:
        #             next_1_x = atom_list[m].x + atom_list[m].v_x * settings.dt
        #             next_1_y = atom_list[m].y + atom_list[m].v_y * settings.dt
        #             next_2_x = atom_list[o].x + atom_list[o].v_x * settings.dt
        #             next_2_y = atom_list[o].y + atom_list[o].v_y * settings.dt
        #             odl_po = math.sqrt((next_2_x - next_1_x) ** 2 + (next_2_y - next_1_y) ** 2)
        #             odl_przed = math.sqrt(
        #                 (atom_list[o].x - atom_list[m].x) ** 2 + (
        #                         atom_list[o].y - atom_list[
        #                     m].y) ** 2)
        #             if 2 * settings.radius < odl_przed <= 2 * settings.radius + settings.d and odl_po < odl_przed:
        #                 normal_x = (atom_list[o].x - atom_list[m].x) / (math.sqrt(
        #                     (atom_list[o].x - atom_list[m].x) ** 2 + (
        #                         atom_list[o].y - atom_list[m].y) ** 2))
        #                 normal_y = (atom_list[o].y - atom_list[m].y) / (math.sqrt(
        #                     (atom_list[o].x - atom_list[m].x) ** 2 + (
        #                             atom_list[o].y - atom_list[m].y) ** 2))
        #                 tangential_x = (-(atom_list[o].y - atom_list[m].y)) / (math.sqrt(
        #                     (atom_list[o].x - atom_list[m].x) ** 2 + (
        #                             atom_list[o].y - atom_list[m].y) ** 2))
        #                 tangential_y = normal_x
        #                 velo_norm_1_x = atom_list[m].v_x * normal_x
        #                 velo_norm_1_y = atom_list[m].v_y * normal_y
        #                 velo_tange_1_x = atom_list[m].v_x * tangential_x
        #                 velo_tange_1_y = atom_list[m].v_y * tangential_y
        #                 velo_norm_2_x = atom_list[o].v_x * normal_x
        #                 velo_norm_2_y = atom_list[o].v_y * normal_y
        #                 velo_tange_2_x = atom_list[o].v_x * tangential_x
        #                 velo_tange_2_y = atom_list[o].v_y * tangential_y
        #                 velo_norm_1_p_x = velo_norm_2_x
        #                 velo_norm_1_p_y = velo_norm_2_y
        #                 velo_norm_2_p_x = velo_norm_1_x
        #                 velo_norm_2_p_y = velo_norm_1_y
        #                 v_1_prim_x = velo_norm_1_p_x * normal_x + velo_tange_1_x * tangential_x
        #                 v_1_prim_y = velo_norm_1_p_y * normal_y + velo_tange_1_y * tangential_y
        #                 v_2_prim_x = velo_norm_2_p_x * normal_x + velo_tange_2_x * tangential_x
        #                 v_2_prim_y = velo_norm_2_p_y * normal_y + velo_tange_2_y * tangential_y
        #                 atom_list[m].v_x = v_1_prim_x
        #                 atom_list[m].v_y = v_1_prim_y
        #                 atom_list[o].v_x = v_2_prim_x
        #                 atom_list[o].v_y = v_2_prim_y
    animation.draw()
