import random
from typing import * 

def do_the_thing(each_row_True_count:List[int], q:int, max_true_count_per_row:int)->List[List[int]]:

	row_count = len(each_row_True_count)
	#cheking if sum of each row true count is deviseable by q
	while sum(each_row_True_count) % q != 0:
		candidate_index:int = random.randint(0, row_count-1)
		if each_row_True_count[candidate_index] >= max_true_count_per_row:
			continue
		else:
			each_row_True_count[candidate_index] += 1



	def sum_each_row_true_counts_and_exclude_specific_rows(rows_to_exculde:List[int])->int:
		index:int
		count:int = 0
		nonlocal each_row_True_count
		for index in range(row_count):
			if index in rows_to_exculde:
				continue 
			else:
				count += each_row_True_count[index]
		return count


	def generate_zero_matrix(rows_count:int, cols_count:int)->List[List[int]]:
		output:List[List[int]] = list()
		for i in range(row_count):
			output.append([False]*cols_count)
		return output


	def append_empty_col_to_matrix(target)->None:
		for i1 in range(len(target)):
			target[i1].append(False)


	def count_rows_with_above_zero_true_count()->int:
		nonlocal each_row_True_count
		counter:int = 0
		for i1 in each_row_True_count:
			counter += i1 > 0
		return counter



	def tell_which_rows_are_picked_up_by_row_pickedupness_state_array(row_pickedupness_state_array:List[int]):
		output:List[int] = list()
		i1:bool 
		index:int 
		for index,i1 in enumerate(row_pickedupness_state_array):
			if i1 == True:
				output.append(index)
		return output


	def print_matrix(a:List[List]):
		for i1 in a:
			for i2 in i1:
				if i2 == 1:
					print("*", end="")
				if i2 == 0:
					print(".", end="")
			print()






	def all_rows_True_count_are_zero():
		nonlocal each_row_True_count
		i1:int
		for i1 in each_row_True_count:
			if i1 != 0:
				return False 
		return True 




	def generate_index_array(a:List[int])->List[int]:
		"""
		a -> [23,45,98,63,12]
		output -> [0,1,2,3,4]
		"""
		output:List[int] = list(range(0, len(a)))
		return output

	the_matrix = generate_zero_matrix(row_count, sum(each_row_True_count)//row_count)
	
	index_array:List[int] = generate_index_array(each_row_True_count)

	row_pickedupness_state_array = [False] * row_count
	current_col:int = 0

	main_loop_flag:bool = True
	while (all_rows_True_count_are_zero() == False) and main_loop_flag:
		if current_col >= len(the_matrix[0]):
			append_empty_col_to_matrix(the_matrix)
		to_be_picked_from_index_of_rows:List[int] = list()

		while len(to_be_picked_from_index_of_rows) < q+1 :
			
			if len(to_be_picked_from_index_of_rows) == count_rows_with_above_zero_true_count():
				break

			print(each_row_True_count, row_pickedupness_state_array, to_be_picked_from_index_of_rows, )
			print(len(to_be_picked_from_index_of_rows) < q+1 , len(to_be_picked_from_index_of_rows) == count_rows_with_above_zero_true_count())
			print(count_rows_with_above_zero_true_count)
			candidate_index:int = random.randint(0, row_count-1)
			if row_pickedupness_state_array[candidate_index] == True:
				continue
			if each_row_True_count[candidate_index] <= 0:
				continue
			rows_to_exculde:List[int] = tell_which_rows_are_picked_up_by_row_pickedupness_state_array(row_pickedupness_state_array)
			number_of_remaining_true_counts_excluding_already_picked_ones:int = sum_each_row_true_counts_and_exclude_specific_rows(rows_to_exculde=rows_to_exculde)
			if number_of_remaining_true_counts_excluding_already_picked_ones == 0:
				main_loop_flag = False
				break
			row_pickedupness_state_array[candidate_index] = True
			to_be_picked_from_index_of_rows.append(candidate_index)


		row_index:int 
		for index, row_index in enumerate(to_be_picked_from_index_of_rows):
			the_matrix[row_index][current_col] = True
			each_row_True_count[row_index] -= 1

		print_matrix(the_matrix)
		input("PRESS ENTER")
		current_col += 1
		row_pickedupness_state_array = [False] * row_count






do_the_thing([20,10,15,8,7,6,9,3], 3, 10)