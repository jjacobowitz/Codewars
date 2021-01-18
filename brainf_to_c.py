"""
Brainf*ck Translator 
Kata: https://www.codewars.com/kata/58924f2ca8c628f21a0001a1/train/python
Reddit: https://www.reddit.com/r/learnpython/comments/ij0t9u/critique_request_on_codewars_optimization_problem/

Brainfuck is one of the most well-known esoteric programming languages. But it 
can be hard to understand any code longer that 5 characters. In this kata you 
have to solve that problem.

Description

In this kata you have to write a function which will do 3 tasks:

1. Optimize the given Brainfuck code.
2. Check it for mistakes.
3. Translate the given Brainfuck programming code into C programming code.

More formally about each of the tasks:

1. Your function has to remove from the source code all useless command 
sequences such as: '+-', '<>', '[]'. Also it must erase all characters 
except +-<>,.[].

    Example:
        
    "++--+." -> "+."
    "[][+++]" -> "[+++]"
    "<>><" -> ""

2. If the source code contains unpaired braces, your function should return 
"Error!" string.

3. Your function must generate a string of the C programming code as follows:

    1. Sequences of the X commands + or - must be replaced by \*p += X;\n or 
    \*p -= X;\n.

        Example:

        "++++++++++" -> "\*p += 10;\n"
        "------" -> "\*p -= 6;\n"
        
    2. Sequences of the Y commands > or < must be replaced by p += Y;\n or 
    p -= Y;\n.

        Example:
            
        ">>>>>>>>>>" -> "p += 10;\n"
        
        "<<<<<<" -> "p -= 6;\n"

    3. . command must be replaced by putchar(\*p);\n.

        Example:

        ".." -> "putchar(\*p);\nputchar(\*p);\n"

    4. , command must be replaced by \*p = getchar();\n.

        Example:

        "," -> "\*p = getchar();\n"

    5. [ command must be replaced by if (\*p) do {\n. ] command must be 
    replaced by } while (\*p);\n.

        Example:

        "[>>]" ->
        
        if (\*p) do {\n
          p += 2;\n
        } while (\*p);\n

    6. Each command in the code block must be shifted 2 spaces to the right 
    accordingly to the previous code block.
       
        Example:
        
        "[>>[<<]]" ->
        if (\*p) do {\n
          p += 2;\n
          if (\*p) do {\n
            p -= 2;\n
          } while (\*p);\n
        } while (\*p);\n

Examples

Input:
    +++++[>++++.<-]
    
Output:
    *p += 5;
    if (*p) do {
      p += 1;
      *p += 4;
      putchar(*p);
      p -= 1;
      *p -= 1;
    } while (*p);

"""

def mismatched_paretheses(code):
    parentheses = []
    for char in code:
        if char =='[':
            parentheses.append('[')
        elif char == ']':
            if len(parentheses) > 0:
                if parentheses.pop(-1) != '[':
                    return True
            else:
                return True
    if len(parentheses) != 0:
        return True
    return False
    # parentheses = [paren for paren in code if paren in "[]"]
    # if len(parentheses)%2 != 0:
    #     print('Mismatch')
    #     return True
    # while len(parentheses) > 0:
    #     if parentheses.pop(0) != parentheses.pop(-1):
    #         print('Mismatch')
    #         return True
    # return False

def remove_junk(code):
    # print(code)
    for j in ['+-', '<>', '[]']:
        while j in code:
            code = code.replace(j, '')
    return code

def brainfuck_to_c(source_code):
    print('Before: ' + source_code)
    if mismatched_paretheses(source_code):
        return "Error!"
    source_code = remove_junk(source_code)
    print('After: ' + source_code)
    
    converter = {'+' : '*p += {};\n', 
                 '>' : 'p += {};\n', 
                 '-' : '*p -= {};\n', 
                 '<' : 'p -= {};\n', 
                 '[' : 'if (*p) do {\n', 
                 '.' : 'putchar(*p);\n', 
                 ']' : '} while (*p);\n', 
                 ',' : '*p = getchar();\n'}
    # repeater = []
    # for char in source_code:
    #     if char in ['+', '-', '<', '>']:
            
    
    return source_code

print(brainfuck_to_c("++++") == "*p += 4;\n")
print(brainfuck_to_c("----") == "*p -= 4;\n")

print(brainfuck_to_c(">>>>") == "p += 4;\n")
print(brainfuck_to_c("<<<<") == "p -= 4;\n")
    
print(brainfuck_to_c(".") == "putchar(*p);\n")
print(brainfuck_to_c(",") == "*p = getchar();\n")
    
print(brainfuck_to_c("[[[]]") == "Error!")
    
print(brainfuck_to_c("[][]") == "")
    
print(brainfuck_to_c("[.]") == "if (*p) do {\n  putchar(*p);\n} while (*p);\n")

print(brainfuck_to_c("++--+.") == "+.")
print(brainfuck_to_c("[][+++]") == "[+++]")
print(brainfuck_to_c("<>><") == "")
print(brainfuck_to_c("+++++[>++++.<-]") == """    *p += 5;
    if (*p) do {
      p += 1;
      *p += 4;
      putchar(*p);
      p -= 1;
      *p -= 1;
    } while (*p);""")