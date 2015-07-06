from collections import namedtuple
Edge = namedtuple('Edge', 'thing, is_top')

class Panel:
    def __init__(self, *args):
        self.edges = [Edge(*arg.split('.')) for arg in args]
        print(self.edges)

class Panel_Board:
    #panel_order = [(0,0),(0,1),]
    def __init__(self):
        self.panels = [[]]
    def add_panel(self, panel):
        

panel_str = """brown.0,red.0,green.1,blue.1;blue.1,red.0,brown.0,red.1;
brown.1,blue.0,green.0,red.1;brown.0,green.0,blue.0,red.1;
green.0,brown.1,green.0,red.1;green.1,brown.0,blue.0,red.0;
red.0,brown.0,blue.0,green.1;brown.0,green.1,blue.0,blue.1;
blue.1,brown.1,red.1,green.0"""
panels = [Panel(*panel.strip().split(',')) for panel in panel_str.split(';')]

def add_panel(usable_panels):
    

def solutions(panels):
        for panel in panels:
            for panel-rotation in panel-rotations:
                this-block = panel-rotation
                if whole_thing.is_legit():
                    
