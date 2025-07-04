def bonAppetit(bill, k, b):
    total_compartido = sum(bill) - bill[k]
    parte_anna = total_compartido // 2
    if b == parte_anna:
        print("Bon Appetit")
    else:
        print(b - parte_anna)
        