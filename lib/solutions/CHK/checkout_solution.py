
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = []
        for item in skus:
            items.append(item)
        
        print(items)

    
if __name__ == "__main__":
    solution = CheckoutSolution()
    solution.checkout("ABCD")  # Example input

