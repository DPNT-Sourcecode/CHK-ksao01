

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = []
        total = 0
        for item in skus:
            items.append(item)
        
        print(items)

        if any(item not in "ABCDE" for item in items):
            return -1
        
        a_count = items.count('A')
        b_count = items.count('B')
        c_count = items.count('C')
        d_count = items.count('D')
        e_count = items.count('E')

        b_count = max(0, b_count - (e_count // 2))

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

        total += 15 * d_count
        print(e_count)
        print(total)
        total += 40 * e_count
            
        print(total)
        return total

    

if __name__ == "__main__":
    solution = CheckoutSolution()

    solution.checkout("EE")