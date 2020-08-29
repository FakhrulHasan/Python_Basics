"""
1. Start with a letter
2. Can only contain letters & numbers
3. Variable names can never contain spaces.
4. Can have CAPS (XYZ = 100)(xyz are not SAME)
5. 2x is a syntax error

"""

message = "What's up, Doc?"
n = 17
pi = 3.14159

print(type(message))
print(type(n))
print(type(pi))


"""
Beginners sometimes confuse “meaningful to the human readers” with “meaningful to the computer”. 
So they’ll wrongly think that because they’ve called some variable average or pi, 
it will somehow automagically calculate an average, or automagically associate the variable pi with the value 3.14159. No! 
The computer doesn’t attach semantic meaning to your variable names.

So you’ll find some instructors who deliberately don’t choose meaningful names when they teach beginners — not because they don’t think it is a good habit, 
but because they’re trying to reinforce the message that you, the programmer, have to write some program code to calculate the average, 
or you must write an assignment statement to give a variable the value you want it to have.

"""
