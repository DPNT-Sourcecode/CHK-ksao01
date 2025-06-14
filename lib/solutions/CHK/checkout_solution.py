
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = []
        total = 0
        for item in skus:
            items.append(item)
        
        print(items)
        
        for item in items:
            if item == 'A':
                total += 50
            elif item == 'B':
                total += 30
            elif item == 'C':
                total += 20
            elif item == 'D':
                total += 15
            else: 
                return -1
    
        print(total)

    
if __name__ == "__main__":
    solution = CheckoutSolution()

    solution.checkout("ABCD")  # Example input
