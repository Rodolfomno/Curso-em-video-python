price = float(input('qual o preco do produto?'))
novo = price - (price * 5 / 100)
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(price, novo))
