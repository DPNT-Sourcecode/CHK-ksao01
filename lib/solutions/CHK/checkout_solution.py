

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = []
        total = 0
        for item in skus:
            items.append(item)
        
        print(items)

        if any(item not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for item in items):
            return -1
        
        print(total)
        
        a_count = items.count('A')
        b_count = items.count('B')
        c_count = items.count('C')
        d_count = items.count('D')
        e_count = items.count('E')
        f_count = items.count('F')
        g_count = items.count('G')
        h_count = items.count('H')
        i_count = items.count('I')
        j_count = items.count('J')
        k_count = items.count('K')
        l_count = items.count('L')
        m_count = items.count('M')
        n_count = items.count('N')
        o_count = items.count('O')
        p_count = items.count('P')
        q_count = items.count('Q')
        r_count = items.count('R')
        s_count = items.count('S')
        t_count = items.count('T')
        u_count = items.count('U')
        v_count = items.count('V')
        w_count = items.count('W')
        x_count = items.count('X')
        y_count = items.count('Y')
        z_count = items.count('Z')


        b_count = max(0, b_count - (e_count // 2))
        m_count = max(0, m_count - (n_count // 3))
        q_count = max(0, q_count - (r_count // 3))

        a5_amount = a_count // 5
        a5_remainder = a_count % 5

        a3_remainder = a5_remainder % 3 
        a3_amount = a5_remainder // 3
    

        total += 130 * a3_amount
        total += 200 * a5_amount
        total += 50 * a3_remainder
        

        b_remainder = b_count % 2 
        b_amount = b_count // 2

        total += 45 * b_amount
        total += 30 * b_remainder
        

        total += 20 * c_count

        total += 15 * (d_count + m_count)

        total += 40 * (e_count * n_count)

        free_f = f_count // 3
        f_count -= free_f

        total += 10 * f_count 

        total += 20 * (g_count + t_count + w_count)

        
        h10_amount = h_count // 10
        h10_remainder = h_count % 10

        h5_remainder = h10_remainder % 5 
        h5_amount = h10_remainder // 5
    

        total += 45 * h5_amount
        total += 80 * h10_amount
        total += 10 * h5_remainder

        print ("i",total)
        total += 35 * i_count

        print ("j",total)
        total += 60 * j_count

        

        k_remainder = k_count % 2 
        k_amount = k_count // 2

        total += 150 * k_amount
        total += 80 * k_remainder

        total += 90 * (l_count + x_count)

        total += 10 * o_count

        p_remainder = p_count % 5 
        p_amount = p_count // 5

        total += 200 * p_amount
        total += 50 * p_remainder
        

        q_remainder = q_count % 3
        q_amount = q_count // 3

        total += 80 * q_amount
        total += 30 * q_remainder

        total += 50 * (r_count + z_count)

        total += 30 * s_count

        free_u = u_count // 4
        u_count -= free_u

        total += 40 * u_count 

        v3_amount = v_count // 3
        v3_remainder = v_count % 3

        v2_remainder = v3_remainder % 2 
        v2_amount = v3_remainder // 2
    

        total += 90 * v2_amount
        total += 130 * v3_amount
        total += 50 * v2_remainder
        
        total += 10 * y_count
            
        print(total)
        return total

    

if __name__ == "__main__":
    solution = CheckoutSolution()

    solution.checkout("A")
