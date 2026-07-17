name="Harry"
letter="Hey my name is {1} and my Id is {0}"
id=512
# 0,1 in {} specifies the positions of variables given in format function
print(letter.format(id,name))
# print(letter.format(name,id))
# use of f-strings 
text=(f"Hey ! My name is {name} and my Id is {id}")
# if we want to display our string as it is with {} we will use {{}} 
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
# .2f means we shall get two decimals after point
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))
