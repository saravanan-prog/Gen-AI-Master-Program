# Python Functions and Modules

## 1. What is a Function?

A **function** is a block of code that performs a specific task.

Imagine you have a task that you need to do many times.

Instead of writing the same code again and again, we can put the code inside a function and reuse it.

### Real-world example

Think about a **washing machine**.

You give clothes as input:

```text
Clothes
   ↓
Washing Machine
   ↓
Clean Clothes
```

Similarly, a Python function can take input and produce output:

```text
Input
  ↓
Function
  ↓
Output
```

---

# 2. Why Do We Need Functions?

Without a function:

```python
print("Hello Arun")
print("Hello Priya")
print("Hello Ravi")
```

If the same logic becomes bigger, the code becomes difficult to manage.

With a function:

```python
def say_hello():
    print("Hello Student")
```

Now we can call it whenever we need it:

```python
say_hello()
say_hello()
say_hello()
```

Output:

```text
Hello Student
Hello Student
Hello Student
```

### Main benefit

> **Write once → Use many times**

---

# 3. Defining a Function

We use the `def` keyword to create a function.

### Syntax

```python
def function_name():
    # code
```

Example:

```python
def say_hello():
    print("Hello Python")
```

Here:

```text
def          → tells Python we are creating a function
say_hello   → function name
()           → parameters will come here
:            → function body starts
```

---

# 4. Calling a Function

Creating a function does not execute it.

We need to **call** the function.

```python
def say_hello():
    print("Hello Python")

say_hello()
```

Output:

```text
Hello Python
```

### Important

```text
Define function
      ↓
Call function
      ↓
Function executes
```

---

# 5. Function with Multiple Lines

A function can contain multiple statements.

```python
def student_details():
    print("Name: Arun")
    print("Age: 22")
    print("Course: Python")

student_details()
```

Output:

```text
Name: Arun
Age: 22
Course: Python
```

---

# 6. Function Parameters

Sometimes we want to give data to a function.

That data is called a **parameter**.

Example:

```python
def say_hello(name):
    print("Hello", name)

say_hello("Arun")
```

Output:

```text
Hello Arun
```

Here:

```text
name → parameter
Arun → argument
```

### Simple understanding

```text
"Arun"
   ↓
say_hello()
   ↓
name
   ↓
Hello Arun
```

---

# 7. Function with Two Parameters

A function can have multiple parameters.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

Here:

```text
a = 10
b = 20
```

The function calculates:

```text
10 + 20
   ↓
  30
```

---

# 8. Parameters vs Arguments

This is an important beginner concept.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Parameter

The variables inside the function definition:

```python
a, b
```

are called **parameters**.

### Argument

The actual values passed when calling the function:

```python
10, 20
```

are called **arguments**.

### Easy way to remember

```text
def add(a, b):
        ↑  ↑
     Parameters


add(10, 20)
    ↑   ↑
  Arguments
```

---

# 9. Return Value

Sometimes we don't want the function to directly print the result.

We want the function to **give the result back**.

For this, we use `return`.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### How it works

```text
10 + 20
   ↓
add()
   ↓
return 30
   ↓
result
   ↓
print(result)
```

---

# 10. `print()` vs `return`

This is very important.

### Using `print()`

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

The function displays the result.

### Using `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The function sends the result back.

We can use the result later:

```python
def add(a, b):
    return a + b

result = add(10, 20)

new_result = result * 2

print(new_result)
```

Output:

```text
60
```

### Simple difference

```text
print()
   ↓
Display result

return
   ↓
Send result back
```

---

#
