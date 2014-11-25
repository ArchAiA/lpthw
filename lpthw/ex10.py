tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""




#Study Drill #2: Use triple single quotes instead
#of triple double quotes.  Result: Same output...
#This is useful if your string that you want to print
#has a triple single quote within it, and vice versa
#for triple double quotes.
single_fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies """
\t* Catnip\n\t* Grass
'''

#Chapter 10 errata: Try this code
#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print single_fat_cat

#Chapter 10 Study Drill #4
print "%s" % "This is a \'test\'"
print "%r" % "This is another \'test\'"