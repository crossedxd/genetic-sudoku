class DancingLinksSolver:
	# Reference: https://arxiv.org/pdf/cs/0011047.pdf
	
	def __init__(self):
		self.links = {}
		# Set up columns in (x, y, v) format
		for x in range(1, 10):
			for y in range(1, 10):
				for v in range(1, 10):
					pass
		
	
class Link:
	
	def __init__(self):
		''' Initializes this Link as a self-referencing Link. '''
		self.left = self
		self.right = self
		self.up = self
		self.down = self
		self.column = self
	
	def set_parent(self, column):
		''' Adds this Link to the bottom of the given column. '''
		self.column = column
		self.down = column
		self.up = column.up
		column.up.down = self
		column.up = self
		column.size += 1
	
	def add_sibling(self, link):
		''' Inserts the given Link to the left of this Link. '''
		link.right = self.right
		link.left = self
		self.right.left = link
		self.right = link

		
class Column(Link):
	
	def __init__(self, name):
		''' Initializes this Column as a named Link. '''
		self.name = name
		self.size = 0
		super().__init__()
	
	def get_size(self):
		''' Counts the number of Links in this Column, excluding itself. '''
		count = 0
		link = self.down
		while link != self:
			count += 1
			link = link.down
		return count
