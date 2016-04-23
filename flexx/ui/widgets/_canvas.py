"""
"""

from ... import event
from ...pyscript import window
from .. import Widget


class CanvasWidget(Widget):
    """ A widget that provides an HTML5 canvas. The canvas is scaled with
    the available space.
    """
    
    CSS = """
    .flx-CanvasWidget {
        min-width: 50px;
        min-height: 50px;
    }
    """ 
    
    class JS:
        
        def init(self):
            
            self.p = window.phosphor.createWidget('div')
            self.canvas = window.document.createElement('canvas')
            self.p.node.appendChild(self.canvas)
            # Set position to absolute so that the canvas is not going
            # to be forcing a size on the container div.
            self.canvas.style.position = 'absolute'
            
            self.canvas.addEventListener('mousemove', self.mouse_move, 0)
        
        @event.connect('size')
        def _update_canvas_size(self, *events):
            size = events[-1].new_value
            if size[0] or size[1]:
                self.canvas.width = size[0]
                self.canvas.height = size[1]
                self.canvas.style.width = size[0] + 'px'
                self.canvas.style.height = size[1] + 'px'
        
        # todo: define in widget?
        @event.emitter
        def mouse_move(self, e):
            """ The current position of the mouse inside this widget.
            """
            ev = self._create_mouse_event(e)
            rect = self.canvas.getBoundingClientRect()
            offset = rect.left, rect.top
            ev.pos = float(pos[0] - offset[0]), float(pos[1] - offset[1])
            return ev
