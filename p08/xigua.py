''' #encoding=utf-8
price=5.2
weight=3.5
price_sum=price*weight-0.5
print('您应当支付的金额是：',price_sum)
'''
#encoding=utf-8
price_str = input('请输入西瓜价格：')
weight_str = input('请输入西瓜重量:')
price = float(price_str)
weight = float(weight_str)
money = price * weight
print('该西瓜的单价是 %.2f 元/斤' % (price))
print('该西瓜的重量是 %.2f 斤' % (weight))
print('您应当支付总金额是 %.2f 元' % (money))
