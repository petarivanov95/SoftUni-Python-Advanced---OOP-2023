def separator(nums):
    nums_list = nums.split()
    positives = [int(x) for x in nums_list if int(x)>0]
    negatives = [int(x) for x in nums_list if int(x)<0]
    sum_positives = sum(positives)
    sum_negatives = sum(negatives)

    print(sum_negatives)
    print(sum_positives)

    if abs(sum_positives)>abs(sum_positives):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')
    

my_nums = '1 2 -3 -4 65 -98 12 57 -84'
separator(my_nums)