# Parens
# print all combination of paranthesis
def bracket(opened, closed, total):
	if opened == total:
		return
	if closed == total:
		print()
		return

	if opened < total:
		print("(", end="")
		bracket(opened+1, closed, total)
	if closed < total:
		print(")", end="")
		bracket(opened, closed+1, total)
	
bracket(0,0,3)