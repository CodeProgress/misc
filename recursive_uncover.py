# part of larger class
def uncover_cell(self, cell):
	# if cell is already uncovered, don't do anything
	if not cell.is_covered:
		return

	cell.uncover()

	# Base case 1: cell is a Mine
	if type(cell) is Mine:
		self.mine_uncovered = True
		return

	self.num_safe_cells_uncovered += 1

	# Base case 2: cell has a mine surrounding it
	if not cell.has_zero_surrounding_mines():
		return

	# Recursive step
	for surrounding_cell_location in cell.surrounding_cell_locations:
		row, col = surrounding_cell_location
		surrounding_cell = self.get_cell(row, col)
		self.uncover_cell(surrounding_cell)