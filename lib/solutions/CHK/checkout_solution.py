

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

        if a_count % 3 == 0:
            amount = a_count // 3
            total += 130 * amount
        else: 
            total += 50 * a_count

        if b_count % 2 == 0:
            amount = b_count // 2
            total += 45 * amount
        else: 
            total += 30 * b_count
        

        total += 20 * c_count

        total += 15 * d_count
            
    
        return total

    





