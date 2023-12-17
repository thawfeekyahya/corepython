## Exception Handling

In Python exception can be handled using try,except and finally keywords , The syntax is as follows

```

try:
   some statements
except ExceptionType:
   print() // throw exception using print statement
else:
   execute result

```

## Without exception Object

except keyword can be written as without any exception objects, in this case it will work for all exceptions but it won't have any info on what exception had occured

```

try:
   some statement
except:
   //show generic error message // No info available on what error had occured

```


## try statement can be used without using except keywoard by having 'finally' block

```

try:
   some statement
finally:
   // print default message  

```
