
#                     CONTRIBUTER: AMARTYA PANDEY


import pandas as pd
data = pd.read_csv(r"E:\Data_analysis\Udemy courses data analysis\7. Udemy Courses.csv")
print(data.head(3))

# QUESTIONS BASED UPON ANALYSING UDEMY ONLINE COURSE DATASETS:

# Q1). FIND OUT ALL THE COURSES THAT ARE FREE OF COST :
# SOLUTION:
c = data[data.is_paid == False]  #FILTERING PROCESS AS DISCUSSED IN THE WEATHER ANALYSIS PROJECT :)
print(c)

# Q2). FIND OUT THE DIFFERENT SUBJECTS THAT UDEMY IS OFFERING:
# SOLUTION:
a = data.subject.unique()
print(a)

# Q3). FIND OUT WHICH SUBJECTS HAS THE MINIMUM NUMBER OF OFFERED COURSES:
# SOLUTION:
b = data.subject.value_counts()
print(b)


# Q4). FIND OUT ALL THE COURSES THAT ARE PAID ONES :
# SOLUTION:
d = data[data.is_paid == True]
print(d)


# Q5). FIND OUT THE TOP RATED COURSES :
# SOLUTION:
e = data.sort_values('num_subscribers',ascending=False)
print(e)


# Q6). FIND OUT THE LEAST REATED COURSES:
# SOLUTION:
f = data.sort_values('num_subscribers')
print(f)


# Q7). FIND OUT ALL THE COURSES RELATED TO GRAPHICS DESIGNING WHERE THE PRICE IS BELOW 97:
# SOLUTION:
g = data[(data.subject == 'Graphic Design') & (data.price < '97')]
print(g)
# b). FIND OUT ALL THE COURSES RELATED TO python where the price is above 97:
gg=data[(data.subject == 'python') & (data.price>'97')]
print(gg)

# Q8). FIND OUT ALL THE COURSES RELATED TO 'python':
# SOLUTION:
h = data[data.course_title.str.contains('python')]
print(h)


# Q9). FIND OUT THAT WHICH UDEMY COURSES ARE PUBLISHED IN THE YEAR 2011:
# SOLUTION:
i = data[data.Year == 2011]
print(i)





//  IN THIS SIMILAR WAY YOU CAN ANALYZE ON VARIOUS PARAMETERS PROVIDED A GOOD HOLD UPON PYTHON SYNTAXES RELATED TO DATA ANALYSIS
