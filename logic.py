#import functions
import functions as fn

class Expression:
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
		self.output = []
		self.precedence = {'-': 1, '=': 1, '|': 2, '&': 3, '~': 4}

	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	def push(self, op):
		self.top += 1
		self.array.append(op)

	def isOperand(self, ch):
		return ch.isalnum()

	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	def resolveNeg(self, exp):
		length = len(exp)
		res = ""
		for i in range(0,length):
			if exp[i] == '~':
				res = res + "0"
			res = res + exp[i]
		return res

	def infixToPostfix(self, exp):
		exp = self.resolveNeg(exp)
		for i in exp:
			if self.isOperand(i):
				self.output.append(i)
			elif i == '(':
				self.push(i)
			elif i == ')':
				while((not self.isEmpty()) and
					self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			# An operator is encountered
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		# pop all the operator from the stack
		while not self.isEmpty():
			self.output.append(self.pop())

		return "".join(self.output)



	def evaluatePostfix(self, exp):
		for i in exp:
			if i.isdigit():
				self.push(i)
			else:
				val1 = self.pop()
				val2 = self.pop()
				res = "0"
				if i == "|":
					res = fn.OR(val1,val2)
				elif i == "&":
					res = fn.AND(val1,val2)
				elif i == "~":
					res = fn.NOT(val1)
				elif i == "-":
					res = fn.IM(val1,val2)
				elif i == "=":
					res = fn.BI(val1,val2)
				self.push(res)
		return (self.pop())

	def resultList(self,exp):
		rs = []
		pf_exp = self.infixToPostfix(exp)
		#print(pf_exp)  
		exps = fn.genExps(pf_exp)
		for exp in exps:
			rs.append(self.evaluatePostfix(exp))	
		return rs


def Ex1():
	exp = input("$ ")
	obj = Expression(len(exp))
	res = obj.resultList(exp);
	if(fn.isTaut(res)):
		print("Your expression is a Tautology\n")
	else:
		print("Your expression is NOT a Tautology\n")

def Ex2():
	exp = input("1$ ")
	exp1 = input("2$ ")
	exp="(" + exp + ")=(" + exp1 + ")"
	obj = Expression(len(exp))
	res = obj.resultList(exp);
	if fn.isTaut(res):
		print("They are logically equivalent")
	else:
		print("They are NOT logically equivalent")


def main():
	print("While entering boolean expression:-\nUse:-\n\tNOT -> ~\n\tOR -> |\n\tAND -> &\n\tIMPLIES -> -\n\tBICONDITIONAL -> =")
	print("1) is_tautology(expression): Read the input as Boolean expression and returns a Boolean value that indicates whether the expression is a tautology or not.")
	print("2) are_equivalent(expression1, expression2): receives two Boolean expressions as input and returns a Boolean value that indicates if the two expressions are logically equivalent.")
	option = "1"
	while option == "1" or option == "2":
		option = input("Enter option(1 or 2 or any other to exit): ")
		if option == "1":
			Ex1()
		elif option == "2":
			Ex2()
		else:
			print("BYE!")        

# Driver's code
if __name__ == '__main__':
  main()

'''

'''