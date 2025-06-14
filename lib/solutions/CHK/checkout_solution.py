

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

        if a_count % 3 == 0:
            amount = a_count / 3
            total += 130 * amount

        if b_count % 2 == 0:
            amount = b_count / 2
            total += 45 * amount
        
        
        for item in items:
            if item == 'C':
                total += 20
            elif item == 'D':
                total += 15
            
    
        print(total)

    
if __name__ == "__main__":
    solution = CheckoutSolution()

    solution.checkout("AAABBCD")  # Example input

