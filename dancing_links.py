import math


class DancingLinksSolver:
    # Reference: https://arxiv.org/pdf/cs/0011047.pdf
    
    def __init__(self):
        self.header = Column('header')
        self.columns = {}
    
    def build_links(self, puzzle: Sudoku):
        self.header = Column('header')
        self.columns = {}
        
        # Set up columns in (r, c, v) format
        for row in puzzle.INDICES:
            for col in puzzle.INDICES:
                for value in range(1, puzzle.SIZE + 1):
                #TODO: this initial setup piece seems to work for now, but was extremely finicky
                    name = self.name(row, col, value)
                    column = Column(name)
                    self.columns[name] = column
                    column.add_sibling(self.header)
                    Link().set_parent(column)
        
        # Establish linkages for all of the Links
        for row in puzzle.INDICES:
            for col in puzzle.INDICES:
                for value in range(1, puzzle.SIZE + 1):
                    name = self.name(row, col, value)
                    link = self.columns[name].down
					# TODO: this area where linkages get set up needs to be fixed (it doesn't link correctly)
                    ## Link to different value, same cell
                    #for i in range(1, puzzle.SIZE + 1):
                    #    if value != i:
                    #        target = self.name(row, col, i)
                    #        link.add_sibling(self.columns[target].down)
                    ## Link to same value, same row
                    #for i in puzzle.INDICES:
                    #    if col != i:
                    #        target = self.name(row, i, value)
                    #        link.add_sibling(self.columns[target].down)
                    ## Link to same value, same column
                    #for i in puzzle.INDICES:
                    #    if row != i:
                    #        target = self.name(i, col, value)
                    #        link.add_sibling(self.columns[target].down)
                    ## Link to same value, same box
                    #box_row = math.floor(row / puzzle.SIZE) * puzzle.SIZE
                    #box_col = math.floor(col / puzzle.SIZE) * puzzle.SIZE
                    #for sub_row in range(box_row, box_row + puzzle.SIZE):
                    #    for sub_col in range(box_col, box_col + puzzle.SIZE):
                    #        target = self.name(sub_row, sub_col, value)
                    #        link.add_sibling(self.columns[target].down)
        
        # Convert Sudoku puzzle into Dancing Links structure
        for row in puzzle.INDICES:
            for col in puzzle.INDICES:
                value = puzzle.get_cell(row, col)
                if value:
                    name = self.name(row, col, value)
                    self.columns[name].cover()
    
    def name(self, row, col, value):
        return '(%s,%s,%s)' % (row, col, value)


class Link:
    
    def __init__(self):
        """ Initializes this Link as a self-referencing Link. """
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.column = self
    
    def set_parent(self, column):
        """ Adds this Link to the bottom of the given column. """
        self.column = column
        self.down = column
        self.up = column.up
        self.up.down = self
        self.down.up = self
        column.size += 1
    
    def add_sibling(self, sibling):
        """ Inserts this Link to the right of the given sibling. """
        #print('Konami for self:')
        #self.konami()
        #print('Konami for sibling:')
        #sibling.konami()
        
        self.left = sibling
        self.right = sibling.right
        self.left.right = self
        self.right.left = self
    
    def konami(self):
        print('    Up: %s' % self.up)
        print('  Down: %s' % self.down)
        print('  Left: %s' % self.left)
        print(' Right: %s' % self.right)
        print('Column: %s' % self.column)
    
    def __repr__(self):
        return 'Link(), parent Column(%s)' % self.column.name if self.column != self else 'Link()'


class Column(Link):
    
    def __init__(self, name):
        """ Initializes this Column as a named Link. """
        self.name = name
        self.size = 0
        super().__init__()
    
    def uncover(self):
        self.left.right = self
        self.right.left = self
        link = self.down
        while link != self:
            r_link = link.right
            while r_link != link:
                r_link.up.down = r_link
                r_link.down.up = r_link
                r_link = r_link.right
            link = link.down
    
    def cover(self):
        print('Covering %s' % self.name)
        self.left.right = self.right
        self.right.left = self.left
        link = self.down
        while link != self:
            r_link = link.right
            while r_link != link:
                print('Unlinking link whose parent is %s' % r_link.column.name)
                r_link.up.down = r_link.down
                r_link.down.up = r_link.up
                r_link = r_link.right
            link = link.down
    
    def get_size(self):
        """ Counts the number of Links in this Column, excluding itself. """
        count = 0
        link = self.down
        while link != self:
            count += 1
            link = link.down
        return count
    
    def __repr__(self):
        return 'Column(%s)' % self.name
