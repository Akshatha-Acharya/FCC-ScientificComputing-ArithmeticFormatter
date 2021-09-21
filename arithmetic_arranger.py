def arithmetic_arranger(problems , *args):
  if(args):
      show_results = True
  else:
      show_results = False
  return process_input(problems,show_results)

def process_input(problems,show_results):
    first_op = []
    second_op = []
    op_list = []

    if(len(problems) > 5):
       return "Error: Too many problems." 
    
    for expr in problems:
        exprsn = expr.split()
        op1,op2,op = exprsn[0].strip(),exprsn[2].strip(),exprsn[1].strip()

        if op not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        if not(op1.isdigit() and op2.isdigit()):
            return "Error: Numbers must only contain digits."
        if((len(op1) > 4) or (len(op2) > 4)):
            return "Error: Numbers cannot be more than four digits."
        
        first_op.append(op1)
        second_op.append(op2)
        op_list.append(op)

    arranged_problems = (build_output(first_op , second_op, op_list , show_results))
    return arranged_problems

def build_output(first_op , second_op, op_list, show_results):
    first_line=""
    second_line=""
    third_line=""
    result=""
    if(show_results):
        for i in range(len(first_op)):
            width = max(len(first_op[i]), len(second_op[i]))
            if(op_list[i] == '+'):
                result += (str(int(first_op[i]) + int(second_op[i]))).rjust(width+2) + " "*4
            else:
                result += (str(int(first_op[i]) - int(second_op[i]))).rjust(width+2) + " "*4
    for i in range(0,len(first_op)):
        width = max(len(first_op[i]), len(second_op[i]))
        first_line += first_op[i].rjust(width+2) + " "*4
        second_line += op_list[i] + " " + second_op[i].rjust(width) + " "*4
        third_line += ("-"*(width+2)).rjust(width+2) + " "*4

    if show_results:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip() + '\n' + result.rstrip()
    else:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()
    return arranged_problems
    


    