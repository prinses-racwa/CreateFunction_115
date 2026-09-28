#def printme( text1 ): #"This is a print function“
#	print(text1)
#	return 

#printme("I'm first call to user defined function!") 
#printme("Again second call to the same function")
#printme("hallo rajwa")
#printme("investasi lewat code ini: semoga kuliahku lancar dan lulus tepat waktu")

#def printme( str ): #"This prints a passed string" 
#	print (str); 
#	return; 
#printme();

#def printinfo( name, age ): #"Test function" 
#   print ("Name: ", name); 
#    print ("Age ", age); 
#    return; 
#printinfo( age=50, name="miki" );
#printinfo( "maka", 30 );
#printinfo( "rajwa", 20 );
#printinfo( "septi", 10 );

#def changeme( mylist ): #This changes a passed list#
#	mylist = ([1,2,3,4]); 
#	print("Values inside the function: ", mylist) 
#	return 
#mylist = [10,20,30]; 
#changeme( mylist ); 
#print ("Values outside the function: ", mylist) 

# def printinfo( arg1, *vartuple ): #"This is test" 
#    print("Output is: ")
#     print(arg1)
#     for var in vartuple: 
#             print (var) 
#     return; 
# printinfo( 10 ); 
# printinfo( 70, 60, 50, 67676767676767676767676767, 7676767676767676767676, 0 )

sum = lambda arg1, arg2: arg1 + arg2;
print ("Value of total : ", sum( 10, 20 )) 
print ("Value of total : ", sum( 20, 20 ) )
print ("Valie of total : ", sum( 30, 60 ))
print ("Value of total : ", sum( 0, 0))
print ("Value of total : ", sum( 1234567890, 987654321))