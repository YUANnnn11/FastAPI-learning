# 用占位符的方式拼接
name = "小王"
message = "我是%s"%name
print(message)

# 用占位符拼接数字、字符串
age = 18
message = "我今年%s岁"%age
print(message)

name = "小王"
age = 18
score_avg = 95.8
message = "我叫%s,今年%d岁,平均分是%f"%(name,age,score_avg)
print(message)

# 精度化控制
num1 = 12
num2 = 12.345
print("数字12宽度限制5，结果是%5d" % num1)
print("数字12宽度限制1，结果是%1d" % num1)
print("数字12.345宽度限制7，小数精度2，结果是%7.2f" % num2)
print("数字12.345宽度不限制，小数精度2，结果是%.2f" % num2)


# 快速格式化：format。语法：f {占位}
name = "小王"
age = 18
avg = 95.8
print(f"我是{name},今年{age}岁,平均分是{avg}")
# 不理会类型、不限制精度



# 表达式的格式化
print("1+1=%d" %(1+1))
print(f"5*2={5*2}")
print("name的类型：%s" % type(name))


#综合
name = "某公司"
stock_price = 19.99
stock_code = "000001"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.2f，经过%d天增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, (stock_price * stock_price_daily_growth_factor ** growth_days)))