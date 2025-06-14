

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = []
        total = 0
        for item in skus:
            items.append(item)
        
        print(items)

        if any(item not in "ABCD" for item in items):
            return -1
        
        a_count = items.count('A')
        b_count = items.count('B')
        c_count = items.count('C')
        d_count = items.count('D')

        a_remainder = a_count % 3 
        a_amount = a_count // 3

        total += 130 * a_amount
        total += 50 * a_remainder
        

        b_remainder = b_count % 2 
        b_amount = b_count // 2

        total += 45 * b_amount
        total += 30 * b_remainder

        total += 20 * c_count

        total += 15 * d_count
            
        print(total)
        return total

    

if __name__ == "__main__":
    solution = CheckoutSolution()

    solution.checkout("AAAA")




