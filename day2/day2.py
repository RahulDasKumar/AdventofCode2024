import copy
total_reports = []
with open('input.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        report = [int(number) for number in line.split(" ")]
        total_reports.append(report)

def is_safe(report,left,right):
    left,right = 0,1
    difference = abs(report[left] - report[right])
    init_ascend = report[left] < report[right]
    while right != len(report):
        report_diff = abs(report[left] - report[right])
        is_ascending = report[left] < report[right]
        if (is_ascending and not init_ascend or init_ascend and not is_ascending) or (report_diff > 3 or report_diff < 1):
            return False
        left +=1 
        right +=1
    return True

def is_safe_2(report,errors,left,right):
    if errors > 1:
        return False
    if right >= len(report):
        return True
    is_ascending = report[0] < report[1]
    # if point is out of bounds
    difference = abs(report[right] - report[left])
    if (report[left] < report[right] and not  is_ascending) or (is_ascending  and not report[left] < report[right]) or (difference > 3 or difference < 1):
        # recursively call function
        # remove left number from report and recursively call that report to see if its a valid string
        left_number_gone = copy.deepcopy(report)
        left_number_gone.pop(left)
        # remove right number from report and recursvely call that report to see if its a valid string
        right_number_gone = copy.deepcopy(report)
        right_number_gone.pop(right)
        return is_safe_2(left_number_gone,errors+1,0,1) or is_safe_2(right_number_gone,errors+1,0,1) or is_safe_2(right_number_gone,errors+1,0,1) or is_safe_2(report[1:],errors+1,0,1) 
    return is_safe_2(report,errors,left+1,right+1) 

safe_reports = 0
# solution one


safe_reports = 0
# solution two
for report in total_reports:
    if is_safe_2(report=report, errors=0,left=0,right=1):
        safe_reports += 1
print(safe_reports)        
        
