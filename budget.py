class Category:

  def __init__(self, cat):
    self.cate = cat
    self.ledger = list()
    self.amount_spent = 0
  
  def deposit(self, amount, description=""):
    update = {"amount": amount, "description": description}
    self.ledger.append(update)

  def check_funds(self, amount):
    if amount > sum(item['amount'] for item in self.ledger):
      return(False)
    else:
      return(True)

  def withdraw(self, amount, description=""):
    update = {"amount": -amount, "description": description}
    if self.check_funds(amount) == True:
      self.ledger.append(update)
      self.amount_spent += amount
      return(True)
    else:
      return(False)
  
  def get_balance(self):
    return(sum(item['amount'] for item in self.ledger))

  def transfer(self, amount, cat):
    if self.check_funds(amount) == True:
      update = {"amount": -amount, "description": "Transfer to " + str(cat.cate)}
      update2 = {"amount": amount, "description": "Transfer from " + str(self.cate)}
      self.ledger.append(update)
      cat.ledger.append(update2)
      return(True)
    else:
      return(False)

  def __str__(self):
    header = self.cate.center(30,"*") + '\n'
    body = str()
    for item in self.ledger:
      if len(item['description']) <= 23:
        line = item['description'].ljust(23) + format(float(item["amount"]),'.2f').rjust(7) + '\n'
      else:
        line = item['description'][:23] + format(float(item["amount"]),'.2f').rjust(7) + '\n'
      body = body + line
    total = sum(item['amount'] for item in self.ledger)
    bottom = "Total: " + str(total)
    table = header + body + bottom
    return(table)

def create_spend_chart(categories):
  num_cats = len(categories)
  chart_axis = ["Percentage spent by category", "\n100|", "\n 90|", "\n 80|", "\n 70|", "\n 60|", "\n 50|", "\n 40|", "\n 30|", "\n 20|", "\n 10|", "\n  0|", "\n    " + "-" * (3 * num_cats + 1)]
  total_spent = 0
  for cat in categories:
    total_spent += cat.amount_spent

  percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
  for cat in categories:
    i = 1
    percent_spent = cat.amount_spent/total_spent*100
    for percent in percentages:
      if percent <= percent_spent:
        chart_axis[i] += " o "
      else:
        chart_axis[i] += "   "
      i+=1

  for i in range(len(percentages)):
    chart_axis[i+1] += " "

  max_name_length = max([len(cat.cate) for cat in categories])
  j = 0
  while j < max_name_length:
    line = ["\n    "]
    for cat in categories:
        if len(cat.cate) > j:
          line.extend((" ", cat.cate[j], " "))
        else:
          line.append("   ")
    line.append(" ")
    chart_axis.append("".join(line))
    j += 1

  spend_chart = "".join(chart_axis)
  return spend_chart
